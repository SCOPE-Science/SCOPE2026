"""Numerical and algebraic consistency checks for a renewal-reset random-acceleration theorem.
Run: python checks.py (requires scipy and numpy). These are finite checks, not a proof.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import gamma
from scipy.stats import norm

def mismatch(alpha):
    power = 2*alpha/3
    numerator = quad(lambda z: z**power*norm.pdf(z)*norm.cdf(-math.sqrt(3)*z), 0, 12, epsabs=1e-12)[0]
    denominator = quad(lambda z: z**power*norm.pdf(z), 0, 12, epsabs=1e-12)[0]
    return numerator/denominator

# Gaussian integrated-Brownian covariance and strict non-degeneracy.
C = np.array([[1/3, 1/2], [1/2, 1]])
assert abs(np.linalg.det(C) - 1/12) < 1e-14
assert np.linalg.eigvalsh(C)[0] > 0

q_values = [mismatch(x) for x in (0.01, 0.1, 0.5, 1.5, 3, 10)]
assert all(x>y>0 for x,y in zip(q_values,q_values[1:]))
assert 0 < 1/6-q_values[0] < 0.002
assert abs(mismatch(1.5) - (2-math.sqrt(3))/4) < 5e-11

# Independent direct stationary age-moment quadrature, alpha=5, b=1.
alpha,b = 5,1
for s in [0.5,1.,2.,3.]:
    numerical=quad(lambda a: a**s*alpha/b*(1+a/b)**(-alpha-1), 0, np.inf)[0]
    closed=b**s*gamma(s+1)*gamma(alpha-s)/gamma(alpha)
    assert abs(numerical-closed)<1e-9

A1=1/4; A2=1/6; A3=1/4; D=1
assert abs(2*D*A3/3 - 1/6)<1e-14  # stationary position second moment
assert abs(2*D*A1 - 1/2)<1e-14    # stationary velocity second moment
assert abs(D*A2 - 1/6)<1e-14      # stationary signed cross moment

# Direct finite-threshold event-conditioned direction reversal, alpha=3/2.
alpha=1.5
for x in [10**3, 10**5, 10**7]:
    def weight(z):
        if z<=0: return 0
        threshold=(x/(math.sqrt(2)*(z/math.sqrt(3))))**(2/3)
        return (1+threshold)**(-alpha)
    den=quad(lambda z:norm.pdf(z)*weight(z),0,12,epsabs=1e-12)[0]
    num=quad(lambda z:norm.pdf(z)*norm.cdf(-math.sqrt(3)*z)*weight(z),0,12,epsabs=1e-12)[0]
    assert abs(num/den-(2-math.sqrt(3))/4)<0.015
    print(f'X>{x:g}: reversal probability {num/den:.10f}')

# The absolute-tail joint coefficient is strictly between zero and one:
# deterministic Gaussian Hermite quadrature approximates its expectation.
from numpy.polynomial.hermite import hermgauss
for n in [40,80]:
    x,w=hermgauss(n); z=np.sqrt(2)*x
    g=z[:,None]/math.sqrt(3)
    h=(math.sqrt(3)/2)*z[:,None]+(1/2)*z[None,:]
    a=1.5
    eg=(1/3)**(a/3)*2**(a/3)*gamma((2*a/3+1)/2)/math.sqrt(math.pi)
    eh=2**a*gamma(a+0.5)/math.sqrt(math.pi)
    val=np.minimum(np.abs(g)**(2*a/3)/eg,np.abs(h)**(2*a)/eh)
    chi=float(np.sum(w[:,None]*w[None,:]*val)/math.pi)
    assert 0 < chi < 1
    print(f'Gauss-Hermite {n}: chi={chi:.8f}')
print('All analytic-identity and finite quadrature checks passed.')
