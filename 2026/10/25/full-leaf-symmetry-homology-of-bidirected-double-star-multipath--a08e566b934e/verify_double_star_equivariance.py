#!/usr/bin/env python3
"""Independent finite signed-Lefschetz tests for bidirected double-star multipath complexes.

The combinatorial proof in RESULT.md is needed for all parameter values;
this file tests explicit finite parameter cases without presupposing their homology.
"""
from itertools import permutations, product
from math import gcd


def model(a, b):
    # Hubs 0 and 1; leaves 2,...,a+1 and a+2,...,a+b+1.
    edges = [(0, 1)] + [(0, 2+i) for i in range(a)] + [(1, 2+a+j) for j in range(b)]
    arrows = sorted([arc for x, y in edges for arc in ((x,y),(y,x))])
    lookup = {edge:i for i, edge in enumerate(arrows)}
    faces = []
    for mask in range(1 << len(arrows)):
        ing, out = set(), set()
        chosen = set()
        valid = True
        for i, (x,y) in enumerate(arrows):
            if (mask >> i) & 1:
                if x in out or y in ing or (y,x) in chosen:
                    valid=False
                    break
                out.add(x); ing.add(y); chosen.add((x,y))
        if valid: faces.append(mask)
    return arrows, lookup, faces


def vertex_permutation(a,b,sa,sb,swap=False):
    if swap:
        assert a==b
        P=[1,0] + [2+a+sa[i] for i in range(a)] + [2+sb[j] for j in range(b)]
    else:
        P=[0,1] + [2+sa[i] for i in range(a)] + [2+a+sb[j] for j in range(b)]
    return P


def trace(arrows,lookup,faces,P):
    verteximages=[lookup[(P[x],P[y])] for x,y in arrows]
    total=-1 # augmented empty face contribution
    for mask in faces:
        if not mask:continue
        inds=[i for i in range(len(arrows)) if (mask>>i)&1]
        imgs=[verteximages[i] for i in inds]
        if set(imgs)!=set(inds):continue
        inversions=sum(imgs[i]>imgs[j] for i in range(len(imgs)) for j in range(i+1,len(imgs)))
        sign=(-1)**(len(inds)-1+inversions)
        total+=sign
    return total


def p(f):return f*f-3*f+1

def fixed(s):return sum(i==x for i,x in enumerate(s))

def composed(s,t):return tuple(s[t[i]] for i in range(len(s)))

def test(a,b,swaps):
    ar, lk, faces=model(a,b)
    count=0
    for sa in permutations(range(a)):
        for sb in permutations(range(b)):
            for swap in ([False,True] if swaps else [False]):
                P=vertex_permutation(a,b,sa,sb,swap)
                observed=trace(ar,lk,faces,P)
                if swap:
                    predicted=-p(fixed(composed(sa,sb)))
                else:
                    predicted=2*(fixed(sa)-1)*(fixed(sb)-1)-p(fixed(sa))*p(fixed(sb))
                assert observed==predicted, (a,b,sa,sb,swap,observed,predicted)
                count+=1
    print('LEFSCHETZ_OK',a,b,'faces',len(faces),'group_elements',count)


def rank_mod2(cols):
    piv={}
    for val in cols:
        while val:
            bit=val.bit_length()-1
            if bit in piv: val^=piv[bit]
            else:
                piv[bit]=val
                break
    return len(piv)


def homology(a,b):
    ar,lk,faces=model(a,b)
    groups={}
    for m in faces:
        if m:groups.setdefault(m.bit_count()-1,[]).append(m)
    dims={i:len(gr) for i,gr in groups.items()}
    ranks={}
    for d,cur in groups.items():
        if d==0:
            ranks[d]=1 # augmented boundary
            continue
        lower={m:j for j,m in enumerate(groups[d-1])}
        cols=[]
        for mask in cur:
            col=0
            for bit in range(len(ar)):
                if mask>>bit &1:
                    col^=1<<lower[mask^(1<<bit)]
            cols.append(col)
        ranks[d]=rank_mod2(cols)
    bets={d:dims[d]-ranks.get(d,0)-ranks.get(d+1,0) for d in dims}
    target={2:2*(a-1)*(b-1),3:p(a)*p(b)}
    assert {d:k for d,k in bets.items() if k}==target,(bets,target)
    print('HOMOLOGY_OK',a,b,'reduced_F2_Betti',bets)


if __name__=='__main__':
    test(3,3,True)
    test(3,4,False)
    homology(3,3)
    homology(3,4)
    print('VERIFY_OK')
