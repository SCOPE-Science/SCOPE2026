#!/usr/bin/env python3
"""Exact, standalone classification of anticanonical pencils on a split degree-seven del Pezzo surface over F2.
Pure Python 3 standard library. Cubic mask order defined below; all arithmetic exact.
"""
from itertools import combinations
from collections import Counter
import json

# Monomial exponents in (X,Y,Z); coordinates e1,e2 are prescribed zeros.
MON3=((3,0,0),(0,3,0),(0,0,3),(2,1,0),(2,0,1),(1,2,0),(0,2,1),(1,0,2),(0,1,2),(1,1,1))
IDX=(3,4,5,6,7,8,9,2)
BASIS=tuple(MON3[i] for i in IDX)
MON2=tuple((a,b,2-a-b) for a in range(3) for b in range(3-a))
MON4=tuple((a,b,4-a-b) for a in range(5) for b in range(5-a))
INDEX4={e:i for i,e in enumerate(MON4)}


def partials(mask):
    polys=[]
    for axis in range(3):
        s=set()
        for i,e in enumerate(BASIS):
            if mask>>i&1 and e[axis]&1:
                deriv=tuple(v-(j==axis) for j,v in enumerate(e))
                if deriv in s:s.remove(deriv)
                else:s.add(deriv)
        polys.append(s)
    return polys


def rank15(mask):
    # Degree-four Macaulay map: S_2^3 -> S_4 by multiplying the three partials.
    piv={}
    for d in partials(mask):
        for b in MON2:
            col=0
            for e in d:
                col ^= 1<<INDEX4[tuple(e[i]+b[i] for i in range(3))]
            while col:
                k=col.bit_length()-1
                if k not in piv:
                    piv[k]=col;break
                col^=piv[k]
    return len(piv)


def smooth_set():
    return {m for m in range(1,256) if rank15(m)==15}


def pencils(S):
    return sorted({tuple(sorted((a,b,a^b))) for a,b in combinations(sorted(S),2) if a^b in S})


def evalmask(mask,point):
    xx,yy,zz=point
    mon=[xx**a*yy**b*zz**c for a,b,c in BASIS]
    return sum(mon[i] for i in range(8) if mask>>i&1)&1


def pointcounts(p):
    points=((1,0,0),(0,1,0),(0,0,1),(1,1,0),(1,0,1),(0,1,1),(1,1,1))
    b=sum(evalmask(p[0],P)==0 and evalmask(p[1],P)==0 for P in points)
    s=tuple(sorted(sum(evalmask(m,P)==0 for P in points) for m in p))
    return b,s


def matrix_actions():
    # Each automorphism fixes the set of two blown-up points; 2 swaps x 4 shears.
    transformations=[]
    for swap in (0,1):
        for a in (0,1):
            for b in (0,1):
                M=((0,1,a),(1,0,b),(0,0,1)) if swap else ((1,0,a),(0,1,b),(0,0,1))
                transformations.append(M)
    # evaluate a transformed cubic on eight F2 points, then solve for coefficient mask
    # instead perform 3-variable polynomial multiplication over F2 explicitly.
    def mult(A,B):
        C=set()
        for u in A:
            for v in B:
                e=tuple(u[i]+v[i] for i in range(3))
                if e in C:C.remove(e)
                else:C.add(e)
        return C
    actions=[]
    for M in transformations:
        L=[{tuple(int(k==j) for k in range(3)) for j in range(3) if M[i][j]} for i in range(3)]
        im_basis=[]
        for exp in BASIS:
            prod={(0,0,0)}
            for i,n in enumerate(exp):
                for _ in range(n):prod=mult(prod,L[i])
            assert prod.issubset(set(BASIS))
            im_basis.append(sum(1<<BASIS.index(e) for e in prod))
        action={}
        for mask in range(1,256):
            image=0
            for i in range(8):
                if mask>>i&1:image^=im_basis[i]
            action[mask]=image
        assert len(set(action.values()))==255
        actions.append(action)
    return actions


def classify():
    S=smooth_set();P=pencils(S);act=matrix_actions()
    assert len(S)==60 and len(P)==104 and len(act)==8
    unseen=set(P);orbits=[]
    while unseen:
        p=min(unseen)
        orbit={tuple(sorted(a[m] for m in p)) for a in act}
        assert len(orbit)==8 and orbit<=unseen
        assert len({pointcounts(e) for e in orbit})==1
        orbits.append({'rep':p,'size':len(orbit),'b':pointcounts(p)[0], 'member_points':pointcounts(p)[1]})
        unseen-=orbit
    assert len(orbits)==13
    assert Counter(pointcounts(p)[0] for p in P)=={2:56,3:48}
    assert not any(a^b in S and a^c in S and b^c in S and a^b^c in S
                   for a,b,c in combinations(sorted(S),3))
    return S,P,orbits


if __name__=='__main__':
    S,P,orbits=classify()
    print(json.dumps({'smooth_anticanonical_sections':len(S),'all_smooth_pencils':len(P),
        'automorphism_group_size':8,'pencil_orbits':len(orbits),
        'rational_base_counts':dict(sorted(Counter(pointcounts(p)[0] for p in P).items())),
        'point_spectra':{str(k):v for k,v in sorted(Counter(pointcounts(p)[1] for p in P).items())},
        'no_all_smooth_net':True,'orbit_reps':orbits},sort_keys=True,indent=2))
