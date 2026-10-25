"""Reproducible numerical diagnostics for Gaussian widths of broom graphical zonotopes.
The proof uses analytic Gaussian moments and a one-dependent CLT, not simulations.
"""
import itertools
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import ndtr

MU=2/math.sqrt(math.pi)
C=1/3+(2*math.sqrt(3)-4)/math.pi
EDGEVAR=2-4/math.pi
SIGMA2=8/3+(4*math.sqrt(3)-14)/math.pi

def psi(x):
    return np.sqrt(2/math.pi)*np.exp(-np.asarray(x)**2/2)+np.asarray(x)*(2*ndtr(x)-1)-MU

def width(g,d):
    # vertices: hub 0; leaves 1...d; path d+1...n-1
    n=len(g)
    assert 0<=d<=n-2
    x=np.abs(g[0]-g[1:d+1]).sum()
    x+=abs(g[0]-g[d+1])
    x+=np.abs(np.diff(g[d+1:])).sum()
    return x/math.sqrt(np.dot(g-g.mean(),g-g.mean()))

def brute_width(g,d):
    # Zonotope is Minkowski sum of centered graph-root segments.
    # Enumerating segment signs independently gives its width.
    n=len(g)
    edges=[(0,j) for j in range(1,d+1)]+[(0,d+1)]+[(i,i+1) for i in range(d+1,n-1)]
    z=(g-g.mean())/np.linalg.norm(g-g.mean())
    maxv=-float('inf'); minv=float('inf')
    for signs in itertools.product((-1,1), repeat=len(edges)):
        y=np.zeros(n)
        for (i,j),s in zip(edges,signs):
            y[i]+=s/2; y[j]-=s/2
        a=float(y@z)
        maxv=max(maxv,a);minv=min(minv,a)
    return maxv-minv

def integrate_check():
    q1=quad(lambda z:psi(z)*math.exp(-z*z/2)/math.sqrt(2*math.pi),-12,12,epsabs=1e-11)[0]
    q2=quad(lambda z:psi(z)**2*math.exp(-z*z/2)/math.sqrt(2*math.pi),-12,12,epsabs=1e-11)[0]
    assert abs(q1)<2e-10,(q1,'center')
    assert abs(q2-C)<2e-10,(q2,C,'variance')
    print('analytic_moments',{'mu':MU,'edge_var':EDGEVAR,'adjacent_covariance':C,'spherical_gaussian_variance':SIGMA2,'psi_var_integral':q2})

def sim(n,d,k=5000,seed=199):
    rng=np.random.default_rng(seed+d)
    vals=[]
    for _ in range((k+99)//100):
        arr=rng.standard_normal((min(100,k-len(vals)),n))
        for g in arr: vals.append(width(g,d))
    vals=np.array(vals)
    centered=vals-MU*math.sqrt(n)
    return {'n':n,'d':d,'replicates':k,'mean':float(centered.mean()),'variance':float(centered.var(ddof=1)),'theoretical_critical_variance':SIGMA2+C*(d/math.sqrt(n))**2,
    'rescaled_variance':float(centered.var(ddof=1)*n/(d*d)) if d>0 else None}

if __name__=='__main__':
    integrate_check()
    rng=np.random.default_rng(12345)
    checks=0
    for n in range(4,11):
        for d in range(0,min(n-2,4)+1):
            for rep in range(12):
                g=rng.normal(size=n)
                w1=width(g,d);w2=brute_width(g,d)
                assert abs(w1-w2)<2e-12,(n,d,w1,w2)
                checks+=1
    print('support_function_enumerations_passed',checks)
    for n,d,k in [(2500,3,5000),(4000,64,5000),(6000,380,5000)]:
        print('diagnostic',sim(n,d,k))
