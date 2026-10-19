#!/usr/bin/env python3
"""Exact fixed-space census of automorphisms of a free class-two Lie algebra of rank three.
Standard-library verification of proposed finite-field rank distributions.
"""
from collections import Counter
from itertools import product
from math import prod


def mul(x, y, q):
    if q == 4:
        out = 0
        a, b = x, y
        while b:
            if b & 1:
                out ^= a
            b >>= 1
            a <<= 1
            if a & 4:
                a ^= 7  # irreducible z^2 + z + 1 over F_2
        return out
    return (x * y) % q


def add(x, y, q):
    return x ^ y if q == 4 else (x + y) % q


def neg(x, q):
    return x if q == 4 else (-x) % q


def inv(x, q):
    assert x
    return next(v for v in range(1, q) if mul(x, v, q) == 1)


def rank(matrix, q):
    if not matrix:
        return 0
    rows = [list(row) for row in matrix]
    ncol = len(rows[0]); lead = 0
    for col in range(ncol):
        pivot = next((i for i in range(lead, len(rows)) if rows[i][col]), None)
        if pivot is None:
            continue
        rows[pivot], rows[lead] = rows[lead], rows[pivot]
        factor = inv(rows[lead][col], q)
        rows[lead] = [mul(z, factor, q) for z in rows[lead]]
        for i in range(len(rows)):
            if i == lead or not rows[i][col]:
                continue
            factor = rows[i][col]
            rows[i] = [add(z, neg(mul(factor, v, q), q), q) for z, v in zip(rows[i], rows[lead])]
        lead += 1
        if lead == len(rows):
            break
    return lead


def determinant3(M, q):
    a, b, c = M[0]; d, e, f = M[1]; g, h, i = M[2]
    terms = [mul(a, add(mul(e, i, q), neg(mul(f, h, q), q), q), q),
             neg(mul(b, add(mul(d, i, q), neg(mul(f, g, q), q), q), q), q),
             mul(c, add(mul(d, h, q), neg(mul(e, g, q), q), q), q)]
    return add(add(terms[0], terms[1], q), terms[2], q)


def wedge2(M, q):
    pairs = [(0, 1), (0, 2), (1, 2)]
    return [[add(mul(M[i][k], M[j][l], q), neg(mul(M[i][l], M[j][k], q), q), q)
             for k, l in pairs] for i, j in pairs]


def minus_identity(M, q):
    return [[add(M[i][j], neg(int(i == j), q), q) for j in range(len(M))]
            for i in range(len(M))]


def gl(n, q):
    return prod(q**n-q**i for i in range(n))


def rank_maps(a, c, t, q):
    if t < 0 or t > min(a, c):
        return 0
    return prod((q**a-q**i)*(q**c-q**i) for i in range(t)) // prod(q**t-q**i for i in range(t))


def theoretical_joint(q):
    z = q*q+q+1
    S = gl(3, q)//(q-1)
    U = z*q**3*(q*q-1)
    V = z*q*q
    d2 = z*(q*q-1)
    d1 = U-(q+1)*d2-z
    d0 = S-d1-d2-1
    out = Counter({(0, 0): d0, (1, 1): d1, (2, 2): d2, (3, 3): 1})
    B = q*q*z*(q*q-1)
    epsilon = int(q % 2 != 0)
    for count, exceptional in ((q-2-epsilon, 0), (epsilon, 1)):
        if not count:
            continue
        a1 = U-(q+1)*V
        c3 = exceptional
        c2 = V-z*exceptional
        c1 = a1+q*z*exceptional
        groups = {(2, 1): V, (1, 1): B, (1, 0): a1-B,
                  (0, 1): c1-V-B, (0, 2): c2, (0, 3): c3,
                  (0, 0): S-a1-c1+B-c2-c3}
        for ac, multiplicity in groups.items():
            out[ac] += count*multiplicity
    out = Counter({k:v for k,v in out.items() if v})
    assert all(v>0 for v in out.values()), out
    assert sum(out.values()) == gl(3,q)
    return out


def theoretical_fixed(q):
    out=Counter()
    for (a,c), mult in theoretical_joint(q).items():
        for t in range(min(a,c)+1):
            out[a+c-t] += mult*q**(9-a*c)*rank_maps(a,c,t,q)
    assert sum(out.values()) == q**9*gl(3,q)
    assert sum(q**d*count for d,count in out.items()) == 3*q**9*gl(3,q)
    poly=q**6-3*q**5+q**4+4*q**3+q*q-3*q-8-int(q%2!=0)
    assert out[0] == q**12*poly
    return +out


def all_gl(q):
    for entries in product(range(q), repeat=9):
        M = [list(entries[i:i+3]) for i in range(0,9,3)]
        if determinant3(M,q):
            yield M


def brute_joint(q):
    out = Counter()
    for M in all_gl(q):
        D=determinant3(M,q)
        a=3-rank(minus_identity(M,q),q)
        c=3-rank([[add(M[i][j], neg(D if i==j else 0,q),q)
                  for j in range(3)] for i in range(3)],q)
        wedge_c=3-rank(minus_identity(wedge2(M,q),q),q)
        assert c==wedge_c,(q,M,c,wedge_c)
        out[(a,c)]+=1
    return out


def binary_full_fixed():
    q=2
    out=Counter()
    for g in all_gl(2):
        W=wedge2(g,2)
        for coefficients in product(range(2),repeat=9):
            f=[coefficients[i:i+3] for i in range(0,9,3)]
            A=[[g[i][j] if i<3 and j<3 else 0 for j in range(6)] for i in range(3)]
            A += [[f[i][j] if j<3 else W[i][j-3] for j in range(6)] for i in range(3)]
            out[6-rank(minus_identity(A,2),2)] += 1
    return out


def run():
    for q in (2,3,4):
        observed=brute_joint(q)
        assert observed == theoretical_joint(q),(q,observed,theoretical_joint(q))
        print('GL3_JOINT_OK',q,sum(observed.values()))
    obs=binary_full_fixed()
    assert obs == theoretical_fixed(2),(obs,theoretical_fixed(2))
    print('COMPLETE_AUTOMORPHISM_ENUMERATION_OK_2',sum(obs.values()))
    for q in (2,3,4,5,7,8,9,11,13,16,17):
        f=theoretical_fixed(q)
        assert all(k in f for k in range(7)),(q,f)
        assert f[6]==1
        print('FORMULA_OK',q, f[0])
    print('VERIFY_OK_FREE_CLASS2_FIXEDSPACE_CENSUS')

if __name__=='__main__':
    run()
