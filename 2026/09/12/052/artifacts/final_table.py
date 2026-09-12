import sys
sys.path.insert(0,'output/artifacts')
import numpy as np
from fp import LIF_FP
N=600; TAUS=2.0; D=4.0; MU0=15.36; SIG0=5.0; JEFF=-600.0
fp=LIF_FP(N=N)
_,nu=fp.stationary(MU0,SIG0)
fs=np.arange(40,130.01,0.25)
A=fp.susceptibility(MU0,SIG0,fs)
rows=[]
for sigD in [0.0,0.5,0.75,1.0,1.1,1.125,1.25,1.5,2.0,2.5,3.0,4.0]:
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
    rows.append((sigD,)+ (gb[0] if gb else (float('nan'),float('nan'))))
for r in rows:
    print(f"sigD={r[0]:5.3f} f*={r[1]:6.2f} Jc={r[2]:8.0f} ratio={abs(JEFF/r[2]):.3f}" if r[1]==r[1] else f"sigD={r[0]:5.3f} none")
# dominant-F value at crossing: loop gain at f*
print("nu0=",nu*1000)
