"""Exact finite example checks for an algebraic theorem. Python 3 standard library only."""
from fractions import Fraction as F

def sample(vals):
    t = tuple(F(v) for v in vals)
    assert len(set(t)) == 3
    s = sum(t)
    U = (F(1),) * 3
    V = t
    vs = []
    for i in range(3):
        j, k = (h for h in range(3) if h != i)
        d = (t[i] - t[j]) * (t[i] - t[k])
        a = (t[i] + 2 - s) / (2 * d)
        b = F(1) / d
        vs.append(tuple(a + b * z for z in t))
    def prod(x, y):
        return tuple(sum(x[i] * y[i] * vs[i][j] for i in range(3)) for j in range(3))
    zero = (F(0),) * 3
    assert prod(U, U) == zero
    assert prod(U, V) == tuple(z / 2 for z in U)
    assert prod(V, V) == tuple(U[j] + V[j] for j in range(3))
    assert tuple(sum(vs[i][j] for i in range(3)) for j in range(3)) == zero
    # For each i, recover a_i and b_i from v_i=a_i U+b_i V, and test projective separation.
    ab = []
    for v in vs:
        b = (v[1] - v[0]) / (t[1] - t[0])
        a = v[0] - b * t[0]
        ab.append((a, b))
    assert all(ab[i][0] * ab[j][1] != ab[j][0] * ab[i][1]
               for i in range(3) for j in range(i))
    center = s / 3
    r = tuple(z - center for z in t)
    p = sum(r[i] * r[j] for i in range(3) for j in range(i))
    q = r[0] * r[1] * r[2]
    delta = -4*p**3-27*q**2
    assert delta != 0
    assert set(r) == set(z-center for z in t)
    return p, q

cases = [(0,1,2), (2,3,4), (0,1,3), (-1,1,3), (F(2,3),2,F(11,7))]
results = [sample(t) for t in cases]
assert results[0] == results[1]
assert results[0] != results[2]
print('VERIFY_OK', results)
