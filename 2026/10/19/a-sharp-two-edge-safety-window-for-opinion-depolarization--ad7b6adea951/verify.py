"""Exact symbolic spot checks for a two-edge Friedkin--Johnsen polarization theorem.

Requires Python 3 and SymPy.  The analytical proof, not finite tests, covers
all graph sizes, positive real edge weights, innate opinions, and times.
"""
import itertools
import sympy as S

A, C, U, V, t = S.symbols('a b u v t', positive=True)
E12 = S.Matrix([[1, -1, 0], [-1, 1, 0], [0, 0, 0]])
E23 = S.Matrix([[0, 0, 0], [0, 1, -1], [0, -1, 1]])
H = S.eye(3) + A * E12 + C * E23
B = U * E12 + V * E23
Q = S.expand(H * B + B * H)

K = 14 * A * C + 8 * (A + C) + 4
expected_trace = 2 * (4 * A * U + A * V + C * U + 4 * C * V + 2 * U + 2 * V)
expected_minor_sum = 3 * (K * U * V - A**2 * V**2 - C**2 * U**2)
minor_sum = sum(Q.extract(ix, ix).det() for ix in ((0, 1), (0, 2), (1, 2)))
assert S.simplify(S.trace(Q) - expected_trace) == 0
assert S.factor(minor_sum - expected_minor_sum) == 0
assert Q * S.ones(3, 1) == S.zeros(3, 1)
assert S.factor(K**2 - 4 * A**2 * C**2).is_positive is True

# Symbolic differentiation of the inverse-square polarization matrix.
x, y = S.symbols('x y')
base = H.subs({A: 1, C: 2})
change = B.subs({U: x, V: y})
T = base + t * change
assert S.simplify(T.diff(t) - change) == S.zeros(3)
assert S.simplify(T.inv().diff(t) + T.inv() * change * T.inv()) == S.zeros(3)
assert S.simplify(
    (T.inv() ** 2).diff(t)
    + T.inv() * change * (T.inv() ** 2)
    + (T.inv() ** 2) * change * T.inv()
) == S.zeros(3)

samples = [(1, 1, True), (15, 1, False), (1, 0, False), (0, 1, False)]
for u, v, is_safe in samples:
    q = Q.subs({A: 1, C: 2, U: u, V: v})
    d = S.factor(sum(q.extract(ix, ix).det() for ix in ((0, 1), (0, 2), (1, 2))))
    assert (d >= 0) == is_safe
    assert S.trace(q) > 0

for u, v, s_tuple in ((1, 0, (0, -1, 1)), (0, 1, (-1, 1, 0)), (15, 1, (0, -1, 1))):
    s = S.Matrix(s_tuple)
    q = Q.subs({A: 1, C: 2, U: u, V: v})
    w = base.inv()**2 * s
    slope = -(w.T * q * w)[0]
    assert slope == S.Rational(10, 2197)
    assert sum(s) == 0

# Samples illustrate the proved implication, but do not establish it.
count = 0
for tup in itertools.product(range(-2, 3), repeat=2):
    s = S.Matrix([tup[0], tup[1], -tup[0] - tup[1]])
    if s == S.zeros(3, 1):
        continue
    p0 = ((base.inv() * s).T * (base.inv() * s))[0]
    for tau in (S.Rational(1, 100), S.Rational(1, 3), S.Integer(1), S.Integer(5)):
        dep = (base + tau * (E12 + E23)).inv() * s
        pt = (dep.T * dep)[0]
        assert pt < p0
        count += 1
print('PASS: symbolic trace, principal-minor sum, inverse derivative, exact unsafe witnesses.')
print(f'PASS: {count} exact finite balanced-batch profile checks; proof covers all parameters.')
