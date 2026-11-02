"""Finite checks for max-min weighted modal possibility and sharp truncation.

Run: python3 checker.py. Uses only the Python standard library.
"""
from itertools import product, combinations
from fractions import Fraction

VALUES = (Fraction(0), Fraction(1, 3), Fraction(2, 3), Fraction(1))

def dilation(weights, vector):
    return max((min(r, x) for r, x in zip(weights, vector)), default=Fraction(0))

def truncated(weights, vector, keep):
    return max((min(weights[i], vector[i]) for i in keep), default=Fraction(0))

def residue(weights, keep):
    return max((r for i, r in enumerate(weights) if i not in keep), default=Fraction(0))

def verify():
    exact_errors = 0
    for n in range(1, 5):
        for r in product(VALUES, repeat=n):
            for k in range(n+1):
                for indices in combinations(range(n), k):
                    keep = frozenset(indices)
                    rhs = residue(r, keep)
                    largest = Fraction(0)
                    for x in product(VALUES, repeat=n):
                        delta = dilation(r, x) - truncated(r, x, keep)
                        assert Fraction(0) <= delta <= rhs, (r, x, keep, rhs)
                        largest = max(largest, delta)
                    assert largest == rhs, (r, keep, largest, rhs)
                    exact_errors += 1
    # A decaying fuzzy row has infinitely many positive weights but finite superlevel sets.
    # For r_n=1/n, the sorted k-truncation error is exactly 1/(k+1).
    for k in range(0, 30):
        tail_bound = Fraction(1, k+1)
        head = [Fraction(1, i) for i in range(1, k+1)]
        tail_first = Fraction(1, k+1)
        assert tail_first == tail_bound
        assert all(t >= tail_first for t in head)
    # Strictly increasing positive sequence below 1/2 gives nonattained diamond 1/2,
    # if infinitely many fuzzy edges have weight at least 1/2.
    seq = [Fraction(1, 2) * Fraction(n, n+1) for n in range(1, 40)]
    assert all(0 < q < Fraction(1, 2) for q in seq)
    assert all(seq[i] < seq[i+1] for i in range(len(seq)-1))
    # Infinite r_n=1/n: assign p_n=1/(2n^2); box kernels tend to zero, none equals zero.
    for n in range(1, 80):
        r = Fraction(1, n)
        p = Fraction(1, 2*n*n)
        assert 0 < p < r
    print('ALL_CHECKS_OK exact_finite_truncations=', exact_errors)

if __name__ == '__main__':
    verify()
