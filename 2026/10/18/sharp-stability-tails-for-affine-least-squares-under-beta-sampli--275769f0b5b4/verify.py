"""Deterministic independent checks of the affine random least-squares tail theorem.
Run: python verify.py (requires numpy and scipy). Numerical probes supplement, not replace, proof.
"""
import math
import numpy as np
from scipy.special import beta as beta_fn, gamma
from scipy.integrate import quad

rng=np.random.default_rng(20261014)
checks=0

def assert_close(x,y,atol=1e-11,rtol=1e-9):
    global checks
    checks+=1
    assert np.isclose(x,y,atol=atol,rtol=rtol), (x,y)

def gram(n,a,b,x):
    mu=a/(a+b)
    sigma=math.sqrt(a*b/((a+b)**2*(a+b+1)))
    psi=np.array([np.ones(n),(x-mu)/sigma]).T
    return psi.T@psi/n

# The event K>t is precisely a mean-and-variance tube for every n>=2.
for n,a,b in ((2,1.,1.),(3,1.,1.),(4,.4,1.),(5,1.3,.8),(7,2.,2.)):
    mu=a/(a+b)
    s2=a*b/((a+b)**2*(a+b+1))
    for _ in range(1000):
        x=rng.beta(a,b,size=n)
        z=x.mean(); q=((x-z)**2).sum()
        G=gram(n,a,b,x)
        e1,e2=np.linalg.eigvalsh(G)
        assert_close(np.linalg.det(G),q/(n*s2),atol=1e-10)
        assert_close(np.trace(G),1+((z-mu)**2+q/n)/s2)
        for t in (1.01,1.5,3,10):
            left=e1<t**(-2)
            right=q<n/t**2*(s2+(z-mu)**2/(1-t**(-2)))
            assert left==right
            checks+=1

# Full two-point UNIFORM probability by an ordinary one-dimensional quadrature.
s2=1./12.
mu=.5
C2=4*quad(lambda z:math.sqrt(s2+(z-mu)**2),0.,1.,epsabs=1e-13)[0]
for t in (20,60,200,600):
    dmax=lambda z:2*math.sqrt((s2+(z-mu)**2/(1-t**-2))/t**2)
    prob=quad(lambda z:2*min(2*min(z,1-z),dmax(z)),0.,1.,points=[.5],epsabs=1e-12,limit=200)[0]
    assert prob>0
    assert abs(t*prob/C2-1.)<2. /t
    checks+=2

# The regular all-n coefficient for n=3 uniform is pi sqrt(3)/2.
v2=math.pi/gamma(2.)
C3=3**(3/2)*v2*quad(lambda z:s2+(z-.5)**2,0.,1.)[0]
assert_close(C3,math.pi*math.sqrt(3)/2.)

# The corner-integral coefficient J_2(a,R) follows independently by
# integrating first along the diagonal, then differentiating its radius.
for a in (.15,.22,.3,.42):
    R=.8+1.5*a
    D=math.sqrt(2)*R
    full=beta_fn(a,1-2*a)*D**(2*a)/a
    deriv_integrated=quad(lambda d:2*beta_fn(a,1-2*a)*d**(2*a-1),0.,D,epsabs=1e-9)[0]
    assert_close(full,deriv_integrated,rtol=1e-8)
    checks+=1

# Direct Gaussian-scale-free numerical comparison to asymptotic regular constant:
# rare events are sampled using uniform random X, not by a Gaussian Gram surrogate.
n=3; total=2_000_000; threshold=30.; hits=0
for _ in range(total//100_000):
    x=rng.random((100_000,n))
    z=x.mean(axis=1)
    q=((x-z[:,None])**2).sum(axis=1)
    hits+=int(np.count_nonzero(q<n/threshold**2*(s2+(z-mu)**2/(1-threshold**(-2)))))
p=hits/total
assert abs(p*threshold**2/C3-1)<.12
checks+=1
print('PASS:',checks,'deterministic assertions; uniform three-point simulation hits=',hits,
      'estimated tail constant=',p*threshold**2,
      'asymptotic constant=',C3)
print('Numerical experiments are neither a novelty check nor a proof of infinite-sample statements.')
