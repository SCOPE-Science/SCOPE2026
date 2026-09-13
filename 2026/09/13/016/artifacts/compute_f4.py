"""F4 short- vs long-root zonotope mixed volumes. Exact arithmetic via Bareiss
on denominator-cleared integer matrices (halves doubled, per-subset rescaling).
Z = sum over short-root pairs: e_i (4) + halves (8, first sign +), mZ=12.
Y = sum over long-root pairs: e_i+e_j, e_i-e_j (12), mY=12. Rank 4, C=(Z,Z).
S0 = sum_{|S|=4 subset Z} |det S|            (denominators 2^h cleared exactly)
S1 = sum_{b in Y} sum_{|T|=3} |det(b,T)|
S2 = sum_{ordered b1!=b2} sum_{|U|=2} |det(b1,b2,U)|
V(Z,Z,C)=16 S0; V(Z,Y,C)=16 S1/4; V(Y,Y,C)=16 S2/12.
Deficit sign N = 3 S1^2 - 4 S0 S2  (all in units of 16^2 after clearing).
Represent every generator as (integer vector, scale_exp): value = vec/2^e.
det of columns with exps e_k = D / 2^(sum e), D = det of integer matrix.
"""
import itertools
from fractions import Fraction


def bareiss(M):
    A = [list(map(int, row)) for row in M]
    n = len(A)
    if n == 0:
        return 1
    prev = 1
    for k in range(n - 1):
        if A[k][k] == 0:
            piv = next((i for i in range(k + 1, n) if A[i][k] != 0), None)
            if piv is None:
                return 0
            A[k], A[piv] = A[piv], A[k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                A[i][j] = (A[i][j] * A[k][k] - A[i][k] * A[k][j]) // prev
            A[i][k] = 0
        prev = A[k][k]
    return A[n - 1][n - 1]


def short_gens():
    G = []
    for i in range(4):
        v = [0] * 4
        v[i] = 1
        G.append((v, 0))
    for s2 in (1, -1):
        for s3 in (1, -1):
            for s4 in (1, -1):
                G.append(([1, s2, s3, s4], 1))  # value = vec/2
    return G


def long_gens():
    G = []
    for i in range(4):
        for j in range(i + 1, 4):
            v = [0] * 4
            v[i] = 1
            v[j] = 1
            G.append((v, 0))
            w = [0] * 4
            w[i] = 1
            w[j] = -1
            G.append((w, 0))
    return G


def adet(cols):
    """cols: list of (vec, exp). Returns Fraction |det|."""
    n = len(cols[0][0])
    M = [[c[0][r] for c in cols] for r in range(n)]
    D = bareiss(M)
    e = sum(c[1] for c in cols)
    return Fraction(abs(D), 2 ** e)


def main():
    Z = short_gens()
    Y = long_gens()
    assert len(Z) == 12 and len(Y) == 12, (len(Z), len(Y))
    S0 = sum((adet([Z[i] for i in S]) for S in itertools.combinations(range(12), 4)),
             Fraction(0))
    S1 = Fraction(0)
    for b in Y:
        for T in itertools.combinations(range(12), 3):
            S1 += adet([b] + [Z[i] for i in T])
    S2 = Fraction(0)
    for a in range(12):
        for b in range(12):
            if a == b:
                continue
            for U in itertools.combinations(range(12), 2):
                S2 += adet([Y[a], Y[b]] + [Z[i] for i in U])
    N = 3 * S1 * S1 - 4 * S0 * S2
    print("S0 =", S0, "=", float(S0))
    print("S1 =", S1, "=", float(S1))
    print("S2 =", S2, "=", float(S2))
    print("N  =", N, "=", float(N))
    print("N > 0:", N > 0)


if __name__ == "__main__":
    main()
