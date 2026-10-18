#!/usr/bin/env python3
"""Exact integer and finite-chain checks for four-row grid symmetry characters.

No external packages are needed. The all-length theorem uses matrix identities
and the published homological-concentration result; finite tests are auxiliary.
"""
from collections import defaultdict
from itertools import combinations

STATES = tuple(s for s in range(16) if (s & (s << 1)) == 0)
WEIGHT = tuple((-1) ** s.bit_count() for s in STATES)
T = tuple(tuple(((-1) ** b.bit_count()) if (a & b) == 0 else 0
                for b in STATES) for a in STATES)
I = tuple(tuple(int(i == j) for j in range(8)) for i in range(8))
ONE = (1,) * 8
EMPTY = STATES.index(0)

def mv(M, v):
    return tuple(sum(row[j] * v[j] for j in range(8)) for row in M)

def matmul(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(8))
                       for j in range(8)) for i in range(8))

def matpow(M, e):
    result = I
    while e:
        if e & 1:
            result = matmul(result, M)
        M = matmul(M, M)
        e //= 2
    return result

def vadd(*vs):
    return tuple(sum(v[i] for v in vs) for i in range(8))

def neg(v):
    return tuple(-x for x in v)

def reflmask(a):
    return sum(((a >> i) & 1) << (3-i) for i in range(4))

ALPHA = tuple(int(not (a & reflmask(a))) for a in STATES)
BETA = tuple(int(bool(a & 9)) for a in STATES)

# These exact 8-coordinate identities hold for every possible boundary state.
TT6 = matpow(T, 6)
V = vadd(mv(TT6, ONE), neg(ONE))
assert V == (2, 1, 1, 1, 0, 1, 0, 0)
assert mv(T, V) == neg(V)
assert ALPHA == mv(matpow(T, 2), ONE)
assert BETA == vadd(ONE, neg(mv(T, ONE)), mv(matpow(T, 3), ONE))

z = [1]
state = ONE
for m in range(1, 501):
    state = mv(T, state)
    z.append(state[EMPTY])
for m in range(495):
    assert z[m+6] == z[m] + 2 * (-1)**m
p = [1, 0]
for m in range(2, 501):
    p.append(p[m-1] - p[m-2])
for m in range(495):
    assert p[m+6] == p[m]

def formula(n):
    h = n//2
    a = z[h-1] if n % 2 == 0 else z[h+1]
    ab = z[h+2] if n % 2 == 0 else z[h] - z[h+1] + z[h+3]
    return tuple((-1)**n * v for v in (z[n], a, p[n], ab))

def predicted_rank(n):
    q, r = divmod(n, 6)
    return 2*q if r == 1 else (2*q+2 if r == 4 else 2*q+1)

def constituents(char):
    t1, ta, tb, tab = char
    return tuple((t1 + ea*ta + eb*tb + ea*eb*tab)//4
                 for ea, eb in ((1,1),(1,-1),(-1,1),(-1,-1)))

for n in range(2, 480):
    chars = formula(n)
    assert chars[0] == predicted_rank(n)
    parts = constituents(chars)
    assert min(parts) >= 0
    assert sum(parts) == chars[0]
    for ea, eb in ((1,1),(1,-1),(-1,1),(-1,-1)):
        assert (chars[0] + ea*chars[1] + eb*chars[2] + ea*eb*chars[3]) % 4 == 0
    later = formula(n+12)
    s = 1 if n % 4 in (1,2) else -1
    assert tuple(later[i]-chars[i] for i in range(4)) == (4, 2*s, 0, -2*s)
    target = (1,2,1,0) if s==1 else (1,0,1,2)
    assert tuple(constituents(later)[i]-parts[i] for i in range(4)) == target

def independent_masks(n):
    def rec(j, old, chosen):
        if j==n:
            yield chosen
            return
        for mask in STATES:
            if not (old & mask):
                yield from rec(j+1, mask, chosen | (mask << (4*j)))
    yield from rec(0, 0, 0)

def permuted(i, n, action):
    col, row = divmod(i, 4)
    if action & 1:
        col = n - col - 1
    if action & 2:
        row = 3 - row
    return 4*col + row

def direct_char(n):
    answer = [0]*4
    for subset in independent_masks(n):
        count = subset.bit_count()
        for action in range(4):
            mapped = sum(1 << permuted(i, n, action)
                         for i in range(4*n) if (subset>>i)&1)
            if mapped != subset:
                continue
            moves = sum(1 for i in range(4*n)
                        if ((subset>>i)&1) and permuted(i,n,action)!=i)
            assert moves % 2 == 0
            answer[action] += (-1) ** (count + moves//2)
    return tuple((-1)**n * v for v in answer)

cases = 0
for n in range(2, 8):
    assert direct_char(n) == formula(n), (n,direct_char(n),formula(n))
    cases += 4


def binary_rank(columns):
    pivots = {}
    for word in columns:
        while word:
            key = word.bit_length()-1
            if key not in pivots:
                pivots[key] = word
                break
            word ^= pivots[key]
    return len(pivots)

def check_small_homology(n):
    buckets = defaultdict(list)
    for subset in independent_masks(n):
        buckets[subset.bit_count()].append(subset)
    max_size = max(buckets)
    ranks = {0:0}
    for size in range(1,max_size+1):
        lower = {mask:j for j,mask in enumerate(buckets[size-1])}
        columns = []
        for mask in buckets[size]:
            x=mask
            col=0
            while x:
                bit=x & -x
                x-=bit
                col ^= 1 << lower[mask^bit]
            columns.append(col)
        ranks[size] = binary_rank(columns)
    ranks[max_size+1]=0
    hom = {size-1:len(buckets[size])-ranks[size]-ranks[size+1]
           for size in range(1,max_size+1)}
    assert hom.get(n-1,0) == predicted_rank(n)
    assert all(dim==n-1 or betti==0 for dim,betti in hom.items())
    return len(list(independent_masks(n)))

counts=[]
for n in (2,3,4,5):
    counts.append((n,check_small_homology(n)))
print('VERIFY_OK; transfer identities; 478 stabilization cases; 24 direct character cases; mod-2 homology cases',counts)
