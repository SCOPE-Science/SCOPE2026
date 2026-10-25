#!/usr/bin/env python3
"""Independent finite checks for the six-generator exterior-algebra centralizer census.
Uses only the Python standard library; no external files or network access.
"""
from itertools import combinations
from fractions import Fraction
from math import prod
from random import Random

N = 6
BASIS = {d: [sum(1 << j for j in c) for c in combinations(range(N), d)]
         for d in range(N + 1)}
ODD = BASIS[1] + BASIS[3] + BASIS[5]
EVEN_POS = {m: i for i, m in enumerate(BASIS[2] + BASIS[4] + BASIS[6])}
TRIPLES = BASIS[3]
FOURS = BASIS[4]
F4_POS = {s:i for i,s in enumerate(FOURS)}

def gauss_rank_mod_q(vectors, q):
    b = {}
    for vec in vectors:
        v = vec[:]
        while True:
            pivot = next((i for i, x in enumerate(v) if x % q), None)
            if pivot is None:
                break
            if pivot in b:
                c = v[pivot] % q
                old = b[pivot]
                v = [(x - c * y) % q for x, y in zip(v, old)]
            else:
                z = pow(v[pivot] % q, -1, q)
                b[pivot] = [x * z % q for x in v]
                break
    return len(b)

def wedge_sign(a, b):
    if a & b:
        return 0
    parity = sum((a >> (j+1)).bit_count() for j in range(6) if (b >> j) & 1) % 2
    return -1 if parity else 1

def wedge_kernel_dim(x, q):
    cols = []
    for y in ODD:
        v = [0]*len(EVEN_POS)
        for a, coeff in x.items():
            if coeff and not (a & y):
                z = a | y
                v[EVEN_POS[z]] += coeff * wedge_sign(a, y)
        cols.append(v)
    return len(ODD) - gauss_rank_mod_q(cols, q)

def xdict(*monomials):
    return {sum(1 << j for j in c): 1 for c in monomials}

# Representatives of all six centralizer strata (odd-component kernel dimensions).
TESTS = [
    ("nonzero degree one", xdict((0,)), 16),
    ("zero wedge-annihilator trivector", xdict((0,1,2),(3,4,5)), 25),
    ("one-dimensional wedge-annihilator", xdict((0,1,2),(0,3,4)), 26),
    ("decomposable trivector", xdict((0,1,2)), 28),
    ("pure nonzero five-form", xdict((0,1,2,3,4)), 31),
    ("zero odd part", {}, 32),
]
for name, element, expected in TESTS:
    observed = wedge_kernel_dim(element, 3)
    assert observed == expected, (name, observed, expected)

rng = Random(8102026)
for _ in range(40):
    monomials = rng.sample(ODD, rng.randint(1, 15))
    x = {a: rng.randrange(1,3) for a in monomials}
    if any(a.bit_count()==1 for a in x):
        assert wedge_kernel_dim(x, 3) == 16
    elif any(a.bit_count()==3 for a in x):
        k = 0
        rows = []
        for i in range(6):
            vec = [0]*15
            for a,c in x.items():
                if a.bit_count()==3 and not (a & (1<<i)):
                    vec[F4_POS[a | (1<<i)]] += c*wedge_sign(1<<i,a)
            rows.append([v%3 for v in vec])
        k = 6-gauss_rank_mod_q(rows,3)
        assert k in (0,1,3)
        assert wedge_kernel_dim(x, 3) == 25+k

# Exhaustively classify the 2^20 ternary-support coefficient vectors over F_2.
# This verifies the char-independent trivector wedge-annihilator incidence counts.
WEDGE_ROWS = [[0]*20 for _ in range(6)]
for j, a in enumerate(TRIPLES):
    for i in range(6):
        if not (a & (1<<i)):
            WEDGE_ROWS[i][j] = 1 << F4_POS[a | (1<<i)]
TABLES = []
for i in range(6):
    tab0, tab1 = [0]*1024, [0]*1024
    for x in range(1,1024):
        z = (x & -x).bit_length()-1
        tab0[x] = tab0[x^(1<<z)] ^ WEDGE_ROWS[i][z]
        tab1[x] = tab1[x^(1<<z)] ^ WEDGE_ROWS[i][z+10]
    TABLES.append((tab0,tab1))
counts = [0]*7
for mask in range(1<<20):
    lo,hi = mask&1023,mask>>10
    basis = [0]*16
    rank = 0
    for a,b in TABLES:
        v = a[lo] ^ b[hi]
        while v:
            z = v.bit_length()-1
            if basis[z]:
                v ^= basis[z]
            else:
                basis[z] = v
                rank += 1
                break
    counts[6-rank] += 1

def qbinom(n,k,q):
    if k<0 or k>n:return 0
    num = prod(q**(n-i)-1 for i in range(k))
    den = prod(q**(k-i)-1 for i in range(k))
    return num//den

q=2
T3=(q-1)*qbinom(6,3,q)
T1=qbinom(6,1,q)*(q**10-1-(q-1)*qbinom(5,2,q))
T0=q**20-1-T1-T3
assert counts == [T0,T1,0,T3,0,0,1], (counts, T0,T1,T3)
for q in (3,5,7):
    t3=(q-1)*qbinom(6,3,q)
    t1=qbinom(6,1,q)*(q**10-1-(q-1)*qbinom(5,2,q))
    t0=q**20-1-t1-t3
    assert min(t0,t1,t3)>0
    odd_multiplicities = {
        48: (q**6-1)*q**26,
        57: t0*q**6,
        58: t1*q**6,
        60: t3*q**6,
        63: q**6-1,
        64: 1,
    }
    assert sum(odd_multiplicities.values()) == q**32
    cpnum = sum(count * q**(dimension-32) for dimension,count in odd_multiplicities.items())
    assert 0 < cpnum <= q**64
    expected = Fraction(q**20 + q**17 + q**16 - q**11 - q**10 + q - 1, q**33)
    assert Fraction(cpnum,q**64) == expected
print('ALL_EXTERIOR_SIX_CENTRALIZER_CHECKS_PASSED', counts, [(name, k+32) for name,_,k in TESTS])
