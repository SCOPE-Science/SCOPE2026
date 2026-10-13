#!/usr/bin/env python3
from itertools import combinations
from fractions import Fraction

def compositions_positive(total, length):
    if length == 1:
        yield (total,)
        return
    for first in range(1, total-length+2):
        for rest in compositions_positive(total-first, length-1):
            yield (first,)+rest

def canonical_comparison(x,y):
    # Joint species relabeling sorts coordinate pairs. Community exchange transposes them.
    a=tuple(sorted(zip(x,y)))
    b=tuple(sorted((v,u) for u,v in zip(x,y)))
    return min(a,b)

def bray_curtis_similarity(c):
    n=sum(x for x,y in c)
    assert sum(y for x,y in c)==n
    return Fraction(sum(min(x,y) for x,y in c),n)

def morisita_horn_similarity(c):
    num=2*sum(x*y for x,y in c)
    den=sum(x*x+y*y for x,y in c)
    return Fraction(num,den)

expected_types={2:1,3:3,4:7,5:15,6:32,7:66,8:137}
expected_pair_tests={2:0,3:1,4:7,5:31,6:136,7:566,8:2357}
expected_reversals={2:0,3:0,4:0,5:0,6:0,7:0,8:1}
found_types={}; found_tests={}; found_reversals={}; all_reversals=[]

for total in range(2,9):
    tcount=0; pcount=0; rcount=0
    for richness in range(2,total+1):
        vecs=list(compositions_positive(total,richness))
        comparisons={}
        for x in vecs:
            for y in vecs:
                c=canonical_comparison(x,y)
                comparisons[c]=(bray_curtis_similarity(c),morisita_horn_similarity(c))
        items=list(comparisons.items())
        tcount += len(items)
        pcount += len(items)*(len(items)-1)//2
        for (ca,(ba,ma)),(cb,(bb,mb)) in combinations(items,2):
            db=(ba>bb)-(ba<bb)
            dm=(ma>mb)-(ma<mb)
            if db*dm < 0:
                rcount += 1
                all_reversals.append((total,richness,ca,cb,ba,bb,ma,mb))
    found_types[total]=tcount
    found_tests[total]=pcount
    found_reversals[total]=rcount

assert found_types==expected_types
assert found_tests==expected_pair_tests
assert found_reversals==expected_reversals
assert len(all_reversals)==1
r=all_reversals[0]
assert r[0]==8 and r[1]==4
A=((1,1),(1,4),(2,2),(4,1))
B=((1,3),(1,3),(3,1),(3,1))
assert {r[2],r[3]}=={A,B}
assert bray_curtis_similarity(A)==Fraction(5,8)
assert morisita_horn_similarity(A)==Fraction(13,22)
assert bray_curtis_similarity(B)==Fraction(1,2)
assert morisita_horn_similarity(B)==Fraction(3,5)
assert Fraction(5,8)>Fraction(1,2)
assert Fraction(13,22)<Fraction(3,5)

# Scaling every count preserves both similarities, so the reversal recurs at totals 8q.
for q in range(1,51):
    Aq=tuple((q*x,q*y) for x,y in A)
    Bq=tuple((q*x,q*y) for x,y in B)
    assert bray_curtis_similarity(Aq)==Fraction(5,8)
    assert morisita_horn_similarity(Aq)==Fraction(13,22)
    assert bray_curtis_similarity(Bq)==Fraction(1,2)
    assert morisita_horn_similarity(Bq)==Fraction(3,5)

print('VERIFY_OK')
print('comparison_types_by_total',found_types)
print('within_richness_pair_tests_by_total',found_tests)
print('strict_reversals_by_total',found_reversals)
print('unique_first_reversal',all_reversals[0])
print('scaled_recurrence_checked_q_1_to_50')
