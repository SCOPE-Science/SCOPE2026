"""Exact checks for the odd-characteristic Barth--Nieto quintic singular strata.

Run: python3 verify.py   (requires SymPy).
The geometric completeness proof is given in RESULT.md; point enumeration is a check.
"""
from itertools import combinations, product
import sympy as sp

z = sp.symbols('z0:4')
x = list(z) + [-1 - sum(z), sp.Integer(1)]
e5 = sp.expand(sum(sp.prod(x[j] for j in range(6) if j != i) for i in range(6)))
grad = [sp.diff(e5, v) for v in z]
hess = sp.hessian(e5, z)

for p in (3, 5):
    for name, coords in {
        'diagonal': (1, 1, 1, 1),
        'segre': (-1, -1, -1, 1),
    }.items():
        # The diagonal lies on the threefold only in characteristic three.
        if name == 'diagonal' and p != 3:
            continue
        subs = dict(zip(z, coords))
        assert int(e5.subs(subs)) % p == 0
        assert all(int(g.subs(subs)) % p == 0 for g in grad)
        det = int(hess.subs(subs).det()) % p
        assert det != 0, (p, name)
        print(f'P{p}_{name.upper()}_HESSIAN_DETERMINANT={det};RANK=4')

    def canon(v):
        a = next(a for a in v if a)
        inv = pow(a, -1, p)
        return tuple(k * inv % p for k in v)

    pts = set()
    # Two projective charts: last coordinate one, or last coordinate zero.
    for u in product(range(p), repeat=5):
        v = u + (1,)
        if sum(v) % p == 0:
            pts.add(canon(v))
    for u in product(range(p), repeat=5):
        v = u + (0,)
        if any(v) and sum(v) % p == 0:
            pts.add(canon(v))

    def val(v):
        return sum(sp.prod(v[j] for j in range(6) if j != i) for i in range(6)) % p

    def derivative(v, i):
        return sum(sp.prod(v[k] for k in range(6) if k not in (i, j))
                   for j in range(6) if j != i) % p

    actual = {v for v in pts if val(v) == 0 and
              len({derivative(v, i) for i in range(6)}) == 1}
    boundary = {v for v in pts if sum(a == 0 for a in v) >= 3}
    segre = {canon(tuple(1 if i in inds else p-1 for i in range(6)))
             for inds in combinations(range(6), 3)}
    extra = {canon((1,) * 6)} if p == 3 else set()
    assert len(segre) == 10
    assert actual == boundary | segre | extra
    assert len(boundary) == 20 * (p - 2) + 15
    assert len(actual) == 20 * p - 25 + 10 + (p == 3)
    print(f'P{p}_GEOMETRIC_PATTERN_F{p}_CHECK=PASS;BOUNDARY={len(boundary)};'
          f'SEGRE={len(segre)};EXTRA={len(extra)};TOTAL={len(actual)}')

print('NONFINITE_COMPLETENESS=PROVED_BY_ZERO-COORDINATE_AND_TORUS_CASEWORK_IN_RESULT')
print('VERIFY_OK')
