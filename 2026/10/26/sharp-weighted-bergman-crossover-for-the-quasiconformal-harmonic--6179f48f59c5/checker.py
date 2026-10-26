#!/usr/bin/env python3
"""Reproducible supplementary checks of the harmonic Koebe boundary profile.

Requires sympy and mpmath; no network access or external files. These finite
checks do not prove convergence of the weighted integral: that uses dominated
convergence and the global pointwise majorant in the manuscript.
"""
import sympy as sp
import mpmath as mp

z, k, y = sp.symbols("z k y", positive=True)
hp = (1 + z) / ((1 - z)**3 * (1 - k*z))
kappaprime = (1 + z) / (1 - z)**3
assert sp.simplify((1 - k*z)*hp - kappaprime) == 0
H = y**(-2) - 2/y + 2*sp.log(1 + 1/y)
assert sp.simplify(sp.diff(H, y) + 2/(y**3*(1+y))) == 0
for n in range(2, 9):
    coefficient = sp.series(hp, z, 0, n).removeO().expand().coeff(z, n-1)/n
    assert sp.simplify(coefficient.subs(k, 0)-n) == 0
    if n == 2:
        assert sp.simplify(coefficient-(k+4)/2) == 0
    if n == 3:
        assert sp.simplify(coefficient-(k**2+4*k+9)/3) == 0

mp.mp.dps = 35
T = lambda v: v**(-2)-2/v+2*mp.log(1+1/v)
for probe in (mp.mpf('0.5'), mp.mpf('1'), mp.mpf('2'), mp.mpc('1.4', '-0.5')):
    goal = T(probe)
    errs = []
    for eps in map(mp.mpf, ('0.1', '0.03', '0.01', '0.003')):
        f = lambda u: (2-eps*u)/(u**3*(1+u-eps*u))
        realpart = mp.re(probe)
        horizontal = mp.quad(lambda t: f(probe+(realpart-probe)*t)*(realpart-probe), [0,1])
        realintegral = mp.quad(f,[realpart,1/eps])
        approx = horizontal+realintegral
        errs.append(abs(approx-goal))
    assert all(errs[j+1] < errs[j] for j in range(len(errs)-1)), (probe, errs)
    assert errs[-1] < mp.mpf('0.001')

print('CHECK_OK: derivatives, Taylor coefficients and real/complex boundary profiles')
