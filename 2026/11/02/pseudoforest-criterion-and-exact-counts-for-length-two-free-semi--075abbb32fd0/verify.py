"""Finite checks for the two-uniform free-semigroup morphism classification.

No external dependencies. Exhaustive checks are finite corroboration; the
all-rank assertions in RESULT.md use symbolic combinatorial proofs.
"""
from itertools import combinations
from math import comb, factorial
from fractions import Fraction


def sparsity_stats(n):
    edges = tuple((u, v) for u in range(n) for v in range(n))
    vertex_sets = tuple(frozenset(B) for k in range(1, n)
                        for B in combinations(range(n), k))
    rank_preserving = prime = 0
    for W in combinations(edges, n):
        e = tuple(sum(u in B and v in B for u, v in W) for B in vertex_sets)
        if all(t <= len(B) for t, B in zip(e, vertex_sets)):
            rank_preserving += 1
            prime += all(t < len(B) for t, B in zip(e, vertex_sets))
    return rank_preserving, prime


def direct_factor_basis_stats(n):
    """Independently enumerate all length-at-most-two factor bases."""
    edges = tuple((u, v) for u in range(n) for v in range(n))
    rank_preserving = prime = 0
    for W in combinations(edges, n):
        candidates = tuple((u,) for u in range(n)) + W
        def covers(V):
            vset = set(V)
            return all(w in vset or ((w[0],) in vset and (w[1],) in vset)
                       for w in W)
        is_lower = any(covers(V) for m in range(1, n)
                       for V in combinations(candidates, m))
        if not is_lower:
            rank_preserving += 1
            prime += not any(covers(V) for V in combinations(candidates, n)
                             if set(V) != set(W)
                             and set(V) != set((u,) for u in range(n)))
    return rank_preserving, prime


def product(a, b, N):
    out = [Fraction(0) for _ in range(N + 1)]
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            if i + j <= N:
                out[i + j] += ai * bj
    return out


def rank_preserving_egf(N):
    T = [Fraction(0)] + [Fraction(2**(n-1)*n**(n-1), factorial(n))
                          for n in range(1, N+1)]
    C = [Fraction(0) for _ in range(N+1)]
    Tpower = [Fraction(1)] + [Fraction(0)]*N
    for ell in range(1, N+1):
        Tpower = product(Tpower, T, N)
        multiplier = (Fraction(1) if ell == 1 else
                      Fraction(1, 2) if ell == 2 else
                      Fraction(2**(ell-1), ell))
        C = [a + multiplier*b for a, b in zip(C, Tpower)]
    A = [Fraction(1)] + [Fraction(0)]*N
    for n in range(1, N+1):
        A[n] = sum(k*C[k]*A[n-k] for k in range(1, n+1))/n
    return [int(factorial(n)*A[n]) for n in range(1, N+1)]


def main():
    expected_ranks = (1, 6, 72, 1274, 29610)
    expected_primes = (1, 1, 8, 48, 384)
    for n, (r0, p0) in enumerate(zip(expected_ranks, expected_primes), 1):
        observed = sparsity_stats(n)
        assert observed == (r0, p0), (n, observed)
        if n <= 4:
            assert direct_factor_basis_stats(n) == observed
        morphisms = factorial(n)*p0
        formula = (1 if n == 1 else 2 if n == 2 else
                   2**(n-1)*factorial(n-1)*factorial(n))
        assert morphisms == formula
        print('n', n, 'rank_preserving_word_sets', r0,
              'irreducible_word_sets', p0, 'irreducible_morphisms', morphisms)
    assert rank_preserving_egf(5) == list(expected_ranks)
    print('ALL_CHECKS_PASSED')


if __name__ == '__main__':
    main()
