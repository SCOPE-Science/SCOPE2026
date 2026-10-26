#!/usr/bin/env python3
"""Exact rational, independent incidence-Laplacian verification for fan graphs.

No external modules or saved intermediate data are required.
"""
from fractions import Fraction


def fibs(n):
    f = [0, 1]
    for _ in range(2, n + 1):
        f.append(f[-1] + f[-2])
    return f


def solve(matrix, rhs):
    """Pivoting exact Gauss elimination; independent of Fibonacci Green formulas."""
    n = len(rhs)
    A = [[Fraction(x) for x in row] + [Fraction(rhs[i])] for i, row in enumerate(matrix)]
    for j in range(n):
        p = next(i for i in range(j, n) if A[i][j] != 0)
        A[j], A[p] = A[p], A[j]
        den = A[j][j]
        for t in range(j, n+1):
            A[j][t] /= den
        for i in range(n):
            if i == j:
                continue
            mul = A[i][j]
            if mul:
                for t in range(j, n+1):
                    A[i][t] -= mul * A[j][t]
    return [A[i][n] for i in range(n)]


def check(n):
    F = fibs(2*n + 2)
    L = F[n-1] + F[n+1]
    D = F[2*n]
    # Grounded vertex Laplacian at the fan apex.
    B = []
    for k in range(n):
        b = [0] * n
        b[k] = 1
        B.append(('spoke', k+1, b))
    for k in range(n-1):
        b = [0] * n
        b[k] = 1
        b[k+1] = -1
        B.append(('rim', k+1, b))
    A = [[sum(e[2][i]*e[2][j] for e in B) for j in range(n)] for i in range(n)]
    maxq = Fraction(0)
    maxc = Fraction(0)
    qmax_labels = []
    cmax_labels = []
    for edge in B:
        kind, k, b = edge
        v = solve(A, b)
        cur = [sum(Fraction(t)*v[i] for i,t in enumerate(e[2])) for e in B]
        q = sum(map(abs, cur), Fraction(0))
        d = sum(Fraction(b[i])*v[i] for i in range(n))
        c = 1 + q - 2*d
        # Exact all-column formula from the claimed theorem.
        if kind == 'spoke':
            a = F[2*k-1]
            z = F[2*(n-k)+1]
            expected_q = 1 + Fraction(2*a*z-a-z, D)
            expected_c = 2 - Fraction(a+z, D)
        else:
            u = F[2*k]
            w = F[2*(n-k)]
            expected_q = 2 - Fraction(u+w, D)
            expected_c = 1 + Fraction(2*u*w-u-w, D)
        assert (q,c)==(expected_q,expected_c), (n,kind,k,q,c,expected_q,expected_c)
        if q > maxq:
            maxq = q
            qmax_labels = [(kind,k)]
        elif q==maxq:
            qmax_labels.append((kind,k))
        if c > maxc:
            maxc = c
            cmax_labels = [(kind,k)]
        elif c==maxc:
            cmax_labels.append((kind,k))
    if n%2==0:
        qe = 2 - Fraction(2,L)
        ce = 2 - Fraction(1,F[n])
    else:
        qe = 2 - Fraction(1,F[n])
        ce = 2 - Fraction(2,L)
    assert (maxq,maxc)==(qe,ce), (n,maxq,maxc,qe,ce)
    assert F[n]*L==D
    if n>=3:
        assert L-2*F[n]==F[n-3]
        assert (maxq-maxc)*((-1)**n)==Fraction(F[n-3], D)
    if n>=4:
        assert all(label[0]=='rim' for label in qmax_labels),qmax_labels
        assert all(label[0]=='spoke' for label in cmax_labels),cmax_labels
    return len(B), qmax_labels, cmax_labels


def main():
    count = 0
    for n in range(2, 23):
        m, qlabels, clabels = check(n)
        count += m
        print('n',n,'columns',m,'Q_witnesses',qlabels,'C_witnesses',clabels)
    print('VERIFIED exact rational:', 21, 'fan graphs;', count, 'full projection columns')

if __name__ == '__main__':
    main()
