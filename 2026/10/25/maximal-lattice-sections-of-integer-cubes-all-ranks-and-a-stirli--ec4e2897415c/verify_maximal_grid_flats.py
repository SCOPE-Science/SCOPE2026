"""Independent exact small-grid checks for maximal lattice affine sections.

Run: python verify_maximal_grid_flats.py
Uses only the Python standard library.  These tests are finite checks; the
proof for arbitrary dimensions and grid sizes is given separately.
"""
from fractions import Fraction
from itertools import combinations, product
from math import comb, factorial


def rref(rows):
    """Canonical reduced echelon rows, in exact rational arithmetic."""
    A = [[Fraction(x) for x in row] for row in rows]
    if not A:
        return ()
    lead = 0
    for c in range(len(A[0])):
        if lead == len(A):
            break
        p = next((i for i in range(lead, len(A)) if A[i][c]), None)
        if p is None:
            continue
        A[lead], A[p] = A[p], A[lead]
        v = A[lead][c]
        A[lead] = [z/v for z in A[lead]]
        for i in range(len(A)):
            if i != lead and A[i][c]:
                q = A[i][c]
                A[i] = [x-q*y for x, y in zip(A[i], A[lead])]
        lead += 1
    return tuple(tuple(row) for row in A if any(row))


def stirling2(m, r):
    if m == r == 0:
        return 1
    if m == 0 or r == 0 or r > m:
        return 0
    return stirling2(m-1, r-1) + r * stirling2(m-1, r)


def predicted(d, ell, k):
    first = sum(comb(d, m)*stirling2(m, ell)*2**(m-ell)*
                (k+1)**(d-m) for m in range(ell, d+1))
    num = sum((-1)**(ell-j)*comb(ell,j)*(k+1+2*j)**d
              for j in range(ell+1))
    assert num == first*2**ell*factorial(ell)
    return first


def actual(d, ell, k):
    points = [p + (1,) for p in product(range(k+1), repeat=d)]
    unique_flats = {}
    for choice in combinations(points, ell+1):
        r = rref(choice)
        if len(r) == ell+1:
            unique_flats[r] = None
    max_count = 0
    winners = 0
    for r in unique_flats:
        count = sum(len(rref(r+(p,))) == ell+1 for p in points)
        max_count = max(max_count, count)
        if count == (k+1)**ell:
            winners += 1
    assert max_count == (k+1)**ell
    return winners, len(unique_flats)


def run():
    cases = [(2,1,1),(2,1,2),(2,1,3),
             (3,1,1),(3,2,1),(3,1,2),(3,2,2),
             (4,1,1),(4,2,1),(4,3,1)]
    for d, ell, k in cases:
        want = predicted(d,ell,k)
        found, tested = actual(d,ell,k)
        assert found == want, (d,ell,k,found,want)
        print('d=%d ell=%d k=%d maximum=%d winning_flats=%d tested_flats=%d' %
              (d,ell,k,(k+1)**ell,found,tested))
    for d in range(1,12):
        for ell in range(0,d+1):
            for k in (1,2,7):
                predicted(d,ell,k)
    print('CUBICAL_MAXIMAL_FLATS_OK exhaustive_cases=%d formula_identities=%d' %
          (len(cases), sum(d+1 for d in range(1,12))*3))

if __name__ == '__main__':
    run()
