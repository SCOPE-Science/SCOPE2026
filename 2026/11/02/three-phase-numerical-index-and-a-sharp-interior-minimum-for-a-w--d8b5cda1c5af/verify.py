"""Exact-rational finite diagnostics for four-cycle numerical-index formulas.
The unrestricted theorem is established by the accompanying analytic proof.
Run: python verify.py
"""
from fractions import Fraction as Q
from itertools import permutations


def vertices(r):
    a = (r - 2, Q(1), Q(1), -r)
    b = (Q(1), Q(1), Q(-1), Q(-1))
    out = set()
    for x in (a, b):
        for p in set(permutations(x[:3])):
            for s in (-1, 1):
                out.add(tuple(s * z for z in (*p, x[3])))
    assert len(out) == 12
    return sorted(out)


def dot(f, y):
    return sum(f[i] * y[i] for i in range(3))


def norm(r, y):
    return min(sum(abs(y[i] + s) for i in range(3)) + r * abs(s)
               for s in (Q(0), *(-z for z in y)))


def exact_radius(r, verts, y, source):
    weights = (Q(1), Q(1), Q(1), r)
    return max(abs(source[i]) * abs(dot(f, y))
               for i in range(4) for f in verts if f[i] == weights[i])


def test(r):
    V = vertices(r)
    KL = (-r*r + 5*r - 2) / (r + 1)
    LH = (3*r - 1) / (r * (3-r))
    KH = min(LH, 3/r)
    K = max(KL, KH)
    # Basis-vector samples of the dual-coordinate domination.
    # The analytic proof supplies the global functional decomposition.
    for i in range(4):
        w = Q(1) if i < 3 else r
        normers = [f for f in V if f[i] == w]
        assert normers
        # Finite checks here are diagnostic, not an exhaustive proof
        # of bounds over arbitrary target vectors.
        for j in range(3):
            y = tuple(Q(k == j) for k in range(3))
            assert max(abs(dot(f,y)) for f in V) <= K * max(abs(dot(f,y)) for f in normers)
    a, b = (3-r)/(1+r), 2/(1+r)
    yL = (a,b,b)
    phiL = (Q(1), Q(-1,2), Q(-1,2), Q(0))
    assert norm(r,yL) == KL
    assert exact_radius(r,V,yL,phiL) == 1
    c, d = (r-1)/(r*(3-r)), (r+1)/(r*(3-r))
    yH = (c,c,-d)
    phiH = (-r/3,-r/3,-r/3,Q(1))
    assert norm(r,yH) == LH
    assert exact_radius(r,V,yH,phiH) == max(Q(1),r*LH/3)
    assert max(KL, KH) == K
    # Exact linear functional identities underlying the analytic bound.
    u = (Q(1),Q(1),r-2,-r)
    v = (Q(1),r-2,Q(1),-r)
    w = (Q(1),Q(-1),Q(-1),Q(1))
    z = (r-2,Q(1),Q(1),-r)
    al = (r-1)/(r+1)
    be = r*(3-r)/(r+1)
    assert tuple(al*(u[j]+v[j])-be*w[j] for j in range(4)) == z
    h1=(2-r,Q(-1),Q(-1),r)
    h2=(Q(-1),2-r,Q(-1),r)
    h3=(Q(-1),Q(-1),2-r,r)
    B=(Q(1),Q(1),Q(-1),Q(-1))
    assert tuple(c*(h1[j]+h2[j])-d*h3[j] for j in range(4)) == B
    return K


def main():
    seen = set()
    for den in range(2,25):
        for num in range(den+1, 3*den):
            r = Q(num,den)
            if r in seen:
                continue
            seen.add(r)
            test(r)
    assert test(Q(5,3)) == Q(9,5)
    assert test(Q(2)) == Q(3,2)
    assert test(Q(5,2)) == Q(17,14)  # light branch beyond 1+sqrt(2)
    print('VERIFY_OK rational_parameters=%d 12_dual_vertices=True exact_norm_radius=True'%len(seen))


if __name__=='__main__':
    main()
