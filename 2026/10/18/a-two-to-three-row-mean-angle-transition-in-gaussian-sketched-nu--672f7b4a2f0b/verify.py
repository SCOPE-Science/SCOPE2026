"""Reproducibility checks for the two-mode Gaussian sketch angle formulas.

Requires numpy and scipy. These finite checks supplement the analytical proof.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import roots_jacobi, gammaln

def squared_sine_from_gram(a, b, d):
    D=math.hypot(a-d,2*b)
    return 0.5*(1-(a-d)/D)

def angular_kernel(x,y):
    # y is the squared cosine between independent Gaussian vectors.
    D=math.sqrt((x-1)**2+4*x*y)
    if x>2:
        return (2*x*y)/(D*(D+x-1))
    return 0.5*(1-(x-1)/D)

def integral_risk(s,eps,nquad=60):
    # Exact beta-prime / beta double integral, using deterministic quadrature.
    nodes,weights=roots_jacobi(nquad,(s-3)/2,-0.5)
    y=(nodes+1)/2
    weights=weights/sum(weights)
    normalizer=math.exp(gammaln(s)-2*gammaln(s/2))
    def density_times_risk(r):
        expectation=sum(w*angular_kernel(r/eps**2,yy) for yy,w in zip(y,weights))
        return normalizer*r**(s/2-1)*(1+r)**(-s)*expectation
    stops=sorted(set((0,eps*eps,2*eps*eps,1,math.inf)))
    return sum(quad(density_times_risk,left,right,epsabs=4e-11,
                    epsrel=2e-8,limit=250)[0]
               for left,right in zip(stops[:-1],stops[1:]))

def test_spectrum_kernel():
    rng=np.random.default_rng(2022)
    for s in (2,3,4,6):
        for eps in (0.03,0.25,0.7):
            for _ in range(125):
                G=rng.normal(size=(s,2))
                Y=G@np.diag([1.,eps])
                w,V=np.linalg.eigh(Y.T@Y)
                direct=V[0,0]**2
                a=G[:,0]@G[:,0]
                b=eps*(G[:,0]@G[:,1])
                d=eps**2*(G[:,1]@G[:,1])
                formula=squared_sine_from_gram(a,b,d)
                assert abs(direct-formula)<2e-11,(s,eps,direct,formula)

def test_exact_three_row_law():
    for eps in (0.05,0.2,0.4,0.7,1.,2.):
        k=1./eps
        # Spectral eigenvector density for Wishart_2(3, diag(1,eps^2))
        # is proportional to (cos(theta)^2 + k^2 sin(theta)^2)^(-2).
        den=quad(lambda z: (1+z*z)/(1+k*k*z*z)**2,
                 -math.inf,math.inf,epsabs=3e-12)[0]
        num=quad(lambda z: z*z/(1+k*k*z*z)**2,
                 -math.inf,math.inf,epsabs=3e-12)[0]
        target=eps**2/(1+eps**2)
        assert abs(num/den-target)<5e-10,(eps,num/den,target)
        assert abs(den-math.pi*(k*k+1)/(2*k**3))<1e-9
        assert abs(num-math.pi/(2*k**3))<1e-9

def test_small_epsilon_frontier():
    for eps in (0.03,0.01,0.003):
        value=integral_risk(2,eps)
        scale=eps*eps*math.log(1/eps)
        assert abs(value/scale-1)<0.065,(eps,value/scale)
    for s in (3,4,5,6):
        value=integral_risk(s,0.01)
        scale=0.0001/(s-2)
        assert abs(value/scale-1)<0.005,(s,value/scale)
    for eps in (0.1,0.25,0.5):
        assert abs(integral_risk(3,eps,120)-eps**2/(1+eps**2))<1e-7

def main():
    test_spectrum_kernel()
    print('Gaussian Gram eigenvector identities: 1,500 passed')
    test_exact_three_row_law()
    print('Three-row exact eigenvector risk and integral identities: 18 passed')
    test_small_epsilon_frontier()
    print('Beta-prime angular integral and asymptotic sanity checks: 10 passed')
    print('All checks passed. Infinite-family statements require the accompanying proof.')

if __name__=='__main__': main()
