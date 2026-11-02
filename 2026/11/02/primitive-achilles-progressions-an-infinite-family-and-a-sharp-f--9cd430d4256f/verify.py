#!/usr/bin/env python3
"""Reproducible integer checks for the Achilles progression theorem.

Requires only Python 3 standard library. The search limit is part of a
mathematically bounded finite statement; no finite loop proves the unbounded
existence claim, whose proof is supplied separately.
"""
from math import gcd, isqrt, prod
from itertools import permutations

LIMIT = 57967


def X(t):
    return -5750*t*t + 8500*t - 621


def Y(t):
    return 4250*t*t - 1242*t + 459


def Z(t):
    return -3250*t*t + 351


def poly_mul(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += x*y
    return c


def det(a):
    n = len(a)
    ans = 0
    for p in permutations(range(n)):
        parity = sum(p[i] > p[j] for i in range(n) for j in range(i + 1, n))
        ans += (-1 if parity & 1 else 1)*prod(a[i][p[i]] for i in range(n))
    return ans


def verify_infinite_family():
    x = [-621, 8500, -5750]
    y = [459, -1242, 4250]
    z = [351, 0, -3250]
    a, b, c = poly_mul(x, x), poly_mul(y, y), poly_mul(z, z)
    assert all(27*a[i] + 343*c[i] == 250*b[i] for i in range(5))
    delta = [125*b[i] - 27*a[i] for i in range(5)]
    assert delta == [15922818, 142519500, -1463062500, 1319625000, 1365125000]
    assert 1365125000*4 > 1463062500  # then delta(t)>0 for all integers t>=2
    assert 0 < 27*X(1)**2 < 125*Y(1)**2 < 343*Z(1)**2

    # Sylvester determinant: a prime dividing X(t),Y(t) divides this integer.
    A, B, C = -5750, 8500, -621
    D, E, F = 4250, -1242, 459
    sylvester = [[A,B,C,0], [0,A,B,C], [D,E,F,0], [0,D,E,F]]
    resultant = det(sylvester)
    assert resultant == 90724673403000
    assert resultant == 2**3*3**3*5**3*7**6*13**4
    assert gcd(27*X(1)**2, 125*Y(1)**2) == 1

    # Each specified root is simple modulo its prime (indeed, v_p == 1).
    for fn, p, t0 in [(X,11,5),(Y,17,0),(Z,19,3)]:
        assert fn(t0) % p == 0 and fn(t0) % (p*p) != 0
    # Construct the unique residue modulo the pairwise coprime moduli.
    mods = [2730, 121, 289, 361]
    residues = [1, 5, 0, 3]
    N = prod(mods)
    t0 = sum(r * (N // m) * pow(N // m, -1, m) for r, m in zip(residues, mods)) % N
    assert (N, t0) == (34462998570, 8482369351)
    for k in [0,1,2,3,7,19,200]:
        t = t0 + N*k
        assert all(t%m==r for r,m in zip(residues,mods))
        aa,bb,cc = 27*X(t)**2,125*Y(t)**2,343*Z(t)**2
        assert aa+cc == 2*bb and 0<aa<bb<cc
        assert gcd(aa,bb)==gcd(aa,cc)==gcd(bb,cc)==1
        assert X(t) % 11 == 0 and X(t) % 121 != 0
        assert Y(t) % 17 == 0 and Y(t) % 289 != 0
        assert Z(t) % 19 == 0 and Z(t) % 361 != 0
    return N, t0, resultant


def achilles_by_spf(limit):
    spf = list(range(limit + 1))
    for p in range(2, isqrt(limit)+1):
        if spf[p] == p:
            for n in range(p*p, limit + 1, p):
                if spf[n] == n:
                    spf[n] = p
    ach = []
    for n in range(2,limit+1):
        m=n
        exps=[]
        while m>1:
            p=spf[m]
            e=0
            while m%p == 0:
                m//=p
                e+=1
            exps.append(e)
        if all(e>=2 for e in exps):
            g=0
            for e in exps:
                g=gcd(g,e)
            if g==1:
                ach.append(n)
    return ach


def achilles_by_square_cube(limit):
    candidates = set()
    for b in range(1, int(round(limit ** (1/3)))+4):
        b3=b*b*b
        if b3>limit:break
        # Keep squarefree b; a^2 b^3 uniquely covers powerful numbers.
        if any(b % (p*p) == 0 for p in range(2,isqrt(b)+1)):
            continue
        for a in range(1,isqrt(limit//b3)+1):
            candidates.add(a*a*b3)
    return candidates


def verify_minimum():
    ach=achilles_by_spf(LIMIT)
    assert len(ach)==186
    cand=achilles_by_square_cube(LIMIT)
    # Check canonical representation produces every powerful number, and no
    # Achilles number was missed by the sieve.
    assert set(ach).issubset(cand)
    ash=set(ach)
    triples=[]
    for i,u in enumerate(ach):
        for v in ach[i+1:]:
            w=2*v-u
            if w>LIMIT:break
            if w in ash and gcd(u,v)==1:
                triples.append((u,v,w))
    assert triples==[(14283,36125,57967)]
    assert 14283==3**3 * 23**2
    assert 36125==5**3 * 17**2
    assert 57967==7**3 * 13**2
    return len(ach),len(cand),triples

if __name__=='__main__':
    N,t0,R=verify_infinite_family()
    ach_count,powerful_count,triples=verify_minimum()
    print('VERIFY_OK residue_modulus=%d residue=%d resultant=%d achilles_upto_limit=%d powerful_upto_limit=%d primitive_triples=%s' % (N,t0,R,ach_count,powerful_count,triples))
