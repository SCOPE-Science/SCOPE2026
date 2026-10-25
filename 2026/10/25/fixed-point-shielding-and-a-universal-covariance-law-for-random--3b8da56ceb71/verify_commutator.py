"""Exact finite checks for pointwise commutator agreements and fixed points.

The analytic proof is independent of the finite computation. No dependencies.
"""
from fractions import Fraction
from itertools import permutations


def check_eta(n, eta, pis):
    fixed = set(i for i in range(n) if eta[i] == i)
    f = len(fixed)
    g = n - f
    A = [0] * n
    B = [0] * n
    AB = [[0] * n for _ in range(n)]
    all_pairs = list(pis)
    for p in all_pairs:
        agreements = [int(eta[p[x]] == p[eta[x]]) for x in range(n)]
        fixed_ind = [int(p[j] == j) for j in range(n)]
        for x in range(n):
            A[x] += agreements[x]
            B[x] += fixed_ind[x]
            for j in range(n):
                AB[x][j] += agreements[x] * fixed_ind[j]
    total = len(all_pairs)
    assert total > 0
    assert all(b == total // n for b in B)
    checked = 0
    total_cov = Fraction(0)
    for x in range(n):
        for j in range(n):
            cov = Fraction(AB[x][j], total) - Fraction(A[x] * B[j], total * total)
            if x in fixed:
                if x == j:
                    want = Fraction(g, n * n)
                elif j in fixed:
                    want = Fraction(-g, n * n * (n - 1))
                else:
                    want = Fraction(f, n * n * (n - 1))
            elif j in (x, eta[x]):
                want = Fraction(f, n * n * (n - 1))
            elif j in fixed:
                want = Fraction(2 * g, n * n * (n - 1) * (n - 2))
            else:
                want = Fraction(-2 * f, n * n * (n - 1) * (n - 2))
            assert cov == want, (n, eta, x, j, cov, want)
            if f in (0, n):
                assert cov == 0
            total_cov += cov
            checked += 1
    assert total_cov == Fraction(f * g, (n - 1) * (n - 2))
    checked += 1
    return checked


def main():
    checks = 0
    for n in range(3, 6):
        pis = list(permutations(range(n)))
        for eta in pis:
            checks += check_eta(n, eta, pis)
    n = 6
    pis = list(permutations(range(n)))
    reps = [pis[0], pis[1], pis[123], pis[500], pis[719]]
    for eta in reps:
        checks += check_eta(n, eta, pis)
    print(f"PASS: {checks} exact rational cross-covariance and aggregate checks")


if __name__ == "__main__":
    main()
