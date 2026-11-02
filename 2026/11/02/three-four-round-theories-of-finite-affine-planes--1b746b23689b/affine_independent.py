#!/usr/bin/env python3
"""Independent four-round finite-model type recursion for affine incidence planes.
All arithmetic explicit; GF(4) uses the polynomial u^2+u+1.
"""
from itertools import product

def add(a,b,q): return a^b if q == 4 else (a+b)%q
def mul(a,b,q):
    if q != 4: return a*b%q
    table = ((0,0,0,0), (0,1,2,3), (0,2,3,1), (0,3,1,2))
    return table[a][b]

def make(q):
    P = [(x,y) for x in range(q) for y in range(q)]
    L = [(slope,b) for slope in range(q+1) for b in range(q)]
    n=len(P)
    memberships = [set() for _ in range(len(L))]
    for i,(slope,b) in enumerate(L):
        for j,(x,y) in enumerate(P):
            if (x==b if slope==q else y==add(mul(slope,x,q),b,q)):
                memberships[i].add(j)
        assert len(memberships[i])==q
    assert all(sum(i in m for m in memberships)==q+1 for i in range(n))
    return n,memberships

def solve(qs=(2,3,4)):
    # Structural tuple-type recurrence: for any tuple, its (r+1)-type is the
    # set of r-types of extensions by one element; atomic 0-types are explicit.
    # The type objects are recursively nested frozensets, no global interner.
    answers = []
    for q in qs:
        np, lines=make(q)
        N=np+len(lines)
        incidence=[[False]*N for _ in range(N)]
        for j, points in enumerate(lines):
            for i in points:
                incidence[i][np+j]=incidence[np+j][i]=True
        base = {}
        atom = {}
        pairbits=tuple((i,j) for i in range(4) for j in range(i+1,4))
        for a in range(N):
            for b in range(N):
                for c in range(N):
                    trio=(a,b,c)
                    codes=set()
                    for d in range(N):
                        v=(a,b,c,d)
                        codes.add((tuple(z>=np for z in v),tuple(v[i]==v[j] for i,j in pairbits),tuple(incidence[v[i]][v[j]] for i,j in pairbits)))
                    atom[trio]=frozenset(codes)
        t2={(a,b):frozenset(atom[(a,b,c)] for c in range(N)) for a in range(N) for b in range(N)}
        t3={a:frozenset(t2[(a,b)] for b in range(N)) for a in range(N)}
        t4=frozenset(t3.values())
        answers.append((q,np,N-np,len(set(atom.values())),len(set(t2.values())),len(set(t3.values())),t4))
    for q,np,nl,s1,s2,s3,_ in answers:
        print(f'q={q} points={np} lines={nl} triple_one_step_types={s1} pair_two_step_types={s2} singleton_three_step_types={s3}')
    for i in range(len(answers)):
        for j in range(i+1,len(answers)):
            print(f'q={answers[i][0]} versus q={answers[j][0]} four_round_equivalent={answers[i][-1]==answers[j][-1]}')
if __name__=='__main__': solve()
