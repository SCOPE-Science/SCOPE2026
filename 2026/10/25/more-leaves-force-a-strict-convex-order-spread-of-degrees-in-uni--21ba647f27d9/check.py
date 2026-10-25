"""Exact finite checks for the leaf-conditioned tagged-degree ordering.

The finite checker is supplementary: the proof in RESULT.md is analytic.
Run with Python 3, no third-party packages required.
"""
from fractions import Fraction
from itertools import product
from math import comb


def stirling_table(nmax):
    s = [[0] * (nmax + 2) for _ in range(nmax + 2)]
    s[0][0] = 1
    for n in range(1, nmax + 2):
        for k in range(1, n + 1):
            s[n][k] = k * s[n-1][k] + s[n-1][k-1]
    return s


def tagged_law(n, j, s):
    N = n - 2
    assert 1 <= j <= N
    return [Fraction(n-j, n)] + [
        Fraction(comb(N, c) * s[N-c][j-1], n * s[N][j])
        for c in range(1, N + 1)
    ]


def size_biased_law(n, j, s):
    N = n - 2
    return [Fraction(0)] + [
        Fraction(comb(N-1, c-1) * s[N-c][j-1], s[N][j])
        for c in range(1, N + 1)
    ]


def main():
    s = stirling_table(65)
    cases = 0
    hinges = 0
    minors = 0
    for n in range(4, 47):
        N = n - 2
        laws = {j: tagged_law(n, j, s) for j in range(1, N+1)}
        star = {j: size_biased_law(n, j, s) for j in range(1, N+1)}
        for j in range(1, N+1):
            p, q = laws[j], star[j]
            assert sum(p) == sum(q) == 1
            assert sum(c * p[c] for c in range(N+1)) == Fraction(N,n)
            for c in range(1, N+1):
                assert q[c] == Fraction(n*c, N) * p[c]
            cases += 1
        for j in range(2, N+1):
            p0, p1 = laws[j], laws[j-1]
            q0, q1 = star[j], star[j-1]
            # Every 2x2 MLR minor, including boundary support zeros.
            for c in range(1,N+1):
                for d in range(c+1,N+1):
                    assert q0[c]*q1[d] >= q1[c]*q0[d], (n,j,c,d)
                    minors += 1
            for t in range(1,N):
                diff = sum((c-t)*(p1[c]-p0[c]) for c in range(t+1,N+1))
                if t <= N-j+1:
                    assert diff > 0, (n,j,t,diff)
                else:
                    assert diff == 0, (n,j,t,diff)
                hinges += 1
    print('Analytic-law rational cases:',cases)
    print('Size-biased likelihood-ratio minors:',minors)
    print('Tagged-degree hinge comparisons:',hinges)
    # Independent full Prüfer-word enumeration, not via Stirling weights.
    enum_cases = 0
    for n in range(4,9):
        N=n-2
        counts={j:[0]*(N+1) for j in range(1,N+1)}
        totals={j:0 for j in range(1,N+1)}
        for word in product(range(n),repeat=N):
            j=len(set(word))
            c=word.count(0)
            counts[j][c]+=1
            totals[j]+=1
        for j in range(1,N+1):
            expected=tagged_law(n,j,s)
            observed=[Fraction(v,totals[j]) for v in counts[j]]
            assert observed==expected,(n,j,observed,expected)
            enum_cases+=1
    print('Full Prüfer enumeration law cases:',enum_cases)
    # Verify ratio monotonicity and Stirling-row log-concavity exactly.
    ratio_checks=0
    for t in range(2,65):
        for k in range(2,t+1):
            assert s[t][k]*s[t][k] >= s[t][k-1]*s[t][k+1]
            if k<=t-1:
                assert Fraction(s[t+1][k-1],s[t+1][k]) < Fraction(s[t][k-1],s[t][k])
                ratio_checks+=1
    print('Stirling ratio monotonicity comparisons:',ratio_checks)
    print('All rational and enumerative checks passed.')

if __name__=='__main__':
    main()
