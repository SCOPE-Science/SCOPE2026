"""Stage 1: scan coupling/drive params for baseline-stable + rho-Hopf structure.
Model: exact MPR E-I mass, 6D (rE,vE,rI,vI,sE,sI), time unit ms, rates 1/ms.
"""
import numpy as np, json

PI = np.pi

def fp_solve(DE, DI, p, nstarts=6):
    tau, eE, eI = p['tau'], p['etaE'], p['etaI']
    JEE, JEI, JIE, JII = p['JEE'], p['JEI'], p['JIE'], p['JII']
    sols = []
    inits = [(0.02,-2,0.05,-3),(0.05,1,0.08,0),(0.01,-5,0.02,-5),
             (0.08,0,0.1,-1),(0.03,-1,0.03,-1),(0.06,-3,0.04,-4)]
    for (rE0,vE0,rI0,vI0) in inits[:nstarts]:
        x = np.array([rE0,vE0,rI0,vI0])
        ok = False
        for _ in range(200):
            rE,vE,rI,vI = x
            F = np.array([
                DE/(PI*tau**2) + 2*rE*vE/tau,
                vE**2 + eE + tau*(JEE*rE+JEI*rI) - (PI*tau*rE)**2,
                DI/(PI*tau**2) + 2*rI*vI/tau,
                vI**2 + eI + tau*(JIE*rE+JII*rI) - (PI*tau*rI)**2])
            if np.max(np.abs(F)) < 1e-13:
                ok = True; break
            aE = 2*vE/tau; bE = 2*rE/tau
            cE = 2*vE; dE = tau*JEE - 2*(PI*tau)**2*rE
            eE_ = tau*JEI; fE = 0.0
            aI = 2*vI/tau; bI = 2*rI/tau
            cI = 2*vI; dI = tau*JII - 2*(PI*tau)**2*rI
            eI_ = tau*JIE
            J = np.array([
              [aE,bE,0,0],
              [dE,cE,eE_,0],
              [0,0,aI,bI],
              [eI_,0,dI,cI]])
            # order x=(rE,vE,rI,vI): F1 deps rE,vE; F2 deps rE,vE,rI; F3 deps rI,vI; F4 deps rE,rI,vI
            try:
                dx = np.linalg.solve(J,F)
            except np.linalg.LinAlgError:
                break
            x = x - dx
            x[0]=max(x[0],1e-6); x[2]=max(x[2],1e-6)
            x = np.clip(x,[-0.0,-50,0.0,-50],[0.5,50,0.6,50])
        if ok and x[0]>1e-5 and x[2]>1e-5:
            if not any(np.max(np.abs(x-s))<1e-6 for s in sols):
                sols.append(x.copy())
    return sols

def jac6(fp, DE, DI, p):
    tau = p['tau']
    tE,tI = p['tauSE'], p['tauSI']
    JEE,JEI,JIE,JII = p['JEE'],p['JEI'],p['JIE'],p['JII']
    rE,vE,rI,vI = fp
    J = np.zeros((6,6))
    J[0,0]=2*vE/tau; J[0,1]=2*rE/tau
    J[1,0]=-2*PI**2*tau*rE; J[1,1]=2*vE/tau; J[1,4]=JEE; J[1,5]=JEI
    J[2,2]=2*vI/tau; J[2,3]=2*rI/tau
    J[3,2]=-2*PI**2*tau*rI; J[3,3]=2*vI/tau; J[3,4]=JIE; J[3,5]=JII
    J[4,0]=1/tE; J[4,4]=-1/tE
    J[5,2]=1/tI; J[5,5]=-1/tI
    return J

def maxeig(fp,DE,DI,p):
    w = np.linalg.eigvals(jac6(fp,DE,DI,p))
    i = np.argmax(w.real)
    return w[i], w

def spec_peak_ratio(fp,DE,DI,p):
    """Linear response peak of y=rE+rI to white noise on vE,vI: max over
    30-100 Hz divided by value at 5 Hz. Crude no-peak metric."""
    import numpy.linalg as la
    A = jac6(fp,DE,DI,p); C = np.array([1,0,1,0,0,0])
    B = np.zeros((6,2)); B[1,0]=1.0; B[3,1]=1.0
    def H(f):
        s = 2j*PI*f/1000.0  # f Hz -> 1/ms angular
        X = la.solve(s*np.eye(6)-A, B)
        return np.sum(np.abs(C@X)**2)
    f = np.concatenate([np.array([5.0]), np.linspace(30,100,36)])
    vals = np.array([H(x) for x in f])
    return vals[1:].max()/vals[0]

