"""Exact-arithmetic finite checks for obligate cyclic food-web equilibria.

The proof for every order uses strict row-permuted diagonal dominance;
these computations are supplemental, not a substitute for the proof.
"""
from fractions import Fraction as Q
from random import Random


def determinant(matrix):
    """Exact determinant by Gaussian elimination over Q."""
    n = len(matrix)
    a = [list(row) for row in matrix]
    sign = 1
    result = Q(1)
    for col in range(n):
        p = next((r for r in range(col, n) if a[r][col]), None)
        if p is None:
            return Q(0)
        if p != col:
            a[p], a[col] = a[col], a[p]
            sign = -sign
        q = a[col][col]
        result *= q
        for r in range(col + 1, n):
            if a[r][col]:
                ratio = a[r][col] / q
                for c in range(col+1, n):
                    a[r][c] -= ratio * a[col][c]
                a[r][col] = Q(0)
    return sign * result


def check_case(n, trial, rng):
    # A strictly positive equilibrium is prescribed in exact rational form.
    x = [Q(rng.randint(1, 9), rng.randint(1, 6)) for _ in range(n)]
    a = [Q(rng.randint(1, 9), rng.randint(1, 6)) for _ in range(n)]
    b = [Q(rng.randint(1, 9), rng.randint(1, 6)) for _ in range(n)]
    B = [[Q(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        B[i][i] = b[i]
        for j in range(n):
            if j != i and j != (i+1) % n:
                B[i][j] = Q(rng.randint(1, 9), rng.randint(1, 6))
        positive = sum((B[i][j]*x[j] for j in range(n)), Q(0))
        B[i][(i+1)%n] = -(a[i] + positive) / x[(i+1)%n]
        assert sum((B[i][j]*x[j] for j in range(n)),Q(0)) == -a[i]
        assert -B[i][(i+1)%n]*x[(i+1)%n] > sum((B[i][j]*x[j] for j in range(n) if j != (i+1)%n),Q(0))
    M = [[B[i][j]*x[j] for j in range(n)] for i in range(n)]
    detM = determinant(M)
    assert detM < 0, (n, trial, detM)
    # Check the homotopy at positive rational points using exact determinants.
    for t in (Q(0), Q(1,4), Q(1,2), Q(3,4), Q(1)):
        Mt = [[M[i][j] if j == (i+1)%n else t*M[i][j] for j in range(n)] for i in range(n)]
        assert determinant(Mt) < 0
    return detM


def main():
    rng = Random(281828)
    cases=0
    for n in range(3, 10):
        for trial in range(12):
            check_case(n, trial, rng)
            cases += 1
    # Symmetric exact witness in each order: a=b=d=1, c=n and x*=1.
    for n in range(3, 16):
        B = [[Q(1) if (i==j or j!=(i+1)%n) else Q(-n) for j in range(n)] for i in range(n)]
        assert all(sum(row,Q(0)) == -1 for row in B)
        assert determinant(B) < 0
        # -B*ones = ones shows positive real eigenvalue exactly 1.
        assert all(-sum(row,Q(0)) == 1 for row in B)
    print('PASS: 84 nonuniform rational equilibria n=3..9, 5 exact homotopy points each; 13 explicit witnesses n=3..15.')

if __name__ == '__main__':
    main()
