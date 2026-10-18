"""Independent numerical consistency tests for quartic Gaussian ambiguity nodal theorem.

Run: python checker.py (requires mpmath and scipy).
All unbounded statements are proved analytically in RESULT.md; these tests
check normalization, constants, local root geometry, and asymptotic scales.
"""
import math
import mpmath as mp
from scipy.optimize import brentq
from scipy.special import ai_zeros, airy

PI = math.pi
mp.mp.dps = 44

def nu_at(kappa, q, u):
    return kappa*q**3/(2*PI) + PI/(6*kappa*q) + u*(12*kappa*q)**(1/3)/(2*PI)

def numerator(kappa, q, u):
    return 3*kappa*q**4/(2*PI) + u*(12*kappa)**(1/3)*q**(4/3)/(6*PI) - PI/(6*kappa)

def minimum(kappa, u):
    q = brentq(lambda x: numerator(kappa,x,u), 1e-12, max(100,10/kappa), xtol=1e-13)
    return q, nu_at(kappa,q,u)

# High-precision checks of Airy-Gauss formula against the original integral.
for lam, tau, freq in [(1,1,0), (1,1,0.8), (1,0.6,-1.2), (2,-1,1.2), (-1,1,-1.5), (.75,1.3,0.4)]:
    aa = 2*mp.pi
    bb = mp.mpf(12)*mp.mpf(str(lam))*mp.mpf(str(tau))
    cc = mp.mpf(str(lam))*mp.mpf(str(tau))**3 - 2*mp.pi*mp.mpf(str(freq))
    alpha = mp.sign(bb)*abs(bb)**(mp.mpf(1)/3)
    rhs = (2*mp.pi/abs(alpha))*mp.exp(2*aa**3/(3*bb**2)+aa*cc/bb)*mp.airyai((cc+aa**2/bb)/alpha)
    lhs = mp.quad(lambda x: mp.exp(-aa*x*x)*mp.cos(bb*x**3/3+cc*x),[-mp.inf,mp.inf])
    assert abs(lhs-rhs) < mp.mpf('1e-17'), (lam,tau,freq,lhs,rhs)
print('PASS: 6 high-precision evaluations of Gaussian-cubic Fourier identity')

for kappa in [0.2, 1.0, 4.0]:
    roots = -ai_zeros(25)[0]
    prev = -1.0
    for i,u in enumerate(roots,1):
        q,m = minimum(kappa,float(u))
        assert m>prev
        prev = m
        assert abs(numerator(kappa,q,float(u))) < 3e-11
        assert nu_at(kappa,q*0.9,float(u))>m
        assert nu_at(kappa,q*1.1,float(u))>m
        assert airy(-float(u))[0] < 1e-10 and airy(-float(u))[0] > -1e-10
    print(f'PASS: 25 distinct nondegenerate folds at strength {kappa:g}')

# Test the two independently derived universal asymptotic constants.
for kappa in [.2, 1, 4]:
    u = float(-ai_zeros(1000)[0][-1])
    q,m = minimum(kappa,u)
    assert abs(m/math.sqrt(1000)-2/3**.25) < .001
    assert abs(kappa*q*math.sqrt(1000)-PI/3**.75) < .002
print('PASS: universal frequency and delay asymptotic coefficients at index 1000')

# The Doppler axis and delay axis contain no zeros; sign-constrained zeros.
for lam in [-2, -1, .5, 3]:
    for tau in [-2, -.5, .5, 2]:
        bb=12*lam*tau
        nu0 = (lam*tau**3+(2*PI)**2/bb - math.copysign(abs(bb)**(1/3),bb)*float(mp.airyaizero(1)))/(2*PI)
        assert (lam*tau*nu0)>0
print('PASS: zero-curve quadrant signs')
print('All checks passed; infinite statements rely on the analytic proof.')
