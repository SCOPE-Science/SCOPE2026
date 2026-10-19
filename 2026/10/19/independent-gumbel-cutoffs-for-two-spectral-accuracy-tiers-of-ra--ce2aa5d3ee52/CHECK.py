"""Reproducibility checks for the two-tier RPCholesky stopping law."""
import numpy as np
from scipy.integrate import quad
from scipy.special import comb
from functools import lru_cache

# Exact dynamic-programming distribution of the number of pivots to complete
# either first contact in all blocks (tier1) or both contacts (tier2).
def dp_pmf(r,s,rho,beta,tier):
    w=1-rho*rho; delta=beta*r/s
    @lru_cache(None)
    def f(a,b,c):  # unvisited blocks a, visited once b, remaining light c
        if a==0 and (tier==1 or b==0): return {0:1.}
        z=2*a+w*b+delta*c
        out={}
        for rate,state in ((2*a,(a-1,b+1,c)),(w*b,(a,b-1,c)),(delta*c,(a,b,c-1))):
            if rate==0:continue
            for k,p in f(*state).items():out[k+1]=out.get(k+1,0.)+rate/z*p
        return out
    return f(r,0,s)

def cdf_tier2_integral(r,s,rho,beta,k):
    w=1-rho*rho;delta=beta*r/s
    def Yc(t):return 1-(2*np.exp(-w*t)-w*np.exp(-2*t))/(2-w)
    def Yp(t):return 2*w/(2-w)*(np.exp(-w*t)-np.exp(-2*t))
    def pdf_M(t):return r*max(0,Yc(t))**(r-1)*Yp(t)
    def bin_cdf(t):
        jmax=min(s,k-2*r)
        if jmax<0:return 0
        p=-np.expm1(-delta*t)
        return sum(comb(s,j)*p**j*(1-p)**(s-j) for j in range(jmax+1))
    return quad(lambda t:pdf_M(t)*bin_cdf(t),0,1200,epsabs=2e-10,limit=300)[0]

for rho in [0.2,0.5,0.8]:
    for r,s in [(1,2),(2,4),(3,5)]:
        for tier in [1,2]:
            d=dp_pmf(r,s,rho,1.,tier)
            assert abs(sum(d.values())-1)<5e-13
            assert all(k>=r if tier==1 else k>=2*r for k in d)
            if tier==2:
                for k in range(2*r,2*r+s+1):
                    exact=sum(v for t,v in d.items() if t<=k)
                    integral=cdf_tier2_integral(r,s,rho,1.,k)
                    assert abs(exact-integral)<4e-9,(r,s,rho,k,exact,integral)
print('SUCCESS: 9 parameter sets, exact finite state DP, tier-2 integral CDF all thresholds, mass checks for tier-1/tier-2')

# Critical CDF from exponential clock simulation; compare to Gumbel for both tiers.
rng=np.random.default_rng(3416)
r=3000;s=60000; rho=0.5; beta=1.0;w=1-rho**2;delta=beta*r/s
xvals=(-1.,0.,1.)
nsim=3200
U=rng.exponential(scale=.5,size=(nsim,r))
V=rng.exponential(scale=1/w,size=(nsim,r))
H=U.max(axis=1); M=(U+V).max(axis=1)
J1=rng.binomial(s, -np.expm1(-delta*H))
J2=rng.binomial(s, -np.expm1(-delta*M))
R1=((U+V)>H[:,None]).sum(axis=1)
T1=2*r-R1+J1;T2=2*r+J2
centers=[2*r+s*(-np.expm1(-delta*np.log(r)/2)),2*r+s*(-np.expm1(-delta*(np.log(r)+np.log(2/(2-w)))/w))]
scales=[beta*r*np.exp(-delta*np.log(r)/2)/2,beta*r*np.exp(-delta*(np.log(r)+np.log(2/(2-w)))/w)/w]
for tier,T,a,b in zip((1,2),(T1,T2),centers,scales):
    err=[float((T<=a+b*x).mean()-np.exp(-np.exp(-x))) for x in xvals]
    print('tier',tier,'mean',float(T.mean()),'scale',b,'cdf errors -1,0,+1',err)
    assert max(map(abs,err))<0.085
print('SUCCESS: two-tier asymptotic Monte Carlo stress test (not relied on for proof).')

# Directly reconstruct selected PSD Schur-complement residuals in matrix form.
for rho in (0.25,0.6,0.9):
    for r,s in ((2,4),(3,6)):
        w=1-rho*rho; delta=r/s
        A=np.zeros((2*r+s,2*r+s))
        for i in range(r):
            A[2*i:2*i+2,2*i:2*i+2]=[[1,rho],[rho,1]]
        A[2*r:,2*r:]=delta*np.eye(s)
        R=A.copy();state=[0]*r;light=s
        for k in range(2*r+s+1):
            actual=np.linalg.norm(R,ord=2)
            expected=max([1+rho if z==0 else w if z==1 else 0 for z in state]+([delta] if light else []))
            assert abs(actual-expected)<2e-12,(rho,r,s,k,actual,expected)
            if k==2*r+s:break
            diagonal=np.maximum(np.diag(R),0)
            p=diagonal/diagonal.sum()
            j=rng.choice(len(diagonal),p=p)
            assert R[j,j]>1e-14
            R-=np.outer(R[:,j].copy(),R[j,:].copy())/R[j,j]
            R=(R+R.T)/2
            if j<2*r:state[j//2]+=1
            else:light-=1
print('SUCCESS: direct Schur residual spectral norms agree with block-state accuracy cutoffs.')
