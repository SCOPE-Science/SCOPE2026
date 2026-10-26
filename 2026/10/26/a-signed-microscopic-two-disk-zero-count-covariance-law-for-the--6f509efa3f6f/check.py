"""Numerical corroboration of an exact covariance formula and its signed limit.

Run: python check.py
Dependencies: scipy, numpy, mpmath.
The all-radius identity and asymptotic are proved analytically in RESULT.md;
numerical testing is not a proof of an infinite assertion.
"""
import math
import numpy as np
import mpmath as mp
from scipy.special import ive, zeta as hurwitz_zeta
from scipy.optimize import brentq

mp.mp.dps = 40

def exact_cov(r, s, terms=5000):
    """Exponentially scaled Bessel representation of exact zero-count covariance."""
    k = np.arange(1, terms + 1, dtype=float)
    x = 2*k*r*s
    delta = r-s
    terms_array = np.exp(-k*delta*delta)*(
        2*r*s*(ive(0,x)-ive(1,x))-delta*delta*ive(1,x))
    value = float(r*s*np.sum(terms_array))
    if delta == 0.:
        # Euler tail from the proved large-order Bessel expansion.
        value += r/(4*math.sqrt(math.pi))*float(hurwitz_zeta(1.5, terms+1))
    return value

def circular_log_cov(r, s, terms=5000):
    """Exact Jensen log-mean covariance, calculated independently."""
    k=np.arange(1, terms+1,dtype=float)
    return float(0.25*np.sum(np.exp(-k*(r-s)**2)*ive(0,2*k*r*s)/k**2))

def limit_cov(delta):
    d = mp.mpf(str(abs(delta)))
    if d == 0:
        return float(mp.zeta(mp.mpf('1.5'))/(4*mp.sqrt(mp.pi)))
    q = mp.exp(-d*d)
    return float((mp.polylog(mp.mpf('1.5'), q) -
                  2*d*d*mp.polylog(mp.mpf('0.5'), q)) /
                 (4*mp.sqrt(mp.pi)))

def check():
    count = 0
    h=0.0007
    for r, s in ((1.3, 2.1), (2.0, 3.2), (1.8, 2.4)):
        mixed=(circular_log_cov(r+h,s+h)-circular_log_cov(r+h,s-h)
             -circular_log_cov(r-h,s+h)+circular_log_cov(r-h,s-h))/(4*h*h)
        assert abs(r*s*mixed-exact_cov(r,s)) < .0001, (r,s,mixed)
        count += 1
    for r in (8.0, 24.0, 70.0):
        for delta in (0.12, 0.3, 0.6, 0.8, 1.2):
            scaled = exact_cov(r, r+delta)/r
            predicted = limit_cov(delta)
            assert abs(scaled-predicted) < 0.75/r, (r, delta, scaled, predicted)
            count += 1
    for r in (9.0, 20.0, 60.0):
        diag = exact_cov(r, r)/r
        assert abs(diag-limit_cov(0)) < 0.02/r, (r, diag)
        count += 1
    root = brentq(limit_cov, 0.2, 0.7, xtol=1.e-14)
    assert abs(root-0.5467690754384508)<1.e-12
    count += 1
    for delta, sign in ((0., 1), (.1,1), (.4,1), (.7,-1), (1.0,-1), (1.5,-1)):
        assert math.copysign(1., limit_cov(delta)) == sign
        count += 1
    assert exact_cov(70.,70.8) < 0.
    count += 1
    print(f"{count} corroborative checks passed; crossover={root:.15f}; "
          f"diagonal={limit_cov(0):.15f}")

if __name__ == '__main__':
    check()
