import sys
sys.path.insert(0,'output/artifacts')
import numpy as np
from fp import LIF_FP
# dominant root for config A (mu0=15.36,sig=5,Jeff=-600): scan complex s grid + refine
N=500; TAUS=2.0; D=4.0; MU0=15.360; SIG0=5.0; JEFF=-600.0
fp=LIF_FP(N=N)
_,nu=fp.stationary(MU0,SIG0)
print(f"nu0={nu*1000:.2f}")
pext=np.zeros(N+1); pext[:N]=fp.p0
dp=np.gradient(pext,fp.dV)[:N]
fvec=-(1.0/fp.tau_m)*dp
Lmat=fp.Lmat; I=np.eye(N)
svec=np.zeros(N); svec[fp.iR]=1.0/fp.dV
cBm=fp.c*fp.Bm[fp.N-1]
def F(s,sigD):
    alpha=1.0/(1.0+s*fp.tref)
    M=s*I+Lmat
    # solve (M)p1 - alpha s nu1 = f ; flux nu1
    A=np.zeros((N+1,N+1),dtype=complex)
    A[:N,:N]=M; A[:N,N]=-alpha*svec
    A[N,N-1]=cBm; A[N,N]=-1.0
    b=np.zeros(N+1,dtype=complex); b[:N]=fvec
    try: x=np.linalg.solve(A,b)
    except: return np.nan
    Aval=x[N]
    Hs=1/(1+s*TAUS)
    L=np.exp(-s*D) if sigD<=1e-9 else (1+(sigD**2/D)*s)**(-(D**2/sigD**2))
    return 1-JEFF*TAUS*Hs*Aval*L
for sigD in [0.0,1.0,1.1,1.25,1.5,2.0]:
    print(f"== sigD={sigD}")
    # scan lam in [-0.05,0.15], f in [55,75]
    best=None
    for lam in [-0.05,0.0,0.03,0.06,0.1]:
        for f in [58,62,65,68,72]:
            s=lam+1j*2*np.pi*f/1000
            v=F(s,sigD)
            if best is None or abs(v)<abs(best[0]): best=(v,lam,f)
    print(f"  coarse best |F|={abs(best[0]):.3f} lam={best[1]} f={best[2]} F={best[0]:.3f}")
    # refine lam at f~65
    for f in [65.0]:
        for lam in np.arange(-0.06,0.16,0.02):
            s=lam+1j*2*np.pi*f/1000
            v=F(s,sigD)
            print(f"   lam={lam:+.2f} f={f} |F|={abs(v):.3f} F={v.real:+.3f}{v.imag:+.3f}j")
