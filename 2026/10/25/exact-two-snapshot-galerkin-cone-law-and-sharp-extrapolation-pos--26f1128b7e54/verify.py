"""Exact rational checks for the two-snapshot Galerkin cone theorem.

Python >=3.10, standard library only. The universal theorem rests on the
mathematical proof; finite checks test calculations but cannot prove it.
"""
from fractions import Fraction as F
from random import Random


def dot(x, y):
    return sum((a * b for a, b in zip(x, y)), F(0))


def gram(x, diag, y):
    return sum((a * d * b for a, d, b in zip(x, diag, y)), F(0))


def inverse2(A, b):
    (aa, ab), (ba, bb) = A
    assert ab == ba
    det = aa * bb - ab * ba
    assert det > 0
    return ((bb * b[0] - ab * b[1]) / det,
            (aa * b[1] - ba * b[0]) / det), det


def check(diag0, diag1, rhs, s, t, values):
    assert s < t
    assert len(diag0) == len(diag1) == len(rhs)
    D = lambda y: [aa + y * dd for aa, dd in zip(diag0, diag1)]
    assert all(all(v > 0 for v in D(y)) for y in values + [s, t])
    us = [bb / aa for bb, aa in zip(rhs, D(s))]
    ut = [bb / aa for bb, aa in zip(rhs, D(t))]
    a, d = dot(rhs, us), dot(rhs, ut)
    Hs = gram(ut, D(s), ut)
    Ht = gram(us, D(t), us)
    Ks = a * Hs - d*d
    Kt = d * Ht - a*a
    assert Ks > 0 and Kt > 0
    checks = 0
    for y in values:
        V = D(y)
        G = ((gram(us, V, us), gram(us, V, ut)),
             (gram(ut, V, us), gram(ut, V, ut)))
        (cs, ct), determinant = inverse2(G, (a, d))
        assert cs == (t-y)/(t-s)*Ks/determinant
        assert ct == (y-s)/(t-s)*Kt/determinant
        assert (cs >= 0 and ct >= 0) == (s <= y <= t)
        # Galerkin residual is orthogonal to both snapshots.
        approx = [cs*xi+ct*zi for xi, zi in zip(us, ut)]
        residual = [bb-vv*aa for bb, vv, aa in zip(rhs, V, approx)]
        assert dot(residual, us) == dot(residual, ut) == 0
        checks += 1
    return checks


def example():
    diag0 = [F(1)] * 3
    diag1 = [F(1,10),F(1,2),F(9,10)]
    rhs = [F(1),F(3),F(10)]
    y, s, t = F(-9,10), F(0), F(1,2)
    assert check(diag0,diag1,rhs,s,t,[y]) == 1
    us = [bb / (a+s*d) for bb,a,d in zip(rhs,diag0,diag1)]
    ut = [bb / (a+t*d) for bb,a,d in zip(rhs,diag0,diag1)]
    V = [a+y*d for a,d in zip(diag0,diag1)]
    G=((gram(us,V,us),gram(us,V,ut)),(gram(ut,V,us),gram(ut,V,ut)))
    (cs,ct), determinant = inverse2(G,(dot(rhs,us),dot(rhs,ut)))
    assert (cs,ct) == (F(523575200,25282667),F(-570826575,25282667))
    assert determinant == F(404522672,165571875)
    reduced = [cs*a+ct*b for a,b in zip(us,ut)]
    assert reduced == [F(-140484100,176978669),
                       F(200741820,25282667),
                       F(1299017000,25282667)]
    exact = [r/z for r,z in zip(rhs,V)]
    assert exact == [F(100,91),F(60,11),F(1000,19)]
    assert reduced[0] < 0 < min(exact)
    return 1


def sweep():
    rng = Random(610341)
    n = 0
    for k in range(250):
        dim = 3 + k%3
        aa=[F(1+rng.randrange(1,10), 2) for _ in range(dim)]
        dd=[F(rng.randrange(1,10),20) for _ in range(dim)]
        rhs=[F(rng.randrange(1,15),2) for _ in range(dim)]
        s,t=F(-1,2),F(1,2)
        samples=[F(j,20) for j in range(-18,19)]
        n+=check(aa,dd,rhs,s,t,samples)
    return n


if __name__ == '__main__':
    assert example() == 1
    tested = sweep()
    print(f'PASS: exact 3D counterexample; {tested} exact rational Galerkin/sign identities')
