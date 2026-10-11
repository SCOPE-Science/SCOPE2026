"""Exact finite-case corroboration of conjugacy-class Fourier restriction spectra.

Run: python3 artifacts/verify.py
Standard library only. Infinite-parameter claims require the accompanying proof.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import permutations
from math import factorial, prod


def cycle_type(p):
    n = len(p)
    seen = set()
    out = []
    for i in range(n):
        if i in seen:
            continue
        j, ell = i, 0
        while j not in seen:
            seen.add(j)
            ell += 1
            j = p[j]
        out.append(ell)
    return tuple(sorted(out, reverse=True))


def theoretical(n, typ, M):
    f, t = typ.count(1), typ.count(2)
    powers = [Fraction((f-1)**2, n-1), Fraction(f*(n-f), n-2)]
    r3 = Fraction(n-f-2*t, 2)
    r2 = n - 1 - sum(powers) - r3
    powers.extend((r2, r3))
    dims = (1, n-1, n*(n-3)//2, (n-1)*(n-2)//2)
    vals = [Fraction(n*n*M)*r/d for r, d in zip(powers, dims)]
    assert all(v.denominator == 1 and v >= 0 for v in vals)
    return [int(v) for v in vals], dims


def matmul(A, B):
    n = len(A)
    C = [[0]*n for _ in range(n)]
    for i in range(n):
        for k, aik in enumerate(A[i]):
            if aik:
                bk = B[k]
                ci = C[i]
                for j, bkj in enumerate(bk):
                    if bkj:
                        ci[j] += aik * bkj
    return C


def verify_class(n, typ, group):
    N = n*n
    T = [[0]*N for _ in range(N)]
    for p in group:
        b = [n*(int(i == p[j])) - 1 for i in range(n) for j in range(n)]
        for row in range(N):
            a = b[row]
            Tr = T[row]
            for col in range(N):
                Tr[col] += a*b[col]
    eig, mult = theoretical(n, typ, len(group))
    # End(C^n) contains the (n-1)^2-dimensional standard block plus
    # 2n-1 extraneous zero directions.
    spectrum = defaultdict(int)
    for e,d in zip(eig, mult):
        spectrum[e] += d
    spectrum[0] += 2*n-1
    assert sum(spectrum.values()) == N
    roots = sorted(spectrum)
    # Polynomial annihilation P(T)=0 checked on every standard basis vector,
    # not just through traces or floating-point diagonalization.
    for column in range(N):
        v = [int(i == column) for i in range(N)]
        for root in roots:
            v = [sum(T[i][j]*v[j] for j in range(N))-root*v[i]
                 for i in range(N)]
        assert not any(v), (n,typ,column,roots)
    current = [[int(i==j) for j in range(N)] for i in range(N)]
    for k in range(len(roots)):
        assert sum(current[i][i] for i in range(N)) == sum(d*e**k for e,d in spectrum.items()), (n,typ,k)
        current = matmul(current, T)
    return (len(group),len(roots))


def main():
    tested = 0
    group_elements = 0
    for n in range(4,8):
        by_type = defaultdict(list)
        for p in permutations(range(n)):
            by_type[cycle_type(p)].append(p)
        assert sum(len(v) for v in by_type.values()) == factorial(n)
        for typ,group in sorted(by_type.items()):
            z = verify_class(n,typ,group)
            tested += 1
            group_elements += z[0]
    print(f'VERIFY_OK conjugacy_classes={tested} permutations={group_elements} '
          'n=4..7 exact_annihilating_polynomial_and_moment_multiplicities')

if __name__ == '__main__':
    main()
