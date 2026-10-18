"""Reproducibility checks for period-capped invariant-conic resonance energies.

Python standard library only. Finite checks illustrate, but do not replace,
the analytic period classification and arithmetic proof.
"""
from fractions import Fraction
from math import atan, gcd, isclose, log, pi, sqrt, tan


def khk_step(x, y, e):
    d = 2*e*e*x*x-e*(e+1)*x-e*y+2*e+1
    if d == 0:
        raise ZeroDivisionError
    return ((e*(e+1)*x*x + e*x*y + (1-2*e)*x)/d,
            (e*(2*e-4)*x*x-e*(e+3)*x*y+6*e*x-e*y*y+(2*e+1)*y)/d)


def first_integral(x, y, e):
    return -((5*e*e-2)*x*x-2*x*y-y*y+6*x+4*y)/(2*e*e*x*x+2)


checks = 0
for e in [Fraction(1, 10), Fraction(1, 2), Fraction(9, 10)]:
    for x in [Fraction(-1, 2), Fraction(1, 4), Fraction(2, 3), Fraction(3, 2)]:
        for y in [Fraction(-1, 2), Fraction(1, 4), Fraction(2, 3)]:
            xx, yy = khk_step(x, y, e)
            assert first_integral(xx, yy, e) == first_integral(x, y, e)
            checks += 1

for epsilon in [0.15, 0.33, 0.70, 0.99]:
    alpha = atan(epsilon)/pi
    def energy(r):
        return -2 - tan(pi*float(r))**2/(2*epsilon*epsilon)
    def gap(r):
        return tan(pi*float(r))**2/(2*epsilon*epsilon)
    for P in [15, 28, 47, 71, 103, 151]:
        if 1/(P-1) >= alpha:
            continue
        fractions = sorted(Fraction(k, q) for q in range(1, P+1)
                           for k in range(1, q) if gcd(k, q) == 1 and k/q < alpha)
        observed = [energy(fractions[i])-energy(fractions[i+1])
                    for i in range(len(fractions)-1)]
        index = min(range(len(observed)), key=observed.__getitem__)
        expected = gap(Fraction(1, P-1)) - gap(Fraction(1, P))
        assert fractions[index] == Fraction(1, P)
        assert fractions[index+1] == Fraction(1, P-1)
        assert isclose(observed[index], expected, rel_tol=2e-10, abs_tol=2e-12)
        assert all(d > 0 for d in observed)
        checks += len(observed)+4
    P = 401
    number = sum(gcd(k, q) == 1 and k/q < alpha
                 for q in range(1, P+1) for k in range(1, q))
    predicted = 3*alpha*P*P/(pi*pi)
    assert abs(number-predicted) < 2*P*log(P)
    checks += 1
    for delta in [0.001, 0.02, 0.12, 0.4]:
        r = atan(epsilon*sqrt(2*delta))/pi
        h = -2 - delta
        assert isclose(energy(r), h, rel_tol=1e-11, abs_tol=1e-11)
        density = epsilon/(atan(epsilon)*sqrt(2*delta)*(1+2*epsilon*epsilon*delta))
        analytical_density = (atan(epsilon*sqrt(2*(delta+1e-6)))
                              -atan(epsilon*sqrt(2*delta))) / (atan(epsilon)*1e-6)
        assert abs(density-analytical_density)/density < 0.002
        checks += 2
print(f'VERIFY_OK {checks} assertions')
