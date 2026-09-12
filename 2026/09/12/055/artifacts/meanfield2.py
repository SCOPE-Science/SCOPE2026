"""Correct edge-based Scharfetter-Gummel FP + susceptibilities + 2-delay determinant.
All analysis under __main__; safe to import helpers.
"""
import math, json, time
import numpy as np

T0 = time.time()
TAU_M_E = 20.0; TAU_M_I = 10.0
V_TH = 20.0; V_RESET = 10.0
TAU_REF_E = 2.0; TAU_REF_I = 1.0
TAU_S_E = 3.0; TAU_S_I = 2.0; TAU_EXT = 2.0
T_STAR = 4.0
R_LIST = [0.2, 0.5, 1.0, 2.0, 5.0]
C_EE = 800; J_EE = 0.3
C_IE = 800; J_IE = 0.35
C_EI = 400; J_EI = -1.2
C_II = 400; J_II = -1.0
C_EXT = 250; J_EXT = 0.7
ERF = np.vectorize(math.erf)

def B(x):
    o = np.empty_like(x); s = np.abs(x) < 1e-8
    o[s] = 1.0 - x[s]/2.0; xs = x[~s]; o[~s] = xs/np.expm1(xs); return o

def siegert_rate(mu, sigma, tau_m, tau_ref):
    if sigma <= 1e-9: return 0.0
    y_th = (V_TH-mu)/sigma; y_r = (V_RESET-mu)/sigma
    lo, hi = max(y_r,-12.0), min(y_th,12.0)
    if hi <= lo: return 0.0
    n = 2001
    u = np.linspace(lo,hi,n)
    f = np.exp(np.clip(u**2,0,300.0))*(1.0+ERF(u))
    h = (hi-lo)/(n-1)
    I = h/3.0*(f[0]+f[-1]+4.0*f[1:-1:2].sum()+2.0*f[2:-1:2].sum())
    return 1.0/(tau_ref+tau_m*math.sqrt(math.pi)*I)

def moments(nuE, nuI, nu_ext, loop):
    jIE = J_IE*loop; jEI = J_EI*loop
    muE = C_EXT*J_EXT*TAU_EXT*nu_ext + C_EE*J_EE*TAU_S_E*nuE + C_EI*jEI*TAU_S_I*nuI
    muI = C_EXT*J_EXT*TAU_EXT*nu_ext + C_IE*jIE*TAU_S_E*nuE + C_II*J_II*TAU_S_I*nuI
    sE2 = TAU_M_E*(C_EXT*J_EXT**2*nu_ext + C_EE*J_EE**2*nuE + C_EI*jEI**2*nuI)
    sI2 = TAU_M_I*(C_EXT*J_EXT**2*nu_ext + C_IE*jIE**2*nuE + C_II*J_II**2*nuI)
    return muE, math.sqrt(max(sE2,1e-12)), muI, math.sqrt(max(sI2,1e-12))

def fixed_point(nu_ext, loop):
    sols = []
    for s0 in ((0.005,0.005),(0.02,0.02),(0.001,0.001)):
        nuE, nuI = s0
        for _ in range(2000):
            muE,sE,muI,sI = moments(nuE,nuI,nu_ext,loop)
            nE = siegert_rate(muE,sE,TAU_M_E,TAU_REF_E)
            nI = siegert_rate(muI,sI,TAU_M_I,TAU_REF_I)
            nuE2 = 0.3*nE+0.7*nuE; nuI2 = 0.3*nI+0.7*nuI
            if abs(nuE2-nuE)+abs(nuI2-nuI) < 1e-12:
                nuE,nuI = nuE2,nuI2; break
            nuE,nuI = nuE2,nuI2
        sols.append((nuE,nuI))
    return sols

