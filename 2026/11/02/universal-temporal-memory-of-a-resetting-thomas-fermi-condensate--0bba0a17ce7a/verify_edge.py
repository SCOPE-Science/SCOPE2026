"""Reproduce exact exponential-moment identities and numerical edge-memory tests.

Requires Python 3.10+. The optional ODE/quadrature section uses NumPy and SciPy.
The model is the Thomas--Fermi support scaling b''=omega**2/b**2.
"""
from math import factorial, comb, exp, sqrt
from fractions import Fraction as F


def covariance_powers(p, q):
    return F(factorial(p + q) - factorial(p) * factorial(q))


def integrated_shift_covariance(p, q):
    # With independent unit-exponential variables Z,U, evaluate
    # E_U[Cov_Z(Z**p,(Z+U)**q)] exactly.
    return sum((F(comb(q, k) * factorial(k)) * covariance_powers(p, q-k)
                for k in range(q+1)), F(0))


def fixed_shift_covariance(p, q, u):
    return sum(F(comb(q, k)) * F(u)**k * covariance_powers(p, q-k)
               for k in range(q+1))

assert covariance_powers(2, 2) == 20
assert covariance_powers(2, 1) == 4
assert covariance_powers(2, 4) == 672
assert integrated_shift_covariance(2, 2) == 28
assert integrated_shift_covariance(2, 4) + integrated_shift_covariance(4, 2) == 2304
for u in range(10):
    assert fixed_shift_covariance(2, 2, u) == 20 + 8*u

# If epsilon=omega/r, b(z/r)=1+(epsilon**2/2)*z**2
# -(epsilon**4/12)*z**4+O(epsilon**6*z**6), then
# variance = 5*epsilon**4 -56*epsilon**6 +O(epsilon**8),
# integrated covariance =7*epsilon**4-96*epsilon**6+O(epsilon**8).
var4 = F(1, 4) * covariance_powers(2, 2)
var6 = 2*F(1, 2)*F(-1, 12)*covariance_powers(2, 4)
int4 = F(1, 4)*integrated_shift_covariance(2, 2)
int6 = F(1, 2)*F(-1, 12)*(integrated_shift_covariance(2, 4)+integrated_shift_covariance(4, 2))
assert (var4, var6, int4, int6) == (5, -56, 7, -96)
assert int4/var4 == F(7, 5)
assert int6/var4 - int4*var6/(var4**2) == F(-88, 25)
print('Exact checks passed: 7/5 limit, -88/25 correction, 20+8u covariance polynomial.')

try:
    import numpy as np
    from numpy.polynomial.laguerre import laggauss
    from scipy.integrate import solve_ivp
except ImportError:
    print('NumPy/SciPy unavailable: exact arithmetic tests completed; numerical tests skipped.')
else:
    zz, ww = laggauss(55)
    uu, vu = laggauss(55)
    max_s = (max(zz)+max(uu))/20 + 0.2
    sol = solve_ivp(lambda t,y: (y[1], 1.0/y[0]**2),
                    (0,max_s), [1.0,0.0], method='DOP853',
                    rtol=3e-12, atol=3e-13, dense_output=True)
    assert sol.success
    def b(s):
        return sol.sol(s)[0]
    for rate in (20.0,40.0):
        zbase=b(zz/rate)
        avg=np.dot(ww,zbase)
        variance=np.dot(ww,zbase*zbase)-avg*avg
        assert variance>0
        # The no-reset part determines covariance at each lag.
        cov=[]
        for u in uu:
            zlag=b((zz+u)/rate)
            cov.append(np.dot(ww,(zbase-avg)*zlag))
        normalized_memory = float(np.dot(vu,cov)/variance)
        expected=1.4-3.52/(rate**2)
        assert abs(normalized_memory-expected)<0.004, (rate,normalized_memory,expected)
        assert normalized_memory>1
        if rate == 40.0:
            u=1.0
            zlag=b((zz+u)/rate)
            nlag=exp(-u)*np.dot(ww,(zbase-avg)*zlag)/variance
            assert abs(nlag-exp(-u)*1.4)<0.002
        print(f'r/omega={rate:g}, r times correlation time={normalized_memory:.9f}, asymptotic={expected:.9f}')
    print('ODE/quadrature checks passed for two finite reset rates.')
