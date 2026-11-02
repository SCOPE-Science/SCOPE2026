#!/usr/bin/env python3
"""Exact integer certificate and direct finite checks for three-color CCA on wheels.

Run: python3 wheel_cca_verifier.py
Requires only the Python standard library. The combinatorial transfer matrices
are generated from their definitions; they are not imported from results tables.
"""
from fractions import Fraction
from itertools import product
from collections import Counter


def matmul(x, y):
    n, m, k = len(x), len(y), len(y[0])
    out = [[0] * k for _ in range(n)]
    for i in range(n):
        row = out[i]
        for j, a in enumerate(x[i]):
            if a:
                yr = y[j]
                for h, b in enumerate(yr):
                    if b:
                        row[h] += a * b
    return out


def eye(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def traces(matrix, limit):
    x = eye(len(matrix))
    ans = []
    for _ in range(limit):
        x = matmul(x, matrix)
        ans.append(sum(x[i][i] for i in range(len(matrix))))
    return ans


def rank_over_q(mat):
    a = [[Fraction(x) for x in row] for row in mat]
    rows, cols = len(a), len(a[0])
    r = 0
    for col in range(cols):
        pivot = next((i for i in range(r, rows) if a[i][col]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        val = a[r][col]
        a[r][col:] = [v / val for v in a[r][col:]]
        for i in range(r + 1, rows):
            f = a[i][col]
            if f:
                a[i][col:] = [x - f * y for x, y in zip(a[i][col:], a[r][col:])]
        r += 1
        if r == rows:
            break
    return r


def newton_sums(poly, max_n):
    """Power sums of roots of a monic integer polynomial, with multiplicities."""
    d = len(poly) - 1
    sums = [d]
    for n in range(1, max_n + 1):
        val = sum(poly[j] * sums[n-j] for j in range(1, min(d, n-1) + 1))
        if n <= d:
            val += n * poly[n]
        sums.append(-val)
    return sums


def convolution(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out


def matrices():
    # No 1--2 edge on the rim: triangular circulation vanishes.
    A = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    pairs2 = list(product(range(2), repeat=2))
    idx2 = {x:i for i, x in enumerate(pairs2)}
    C = [[0]*4 for _ in range(4)]
    for a,b in pairs2:
        for c in range(2):
            if (a,b,c) != (0,0,0):
                C[idx2[a,b]][idx2[b,c]] = 1

    pairs3 = list(product(range(3), repeat=2))
    idx3 = {x:i for i, x in enumerate(pairs3)}
    B = [[0]*9 for _ in range(9)]
    for a,b in pairs3:
        for c in range(3):
            if b == 2 or (b+1)%3 in (a,c):
                B[idx3[a,b]][idx3[b,c]] = 1

    def out(a,b,c):
        return (b+1)%3 if (b+1)%3 in (0,a,c) else b

    quads = list(product(range(3), repeat=4))
    idx4 = {x:i for i, x in enumerate(quads)}
    M = [[0]*81 for _ in range(81)]
    for a,b,c,d in quads:
        for e in range(3):
            left, mid, right = out(a,b,c), out(b,c,d), out(c,d,e)
            if mid == 0 or (mid+1)%3 in (left,right):
                M[idx4[a,b,c,d]][idx4[b,c,d,e]] = 1
    return A,B,C,M


def step(s):
    h, *r = s
    n = len(r)
    hub = (h+1)%3 if (h+1)%3 in r else h
    y = [hub]
    for i,b in enumerate(r):
        y.append((b+1)%3 if (b+1)%3 in (h,r[(i-1)%n],r[(i+1)%n]) else b)
    return tuple(y)


def theorem_counts(n, A,B,C,M):
    a,b,c,m = (newton_sums(p,n)[n] for p in (A,B,C,M))
    return {
        ('fixed',0):3,
        ('fixed',1):3*(2**n+c)-3,
        ('fixed',2):3*a-3*(2**n+c),
        ('three',0):3*(b-1),
        ('three',1):3*(m-2**n-b+1),
        ('three',2):3**(n+1)-3*a-3*(m-2**n)
    }


def prove_transfer_spectrum(A,B,C,M):
    poly_a = [1,-3,1,1]
    poly_b = convolution([1,1,1],[1,-2,0,-1])
    poly_c = [1,-1,-1,-1]
    poly_m = [1,-2,-1,-2,-1,-2,3]
    # Directly prove the complete characteristic polynomials of B and C:
    # B has four zero eigenvalues, C one. Traces of powers 1..dimension
    # determine every coefficient via Newton identities.
    for mat, core, zeros in [(B,poly_b,4),(C,poly_c,1)]:
        full = [1] + core[1:] + [0]*zeros
        assert traces(mat,len(mat)) == newton_sums(full,len(mat))[1:]
    assert traces(A,3) == newton_sums(poly_a,3)[1:]

    # M has only six nonzero spectral degrees of freedom. The following
    # equalities certify the stable invariant image and its 6D char poly.
    powers = [eye(81)]
    for _ in range(11):
        powers.append(matmul(powers[-1],M))
    assert rank_over_q(powers[5]) == 6
    assert rank_over_q(powers[6]) == 6
    # M^5 q(M)=0 is an independent integer-matrix identity.
    for i in range(81):
        for j in range(81):
            assert sum(poly_m[k] * powers[11-k][i][j] for k in range(7)) == 0
    actual = [sum(powers[n][i][i] for i in range(81)) for n in range(1,7)]
    assert actual == newton_sums(poly_m,6)[1:]
    print('EXACT_TRANSFER_SPECTRA_OK')
    print('M_STABLE_RANK=6; M_FIRST_SIX_TRACES=' + str(actual))
    return poly_a,poly_b,poly_c,poly_m


def brute_wheels(polys):
    total_states=0
    for n in range(3,11):
        expected = theorem_counts(n,*polys)
        observed=Counter()
        for s in product(range(3), repeat=n+1):
            seq=[s]
            for _ in range(5):seq.append(step(seq[-1]))
            assert seq[5] == seq[2]  # Universal sharp two-step entry.
            eventual = 'fixed' if seq[2] == seq[3] else 'three'
            tau = next(t for t in range(3) if seq[t] == seq[t+(1 if eventual=='fixed' else 3)])
            observed[eventual,tau] += 1
            total_states+=1
        assert dict(observed)=={k:v for k,v in expected.items() if v>0}, (n,observed,expected)
        assert sum(expected.values())==3**(n+1)
        print('n=%d six_class_counts=%s' % (n, [expected[('fixed',j)] for j in range(3)]+[expected[('three',j)] for j in range(3)]))
    print('BRUTE_FORCE_CONFIGURATIONS='+str(total_states))
    print('WHEEL_CCA_EXACT_VERIFY_OK')

if __name__=='__main__':
    A,B,C,M=matrices()
    specs=prove_transfer_spectrum(A,B,C,M)
    brute_wheels(specs)
