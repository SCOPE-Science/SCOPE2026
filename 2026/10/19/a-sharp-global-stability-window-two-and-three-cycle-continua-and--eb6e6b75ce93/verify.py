"""Exact rational sanity checks for a piecewise-homogeneous border-collision map.

The infinite-parameter conclusions are established by the accompanying proof,
not by these finite tests. Requires only the Python standard library.
"""
from fractions import Fraction as Q
from itertools import product
from random import Random


def F(z, a, b, d):
    x, y = z
    return ((-a*x+y, Q(0)) if x <= 0 else (-b*x+y, -d*x))


def iterate(z, n, a, b, d):
    for _ in range(n):
        z = F(z, a, b, d)
    return z


def ray_or_zero(z):
    return z == (0, 0) or (z[0] > 0 and z[1] == 0)


def check(a, b, d, pts):
    assert a > 0 and b >= 0 and d > 0
    t = a*b
    lam = t-d if d < t else (a*(d-t) if d > t else Q(0))
    period = 2 if d <= t else 3
    for z in pts:
        traj = [iterate(z, n, a, b, d) for n in range(5)]
        assert any(ray_or_zero(v) for v in traj), (a, b, d, z, traj)
    for r in (Q(1,13), Q(1), Q(29,7)):
        v = (r, Q(0))
        w = iterate(v, period, a, b, d)
        assert w == (lam*r, Q(0)), (a, b, d, v, w, lam)
        if lam == 1:
            assert iterate(v, 1, a, b, d) != v
            if period == 3:
                assert iterate(v, 2, a, b, d) != v
            assert w == v
    if d == t:
        assert all(iterate(z, 5, a, b, d) == (0, 0) for z in pts)
        v = (Q(1), b/Q(2))
        assert iterate(v, 4, a, b, d) != (0, 0)


def main():
    rng = Random(13017)
    candidates = [(Q(2), Q(1), Q(1,2)),
                  (Q(2), Q(1), Q(1)),
                  (Q(2), Q(1), Q(3,2)),
                  (Q(2), Q(1), Q(2)),
                  (Q(2), Q(1), Q(5,2)),
                  (Q(2), Q(1), Q(3)),
                  (Q(3,2), Q(0), Q(1,2)),
                  (Q(3,2), Q(0), Q(2,3))]
    for _ in range(64):
        a = Q(rng.randrange(1,9), rng.randrange(1,7))
        b = Q(rng.randrange(0,9), rng.randrange(1,7))
        d = Q(rng.randrange(1,13), rng.randrange(1,7))
        candidates.append((a,b,d))
        if b > 0:
            candidates.append((a,b,a*b))
            candidates.append((a,b,a*b+1/a))
            if a*b>1:
                candidates.append((a,b,a*b-1))
    vals = [Q(i, 3) for i in range(-9,10)]
    pts = list(product(vals, vals))
    for a,b,d in candidates:
        check(a,b,d,pts)
    print(f"PASS: {len(candidates)} parameter triples x {len(pts)} exact rational initial states;")
    print("       ray entrance, 2/3-step return, critical five-step nilpotence, and neutral cycles.")

if __name__ == '__main__':
    main()
