#!/usr/bin/env python3
from fractions import Fraction
import sympy as s

def round_half(vectors):
    """
    Exact implementation of the proof's rounding lemma for rational vectors.
    Returns eps_i in {0,1} and checks preservation during nullspace elimination.
    """
    if not vectors:
        return []
    d = len(vectors[0])
    V = [s.Matrix([s.Rational(x.numerator, x.denominator) if isinstance(x, Fraction) else s.Rational(x)
                   for x in v]) for v in vectors]
    q = [s.Rational(1,2) for _ in V]
    target = sum((q[i]*V[i] for i in range(len(V))), s.zeros(d,1))

    while True:
        F = [i for i,x in enumerate(q) if 0 < x < 1]
        if len(F) <= d:
            break
        M = s.Matrix.hstack(*[V[i] for i in F])
        ns = M.nullspace()
        assert ns
        a = ns[0]

        lo = None
        hi = None
        for jj, i in enumerate(F):
            ai = a[jj]
            if ai == 0:
                continue
            l1 = (s.Rational(0)-q[i])/ai
            l2 = (s.Rational(1)-q[i])/ai
            l, h = (l1,l2) if l1 <= l2 else (l2,l1)
            lo = l if lo is None or l > lo else lo
            hi = h if hi is None or h < hi else hi
        assert lo is not None and hi is not None and lo <= 0 <= hi

        # Pick a nonzero endpoint; an endpoint forces at least one variable integral.
        tau = hi if hi != 0 else lo
        assert tau != 0
        old = list(q)
        for jj, i in enumerate(F):
            q[i] = s.simplify(q[i] + tau*a[jj])
            assert 0 <= q[i] <= 1
        represented = sum((q[i]*V[i] for i in range(len(V))), s.zeros(d,1))
        assert represented == target
        assert sum(1 for x in q if 0 < x < 1) < sum(1 for x in old if 0 < x < 1)

    eps = []
    for x in q:
        eps.append(0 if x < s.Rational(1,2) else 1)

    err = sum(((s.Rational(eps[i])-s.Rational(1,2))*V[i] for i in range(len(V))), s.zeros(d,1))
    maxnorm2 = max(sum(c*c for c in v) for v in V)
    err2 = s.expand(sum(c*c for c in err))
    bound2 = s.Rational(d*d,4)*maxnorm2
    assert s.simplify(bound2-err2) >= 0
    return eps, err2, bound2

tests = [
    [[1],[2],[3],[-4],[5]],
    [[1,0],[0,1],[1,1],[2,-1],[-1,2],[3,2]],
    [[1,0,0],[0,1,0],[0,0,1],[1,1,0],[0,1,1],[1,0,1],[2,-1,3]],
    [[1,2,0,1],[0,1,1,2],[2,0,1,-1],[1,1,1,1],[-1,2,3,0],[3,-1,0,2],[2,2,-1,1]],
]
for vecs in tests:
    eps, err2, bound2 = round_half(vecs)
    assert all(e in (0,1) for e in eps)
    assert err2 <= bound2

# Symbolic central-reflection composition in dimension three.
x1,x2,x3,a1,a2,a3,b1,b2,b3 = s.symbols("x1 x2 x3 a1 a2 a3 b1 b2 b3")
x = s.Matrix([x1,x2,x3])
a = s.Matrix([a1,a2,a3])
b = s.Matrix([b1,b2,b3])
Ra = 2*a-x
RbRa = 2*b-Ra
assert s.simplify(RbRa-(x+2*(b-a))) == s.zeros(3,1)

print("VERIFY_OK")
print("rounding_tests =", len(tests))
print("reflection_identity = x + 2(b-a)")
