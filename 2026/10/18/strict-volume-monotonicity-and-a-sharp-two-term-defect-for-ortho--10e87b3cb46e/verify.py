"""Reproducibility checks for normalized volumes of perpendicular cylinders.

Install mpmath and sympy. Numerical checks supplement, not replace,
the all-dimensional analytic proof provided separately.
"""
from mpmath import mp
import sympy as sp

mp.dps = 45
u = sp.Symbol('u')
series = sp.series(sp.exp(sp.erfinv(u)**2), u, 0, 6).removeO().expand()
expected = 1 + sp.pi*u**2/4 + 7*sp.pi**2*u**4/96
assert sp.simplify(series - expected) == 0


def unit_ball(n):
    return mp.pi**(mp.mpf(n)/2)/mp.gamma(1+mp.mpf(n)/2)


def ratio(n):
    assert n >= 2 and isinstance(n, int)
    integrand = lambda t: mp.erfc(t)**(n-1)
    integral = mp.quad(integrand, [0, 1, 3, mp.inf])
    return 2*n*integral/mp.sqrt(mp.pi)


def asymptotic(n):
    z = mp.mpf(n)
    return (1 + mp.pi/(2*(z+1)*(z+2))
            + 7*mp.pi**2/(4*(z+1)*(z+2)*(z+3)*(z+4)))


r = {n: ratio(n) for n in list(range(2, 41)) + [60, 80, 160, 320]}
for n in range(2, 40):
    assert 1 < r[n+1] < r[n]
assert abs(r[2]*unit_ball(2) - 4) < mp.mpf('1e-35')
assert abs(r[3]*unit_ball(3) - 8*(2-mp.sqrt(2))) < mp.mpf('1e-35')
known_four = 16 * 3*(mp.pi/4-mp.atan(mp.sqrt(2))/mp.sqrt(2))
known_five = 32 * 8*(mp.pi/12-mp.atan(1/(2*mp.sqrt(2)))/mp.sqrt(2))
assert abs(r[4]*unit_ball(4) - known_four) < mp.mpf('1e-35')
assert abs(r[5]*unit_ball(5) - known_five) < mp.mpf('1e-35')

for n in [20, 40, 80, 160, 320]:
    residue = r[n] - asymptotic(n)
    # The first omitted nonzero coefficient is positive, of order n^(-6).
    assert residue > 0
    assert residue*n**6 < mp.mpf('1e5')
    print('n=', n, 'volume_ratio=', mp.nstr(r[n], 20),
          'n^2 excess=', mp.nstr(n*n*(r[n]-1), 15),
          'n^6 remainder=', mp.nstr(residue*n**6, 15))
print('PASS: exact series, dimensions 2-5, strict numerical comparisons, high-dimensional asymptotic checks')
