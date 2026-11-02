#!/usr/bin/env python3
"""Exact invariant checks and sampled inertia comparisons for real coordinate-tangent quadrics."""
import random
import sympy as sp

u, v, s, t = sp.symbols('u v s t')
b01, b02, b03, b12, b13, b23 = sp.symbols('b01 b02 b03 b12 b13 b23')
B = sp.Matrix([[0, b01, b02, b03], [b01, 0, b12, b13],
               [b02, b12, 0, b23], [b03, b13, b23, 0]])
a, b, c = b01*b23, b02*b13, b03*b12
Delta = a*a+b*b+c*c - 2*(a*b+a*c+b*c)
assert sp.expand(B.det()-Delta) == 0

split = sp.Matrix([[0, 0, 0, 1], [0, 0, -1, 0],
                   [0, -1, 0, 0], [1, 0, 0, 0]])
nonsplit = sp.ones(4)-sp.eye(4)
assert split.det() == 1
assert nonsplit.det() == -3
assert split.eigenvals() == {-1: 2, 1: 2}
assert nonsplit.eigenvals() == {-1: 3, 3: 1}
for C in (split, nonsplit):
    A = C.inv()
    assert A*C == sp.eye(4)
    assert list(C.diagonal()) == [0, 0, 0, 0]
    assert C.trace() == 0
    # For a real symmetric invertible B with zero diagonal, sign det(B) gives
    # the parity of negative eigenvalues; trace zero excludes definite cases.

# The split model is an actual coordinatewise product of real lines.
L = sp.Matrix([s, s, t, t]); R = sp.Matrix([u, v, u, v])
X = sp.Matrix([L[i]*R[i] for i in range(4)])
assert sp.expand((X.T*split*X)[0]) == 0
assert sp.Matrix([[1,1,0,0], [0,0,1,1]]).rank() == 2
assert sp.Matrix([[1,0,1,0], [0,1,0,1]]).rank() == 2

# Deterministic exact-det finite checks, with floating eigenvalues only as
# diagnostics (the general signature assertion is proved, not sampled).
try:
    import numpy as np
    rng = random.Random(20261030)
    tested = 0
    while tested < 128:
        vals = [rng.randint(-5,5) for _ in range(6)]
        M = B.subs(dict(zip((b01,b02,b03,b12,b13,b23), vals)))
        determinant = int(M.det())
        if abs(determinant) < 10:
            continue
        ev = np.linalg.eigvalsh(np.array(M).astype(float))
        if min(abs(float(z)) for z in ev) < 1e-8:
            continue
        negative = sum(float(z)<0 for z in ev)
        assert 1 <= negative <= 3
        assert (determinant > 0) == (negative == 2)
        tested += 1
    print('VERIFY_OK: symbolic determinant identity, 2 exact examples, '
          f'{tested} sampled signature checks')
except ImportError:
    print('VERIFY_OK: symbolic determinant identity and 2 exact examples '
          '(optional numpy signature samples skipped)')
