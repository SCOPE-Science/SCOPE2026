"""Independent two-time polynomial-semigroup checks for a Poisson rescaling diffusion."""
import math
import numpy as np
from scipy.linalg import expm


def verify(qs, ps, r, D, t):
    qs=np.asarray(qs,float); ps=np.asarray(ps,float)
    assert np.isclose(sum(ps),1) and max(abs(qs))<1
    moments=[float(np.dot(ps,qs**k)) for k in range(5)]
    lam=lambda k:r*(1-moments[k])
    m2=2*D/lam(2)
    m4=12*D*m2/lam(4)
    # Conditional semigroup of polynomials 1,x,x^2,x^3 (columns are starting polynomials)
    A=np.zeros((4,4));
    for n in range(1,4):
        A[n,n]=-lam(n)
        if n>=2:A[n-2,n]=D*n*(n-1)
    E=expm(A*t)
    # <X_0 X_t^3> and <X_0^3 X_t> computed independently via semigroup.
    qm=E[1,3]*m2+E[3,3]*m4
    pm=E[1,1]*m4
    measured=qm-pm
    slope=6*D*m2*np.dot(ps,(1-qs)**3*(1+qs))/(1-moments[4])
    k1,k3=lam(1),lam(3)
    h=t*math.exp(-k1*t) if abs(k3-k1)<1e-11 else (math.exp(-k1*t)-math.exp(-k3*t))/(k3-k1)
    predicted=slope*h
    assert measured>0 and np.isclose(measured,predicted,rtol=1e-8,atol=1e-9),(measured,predicted)
    star=1/k1 if abs(k3-k1)<1e-11 else math.log(k3/k1)/(k3-k1)
    assert star>0
    h_eval=lambda z:z*math.exp(-k1*z) if abs(k3-k1)<1e-11 else (math.exp(-k1*z)-math.exp(-k3*z))/(k3-k1)
    assert h_eval(star)>h_eval(star*.6) and h_eval(star)>h_eval(star*1.5)
    return measured, star

rng=np.random.default_rng(41051)
count=0
for i in range(500):
    qs=rng.uniform(-.95,.95,size=4)
    ps=rng.dirichlet(np.ones(4))
    r=10**rng.uniform(-.4,.4);D=10**rng.uniform(-.3,.3)
    t=10**rng.uniform(-1,0.4)/r
    verify(qs,ps,r,D,t);count+=1
for q in [-.9,-.5,0,.3,.8]:
    for t in [.01,.2,1,3]:
        verify([q],[1],1.3,.7,t);count+=1
print('PASS',count,'independent polynomial-semigroup comparisons and unique maximum checks')
