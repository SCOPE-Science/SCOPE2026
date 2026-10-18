"""Exact lattice-point checks of anchored Lipschitz polytope volumes.

Uses only the Python standard library. The analytic all-dimensional proof is
separate; these checks verify selected cases independently by Ehrhart theory.
"""
from fractions import Fraction
from math import factorial

CASES = [(3,(1,)), (4,(1,1)), (6,(4,)), (4,(2,)), (5,(3,)), (5,(1,1)), (6,(2,2)),
         (6,(1,2)), (7,(2,2)), (7,(1,1,2)), (7,(3,2))]


def lattice_count(n, components, dilation):
    """Count integer anchored Lipschitz potentials of graph complement."""
    missing = set()
    start = 0
    for m in components:
        missing.update((start, start+j) for j in range(1, m+1))
        start += m + 1
    assert start <= n
    edges = {(u,v) for u in range(n) for v in range(u+1,n)
             if (u,v) not in missing}
    coords = [0] * n
    count = 0
    def visit(i):
        nonlocal count
        if i == n:
            count += 1
            return
        for val in range(-2*dilation, 2*dilation+1):
            if all(abs(coords[j]-val) <= dilation
                   for j in range(i) if (j,i) in edges):
                coords[i] = val
                visit(i+1)
    visit(1)
    return count


def volume_from_counts(n, components):
    dim = n-1
    counts = [lattice_count(n, components, k) for k in range(dim+1)]
    diffs = counts
    for _ in range(dim):
        diffs = [b-a for a,b in zip(diffs,diffs[1:])]
    return Fraction(diffs[0], factorial(dim)),counts


def theorem_volume(n, components):
    return Fraction(n)+sum((Fraction(2*m,n-m) for m in components),Fraction())


def main():
    for n,components in CASES:
        observed,counts=volume_from_counts(n,components)
        expected=theorem_volume(n,components)
        assert observed==expected,(n,components,observed,expected)
        print('PASS',n,components,str(observed),'Ehrhart',counts)
    print('PASS: 11 exact independent volume checks')


if __name__=='__main__':
    main()
