"""Numerical checks for Gaussian directional widths of partial permutohedra."""
import itertools, math
import numpy as np
from scipy.integrate import quad
from scipy.stats import norm
from scipy.special import gamma

def expectation_radius(m):
    from scipy.special import gammaln
    return math.sqrt(2)*math.exp(float(gammaln((m+1)/2)-gammaln(m/2)))

def exact_width(m,n):
    mu=expectation_radius(m)
    accum=0.
    for j in range(1,min(m,n)+1):
        C=math.exp(math.lgamma(m+1)-math.lgamma(j)-math.lgamma(m-j+1))
        val=quad(lambda x: x*norm.pdf(x)*norm.cdf(x)**(m-j)*(norm.sf(x))**(j-1),0,9,epsabs=2e-11)[0]
        accum+=(n-j+1)*C*val
    return 2*accum/mu

def greed(g,n):
    s=np.sort(g)[::-1]
    k=min(len(s),n)
    return float(np.dot(np.arange(n,n-k,-1),np.maximum(s[:k],0)))

def exhaustive(g,n):
    m=len(g)
    opts=[]
    for k in range(min(m,n)+1):
        for js in itertools.combinations(range(m),k):
            for labs in itertools.permutations(range(1,n+1),k):
                v=np.zeros(m)
                v[list(js)]=labs
                opts.append(v@g)
    return max(opts)

rng=np.random.default_rng(2042207)
for m,n in [(2,1),(3,2),(4,2),(3,4)]:
    for _ in range(25):
        g=rng.normal(size=m)
        assert abs(greed(g,n)-exhaustive(g,n))<1e-11,(m,n,g)
    # Exact 1-d formula vs direct Gaussian sampling.
    G=rng.normal(size=(70000,m))
    mu=expectation_radius(m)
    emp=2*np.mean([greed(x,n) for x in G])/mu
    exact=exact_width(m,n)
    assert abs(emp-exact)<0.035,(m,n,emp,exact)
    print('finite',m,n,round(emp,6),round(exact,6))

def f(a):
    if a>=.5: return (2*a-1)/math.sqrt(2*math.pi)+1/(2*math.sqrt(math.pi))
    return 2*quad(lambda t:(a-t)*norm.isf(t),0,a,epsabs=1e-10)[0]

for a in (.20,.5,.8,1.3):
    m=4500;n=round(a*m);G=rng.normal(size=(330,m))
    emp=2*np.mean([greed(x,n) for x in G])/(expectation_radius(m)*m**1.5)
    target=f(a)
    print('asympt',a,round(emp,6),round(target,6))
    assert abs(emp-target)<0.028,(a,emp,target)
assert abs(f(.5)-1/(2*math.sqrt(math.pi)))<1e-10
assert abs(f(1)-(1/math.sqrt(2*math.pi)+1/(2*math.sqrt(math.pi))))<1e-10
print('PARTIAL_PERMUTOHEDRON_GAUSSIAN_WIDTH_CHECKS_PASSED')