def track(p):
    S=2.0
    rhos = np.concatenate([np.linspace(0.1,1,25), np.linspace(1.05,10,25)])
    DE = S*rhos/(1+rhos); DI = S/(1+rhos)
    # baseline
    sols = fp_solve(1.0,1.0,p)
    if not sols: return None
    # pick lowest-rate physical fp
    sols.sort(key=lambda s: s[0]+s[2])
    fp0 = sols[0]
    lam0,_ = maxeig(fp0,1.0,1.0,p)
    if lam0.real >= -0.001: return None  # need stable baseline w/ margin
    pr = spec_peak_ratio(fp0,1.0,1.0,p)
    if pr > 4.0: return None  # baseline must have no gamma peak
    # warm-start continuation from rho=1 both directions
    order = np.argsort(np.abs(np.log(rhos)))
    fps = {}; fps[1.0]=fp0
    # do each side sequentially
    for side in ['lo','hi']:
        if side=='lo': seq=[r for r in rhos if r<1][::-1]
        else: seq=[r for r in rhos if r>1]
        fp_prev = fp0
        for r in seq:
            dE=S*r/(1+r); dI=S/(1+r)
            # newton warm start single
            x=fp_prev.copy()
            ok=False
            for _ in range(100):
                rE,vE,rI,vI=x
                F=np.array([dE/(PI*p['tau']**2)+2*rE*vE/p['tau'],
                  vE**2+p['etaE']+p['tau']*(p['JEE']*rE+p['JEI']*rI)-(PI*p['tau']*rE)**2,
                  dI/(PI*p['tau']**2)+2*rI*vI/p['tau'],
                  vI**2+p['etaI']+p['tau']*(p['JIE']*rE+p['JII']*rI)-(PI*p['tau']*rI)**2])
                if np.max(np.abs(F))<1e-12: ok=True;break
                Jm=np.array([[2*vE/p['tau'],2*rE/p['tau'],0,0],
                  [p['tau']*p['JEE']-2*(PI*p['tau'])**2*rE,2*vE,p['tau']*p['JEI'],0],
                  [0,0,2*vI/p['tau'],2*rI/p['tau']],
                  [p['tau']*p['JIE'],0,p['tau']*p['JII']-2*(PI*p['tau'])**2*rI,2*vI]])
                try: dx=np.linalg.solve(Jm,F)
                except: break
                x=x-dx; x[0]=max(x[0],1e-6);x[2]=max(x[2],1e-6)
            if not ok:
                ss=fp_solve(dE,dI,p)
                if not ss: break
                x=min(ss,key=lambda s: np.sum((s-fp_prev)**2))
            fps[r]=x.copy(); fp_prev=x.copy()
    # scan maxRe
    curve=[]
    for r in rhos:
        if r not in fps: curve.append(np.nan); continue
        lam,_=maxeig(fps[r],S*r/(1+r),S/(1+r),p)
        curve.append(lam.real)
    curve=np.array(curve)
    # find crossings from below (stable->unstable) on either side
    res={'fp0':fp0,'lam0':lam0,'peak0':pr,'curve':curve,'rhos':rhos,'fps':fps}
    return res

base = dict(tau=10.0, tauSE=2.0, tauSI=8.0, JEE=6.0, JII=-4.0,
            JEI=0.0, JIE=0.0, etaE=0.0, etaI=0.0)
cands=[]
for JEI in [-10,-14,-18,-24,-30]:
    for JIE in [8,12,16,20]:
        for etaE in [1.0,2.0,3.0]:
            for etaI in [-1.0,0.0,1.0]:
                p=dict(base); p.update(JEI=float(JEI),JIE=float(JIE),etaE=etaE,etaI=etaI)
                r=track(p)
                if r is None: continue
                cu=r['curve']; rh=r['rhos']
                # crossing indices where curve goes - to +
                cross=[]
                for k in range(len(rh)-1):
                    if np.isnan(cu[k]) or np.isnan(cu[k+1]): continue
                    if cu[k]<0 and cu[k+1]>0:
                        # need oscillatory (imag nonzero at dest)
                        lam,_=maxeig(r['fps'][rh[k+1]],2*rh[k+1]/(1+rh[k+1]),2/(1+rh[k+1]),p)
                        f=abs(lam.imag)*1000/(2*PI)
                        cross.append((rh[k],rh[k+1],f))
                if cross:
                    cands.append((p,r['lam0'],r['peak0'],cross,p.copy()))
                else:
                    # record max destabilization approach
                    pass
print("num cand:",len(cands))
for (p,lam0,pr,cross,pp) in cands[:40]:
    print({k:pp[k] for k in ['JEI','JIE','etaE','etaI']},
          'lam0=',round(float(lam0.real),4),'f0mode=',round(float(abs(lam0.imag)*1000/(2*PI)),1),
          'peak0=',round(float(pr),2),'cross=',[(round(a,3),round(b,3),round(f,1)) for a,b,f in cross])
