"""Stage 6: mean-field limit cycle beyond rho_c: integrate 6D, measure freq/amps/phase + stability via Floquet-less check (decay test on other side)."""
import numpy as np, json
exec(open('output/artifacts/scan1.py').read().split("base =")[0])
P = dict(tau=5.0, tauSE=2.0, tauSI=4.0, JEE=6.0, JII=-6.0, JEI=-20.0, JIE=8.0, etaE=1.0, etaI=-2.0)
S=2.0
def d_of(r): return S*r/(1+r), S/(1+r)
B=json.load(open("output/artifacts/bisect.json")); rhoc=B["rho_c"]; print("rhoc:",rhoc,"fc:",B["fc"])

def rhs(y,DE,DI):
    rE,vE,rI,vI,sE,sI=y; tau=P['tau']
    return np.array([
      DE/(np.pi*tau**2)+2*rE*vE/tau,
      (vE**2+P['etaE']+tau*(P['JEE']*sE+P['JEI']*sI)-(np.pi*tau*rE)**2)/tau,
      DI/(np.pi*tau**2)+2*rI*vI/tau,
      (vI**2+P['etaI']+tau*(P['JIE']*sE+P['JII']*sI)-(np.pi*tau*rI)**2)/tau,
      (-sE+rE)/P['tauSE'], (-sI+rI)/P['tauSI']])

def run(rho,T=3000.0,dt=0.05,trans=1500.0,pert=1e-3):
    DE,DI=d_of(rho)
    fp=np.array(B["fp_crit"]) if abs(rho-rhoc)<0.01 else None
    # get fp by continuation: use crit fp as guess via simple newton inline
    import subprocess
    x = np.array(B["fp_crit"]) if fp is not None else np.array([0.05,-0.8,0.03,-0.8])
    # newton
    for _ in range(100):
        rE,vE,rI,vI=x
        F=np.array([DE/(np.pi*P['tau']**2)+2*rE*vE/P['tau'],
          vE**2+P['etaE']+P['tau']*(P['JEE']*rE+P['JEI']*rI)-(np.pi*P['tau']*rE)**2,
          DI/(np.pi*P['tau']**2)+2*rI*vI/P['tau'],
          vI**2+P['etaI']+P['tau']*(P['JIE']*rE+P['JII']*rI)-(np.pi*P['tau']*rI)**2])
        if np.max(np.abs(F))<1e-12: break
        Jm=np.array([[2*vE/P['tau'],2*rE/P['tau'],0,0],
          [P['tau']*P['JEE']-2*(np.pi*P['tau'])**2*rE,2*vE,P['tau']*P['JEI'],0],
          [0,0,2*vI/P['tau'],2*rI/P['tau']],
          [P['tau']*P['JIE'],0,P['tau']*P['JII']-2*(np.pi*P['tau'])**2*rI,2*vI]])
        x=x-np.linalg.solve(Jm,F); x[0]=max(x[0],1e-9);x[2]=max(x[2],1e-9)
    y=np.array([x[0],x[1],x[2],x[3],x[0],x[2]])*(1+pert*np.array([1,-0.5,1,0.3,1,1]))
    n=int(T/dt); nt=int(trans/dt)
    t=np.arange(n)*dt
    rEs=np.empty(n); rIs=np.empty(n)
    for i in range(n):
        # RK4
        k1=rhs(y,DE,DI); k2=rhs(y+0.5*dt*k1,DE,DI); k3=rhs(y+0.5*dt*k2,DE,DI); k4=rhs(y+dt*k3,DE,DI)
        y=y+dt*(k1+2*k2+2*k3+k4)/6
        rEs[i]=y[0]; rIs[i]=y[2]
    seg_E=rEs[nt:]*1000; seg_I=rIs[nt:]*1000  # Hz
    # cycle metrics: peak-to-peak, mean, freq via FFT
    mE=seg_E.mean(); mI=seg_I.mean()
    aE=(seg_E.max()-seg_E.min())/2; aI=(seg_I.max()-seg_I.min())/2
    dt_s=dt/1000
    F=np.fft.rfft(seg_E-mE); fr=np.fft.rfftfreq(len(seg_E),dt_s)
    band=(fr>=5)&(fr<=150)
    fpk=fr[band][np.argmax(np.abs(F[band]))]
    # phase lag E->I at fpk via cross spectrum
    FI=np.fft.rfft(seg_I-mI)
    k=np.argmin(np.abs(fr-fpk))
    ph=np.angle(FI[k]/F[k])  # + means I leads E? define I-minus-E phase
    # check decay vs persist: amplitude in last quarter vs third quarter
    q=len(seg_E)//4
    a1=(seg_E[q:2*q].max()-seg_E[q:2*q].min())
    a2=(seg_E[3*q:].max()-seg_E[3*q:].min())
    return dict(rho=rho,meanE=float(mE),meanI=float(mI),ampE=float(aE),ampI=float(aI),
      f=float(fpk),phaseIE=float(ph),persist=float(a2/max(a1,1e-12)),fp=x.tolist())

for rho in [1.0, 2.0, 2.5453391692019522, 2.8, 3.2, 4.0, 6.0]:
    r=run(rho)
    print(f"rho={rho:.3f} f={r['f']:.1f}Hz mE={r['meanE']:.1f} mI={r['meanI']:.1f} aE={r['ampE']:.2f} aI={r['ampI']:.2f} ph(I-E)={r['phaseIE']:.2f} persist={r['persist']:.2f}")
    json.dump(r, open(f"output/artifacts/cycle_rho{rho:.3f}.json","w"), indent=1)
