"""Exact finite-arithmetic check of the two-survivor extinction theorem.

Run: python verify.py
Uses only the Python standard library.
"""
from itertools import combinations
from math import comb

sols = {}
for n in range(3, 11):
    pairs = []
    for x in range(2, n):
        for y in range(x, n):
            for z in range(max(2, x+y-n), min(x,y)+1):
                if comb(z, 2)*comb(n, 2) == comb(x, 2)*comb(y, 2):
                    pairs.append((x,y,z))
    sols[n] = pairs
assert all(not sols[n] for n in range(3,9))
assert sols[9] == [(4,4,2)], sols[9]
assert sols[10] == [(3,6,2)], sols[10]
print('pair_parameter_solutions_n3_to_n10',sols)

for t in (1,2,3):
    pos = 0
    core = set(range(pos,pos+t)); pos += t
    pair_ab = set(range(pos,pos+3-t)); pos += 3-t
    pair_ac = set(range(pos,pos+3-t)); pos += 3-t
    pair_bc = set(range(pos,pos+3-t)); pos += 3-t
    only_a = set(range(pos,pos+t-1)); pos += t-1
    only_b = set(range(pos,pos+t-1)); pos += t-1
    only_c = set(range(pos,pos+t-1)); pos += t-1
    a,b,c = core|pair_ab|pair_ac|only_a,core|pair_ab|pair_bc|only_b,core|pair_ac|pair_bc|only_c
    assert len(a)==len(b)==len(c)==5
    assert [len(a&b),len(a&c),len(b&c)] == [3]*3
    assert len(a|b|c)==6+t
    samples = [set(s) for s in combinations(range(9),2)]
    p1 = [sum(not (s & d) for s in samples) for d in (a,b,c)]
    p2 = [sum(not(s&d) and not(s&e) for s in samples) for d,e in ((a,b),(a,c),(b,c))]
    p3 = sum(not(s&a) and not(s&b) and not(s&c) for s in samples)
    assert p1==[6]*3 and p2==[1]*3 and p3==(1 if t==1 else 0)
    assert 216*p3 != 36
    print('triple_intersection',t,'union_size',6+t,'single_event_counts',p1,'pair_event_counts',p2,'triple_event_count',p3,'of',len(samples))
print('ALL_EXACT_CHECKS_PASSED')
