"""Stage 5: lock candidate, bisect rho_c, characterize Hopf, cycle, spectra."""
import numpy as np, json
exec(open('output/artifacts/scan1.py').read().split("base =")[0])

P = dict(tau=5.0, tauSE=2.0, tauSI=4.0, JEE=6.0, JII=-6.0, JEI=-20.0, JIE=8.0, etaE=1.0, etaI=-2.0)
S = 2.0
def d_of(r): return S*r/(1+r), S/(1+r)

def cont_fp(r, fp_guess):
    dE,dI = d_of(r)
    x = fp_guess.copy()
    for _ in range(200):
        rE,vE,rI,vI = x
        F = np.array([dE/(np.pi*P['tau']**2)+2*rE*vE/P['tau'],
          vE**2+P['etaE']+P['tau']*(P['JEE']*rE+P['JEI']*rI)-(np.pi*P['tau']*rE)**2,
          dI/(np.pi*P['tau']**2)+2*rI*vI/P['tau'],
          vI**2+P['etaI']+P['tau']*(P['JIE']*rE+P['JII']*rI)-(np.pi*P['tau']*rI)**2])
        if np.max(np.abs(F)) < 1e-13: return x, True
        Jm = np.array([[2*vE/P['tau'],2*rE/P['tau'],0,0],
          [P['tau']*P['JEE']-2*(np.pi*P['tau'])**2*rE,2*vE,P['tau']*P['JEI'],0],
          [0,0,2*vI/P['tau'],2*rI/P['tau']],
          [P['tau']*P['JIE'],0,P['tau']*P['JII']-2*(np.pi*P['tau'])**2*rI,2*vI]])
        try: dx = np.linalg.solve(Jm,F)
        except Exception: return x, False
        x = x - dx; x[0]=max(x[0],1e-9); x[2]=max(x[2],1e-9)
    return x, False

# baseline
sols = fp_solve(1.0,1.0,P)
sols.sort(key=lambda s: s[0]+s[2])
fp0 = sols[0]
lam0,w0 = maxeig(fp0,1.0,1.0,P)
print("n fps @rho=1:", len(sols))
print("fp0:", fp0, "lam0:", lam0, "peak0:", spec_peak_ratio(fp0,1.0,1.0,P))
for s in sols:
    lam,_ = maxeig(s,1.0,1.0,P)
    print("  fp:", np.round(s,5), "maxRe:", round(float(lam.real),5), "fmode:", round(float(abs(lam.imag)*1000/(2*np.pi)),2))

# fine curve rho in [0.1,10]
rhos = np.concatenate([np.linspace(0.1,1,40), np.linspace(1.02,10,120)])
fps={}; fp_prev=fp0; okcount=0
# continue upward from 1
seq_up = sorted([r for r in rhos if r>=1.0]); seq_lo = sorted([r for r in rhos if r<1.0], reverse=True)
fps[1.0]=fp0
for seq in [seq_up[1:], seq_lo]:
    fp_prev = fp0
    for r in seq:
        x,ok = cont_fp(r, fp_prev)
        if ok: fps[r]=x; fp_prev=x; okcount+=1
        else:
            ss = fp_solve(*d_of(r),P)
            if ss:
                x2=min(ss,key=lambda s: np.sum((s-fp_prev)**2)); fps[r]=x2; fp_prev=x2
print("continued:", okcount, "/", len(rhos))

curve=[]
for r in rhos:
    if r not in fps: curve.append((np.nan,np.nan)); continue
    lam,_ = maxeig(fps[r],*d_of(r),P)
    curve.append((lam.real, abs(lam.imag)*1000/(2*np.pi)))
curve=np.array(curve)
# print sign changes
for k in range(len(rhos)-1):
    a,b = curve[k][0], curve[k+1][0]
    if np.isnan(a) or np.isnan(b): continue
    flag = ""
    if a<0 and b>0: flag=" <-- STABLE->UNSTABLE"
    if a>0 and b<0: flag=" <-- UNSTABLE->STABLE"
    if flag or k%20==0:
        print(f"rho={rhos[k]:.3f} maxRe={a:+.5f} f={curve[k][1]:.1f}Hz{flag}")
print(f"rho={rhos[-1]:.3f} maxRe={curve[-1][0]:+.5f} f={curve[-1][1]:.1f}Hz")
# also low side
for k in range(0,40,5):
    print(f"lo rho={rhos[k]:.3f} maxRe={curve[k][0]:+.5f} f={curve[k][1]:.1f}Hz")

# bisection of first upward crossing
k0=None
for k in range(len(rhos)-1):
    a,b=curve[k][0],curve[k+1][0]
    if np.isnan(a)or np.isnan(b): continue
    if a<0 and b>0 and rhos[k]>=1.0: k0=k; break
print("first up-cross idx:", k0, rhos[k0] if k0 is not None else None, rhos[k0+1] if k0 is not None else None)
if k0 is not None:
    lo,hi = rhos[k0],rhos[k0+1]
    flo = fps[lo].copy(); fhi=fps[hi].copy()
    for _ in range(40):
        mid=(lo+hi)/2
        xm,ok=cont_fp(mid,(flo+fhi)/2)
        lam,_=maxeig(xm,*d_of(mid),P)
        if lam.real<0: lo,flo=mid,xm
        else: hi,fhi=mid,xm
    rhoc=(lo+hi)/2
    xmc,_=cont_fp(rhoc,(flo+fhi)/2)
    lamc,wc=maxeig(xmc,*d_of(rhoc),P)
    fc=abs(lamc.imag)*1000/(2*np.pi)
    print("rho_c =",rhoc," fc =",fc," lamc=",lamc," fp=",xmc)
    # transversality: d Re/d rho
    e=1e-3
    xp,_=cont_fp(rhoc+e,xmc); xm,_=cont_fp(rhoc-e,xmc)
    lp,_=maxeig(xp,*d_of(rhoc+e),P); lm,_=maxeig(xm,*d_of(rhoc-e),P)
    print("dRe/drho ~", (lp.real-lm.real)/(2*e))
    # eigenvector at crit
    A=jac6(xmc,*d_of(rhoc),P)
    w2,V=np.linalg.eig(A)
    i=np.argmax(w2.real)
    print("crit eig:",w2[i]," other Re:",np.sort(w2.real))
    print("eigvec:",V[:,i]/V[:,i][np.argmax(np.abs(V[:,i]))])
    json.dump({"rho_c":float(rhoc),"fc":float(fc),"fp_crit":xmc.tolist(),
      "lam_crit":[float(lamc.real),float(lamc.imag)],
      "transv":float((lp.real-lm.real)/(2*e)),
      "P":P}, open("output/artifacts/bisect.json","w"), indent=1)
