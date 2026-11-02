#!/usr/bin/env python3
"""Exact finite-support certificate for five-state firefly dynamics on friendship graphs.

Run: python3 verify_fca5_friend.py. Uses only the standard library.
"""
from collections import Counter
from itertools import combinations_with_replacement, product
from math import comb

P = list(combinations_with_replacement(range(5), 2))
INDEX = {pair: i for i, pair in enumerate(P)}
SPACE = 1 << len(P)
BLINK_TYPES = sum(1 << i for i, (a,b) in enumerate(P) if a==2 or b==2)


def move(c, blink):
    return c if (c>2 and blink) else (c+1)%5


def petal(a,b,h):
    return move(a, h==2 or b==2),move(b,h==2 or a==2)


def update_micro(x):
    h,*vals=x
    assert len(vals)%2==0
    h2=move(h,2 in vals)
    out=[]
    for j in range(0,len(vals),2):
        out.extend(petal(vals[j],vals[j+1],h))
    return (h2,*out)


def mask_types(S):
    return [j for j in range(15) if (S>>j)&1]


TRANS=[]
for h in range(5):
    row=[]
    for a,b in P:
        row.append(INDEX[tuple(sorted(petal(a,b,h)))])
    TRANS.append(row)


def macro_update(v):
    h,S=divmod(v,SPACE)
    h2=move(h,bool(S&BLINK_TYPES))
    dest=0
    while S:
        lowbit=S&-S
        dest|=1<<TRANS[h][lowbit.bit_length()-1]
        S^=lowbit
    return h2*SPACE+dest


def project(x):
    h,*vals=x
    S=0
    for i in range(0,len(vals),2):
        S|=1<<INDEX[tuple(sorted((vals[i],vals[i+1])))]
    return h*SPACE+S


def orbit(x,func):
    seen={};path=[]
    while x not in seen:
        seen[x]=len(path);path.append(x);x=func(x)
    return seen[x],path[seen[x]:]


def onto_weighted(m,weights):
    k=len(weights)
    return sum((-1)**(k-s.bit_count()) * (
        sum(weights[j] for j in range(k) if s>>j&1))**m
        for s in range(1<<k))


def main():
    assert len(P)==15
    N=5*SPACE
    NEXT=[macro_update(i) for i in range(N)]
    tails=[-1]*N;periods=[0]*N;cycles=[]
    for initial in range(N):
        if tails[initial]>=0: continue
        path=[];where={};v=initial
        while tails[v]<0 and v not in where:
            where[v]=len(path);path.append(v);v=NEXT[v]
        if tails[v]>=0:
            p=periods[v];t=tails[v]
            for u in reversed(path):
                t+=1; tails[u]=t;periods[u]=p
        else:
            k=where[v];cyc=path[k:];p=len(cyc);cycles.append(cyc)
            for u in cyc: tails[u]=0;periods[u]=p
            t=0
            for u in reversed(path[:k]):
                t+=1; tails[u]=t;periods[u]=p

    # Exclude empty type supports: at least one actual petal is present.
    recurrent=[v for v in range(N) if v%SPACE and tails[v]==0]
    counts=Counter((periods[v],len(mask_types(v%SPACE))) for v in recurrent)
    assert counts=={(1,5):2,(5,1):5,(6,1):6,(6,2):12,(6,3):6},counts
    assert all(periods[v] in (1,5,6) for v in range(N) if v%SPACE)
    assert {v for v in recurrent if periods[v]==1}=={
        h*SPACE+sum(1<<INDEX[(c,c)] for c in range(5)) for h in (3,4)}
    assert {v for v in recurrent if periods[v]==5}=={
        c*SPACE+(1<<INDEX[(c,c)]) for c in range(5)}

    # Recurrent six-cycles return each individual ordered petal pair in six steps.
    # The quotient uses unordered types; this orientation check is essential.
    for v in recurrent:
        if periods[v]!=6: continue
        for k in mask_types(v%SPACE):
            a,b=P[k];hstate=v
            for j in range(6):
                h=hstate//SPACE
                a,b=petal(a,b,h)
                hstate=NEXT[hstate]
            assert hstate==v and (a,b)==P[k]
    # A singleton consensus type returns in five steps. The two fixed
    # macro supports consist of all five monochrome pair types, whose
    # microscopic colors rotate freely while the hub remains inhibited.

    # Weighted onto sums count ordered labelled petal pairs.
    profiles=Counter();six_coeff=Counter()
    for v in recurrent:
        if periods[v]!=6: continue
        weights=[1 if P[j][0]==P[j][1] else 2 for j in mask_types(v%SPACE)]
        profiles[tuple(sorted(weights))]+=1
        k=len(weights)
        for S in range(1<<k):
            six_coeff[sum(weights[j] for j in range(k) if S>>j&1)]+=(
                (-1)**(k-S.bit_count()))
    assert profiles=={(2,):6,(1,2):12,(1,1,2):6},profiles
    assert dict((b,c) for b,c in six_coeff.items() if c)=={2:-6,4:6}

    bound={1:10,2:28,3:28,4:32,5:33}
    for m in range(1,6):
        mt=max(tails[v] for v in range(N)
               if v%SPACE and (v%SPACE).bit_count()<=m)
        assert mt==bound[m],(m,mt)
    assert max(tails[v] for v in range(N) if v%SPACE)==33

    for m in range(1,10):
        fixed5=onto_weighted(m,[1]*5)
        states6=sum(onto_weighted(m,[1 if P[j][0]==P[j][1] else 2
                   for j in mask_types(v%SPACE)]) for v in recurrent if periods[v]==6)
        assert states6==6*(4**m-2**m)
        assert fixed5%5==0
        assert (5+2*fixed5)%5==0

    microscopic_checked=0
    for m in range(1,4):
        counters=Counter()
        max_t=0
        for state in product(range(5),repeat=1+2*m):
            microscopic_checked+=1
            t,cyc=orbit(state,update_micro)
            assert len(cyc) in (5,6)
            assert project(update_micro(state))==macro_update(project(state))
            v=project(state)
            assert t==tails[v] and len(cyc)==(5 if periods[v]==1 else periods[v])
            counters[len(cyc)]+=1
            max_t=max(max_t,t)
        print('m=%d states=%d six_basin=%d max_first_entry=%d' %
              (m,5**(1+2*m),counters[6],max_t))
        assert max_t==bound[m]
    print('recurrent_macro_profiles=',dict(sorted(counts.items())))
    print('period_six_weight_profiles=',dict(sorted(profiles.items())))
    print('period_six_state_formula=6*(4**m-2**m)')
    print('microstates_checked=',microscopic_checked)
    print('FCA5_FRIENDSHIP_VERIFY_OK')

if __name__=='__main__':main()
