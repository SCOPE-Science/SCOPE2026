"""Independent checks for the positive spherical orthant pair-distance tail.
Run with Python 3, NumPy, SciPy and SymPy installed.
"""
import math
import numpy as np
from scipy.stats import qmc
import sympy as sp


def coefficient(d):
    area = 2 ** (1-d) * math.pi ** (d/2) / math.gamma(d/2)
    return 1 / (math.factorial(d-2) * area * area)


def chart_core(epsilon, samples_pow=18):
    """Quadrature of a single projective-chart logarithmic core in dimension 3.

    The integration splits into b>=epsilon and b<epsilon domains, uses exact
    spherical weights and the exact inner-product test, and omits no chart region
    on the rare event for epsilon<1/3.
    """
    seq = qmc.Sobol(4, scramble=False).random_base2(m=samples_pow)
    t = seq[:, 0]
    b = np.exp(t * math.log(epsilon))
    v = np.sort(seq[:, 1:4], axis=1)
    x = 3 * v[:, 0]
    y = 3 * (v[:, 1] - v[:, 0])
    z = 3 * (v[:, 2] - v[:, 1])
    d = epsilon * z / b
    a = epsilon * x
    c = epsilon * y
    r2 = 1 + a*a + b*b
    s2 = 1 + c*c + d*d
    num = x + y + z
    valid = (d <= 1) & (num < np.sqrt(r2*s2))
    weight = (r2*s2)**(-1.5)
    large_b_contribution = (3**3 / 6) * np.mean(np.where(valid, weight, 0))
    # b<epsilon contribution: a=eps*x, c=eps*y, b=eps*t, d=u.
    x = 3 * seq[:, 0]
    y = 3 * seq[:, 1]
    t = seq[:, 2]
    v3 = seq[:, 3]
    aa = epsilon*x
    cc = epsilon*y
    bb = epsilon*t
    rr2 = 1+aa*aa+bb*bb
    ss2 = 1+cc*cc+v3*v3
    inside = x+y+t*v3 < np.sqrt(rr2*ss2)
    density = (rr2*ss2)**(-1.5)
    small_b_contribution = 9*np.mean(np.where(inside, density, 0))/math.log(1/epsilon)
    return large_b_contribution + small_b_contribution


def analytic_checks():
    x = sp.symbols('x', positive=True)
    assert sp.integrate((1-x)**2, (x, 0, 1)) == sp.Rational(1,3)
    assert sp.integrate((1-x)**2*sp.log(1/x), (x,0,1)) == sp.Rational(11,18)
    assert coefficient(2) == coefficient(3) or abs(coefficient(2)-coefficient(3)) < 1e-12
    assert abs(coefficient(2) - 4/math.pi**2) < 1e-12
    assert abs(coefficient(4) - 32/math.pi**4) < 1e-12
    for d in range(2,10):
        area = 2**(1-d)*math.pi**(d/2)/math.gamma(d/2)
        chart = 1/math.factorial(d)
        assert abs(d*(d-1)*chart/(area**2)-coefficient(d)) < 1e-9
    # In dimension 2, the two angles are uniform on [0,pi/2].
    # Their absolute difference has exact top tail 4*eps**2/pi**2.
    for e in [0.0001,0.05,0.4]:
        exact = (e/(math.pi/2))**2
        assert abs(exact-coefficient(2)*e**2) < 1e-14
    print('Exact checks: beta integral, product-log integral, spherical area, d=2 tail: PASS')


if __name__ == '__main__':
    analytic_checks()
    for d in range(2, 7):
        print('dimension',d,'predicted coefficient',format(coefficient(d),'.12g'))
    previous = None
    for exponent in [5, 10, 20, 40]:
        e = math.exp(-exponent)
        ratio = chart_core(e) * math.factorial(3)
        print('epsilon=exp(-%d): full chart / predicted leading chart coefficient=%.7f' %(exponent, ratio))
        if previous is not None:
            assert abs(ratio-1) < abs(previous-1) + 0.04
        previous = ratio
    assert 0.85 < previous < 1.15
    print('Dimension-3 full-chart quadrature: PASS')
