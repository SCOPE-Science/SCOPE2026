#!/usr/bin/env python3
"""Exact finite check of the truncated-tetrahedral Ising ground-state classification.

Uses integer arithmetic, exhaustive traversal of all 2**12 spin configurations,
and an independent local-constraint characterization.
"""
from collections import Counter
from itertools import combinations, product
from fractions import Fraction

V = [(i,j) for i in range(4) for j in range(4) if j != i]
number = {vertex:index for index,vertex in enumerate(V)}
T = [(number[(i,j)], number[(i,k)]) for i in range(4)
     for j,k in combinations((x for x in range(4) if x != i), 2)]
B = [(number[(i,j)], number[(j,i)]) for i in range(4) for j in range(i+1,4)]
assert len(V) == 12 and len(T) == 12 and len(B) == 6

states=[]
for z in range(1 << 12):
    s=tuple(1 if z&(1<<p) else -1 for p in range(12))
    t=sum(s[u]*s[v] for u,v in T)
    b=sum(s[u]*s[v] for u,v in B)
    m=sum(s)
    states.append((s,t,b,m))

def local_condition(s, phase):
    Ts = [sum(s[number[(i,j)]] for j in range(4) if j != i) for i in range(4)]
    bb = [s[u]+s[v] for u,v in B]
    if phase == 'low': return all(abs(q)==1 for q in Ts) and all(q==0 for q in bb)
    if phase == 'lower_critical': return all(abs(q)==1 for q in Ts) and all(q!=-2 for q in bb)
    if phase == 'middle': return all(q==1 for q in Ts) and all(q!=-2 for q in bb)
    if phase == 'upper_critical': return all(q in (1,3) for q in Ts) and all(q!=-2 for q in bb)
    if phase == 'high': return all(q==3 for q in Ts)
    raise ValueError(phase)

def formula(J,K,h):
    if h < K: return -4*J-6*K,'low',24,0
    if h == K: return -4*J-6*K,'lower_critical',114,None
    if h < K+2*J: return -4*J-2*K-4*h,'middle',30,4
    if h == K+2*J: return -12*J-6*K,'upper_critical',163,None
    return 12*J+6*K-12*h,'high',1,12

checks=0
for J,K in [(1,1),(1,7),(7,1),(2,5),(9,4),(11,13),(1,27)]:
    for h in sorted(set([Fraction(0),Fraction(K,2),Fraction(K),
                         Fraction(K+J,1),Fraction(K+2*J,1),
                         Fraction(K+3*J,1),Fraction(10*(K+2*J),1)])):
        energy,phase,want,M = formula(J,K,h)
        minima=[v for v in states if J*v[1]+K*v[2]-h*v[3]==energy]
        E=min(J*t+K*b-h*m for _,t,b,m in states)
        assert E==energy, (J,K,h,phase,E,energy)
        assert len(minima)==want, (J,K,h,phase,len(minima),want)
        assert all(local_condition(s,phase)==(J*t+K*b-h*m==energy)
                   for s,t,b,m in states), (J,K,h,phase)
        if M is not None:assert all(m==M for _,_,_,m in minima)
        if phase=='lower_critical':
            assert Counter(m for _,_,_,m in minima)=={0:24,2:60,4:30}
        if phase=='upper_critical':
            assert Counter(m for _,_,_,m in minima)=={4:30,6:72,8:48,10:12,12:1}
        checks+=4+(1 if M is not None else 1)

# Independently compare direct count of the two constrained critical manifolds.
local_counts = {q:sum(local_condition(s,q) for s,t,b,m in states)
                for q in ('low','lower_critical','middle','upper_critical','high')}
assert local_counts == {'low':24,'lower_critical':114,
                        'middle':30,'upper_critical':163,'high':1}
checks+=1

# Independent small-graph combinatorial counts used in the symbolic proof.
# The missing-bridge orientation count has 5 admissible four-spoke assignments
# for either of the two orientations of the remaining central edge.
for central in (0,1):
    admissible=0
    for a,b,c,d in product((0,1),repeat=4):
        negative_counts=(a+b,c+d,2-a-c+central,2-b-d+(1-central))
        admissible+=all(1 <= k <= 2 for k in negative_counts)
    assert admissible == 5
    checks+=1

assert 3**4 - 6*3**2 + 3 == 30
assert 24 + 6*10 + 30 == 114
assert 1 + 12 + 48 + 72 + 30 == 163
checks+=3
print('PASS' ,checks,'assertion groups; 4096 spin states;',
      len(T),'triangle bonds;',len(B),'bridges;',local_counts)
