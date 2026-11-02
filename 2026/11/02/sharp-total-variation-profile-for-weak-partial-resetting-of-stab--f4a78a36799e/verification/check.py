"""Finite reproducibility checks for a stationary partial-reset stable-law expansion.

The analytical L1 expansion is proved in RESULT.md; these tests are illustrations,
not exhaustive verification of any continuum statement.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import ndtr

count=0

def close(a,b,atol=1e-9,rtol=1e-8):
    global count
    assert abs(a-b) <= atol+rtol*max(abs(a),abs(b)), (a,b)
    count+=1

# Exact scale-mixture cumulants and their near-unit-contraction behavior.
for delta in (0.4,0.2,0.1,0.04,0.01):
    q=1-delta
    epsilon=delta/(2-delta)
    k2=delta**2/(1-q**2)
    k4=6*delta**4/(1-q**4)
    close(k2,epsilon)
    assert k4>0
    count+=1
    fourth=3*k2**2+k4
    assert 0<fourth <= 8*delta**2
    count+=1

# A finite Fourier-product evaluation independent of the limiting expansion.
for alpha in (0.5,1.,1.3,2.):
    for delta in (0.15,0.07,0.03,0.01):
        q=1-delta
        epsilon=delta/(2-delta)
        m=int(math.ceil(math.log(1e-14)/math.log(q)))
        weights=delta*q**np.arange(m)
        for t in (0.35,0.65,1.,1.4):
            T=t**alpha
            product=math.exp(-float(np.log1p(weights*T).sum()))
            approx=math.exp(-T)*(1+epsilon*T*T/2)
            assert abs(product-approx) <= 1.15*delta**2
            count+=1
            assert product>math.exp(-T)
            count+=1

# Cauchy second scale derivative; its sign flips at +/-1/sqrt(3).
def cauchy_K(x):
    return 2*(1-3*x*x)/(math.pi*(1+x*x)**3)

h=1/math.sqrt(3)
positive=2*quad(cauchy_K,0,h,epsabs=1e-12)[0]
negative=-2*quad(cauchy_K,h,np.inf,epsabs=1e-12)[0]
close(positive,negative,atol=1e-11)
close((positive+negative)/4,3*math.sqrt(3)/(8*math.pi),atol=1e-11)

# Gaussian second scale derivative and Hermite sign-change intervals.
a=math.sqrt(3-math.sqrt(6)); b=math.sqrt(3+math.sqrt(6))
phi=lambda z: math.exp(-z*z/2)/math.sqrt(2*math.pi)
H4=lambda z: z**4-6*z*z+3
K_gauss=lambda z:phi(z)*H4(z)/4
negative=-2*quad(K_gauss,a,b,epsabs=1e-12)[0]
positive=2*(quad(K_gauss,0,a,epsabs=1e-12)[0]+quad(K_gauss,b,np.inf,epsabs=1e-12)[0])
close(negative,positive,atol=1e-11)
close((negative+positive)/4,(math.sqrt(6)/4)*(a*phi(a)+b*phi(b)),atol=1e-11)

# Independent Fourier integral for second scale derivatives at selected positions.
for alpha in (0.6,1.,1.4,2.):
    for x in (0.,0.5,1.5,3.):
        integral=quad(lambda t: math.cos(t*x)*t**(2*alpha)*math.exp(-t**alpha)/math.pi,0,np.inf,epsabs=2e-9,limit=300)[0]
        if alpha==1.:
            close(integral,cauchy_K(x),atol=1e-8)
        if alpha==2.:
            z=x/math.sqrt(2)
            close(integral,phi(z)*H4(z)/(4*math.sqrt(2)),atol=1e-8)
        assert math.isfinite(integral)
        count+=1
print('PASS',count,'finite numerical assertions')
print('Cauchy TV coefficient',3*math.sqrt(3)/(8*math.pi))
print('Gaussian TV coefficient',(math.sqrt(6)/4)*(a*phi(a)+b*phi(b)))
