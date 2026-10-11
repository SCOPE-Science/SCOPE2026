"""Deterministic rational checks for orbit witnesses in free p-convex lattices.

These are finite illustrative checks of the column identity and order-statistic
extremizers. The analytic theorem does not depend on them.
"""
from fractions import Fraction
from itertools import product


def rot(v, k):
    return v[k:] + v[:k]


def check_column_identity(v, p):
    """For cyclic shifts, verify all normalized weak-p column sums equal 1."""
    n = len(v)
    energy = sum(abs(x) ** p for x in v)
    if energy == 0:
        return False
    scale_p = Fraction(1, energy)  # |G|=n, orbit scaling^p=1/energy
    rows = [rot(v, k) for k in range(n)]
    return all(sum(abs(row[j]) ** p * scale_p for row in rows) == 1
               for j in range(n))


def check_orbit_witness(v, p, fn):
    n = len(v)
    energy = sum(abs(x) ** p for x in v)
    if not energy:
        return False
    assert all(fn(rot(v, k)) == fn(v) for k in range(n))
    # The proposed equality is between pth powers of the multi-row
    # witness and the formula n^(1/p)*sup_{S_p}|fn| at direction v.
    orbit_p = sum(Fraction(fn(rot(v, k)) ** p, energy) for k in range(n))
    target_p = Fraction(n * fn(v) ** p, energy)
    return orbit_p == target_p


def kth_abs(v, k):
    return sorted((abs(x) for x in v), reverse=True)[k-1]


def main():
    checks = 0
    for n in range(2, 6):
        for p in (1, 2, 3):
            for tup in product((-2, 0, 1), repeat=n):
                v = list(tup)
                if not any(v):
                    continue
                assert check_column_identity(v, p)
                checks += 1
                for fn in (lambda u: max(abs(x) for x in u),
                           lambda u: sum(abs(x) for x in u),
                           lambda u: abs(sum(u))):
                    assert check_orbit_witness(v, p, fn)
                    checks += 1
                for k in range(1, n+1):
                    assert check_orbit_witness(v, p, lambda u, k=k: kth_abs(u,k))
                    checks += 1
            for k in range(1,n+1):
                # Sharp order-statistic bound: k times the pth power of
                # the k-th largest coordinate never exceeds p-energy.
                for tup in product((-2, 0, 1), repeat=n):
                    energy = sum(abs(x)**p for x in tup)
                    kth = kth_abs(tup, k)
                    assert k * kth**p <= energy
                    checks += 1
                extremal = [1]*k + [0]*(n-k)
                assert k*kth_abs(extremal,k)**p == sum(abs(x)**p for x in extremal)
                checks += 1
    # The two pointwise-disjoint positive functions
    # h=(|u_1|-|u_2|)_+, k=(|u_2|-|u_1|)_+ attain the rows e1,e2.
    for p in (1,2,3):
        rows = ((1,0),(0,1))
        h = lambda u: max(abs(u[0])-abs(u[1]), 0)
        k = lambda u: max(abs(u[1])-abs(u[0]), 0)
        assert all(min(h(u),k(u))==0 for u in rows)
        assert sum(max(h(u),k(u))**p for u in rows) == 2
        assert max(sum(abs(u[j])**p for u in rows) for j in (0,1)) == 1
        checks += 3
    print('PASS: %d exact integer/rational checks; dimensions 2..5, exponents 1,2,3' % checks)


if __name__ == '__main__':
    main()
