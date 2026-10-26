"""Exact finite checks for the periodic P1 consistent-mass backward-Euler step.
Run with: python verify.py
Only the Python standard library is required. These checks corroborate but are
not a proof of the all-parameter theorem; see RESULT.md for that proof.
"""
from fractions import Fraction as F

def eye(n):
    return [[F(int(i == j)) for j in range(n)] for i in range(n)]

def add(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A))] for i in range(len(A))]

def scale(c, A):
    return [[c * A[i][j] for j in range(len(A))] for i in range(len(A))]

def mul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

def inv(A):
    n = len(A)
    E = eye(n)
    X = [A[i][:] + E[i] for i in range(n)]
    for j in range(n):
        p = next((i for i in range(j, n) if X[i][j]), None)
        assert p is not None
        X[j], X[p] = X[p], X[j]
        d = X[j][j]
        X[j] = [v / d for v in X[j]]
        for i in range(n):
            if i != j and X[i][j]:
                c = X[i][j]
                X[i] = [X[i][k] - c * X[j][k] for k in range(2*n)]
    return [row[n:] for row in X]

def transition(n, r):
    I = eye(n)
    A = [[F(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        A[i][(i+1) % n] += 1
        A[i][(i-1) % n] += 1
    M = add(scale(F(4), I), A)
    K = add(scale(F(2), I), scale(F(-1), A))
    B = add(M, scale(6*r, K))
    return mul(inv(B), M)

def main():
    safe = (F(0), F(1, 6), F(1, 3))
    unsafe = (F(1, 100), F(1, 12), F(47, 300))
    tested = 0
    for n in range(3, 11):
        for r in safe + unsafe:
            T = transition(n, r)
            assert all(sum(row) == 1 for row in T), (n, r, "row sums")
            if n == 3 or r in safe:
                assert all(x >= 0 for row in T for x in row), (n, r, "nonnegative")
            else:
                assert T[0][2] < 0, (n, r, "negative distance-two entry")
            tested += 1
    print(f"FINITE_CHECKS_OK {tested} exact matrix instances")

if __name__ == "__main__":
    main()
