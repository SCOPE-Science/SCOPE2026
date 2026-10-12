"""Standalone exact-rational checks for sketched harmonic Ritz positivity.

Requires only Python 3 standard library. The infinite-dimensional quantifiers
(in finite matrix sizes) follow from the accompanying mathematical proof.
"""
from fractions import Fraction as Q
from random import Random


def mm(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def trans(a):
    return list(map(list, zip(*a)))


def spd2(a):
    return a[0][0] > 0 and a[0][0] * a[1][1] - a[0][1] ** 2 > 0


def witness(q, eps):
    """Exact two-mode witness with A=diag(1,1/q^2), raw x=(q,1)."""
    k = q*q
    c = Q(2*q, k+1)
    a = [[Q(1), Q(0)], [Q(0), Q(1,k)]]
    x = [[Q(q)], [Q(1)]]
    b = [[Q(q)], [Q(k)]]
    e = [[Q(1), -eps], [-eps, Q(1)]]
    assert mm(a, b) == x
    F = mm(trans(x), mm(e,x))[0][0]
    G = mm(trans(x), mm(e,b))[0][0]
    assert F == Q(k+1) - 2*eps*q
    assert G == Q(2*k) - eps*q*(k+1)
    assert F > 0 and 0 <= eps < 1
    assert (G > 0) == (eps < c)
    assert (G == 0) == (eps == c)
    if G:
        assert F/G == (1-eps*c)/(q*(c-eps))
    return G, F, c


def check_3d(k, eps, rng):
    """Check arbitrary 2D trial bases in 3D, with a sharp 2-plane sketch distortion."""
    a = [[Q(1),Q(0),Q(0)],
         [Q(0),Q(1,k),Q(0)],
         [Q(0),Q(0),Q(1)]]
    e = [[Q(1),-eps,Q(0)],
         [-eps,Q(1),Q(0)],
         [Q(0),Q(0),Q(1)]]
    b = [[Q(rng.randrange(-8,9)),Q(rng.randrange(-8,9))] for _ in range(3)]
    w = mm(a,b)
    G = mm(trans(w),mm(e,b))
    F = mm(trans(w),mm(e,w))
    sym = [[(G[i][j]+G[j][i])/2 for j in range(2)] for i in range(2)]
    # Skip rank-deficient bases: their positive definiteness is not claimed.
    minors = [(b[i][0]*b[j][1]-b[i][1]*b[j][0]) for i in range(3) for j in range(i+1,3)]
    if all(v == 0 for v in minors):
        return 0
    assert spd2(sym) and spd2(F)
    return 1


def main():
    exact_witness = 0
    boundary = 0
    for q in range(2,35):
        c = Q(2*q,q*q+1)
        for eps in (Q(0), c/2, c-Q(1,10000), c, (c+1)/2, Q(99,100)):
            if eps < 0 or eps >= 1:
                continue
            witness(q,eps)
            exact_witness += 1
            if eps == c:
                boundary += 1
    assert witness(3,Q(3,5))[0] == 0
    g,f,c = witness(3,Q(2,3))
    assert (c,g,f,f/g) == (Q(3,5),Q(-2),Q(6),Q(-3))
    # F, G above use unnormalized vectors, so F= (k+1)*(1-eps*c).
    # For eps=2/3, F=6 and G=-2; equivalently normalized F=3/5,G=-1/5.
    rng = Random(27182818)
    multi = 0
    for q in range(2,24):
        c = Q(2*q,q*q+1)
        for eps in (Q(0), Q(1,2)*c, Q(99,100)*c):
            for _ in range(150):
                multi += check_3d(q*q,eps,rng)
    print(f"VERIFY_OK exact_rational_witnesses={exact_witness} singular_boundaries={boundary} trial_subspace_checks={multi} negative_Ritz_minus3=true")


if __name__ == "__main__":
    main()
