"""Exact identity and trajectory checks for two-stage counteracting networks.
Only mathematical reproducibility; standard Python, NumPy and SciPy.
"""
from fractions import Fraction as Q
from math import log,exp
import random
import numpy as np
from scipy.integrate import solve_ivp

def phi(z):
    return z-1-log(z)

def rhs(time,y,A,m):
    n=len(y)//2
    u=np.asarray(y[:n]);v=np.asarray(y[n:]);
    return np.r_[m*(v-u)+u*(2-u-v+A@u), m*(u-v)+v*(2-u-v-A@v)]

def exact_derivative_check():
    r=random.Random(1729)
    for n in (3,4,5,7):
        for repetition in range(12):
            M=[[Q(0) for _ in range(n)] for _ in range(n)]
            # elementary cycle matrices guarantee zero row sums
            for k in range(n-2):
                a=Q(r.randrange(-9,10),r.randrange(1,7))
                for i,j in ((0,k+1),(k+1,k+2),(k+2,0)):
                    M[i][j]+=a;M[j][i]-=a
            assert all(sum(row)==0 for row in M)
            assert all(M[i][j]==-M[j][i] for i in range(n) for j in range(n))
            u=[Q(r.randrange(2,25),7) for _ in range(n)]
            v=[Q(r.randrange(2,25),7) for _ in range(n)]
            m=Q(r.randrange(2,13))
            du=[m*(v[i]-u[i])+u[i]*(2-u[i]-v[i]+sum(M[i][j]*u[j] for j in range(n))) for i in range(n)]
            dv=[m*(u[i]-v[i])+v[i]*(2-u[i]-v[i]-sum(M[i][j]*v[j] for j in range(n))) for i in range(n)]
            derivative=sum((1-Q(1,u[i]))*du[i]+(1-Q(1,v[i]))*dv[i] for i in range(n))
            dissip=-sum((u[i]+v[i]-2)**2+m*(u[i]-v[i])**2/(u[i]*v[i]) for i in range(n))
            assert derivative==dissip,(n,derivative,dissip)
    print('PASS exact rational entropy identities: 48 tests, 3/4/5/7 populations')

def solve_scalar(V,low):
    if V==0: return 1.
    if low:
        lo,hi=exp(-max(1.,V+3)),1.
        while phi(lo)<V:lo*=0.1
    else:
        lo,hi=1.,max(3.,V+3.)
        while phi(hi)<V:hi*=2
    for i in range(110):
        md=(lo+hi)/2
        if (phi(md)>V)==low:lo=md
        else:hi=md
    return (lo+hi)/2

def numerical_check():
    n=5
    B=np.zeros((n,n),float)
    for k,a in [(1,20.),(2,-17.),(3,41.)]:
        for i,j in ((0,k),(k,k+1),(k+1,0)):
            B[i,j]+=a;B[j,i]-=a
    assert np.max(np.abs(B+B.T))<1e-12
    assert np.max(np.abs(B@np.ones(n)))<1e-12
    def A(t):return (1+0.4*np.sin(5*t)+0.2*np.cos(13*t))*B
    m_min=2.4
    def m(t): return m_min + 0.3*(1+np.sin(3*t))
    y0=np.r_[[0.75,1.25,1.1,0.9,1.15],[1.18,0.8,0.95,1.14,0.85]]
    V0=sum(phi(x) for x in y0)
    lo,L=solve_scalar(V0,True),solve_scalar(V0,False)
    kappa=4*lo**2*min(1,m_min/L**2)
    sol=solve_ivp(lambda t,y:rhs(t,y,A(t),m(t)),[0,4],y0,rtol=2e-11,atol=2e-13,dense_output=True,max_step=0.002)
    assert sol.success, sol.message
    for t in np.linspace(0,4,41):
        z=sol.sol(t)
        assert min(z)>0
        V=sum(phi(float(x)) for x in z)
        assert V<=V0*exp(-kappa*t)+1e-9,(t,V,V0*exp(-kappa*t))
    print('PASS time-dependent interaction trajectory: decreasing entropy and uniform exponential envelope')
    print('  V0=',round(V0,8),'ell=',round(lo,8),'L=',round(L,8),'kappa=',round(kappa,8))

if __name__=='__main__':
    exact_derivative_check()
    numerical_check()