class Pop:
    def __init__(self, mu, sigma, tau_m, tau_ref, N=200, vlb=None):
        self.mu, self.sigma, self.tau_m, self.tau_ref = mu, sigma, tau_m, tau_ref
        V_LB = vlb if vlb is not None else min(-30.0, mu-6*sigma)
        D = sigma**2/(2.0*tau_m)
        vc = np.linspace(V_LB, V_TH, N+1); h = vc[1]-vc[0]
        vm = 0.5*(vc[:-1]+vc[1:])
        ve = vc[1:-1]  # interior edges
        ae = (-ve+mu)/tau_m; Pe = ae*h/D
        Bpos = B(Pe); Bneg = B(-Pe)
        Pth = ((-V_TH+mu)/tau_m)*h/D; Bm_th = float(B(-np.array([Pth]))[0]); Bp_th = float(B(np.array([Pth]))[0])
        c = D/h**2
        kr = int(np.argmin(np.abs(vm-V_RESET)))
        n = N+1; L = np.zeros((n,n)); ii = np.arange(1,N-1)
        L[0,0] = -c*Bneg[0]; L[0,1] = c*Bpos[0]
        L[ii,ii-1] = c*Bneg[ii-1]; L[ii,ii] = -c*(Bpos[ii-1]+Bneg[ii]); L[ii,ii+1] = c*Bpos[ii]
        L[N-1,N-2] = c*Bneg[-1]; L[N-1,N-1] = -c*(Bpos[-1]+Bm_th)
        L[kr,N] += 1.0/(tau_ref*h)
        t = np.zeros(N); t[N-1] = (D/h)*Bm_th
        L[N,:] = 0.0; L[N,N-1] = t[N-1]; L[N,N] = -1.0/tau_ref
        self.L, self.t, self.h, self.V_LB = L, t, h, V_LB
        Lc = L.copy(); Lc[N,:] = 0.0; Lc[N,:N] = h; Lc[N,N] = 1.0
        rhs = np.zeros(n); rhs[N] = 1.0
        x = np.linalg.solve(Lc, rhs)
        self.x0 = x; self.nu0 = float(t @ x[:N])
        self.negfrac = float(np.sum(x[:-1] < 0)/N)
        self.negmag = float(-np.min(x[:-1])/np.max(x[:-1])) if np.min(x[:-1]) < 0 else 0.0
        dd = max(0.05, 0.002*abs(mu))
        def asm(m):
            a2 = (-ve+m)/tau_m; P2 = a2*h/D
            Bo = B(P2); Bn = B(-P2)
            Pth2 = ((-V_TH+m)/tau_m)*h/D
            Bm2 = float(B(-np.array([Pth2]))[0])
            L2 = np.zeros((n,n))
            L2[0,0] = -c*Bn[0]; L2[0,1] = c*Bo[0]
            L2[ii,ii-1] = c*Bn[ii-1]; L2[ii,ii] = -c*(Bo[ii-1]+Bn[ii]); L2[ii,ii+1] = c*Bo[ii]
            L2[N-1,N-2] = c*Bn[-1]; L2[N-1,N-1] = -c*(Bo[-1]+Bm2)
            L2[kr,N] += 1.0/(tau_ref*h)
            t2 = np.zeros(N); t2[N-1] = (D/h)*Bm2
            L2[N,:] = 0.0; L2[N,N-1] = t2[N-1]; L2[N,N] = -1.0/tau_ref
            return L2, t2
        Lp,tp = asm(mu+dd); Lm,tm = asm(mu-dd)
        self.dL = (Lp-Lm)/(2*dd); self.dt = (tp-tm)/(2*dd)
        self.b = self.dL @ x
        self.dnu = (siegert_rate(mu+0.1,sigma,tau_m,tau_ref)-siegert_rate(mu-0.1,sigma,tau_m,tau_ref))/0.2

    def chi(self, freqs):
        n = self.L.shape[0]
        I = np.eye(n)
        rhs = self.b.copy(); rhs[n-1] = 0.0
        out = np.zeros(len(freqs), dtype=complex)
        for k,f in enumerate(freqs):
            w = 2*np.pi*f/1000.0
            M = 1j*w*I - self.L; M[n-1,:] = 0.0; M[n-1,:n-1] = self.h; M[n-1,n-1] = 1.0
            x1 = np.linalg.solve(M, rhs)
            out[k] = complex(self.t @ x1[:n-1]) + float(self.dt @ self.x0[:n-1])
        return out

