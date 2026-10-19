"""Reproduce exact two-coordinate RCGLS stopping laws using rational arithmetic.

Run: python verify.py
Requires Python 3 and SymPy. All matrix/sample-path checks use Fractions.
This is finite corroboration; the full distribution and infinite-time claims are proved analytically.
"""
from fractions import Fraction as Q
from itertools import product
from collections import defaultdict
import sympy as sym


def mv(H, v):
    return [sum(H[i][j] * v[j] for j in range(2)) for i in range(2)]


def dot(u, v):
    return sum(x * y for x, y in zip(u, v))


def rcgls(H, e0, choices):
    """Source algorithm's equivalent error/direction form, S=e_i/sqrt(H_ii).

    With gradient g=H*e, the sketched gradient is (g_i/H_ii)*e_i.
    If a denominator vanishes its quotient is set to zero.
    """
    e = [Q(x) for x in e0]
    direction = [Q(0), Q(0)]
    stopping = None
    activities = []
    for step, chosen in enumerate(choices, 1):
        g = mv(H, e)
        sketch = [Q(0), Q(0)]
        sketch[chosen] = g[chosen] / H[chosen][chosen]
        Hd = mv(H, direction)
        denom = dot(direction, Hd)
        t = -dot(sketch, Hd) / denom if denom else Q(0)
        direction = [sketch[i] + t * direction[i] for i in range(2)]
        new_denom = dot(direction, mv(H, direction))
        step_size = dot(g, direction) / new_denom if new_denom else Q(0)
        e = [e[i] - step_size * direction[i] for i in range(2)]
        active = bool(new_denom)
        activities.append(active)
        if e == [0, 0] and stopping is None:
            stopping = step
            break
    return stopping, activities


def predicted_stop(choices, coupled):
    if not coupled:
        return next((k for k, i in enumerate(choices, 1)
                     if i != choices[0]), None)
    active = True
    prev = choices[0]
    for t, i in enumerate(choices[1:], 2):
        if active and i != prev:
            return t
        active = (i != prev) if not active else False
        prev = i
    return None


checks = 0
cases = [
    ([[Q(2), Q(0)], [Q(0), Q(3)]], False),
    ([[Q(2), Q(1, 3)], [Q(1, 3), Q(3)]], True),
    ([[Q(2), Q(-1, 3)], [Q(-1, 3), Q(3)]], True),
]
for H, coupled in cases:
    for start_error in [(Q(1), Q(2)), (Q(-2), Q(3))]:
        assert all(start_error)
        assert all(mv(H, start_error))
        for length in range(1, 11):
            for choices in product((0, 1), repeat=length):
                observed, activity = rcgls(H, start_error, choices)
                expected = predicted_stop(choices, coupled)
                assert observed == expected, (H, start_error, choices, observed, expected)
                checks += 1

p, z = sym.symbols('p z')
q, h = 1 - p, p * (1 - p)
F_c = h*z**2*(2-2*z+z**2-h*z**3)/(1-z+h*z**2-h*h*z**4)
F_0 = h*z**2*(2-z)/(1-z+h*z**2)
assert sym.factor(F_c.subs(z, 1) - 1) == 0
assert sym.factor(F_0.subs(z, 1) - 1) == 0
assert sym.factor(sym.diff(F_c, z).subs(z, 1) - (1 + 1/h)) == 0
assert sym.factor(sym.diff(F_0, z).subs(z, 1) - (1/h - 1)) == 0
checks += 4

for prob in [sym.Rational(1,2), sym.Rational(1,3), sym.Rational(3,4)]:
    for coupled, F in [(False, F_0), (True, F_c)]:
        coefficient_list = sym.series(F.subs(p, prob), z, 0, 10).removeO().expand()
        for k in range(1, 10):
            direct = sym.S(0)
            for seq in product((0, 1), repeat=k):
                if predicted_stop(seq, coupled) == k:
                    direct += prob**seq.count(0)*(1-prob)**seq.count(1)
            assert coefficient_list.coeff(z, k) == direct, (prob, coupled, k)
            checks += 1

print('PASS: %d exact-path, symbolic, and finite-law checks' % checks)
print('Coupled exact expected updates = 1 + 1/(p(1-p)); diagonal = 1/(p(1-p)) - 1.')
