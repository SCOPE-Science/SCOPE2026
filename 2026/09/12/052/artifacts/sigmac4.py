import sys
sys.path.insert(0,'output/artifacts')
import numpy as np
from fp import LIF_FP
N=600; TAUS=2.0; D=4.0
jobs=[(28.0,5.0,-600.0,15.360),(34.0,5.0,-800.0,15.660)]
for (mu_ext,sig0,Jeff,mu0) in jobs:
    fp=LIF_FP(N=N)
    _,nu=fp.stationary(mu0,sig0)
    print(f"muext={mu_ext} Jeff={Jeff}: mu0={mu0:.3f} nu0={nu*1000:.2f}Hz")
    fs=np.arange(30,140.01,0.25)
    A=fp.susceptibility(mu0,sig0,fs)
    print(" A done",flush=True)
    prev=None
    for sigD in [0.0,0.25,0.5,0.75,1.0,1.25,1.5,1.75,2.0,2.5,3.0,3.5,4.0]:
        G=np.zeros_like(A)
        for i,(f,a) in enumerate(zip(fs,A)):
            w=2*np.pi*f/1000
            Hs=1/(1+1j*w*TAUS)
            L=np.exp(-1j*w*D) if sigD<=1e-9 else (1+1j*(sigD**2/D)*w)**(-(D**2/sigD**2))
            G[i]=Hs*a*L
        cands=[]
        for i in range(len(fs)-1):
            if G[i].imag*G[i+1].imag<0:
                t=abs(G[i].imag)/(abs(G[i].imag)+abs(G[i+1].imag))
                f0=fs[i]*(1-t)+fs[i+1]*t; r0=G[i].real*(1-t)+G[i+1].real*t
                if r0<0: cands.append((f0,1/(TAUS*r0)))
        gb=[c for c in cands if 30<=c[0]<=120]
        if gb:
            f0,Jc=gb[0]
            st='UNSTABLE' if abs(Jeff)>abs(Jc) else 'stable'
            print(f"  sigD={sigD}: f*={f0:.2f} Jc={Jc:.0f} {st} ratio={abs(Jeff/Jc):.3f}")
        else: print(f"  sigD={sigD}: no gamma crossing stable")
