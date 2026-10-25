#!/usr/bin/env python3
"""Independent finite checks for 2-binomial powers of the Thue--Morse word.
No third-party dependencies. Tests do not substitute for the unrestricted proof.
"""
from itertools import product

def subseq2(word):
    totals = {'0':0,'1':0,'00':0,'01':0,'10':0,'11':0}
    for x in word:
        x=str(x)
        for y in '01':
            totals[y+x] += totals[y]
        totals[x] += 1
    return tuple(totals[z] for z in ('0','1','00','01','10','11'))

def moment(word):
    return (len(word),sum(word),sum(j*x for j,x in enumerate(word)))

def mu(word):
    return tuple(y for x in word for y in (x,1-x))

# Check the fundamental two-statistic criterion exhaustively.
for n in range(0,11):
    by_moment = {}
    by_subseq = {}
    for word in product((0,1),repeat=n):
        a,b = moment(word),subseq2(word)
        if a in by_moment: assert by_moment[a]==b
        if b in by_subseq: assert by_subseq[b]==a
        by_moment[a]=b;by_subseq[b]=a
print('VERIFY_OK binary_signature_equivalence_all_words_lengths_0_to_10')

# The 4-uniform morphism mu^2 erases all order-2 binomial distinctions.
for k in range(0,9):
    values=set()
    for word in product((0,1),repeat=k):
        values.add(subseq2(mu(mu(word))))
    assert len(values)==1,(k,len(values))
print('VERIFY_OK order_two_uniform_block_equivalence_source_lengths_0_to_8')

# Independent arithmetic generation instead of repeated morphism.
N=32768
a=tuple(i.bit_count()&1 for i in range(N))
p=[0]*(N+1);w=[0]*(N+1)
for i,x in enumerate(a):
    p[i+1]=p[i]+x
    w[i+1]=w[i]+i*x

def sig(start,length):
    ones=p[start+length]-p[start]
    return ones,w[start+length]-w[start]-start*ones

# Check the existential spectrum exhaustively over this complete finite prefix.
# This is independent of source parity, and includes both source alignments.
for m in range(1,257):
    exists=False
    for start in range(N-3*m+1):
        s=sig(start,m)
        if s==sig(start+m,m)==sig(start+2*m,m):
            exists=True
            break
    assert exists==(m%4==0),(m,start if exists else None)
    if m%4==0: assert sig(0,m)==sig(m,m)==sig(2*m,m)
print('VERIFY_OK all_starts_root_spectrum_1_to_256_in_arithmetic_prefix_length_32768')

# Direct scattered-subsequence counts (not moment signatures) for 4+ blocks.
for m in range(1,49):
    for start in range(0,200):
        pieces=[a[start+j*m:start+(j+1)*m] for j in range(4)]
        values=[subseq2(v) for v in pieces]
        if len(set(values))==1: assert m%4==0
for m in range(4,101,4):
    for exponent in (3,4,5,7):
        pieces=[a[j*m:(j+1)*m] for j in range(exponent)]
        assert len({subseq2(v) for v in pieces})==1,(m,exponent)
print('VERIFY_OK direct_scattered_subsequence_4_block_checks_and_all_exponents_3_4_5_7')

# Test the odd-length abelian cube prohibition independently at every start.
for odd_m in range(1,258,2):
    for i in range(N-3*odd_m+1):
        x=p[i+odd_m]-p[i]; y=p[i+2*odd_m]-p[i+odd_m]; z=p[i+3*odd_m]-p[i+2*odd_m]
        assert x!=y or y!=z
print('VERIFY_OK no_odd_root_abelian_cubes_within_finite_prefix')
print('VERIFY_OK')
