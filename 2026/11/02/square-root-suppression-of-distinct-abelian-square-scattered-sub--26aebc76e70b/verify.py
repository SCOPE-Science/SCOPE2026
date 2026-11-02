#!/usr/bin/env python3
"""Independent exact checks for random binary scattered Abelian squares.

Requires only the Python standard library.  The host-word enumeration,
pattern waiting-time expansion, and algebraic power-series recurrence are
separate computational paths.
"""
from collections import defaultdict
from fractions import Fraction
from math import comb


def host_spectrum(max_n=12):
    # C[n][k] sums the actual number of distinct Abelian-square subsequence
    # strings over all length-n hosts having k ones.
    C = [{0: 0}]
    tested = 0
    for n in range(1, max_n + 1):
        row = defaultdict(int)
        for h in range(1 << n):
            w = f"{h:0{n}b}"
            subseqs = {""}
            for letter in w:
                subseqs |= {u + letter for u in subseqs}
            count = 0
            for u in subseqs:
                L, odd = divmod(len(u), 2)
                if L and not odd and u[:L].count("1") == u[L:].count("1"):
                    count += 1
            row[w.count("1")] += count
            tested += 1
        C.append(dict(row))
    return C, tested


def host_expectation(row, n, p):
    return sum((total * p**k * (1-p)**(n-k)
                for k, total in row.items()), Fraction(0))


def coeff_inv_power(ell, i, x):
    # [z^i](1-xz)^(-ell), including the ell=0 case.
    if ell == 0:
        return Fraction(int(i == 0))
    return comb(ell+i-1, i) * x**i


def greedy_expectation(n, p):
    # Independent pattern-first enumeration, not using the algebraic GF.
    p0, p1 = 1-p, p
    answer = Fraction(0)
    for L in range(1, n//2 + 1):
        for j in range(L+1):
            n0, n1 = 2*j, 2*(L-j)
            tail = Fraction(0)
            for t in range(n-2*L+1):
                for i in range(t+1):
                    tail += (coeff_inv_power(n0, i, p1)
                             * coeff_inv_power(n1, t-i, p0))
            answer += (comb(L,j)**2 * p0**n0 * p1**n1 * tail)
    return answer


def conv(a, b, N):
    out = [Fraction(0) for _ in range(N+1)]
    for i in range(N+1):
        for j in range(N+1-i):
            out[i+j] += a[i]*b[j]
    return out


def algebraic_expectations(N, p):
    # From H(z)^2*(1-S(z)^2)*(1-T(z)^2)=1 and H(0)=1.
    p0,p1=1-p,p
    g0 = [Fraction(0)] + [p0*p1**(j-1) for j in range(1,N+1)]
    g1 = [Fraction(0)] + [p1*p0**(j-1) for j in range(1,N+1)]
    S = [g0[j]+g1[j] for j in range(N+1)]
    T = [g0[j]-g1[j] for j in range(N+1)]
    S2 = conv(S,S,N); T2=conv(T,T,N)
    one_minus_S2 = [int(j==0)-S2[j] for j in range(N+1)]
    one_minus_T2 = [int(j==0)-T2[j] for j in range(N+1)]
    Delta = conv(one_minus_S2,one_minus_T2,N)
    assert Delta[0]==1
    H = [Fraction(1)]
    Hsq = [Fraction(1)]
    for n in range(1,N+1):
        # Coefficient of z^n in Delta * H^2 equals zero.
        prev = sum(H[i]*H[n-i] for i in range(1,n))
        external = sum(Delta[j]*Hsq[n-j] for j in range(1,n+1))
        v=-(prev+external)/2
        H.append(v)
        Hsq.append(2*v+prev)
    abelian = [Fraction(0)]; total=Fraction(0)
    for n in range(1,N+1):
        total+=H[n]
        abelian.append(total)
    # All nonempty patterns: S(z)/(1-S(z)) followed by a prefix sum.
    U = [Fraction(1)]
    for n in range(1,N+1):
        U.append(sum(S[j]*U[n-j] for j in range(1,n+1)))
    D=[Fraction(0)]; total=Fraction(0)
    for n in range(1,N+1):
        total+=U[n]
        D.append(total)
    return abelian,D


def main():
    MaxN=12
    C,hosts=host_spectrum(MaxN)
    probs=[Fraction(1,2),Fraction(1,3),Fraction(2,5),Fraction(1,5)]
    comparisons=0
    for p in probs:
        algebraic,D=algebraic_expectations(MaxN,p)
        for n in range(MaxN+1):
            expected=host_expectation(C[n],n,p)
            via_patterns=greedy_expectation(n,p)
            assert expected==via_patterns==algebraic[n], (p,n,expected,via_patterns,algebraic[n])
            comparisons+=1
        assert D[0]==0
        assert D[1]==1
    # All-zero and all-one words provide the degenerate-source boundary.
    for n in range(1,MaxN+1):
        assert C[n].get(0,0)==n//2
        assert C[n].get(n,0)==n//2
    print(f'VERIFY_OK hosts={hosts} rational_sources={len(probs)} '
          f'exact_three_way_comparisons={comparisons} n=0..{MaxN} '
          'degenerate_boundaries=TRUE')
    print('fair_source_abelian_expectations=',
          [str(x) for x in algebraic_expectations(10,Fraction(1,2))[0]])

if __name__=='__main__':
    main()
