#!/usr/bin/env python3
"""Reconstruct closed neighborhoods of crown graphs; calculate reduced F2 homology.
Finite checks only; not a proof for unrestricted n.
"""
from itertools import combinations

def gf2_rank(columns):
    p={}
    for x in columns:
        while x:
            a=x.bit_length()-1
            if a in p:x^=p[a]
            else:p[a]=x;break
    return len(p)

def bettis(n):
    verts=list(range(2*n))
    def adjacent(x,y):
        return (x<n) != (y<n) and x%n!=y%n
    facets=[frozenset((v,)+tuple(w for w in verts if adjacent(v,w))) for v in verts]
    levels={-1:[()]}
    for k in range(1,n+1):
        levels[k-1]=sorted(set(c for f in facets for c in combinations(sorted(f),k)))
    # augmented chain
    ranks={}
    for d in range(0,n):
        rows={face:i for i,face in enumerate(levels[d-1])}
        cols=[]
        for face in levels[d]:
            x=0
            for j in range(len(face)):
                x^=1<<rows[face[:j]+face[j+1:]]
            cols.append(x)
        ranks[d]=gf2_rank(cols)
    b={d:len(levels[d])-ranks.get(d,0)-ranks.get(d+1,0) for d in range(0,n)}
    actual={k:v for k,v in b.items() if v}
    expected=({1:1} if n==3 else {2:n*n-3*n+1, n-2:2})
    if n==4:expected={2:n*n-3*n+3}
    if actual!=expected:raise AssertionError((n,actual,expected))
    print('n=',n,'facets=',len(facets),'faces=',sum(map(len,levels.values()))-1,'ranks=',ranks,'betti=',actual)
    return actual

if __name__=='__main__':
    for n in range(3,9):bettis(n)
    print('FINITE_CHECK_OK')

def check_characters():
    from itertools import permutations
    for n in (5,6):
        verts=list(range(2*n))
        def adjacent(x,y):return (x<n)!=(y<n) and x%n!=y%n
        facets=[frozenset((v,)+tuple(w for w in verts if adjacent(v,w))) for v in verts]
        faces=set(c for f in facets for k in range(1,n+1) for c in combinations(sorted(f),k))
        ps=list(permutations(range(n)))
        # Every permutation for n=5; conjugacy representatives for n=6
        for j,p in enumerate(ps):
            if n==6 and j%19:continue
            f=sum(p[i]==i for i in range(n))
            t=sum(i<p[i] and p[p[i]]==i for i in range(n))
            sgn=(-1)**sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))
            for side in (False,True):
                mp=[(n*(x<n if side else x>=n)) + p[x%n] for x in verts]
                reduced_lef=-1
                for face in faces:
                    mapped=[mp[v] for v in face]
                    if set(mapped)==set(face):
                        parity=sum(mapped[i]>mapped[j] for i in range(len(face)) for j in range(i+1,len(face)))%2
                        reduced_lef += (-1)**(len(face)-1+parity)
                c2=(2*t-1 if side else f*f-3*f+1)
                ct=(0 if side else 2*sgn)
                expected=c2 + ((-1)**(n-2))*ct
                assert reduced_lef==expected,(n,p,side,reduced_lef,expected)
        print('character traces checked for n=',n)
    print('CHARACTER_CHECK_OK')

if __name__=='__main__':check_characters()
