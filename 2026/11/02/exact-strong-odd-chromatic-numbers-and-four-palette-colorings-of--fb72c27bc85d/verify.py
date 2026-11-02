#!/usr/bin/env python3
"""Finite cross-checks of strong odd colorings on cycle prisms.

Run with Python 3.9 or newer, standard library only.
"""
from collections import Counter
from itertools import product

BLOCK4=((2,3),(1,0),(3,2),(0,1))
BLOCK5=((2,3),(1,4),(3,0),(4,2),(0,1))
BLOCK7=((2,3),(1,0),(3,2),(0,4),(1,3),(4,2),(0,1))

def valid(columns):
    n=len(columns)
    if n<3:return False
    for i,(top,bot) in enumerate(columns):
        if top==bot:return False
        lt,lb=columns[(i-1)%n]; rt,rb=columns[(i+1)%n]
        if top in (lt,rt) or bot in (lb,rb):return False
        for colors in ((lt,rt,bot),(lb,rb,top)):
            counts=Counter(colors)
            if any(count%2==0 for count in counts.values()):return False
    return True

def four_transition():
    cs=tuple((a,b) for a in range(4) for b in range(4) if a!=b)
    states=tuple((P,Q) for P in cs for Q in cs if P[0]!=Q[0] and P[1]!=Q[1])
    nxt={}
    for P,Q in states:
        legal=[]
        for R in cs:
            if Q[0]==R[0] or Q[1]==R[1]:continue
            x=(P[0],R[0],Q[1]);y=(P[1],R[1],Q[0])
            if all(len(set(t)) in (1,3) for t in (x,y)):
                legal.append((Q,R))
        assert len(legal)==1,(P,Q,legal)
        nxt[(P,Q)]=legal[0]
    assert len(states)==84
    unvisited=set(states);length_counts=Counter()
    while unvisited:
        s=min(unvisited);p=s;cyc=[]
        while p not in cyc:
            cyc.append(p); p=nxt[p]
        assert p==s, 'transition is a permutation of all states'
        for t in cyc:unvisited.remove(t)
        length_counts[len(cyc)]+=1
    assert length_counts=={2:6,4:6,6:8},length_counts
    for n in range(3,31):
        fixed=0
        for st in states:
            z=st
            for _ in range(n):z=nxt[z]
            if z==st:fixed+=1
        expected=12*(n%2==0)+24*(n%4==0)+48*(n%6==0)
        assert fixed==expected,(n,fixed,expected)
    print('FOUR_COLOR_STATE_TRANSITION_OK',len(states),'CYCLES',dict(length_counts))


def independent_short_census():
    cs=tuple((a,b) for a in range(4) for b in range(4) if a!=b)
    for n in range(3,7):
        counter=0
        def rec(col):
            nonlocal counter
            if len(col)==n:
                counter+=valid(col)
                return
            for z in cs:
                if col and (col[-1][0]==z[0] or col[-1][1]==z[1]):continue
                rec(col+[z])
        rec([])
        expected=12*(n%2==0)+24*(n%4==0)+48*(n%6==0)
        assert counter==expected,(n,counter,expected)
        print('DIRECT_CYCLIC_COLORING_ENUMERATION_OK',n,counter)


def constructions():
    for n in range(4,121,2):
        col=tuple(((i%2),(1-i%2)) for i in range(n))
        assert valid(col),n
    for b in (BLOCK4,BLOCK5,BLOCK7): assert valid(b),b
    for n in range(5,122,2):
        # n = 5 + 4t or n = 7 + 4t
        t=(n-5)//4 if n%4==1 else (n-7)//4
        tail=BLOCK5 if n%4==1 else BLOCK7
        cols=BLOCK4*t+tail
        assert len(cols)==n
        assert valid(cols),n
    print('DIRECT_CONSTRUCTED_COLORINGS_OK 4 5 7 AND ALL ODD UP TO 121')
    assert valid(((0,3),(1,4),(2,5)))
    for a in product(range(5),repeat=6):
        if valid(((a[0],a[1]),(a[2],a[3]),(a[4],a[5]))):
            raise AssertionError('Unexpected five-color triangular prism')
    print('TRIANGULAR_PRISM_FIVE_COLOR_EXHAUSTIVE_EXCLUSION_OK',5**6)

if __name__=='__main__':
    four_transition()
    independent_short_census()
    constructions()
    print('VERIFY_OK')
