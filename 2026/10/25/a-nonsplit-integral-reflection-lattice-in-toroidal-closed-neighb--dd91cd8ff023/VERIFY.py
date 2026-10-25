#!/usr/bin/env python3
"""Reproduce finite combinatorial checks for neighborhood nerves of Cartesian cycle products."""
from itertools import combinations
from collections import defaultdict


def verify(m, n):
    assert m >= 5 and n >= 5
    idx=lambda x,y:(x % m)*n+(y % n)
    verts=range(m*n)
    nbr=lambda x,y:[idx(x+1,y),idx(x,y+1),idx(x-1,y),idx(x,y-1)]
    faces=set()
    for x in range(m):
        for y in range(n):
            B=[idx(x,y)]+nbr(x,y)
            for k in range(1,6):
                faces.update(frozenset(c) for c in combinations(B,k))
    initial=len(faces)
    removed=0
    for card in (4,3,2):
        for x in range(m):
            for y in range(n):
                v=idx(x,y); ns=nbr(x,y)
                for comb in combinations(ns,card):
                    S=frozenset(comb)
                    # The 4 perimeter edges of the neighbor cycle remain.
                    if card==2 and S not in (frozenset([ns[0],ns[2]]),frozenset([ns[1],ns[3]])):
                        continue
                    T=S|{v}
                    assert S in faces and T in faces,('missing',m,n,x,y,S)
                    codim1=[U for U in faces if len(U)==card+1 and S.issubset(U)]
                    assert codim1==[T],('not free',m,n,x,y,S,codim1)
                    faces.remove(S); faces.remove(T); removed+=2
    target=set()
    for x in range(m):
        for y in range(n):
            a=idx(x,y);b=idx(x+1,y);c=idx(x+1,y+1);d=idx(x,y+1)
            for T in combinations([a,b,c,d],1):target.add(frozenset(T))
            for T in combinations([a,b,c,d],2):target.add(frozenset(T))
            for T in combinations([a,b,c,d],3):target.add(frozenset(T))
    assert faces==target,('target mismatch',m,n,len(faces),len(target),len(faces-target),len(target-faces))
    assert removed==14*m*n
    # Every unit square embeds a tetrahedral boundary, with original grid edges as equator.
    assert len([S for S in faces if len(S)==3])==4*m*n
    def tri(t):
        p=sorted(t)
        return (frozenset(t), -1 if sum(t[i]>t[j] for i in range(3) for j in range(i+1,3))%2 else 1)
    def chain(triangles):
        out=defaultdict(int)
        for x in triangles:
            key,sg=tri(x);out[key]+=sg
        return {k:v for k,v in out.items() if v}
    def transforms(T,f):return chain([tuple(f(z) for z in t) for t in T])
    for x in range(m):
        for y in range(n):
            a,b,c,d=idx(x,y),idx(x+1,y),idx(x+1,y+1),idx(x,y+1)
            D=[(a,b,c),(a,c,d)]
            E=[(a,b,d),(b,c,d)]
            h=lambda v:idx(-(v//n),v%n)
            v=lambda v:idx(v//n,-(v%n))
            tx=lambda v:idx(v//n+1,v%n)
            ty=lambda v:idx(v//n,v%n+1)
            for name,g,x0,y0,sg,switch in [
                ('hx',h,-x-1,y,-1,True),('vy',v,x,-y-1,-1,True),
                ('tx',tx,x+1,y,1,False),('ty',ty,x,y+1,1,False)]:
                aa,bb,cc,dd=idx(x0,y0),idx(x0+1,y0),idx(x0+1,y0+1),idx(x0,y0+1)
                Dnew=[(aa,bb,cc),(aa,cc,dd)]
                Enew=[(aa,bb,dd),(bb,cc,dd)]
                def scale(C,s):return {t:s*coef for t,coef in chain(C).items()}
                assert transforms(D,g)==scale(Enew if switch else Dnew,sg),(m,n,x,y,name,'D')
                assert transforms(E,g)==scale(Dnew if switch else Enew,sg),(m,n,x,y,name,'E')
    return {'m':m,'n':n,'initial_faces':initial,'collapse_pairs':removed//2,'remaining_faces':len(faces),
            'square_spheres':m*n,'rank_H1':2,'rank_H2':m*n+1,
            'symmetry_checks':4*m*n*2}

if __name__=='__main__':
    for m,n in [(5,5),(5,6),(6,5),(6,6),(5,7),(7,5)]:
        print('PASS',verify(m,n))
