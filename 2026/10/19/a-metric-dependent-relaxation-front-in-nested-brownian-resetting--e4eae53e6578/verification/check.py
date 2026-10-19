"""Independent numerical checks for nested-resetting transport-distance identities.

Use: python check.py
Dependencies: numpy, scipy.
"""
import math
import numpy as np
from scipy.special import gammaln, gammaincc, ndtr
from scipy.stats import gamma

D, rate = 1.7, 1.3
root = math.sqrt(4*D/(math.pi*rate))
def exact_w1(n,s):
    # G ~ Gamma(n,1), dimensionless observation time s=rate*t.
    return root*(math.exp(gammaln(n+0.5)-gammaln(n))*gammaincc(n+0.5,s)
                 -math.sqrt(s)*gammaincc(n,s))
def A(z):
    return math.exp(-z*z/2)/math.sqrt(2*math.pi)-z*ndtr(-z)

def grid_distances(n,s,samples=2500,grid=1201):
    g=gamma.ppf((np.arange(samples)+0.5)/samples,n)
    lo=min(1.,math.sqrt(s/n))
    bound=6.5*math.sqrt(2*D*max(n,s)/rate)
    x=np.linspace(-bound,bound,grid)
    ft=np.zeros_like(x); fs=np.zeros_like(x)
    scale=2*D/rate
    for start in range(0,samples,125):
        gg=g[start:start+125]
        vv=scale*gg
        uu=scale*np.minimum(gg,s)
        ft+=np.sum(np.exp(-x[:,None]**2/(2*uu))/np.sqrt(2*math.pi*uu),axis=1)
        fs+=np.sum(np.exp(-x[:,None]**2/(2*vv))/np.sqrt(2*math.pi*vv),axis=1)
    ft/=samples; fs/=samples
    return np.trapezoid(np.abs(ft-fs),x)/2

checks=0
for n in (1,2,3,5,8,20,50,150):
    for s in (.5,2.,float(n),float(n)*1.3):
        # Independent deterministic quadrature of the exact W1 transport
        # identity, using midpoint quantiles rather than incomplete gamma.
        g=gamma.ppf((np.arange(12000)+.5)/12000,n)
        approx=root*np.mean(np.sqrt(g)-np.sqrt(np.minimum(g,s)))
        exact=exact_w1(n,s)
        assert abs(approx-exact) < 0.005+0.001*exact,(n,s,approx,exact)
        checks+=1

for n in (40,100,300,1000):
    for z in (-1.,0.,1.):
        s=n+z*math.sqrt(n)
        w1=exact_w1(n,s)
        limit=math.sqrt(D/(math.pi*rate))*A(z)
        err=abs(w1-limit)
        assert err < 2.6/math.sqrt(n),(n,z,w1,limit)
        checks+=1
for n in (150,700,2500):
    s=n
    tv=grid_distances(n,s,samples=3000,grid=801)
    limit=math.exp(-0.5)/(2*math.pi)
    assert abs(tv*math.sqrt(n)-limit) < .03,(n,tv*math.sqrt(n),limit)
    checks+=1

for n in (50,200):
    for c in (.5,.85,1.2):
        s=n*c
        w1=exact_w1(n,s)
        pred=root*math.sqrt(n)*max(1-math.sqrt(c),0)
        if c<1: assert abs(w1-pred)<.1,(n,c,w1,pred)
        else: assert w1<.5
        checks+=1
print('PASS',checks,'transport and critical-window comparisons')
