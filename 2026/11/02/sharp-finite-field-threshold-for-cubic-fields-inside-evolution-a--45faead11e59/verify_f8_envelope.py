"""Exact finite checks for the six-dimensional evolution envelope of F_8.

This checker is corroborative: the accompanying proof treats all possible
smaller evolution envelopes without relying on the finite enumeration.
"""
from itertools import permutations, product

# Binary polynomial representation modulo t^3+t+1.
def multiply(x, y):
    out = 0
    for i in range(3):
        if (y >> i) & 1:
            out ^= x << i
    for j in range(4, 2, -1):
        if (out >> j) & 1:
            out ^= (0b1011 << (j-3))
    return out


def rank3(values):
    pivots = [0, 0, 0]
    r = 0
    for v in values:
        for bit in (2, 1, 0):
            if not ((v >> bit) & 1):
                continue
            if pivots[bit]:
                v ^= pivots[bit]
            else:
                pivots[bit] = v
                r += 1
                break
    return r

assert all(multiply(x, y) == multiply(y, x) for x in range(8) for y in range(8))
assert all(multiply(x, y) != 0 for x in range(1,8) for y in range(1,8))
assert all(multiply(1, x) == x for x in range(8))
assert multiply(2,4) == 3 and multiply(4,4) == 6

# Basis pattern (ab,ac,bc) for one binary linear form.
patterns = {((v & 1) & ((v>>1)&1)) + 2*((v & 1) & ((v>>2)&1)) + 4*(((v>>1)&1) & ((v>>2)&1)) for v in range(8)}
assert patterns == {0,1,2,4,7}

bases = [trip for trip in permutations(range(1,8),3) if rank3(trip)==3]
assert len(bases)==168
rank_distribution = {2:0,3:0}
for x,y,z in bases:
    triple = (multiply(x,y),multiply(x,z),multiply(y,z))
    assert len(set(triple))==3 and 0 not in triple
    r = rank3(triple)
    assert r in (2,3)
    rank_distribution[r] += 1
    if r==2:
        assert triple[0]^triple[1]^triple[2] == 0
    # Exhaust all decompositions by <=2 offdiagonal rank-one summands.
    assert all(tuple(((u if (p>>i)&1 else 0) ^ (v if (s>>i)&1 else 0)) for i in range(3)) != triple for p,s,u,v in product(patterns,patterns,range(8),range(8)))
assert rank_distribution == {2:42,3:126}

# Natural basis of the six-dimensional evolution algebra in order
# [f00, f01, f02, f11, f12, f22].
# iota(1)=f00+f01+f02, iota(t)=f01+f11+f12,
# iota(t^2)=f02+f12+f22.
def iota(x):
    out=0
    if x&1:out^=0b000111
    if x&2:out^=0b011010
    if x&4:out^=0b110100
    return out

assert len({iota(x) for x in range(8)})==8
# Squares: iota(1+t+t^2), iota(t), iota(t^2), iota(1+t^2),
# iota(1+t), iota(1) respectively.
squares = tuple(iota(x) for x in (7,2,4,5,3,1))
def evolution_multiply(a,b):
    out=0
    for i in range(6):
        if ((a>>i)&1) and ((b>>i)&1):out ^= squares[i]
    return out

for x,y in product(range(8),repeat=2):
    assert evolution_multiply(iota(x),iota(y)) == iota(multiply(x,y))
for a,x in product(range(64),range(8)):
    assert evolution_multiply(a,iota(x)) in {iota(z) for z in range(8)}
assert {iota(1),iota(2),iota(4)}.issubset(set(squares))
print('FIELD_F8_OK')
print('ORDERED_BASES=168')
print('CROSS_PRODUCT_RANK2=42 RANK3=126')
print('TWO_TERM_OFFDIAGONAL_DECOMPOSITIONS=0')
print('SIX_DIMENSIONAL_EVOLUTION_EMBEDDING_AND_IDEAL=VERIFIED')
print('VERIFY_OK')