def analyze(nu_ext_Hz, loop, N=200, nf=60, fmax=150.0):
    nu_ext = nu_ext_Hz/1000.0
    sols = fixed_point(nu_ext, loop)
    nuE, nuI = sols[0]
    muE,sE,muI,sI = moments(nuE,nuI,nu_ext,loop)
    E = Pop(muE,sE,TAU_M_E,TAU_REF_E,N=N)
    I = Pop(muI,sI,TAU_M_I,TAU_REF_I,N=N)
    freqs = np.linspace(2,fmax,nf)
    chiE = E.chi(freqs); chiI = I.chi(freqs)
    def coupling(g, tau_s):
        w = 2*np.pi*freqs/1000.0
        return g/(1.0+1j*w*tau_s)
    gEE = C_EE*J_EE*TAU_S_E; gIE = C_IE*(J_IE*loop)*TAU_S_E
    gEI = C_EI*(J_EI*loop)*TAU_S_I; gII = C_II*J_II*TAU_S_I
    AEE = coupling(gEE,TAU_S_E); AII = coupling(gII,TAU_S_I)
    AEI0 = coupling(gEI,TAU_S_I); AIE0 = coupling(gIE,TAU_S_E)
    def band_min(D, flo=30.0, fhi=90.0):
        m = (freqs>=flo)&(freqs<=fhi)
        idxs = np.where(m)[0]; k = int(np.argmin(np.abs(D[m]))); idx = idxs[k]
        return float(freqs[idx]), float(abs(D[idx])), idx
    per_r, Db = {}, {}
    for r in R_LIST:
        dEI = r*T_STAR/(1+r); dIE = T_STAR/(1+r)
        w = 2*np.pi*freqs/1000.0
        AEI = AEI0*np.exp(-1j*w*dEI); AIE = AIE0*np.exp(-1j*w*dIE)
        D = (1-chiE*AEE)*(1-chiI*AII) - chiE*AEI*chiI*AIE
        Db[r] = D
        ratio = (1-chiI*AII)/(chiI*AIE)
        ph = np.angle(ratio)
        fstar, m, idx = band_min(D)
        per_r[str(r)] = dict(fstar=fstar, minabs=m, phase=float(ph[idx]), dEI=dEI, dIE=dIE)
    D0 = (1-chiE*AEE)*(1-chiI*AII) - chiE*AEI0*chiI*AIE0
    f0,m0,_ = band_min(D0)
    return dict(sols=sols, nuE=nuE*1000, nuI=nuI*1000, muE=muE, sE=sE, muI=muI, sI=sI,
                Efp=E.nu0*1000, Ifp=I.nu0*1000, Esieg=siegert_rate(muE,sE,TAU_M_E,TAU_REF_E)*1000,
                Isieg=siegert_rate(muI,sI,TAU_M_I,TAU_REF_I)*1000,
                chi0E=float(chiE[0].real), dnuE=E.dnu, chi0I=float(chiI[0].real), dnuI=I.dnu,
                Eneg=(E.negfrac,E.negmag), Ineg=(I.negfrac,I.negmag),
                per_r=per_r, Db=Db, freqs=freqs, chiE=chiE, chiI=chiI,
                zero=(f0,m0))

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "scan":
        print("loop nueHz nuE nuI muE muI | f*(30-90) min|D|", flush=True)
        for loop in [0.6, 1.0, 1.5, 2.0, 2.5]:
            for nue in [14, 18, 24, 30]:
                try:
                    a = analyze(nue, loop, N=120, nf=40)
                    r1 = a["per_r"]["1.0"]
                    print(f"L={loop} nue={nue}: nuE={a['nuE']:.1f} nuI={a['nuI']:.1f} "
                          f"muE={a['muE']:.1f} muI={a['muI']:.1f} | f*={r1['fstar']:.1f} min|D|={r1['minabs']:.3f} "
                          f"FPchk=({a['Efp']:.2f},{a['Ifp']:.2f})vsSieg=({a['Esieg']:.2f},{a['Isieg']:.2f}) "
                          f"chi0=({a['chi0E']:.4f}/{a['dnuE']:.4f},{a['chi0I']:.4f}/{a['dnuI']:.4f})", flush=True)
                except Exception as e:
                    print(f"L={loop} nue={nue}: FAIL {e}", flush=True)
        print(f"SCAN DONE t={time.time()-T0:.0f}s", flush=True)
    else:
        loop = float(sys.argv[1]) if len(sys.argv) > 1 else 2.0
        nue = float(sys.argv[2]) if len(sys.argv) > 2 else 24.0
        a = analyze(nue, loop, N=250, nf=80)
        print(f"OPERATING L={loop} nue={nue}: nuE={a['nuE']:.2f} nuI={a['nuI']:.2f} "
              f"muE={a['muE']:.2f} sE={a['sE']:.2f} muI={a['muI']:.2f} sI={a['sI']:.2f}", flush=True)
        print(f"FP vs Siegert: E {a['Efp']:.3f} vs {a['Esieg']:.3f} | I {a['Ifp']:.3f} vs {a['Isieg']:.3f}", flush=True)
        print(f"chi(0) vs dnu/dmu: E {a['chi0E']:.4f} vs {a['dnuE']:.4f} | I {a['chi0I']:.4f} vs {a['dnuI']:.4f}", flush=True)
        print(f"negativity E frac={a['Eneg'][0]:.3f} mag={a['Eneg'][1]:.2e} | I frac={a['Ineg'][0]:.3f} mag={a['Ineg'][1]:.2e}", flush=True)
        for r in R_LIST:
            d = a["per_r"][str(r)]
            print(f"r={r:4}: f*={d['fstar']:6.2f}Hz min|D|={d['minabs']:.4f} phase(E-I)={d['phase']:+.3f}rad (dEI={d['dEI']:.2f},dIE={d['dIE']:.2f})", flush=True)
        inv = max(float(np.max(np.abs(a["Db"][r]-a["Db"][1.0]))) for r in R_LIST)
        rel = inv/float(np.max(np.abs(a["Db"][1.0])))
        print(f"INVARIANCE max|D_r-D_1|={inv:.3e} rel={rel:.3e}", flush=True)
        print(f"ZERO-DELAY f*={a['zero'][0]:.1f}Hz min|D|={a['zero'][1]:.4f}", flush=True)
        json.dump(dict(params=dict(loop=loop, nu_ext_Hz=nue, T_star=T_STAR),
                       rates_Hz=dict(nuE=a["nuE"], nuI=a["nuI"]),
                       moments=dict(muE=a["muE"], sE=a["sE"], muI=a["muI"], sI=a["sI"]),
                       fp_check=dict(Efp=a["Efp"], Esieg=a["Esieg"], Ifp=a["Ifp"], Isieg=a["Isieg"],
                                     chi0E=a["chi0E"], dnuE=a["dnuE"], chi0I=a["chi0I"], dnuI=a["dnuI"],
                                     Eneg=a["Eneg"], Ineg=a["Ineg"]),
                       per_r=a["per_r"], invariance=dict(maxabs=inv, rel=rel),
                       zero_delay=dict(fstar=a["zero"][0], minabs=a["zero"][1])),
                  open("output/artifacts/meanfield_results.json","w"), indent=1)
        np.savez("output/artifacts/meanfield_curves.npz", freqs=a["freqs"],
                 **{f"D_{r}": a["Db"][r] for r in R_LIST}, chiE=a["chiE"], chiI=a["chiI"])
        print(f"DONE t={time.time()-T0:.0f}s", flush=True)
