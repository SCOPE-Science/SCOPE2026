#!/usr/bin/env python3
"""Exact finite face and Lefschetz checks for cyclic Latin-square clique complexes.
The all-odd-order theorem rests on the separate combinatorial proof, not enumeration.
Standard Python library only.
"""
from itertools import combinations
from collections import Counter

def sign_of_permutation(p):
    return -1 if sum(p[i] > p[j] for i in range(len(p)) for j in range(i+1,len(p))) % 2 else 1

def model(n):
    V=range(n*n)
    xy=lambda v:divmod(v,n)
    idx=lambda x,y:(x%n)*n+(y%n)
    graph={v:set() for v in V}
    for u,v in combinations(V,2):
        x,y=xy(u);z,w=xy(v)
        if x==z or y==w or (x+y-z-w)%n==0:
            graph[u].add(v);graph[v].add(u)
    lines=set()
    for a in range(n):
        lines.add(frozenset(idx(a,b) for b in range(n)))
        lines.add(frozenset(idx(b,a) for b in range(n)))
        lines.add(frozenset(idx(b,a-b) for b in range(n)))
    mixed=set()
    for x in range(n):
        for y in range(n):
            for a in range(1,n):
                mixed.add(frozenset([idx(x,y),idx(x+a,y),idx(x,y+a)]))
    assert len(lines)==3*n and len(mixed)==n*n*(n-1)
    assert all(len(t)==3 and all(v in graph[u] for u,v in combinations(t,2)) for t in mixed)
    assert all(all(v in graph[u] for u,v in combinations(t,2)) for t in lines)
    faces=set()
    for simplex in lines|mixed:
        s=sorted(simplex)
        for m in range(1,len(s)+1):
            faces.update(combinations(s,m))
    fvec=Counter(len(s)-1 for s in faces)
    assert sum((-1)**d*c for d,c in fvec.items()) == 1+(n-1)**3
    # Check no additional maximal cliques, without using a graph package.
    if n<=7:
        maximal=[]
        def bronk(R,P,X):
            if not P and not X:
                maximal.append(frozenset(R));return
            pivot=max(P|X,key=lambda z:len(P & graph[z])) if P or X else None
            for v in list(P - (graph[pivot] if pivot is not None else set())):
                bronk(R|{v},P&graph[v],X&graph[v]);P.remove(v);X.add(v)
        bronk(set(),set(V),set())
        assert set(maximal)==lines|mixed,(n,len(maximal),len(lines|mixed))
    traces={}
    for a in range(n):
        for b in range(n):
            l=0
            for simplex in faces:
                moved=tuple(sorted(idx(*((xy(v)[0]+a,xy(v)[1]+b))) for v in simplex))
                if moved != simplex:continue
                perm=[moved.index(idx(xy(v)[0]+a,xy(v)[1]+b)) for v in simplex]
                l+=(-1)**(len(simplex)-1)*sign_of_permutation(perm)
            expect=1+(n-1)**3 if (a,b)==(0,0) else (n if a==0 or b==0 or (a+b)%n==0 else 0)
            assert l==expect,(n,a,b,l,expect)
            traces[(a,b)]=l-1
    # Integer Fourier orthogonality: sum of translated traces times a character's
    # inverse, implemented with complex roots for the finite test cases only.
    import cmath
    mult=Counter()
    for r in range(n):
        for s in range(n):
            actual=sum(t*cmath.exp(-2j*cmath.pi*((r*a+s*b)%n)/n)
                       for (a,b),t in traces.items())/(n*n)
            expected=n-3+int(r==0)+int(s==0)+int(r==s)-int(r==0 and s==0)
            assert abs(actual-expected)<1.e-7,(n,r,s,actual,expected)
            mult[expected]+=1
    assert sum(k*v for k,v in mult.items())==(n-1)**3
    return n,dict(sorted(fvec.items())),dict(sorted(mult.items()))

if __name__=='__main__':
    for n in (3,5,7):
        p,f,m=model(n)
        print('n',p,'face_vector',f,'character_multiplicities',m)
    print('VERIFY_OK_CYCLIC_LATIN_CLIQUE_TRANSLATION_CHARACTER')
