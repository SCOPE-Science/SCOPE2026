"""Exact finite-grid sanity checks for balanced partition interpolation.

This program tests discrete analogues; the analytic result is not inferred
from any finite run. Only the standard library is required.
"""
from itertools import permutations, combinations
from fractions import Fraction

checks=0

def verify(condition, message):
    global checks
    if not condition:
        raise AssertionError(message)
    checks+=1


def matched_distance(P,Q,m):
    n=len(P)
    return Fraction(n-max(sum(P[k]==permutation[Q[k]] for k in range(n))
                         for permutation in permutations(range(m))),n)

for m in (2,3,4):
    side=24 if m!=4 else 32
    points=[(x,y) for x in range(side) for y in range(side)]
    for variant in (0,1):
        P=[x%m for x,y in points]
        Q=[y%m if variant==0 else (y+x//m)%m for x,y in points]
        # Choose an optimal permutation to align the terminal labeling.
        perm=max(permutations(range(m)), key=lambda sigma: sum(P[k]==sigma[Q[k]] for k in range(len(P))))
        Q=[perm[q] for q in Q]
        M=len(P)
        verify(all(P.count(i)==M//m and Q.count(i)==M//m for i in range(m)),
               'endpoint mass balance')
        blocks={(i,j):[k for k in range(M) if P[k]==i and Q[k]==j]
                for i in range(m) for j in range(m) if i!=j}
        # A lexicographic cut on pixels is the finite analogue of a sweep.
        times=[Fraction(i,4) for i in range(5)]
        states=[]
        for t in times:
            selected=set()
            for block in blocks.values():
                verify((len(block)*t).denominator==1, 'quantile realizability')
                selected.update(block[:int(len(block)*t)])
            R=tuple(Q[k] if k in selected else P[k] for k in range(M))
            verify(all(R.count(i)==M//m for i in range(m)), 'intermediate mass balance')
            states.append(R)
        distance=matched_distance(P,Q,m)
        for i,j in combinations(range(len(times)),2):
            verify(matched_distance(states[i],states[j],m)==(times[j]-times[i])*distance,
                   'constant-speed distance identity')
        verify(states[0]==tuple(P) and states[-1]==tuple(Q), 'endpoint agreement')
print(f'PASS: {checks} exact assertions for 2-,3-,4-cell balanced partitions')
