#!/usr/bin/env python3
"""Exact finite-field census of maximal-dimensional abelian subspaces
of a graph-defined 2-step nilpotent Lie algebra. No third-party libraries.
"""
from itertools import combinations,product

def independence_number(n,edges):
    E={tuple(sorted(x)) for x in edges}
    return max((len(S) for k in range(n+1) for S in combinations(range(n),k)
                if not any(tuple(sorted(e)) in E for e in combinations(S,2))), default=0)

def rref_subspaces(n,d,q):
    for S in combinations(range(n),d):
        P=set(S)
        spots=[(i,j) for i,p in enumerate(S) for j in range(p+1,n) if j not in P]
        for values in product(range(q),repeat=len(spots)):
            B=[[int(j==S[i]) for j in range(n)] for i in range(d)]
            for (i,j),t in zip(spots,values):B[i][j]=t
            yield S,B

def commutes(B,edges,q):
    for a,b in combinations(B,2):
        for u,v in edges:
            if (a[u]*b[v]-a[v]*b[u])%q:return False
    return True

def count_formula(n,E,q):
    E={tuple(sorted(e)) for e in E}
    d=independence_number(n,E)
    total=0
    for S in combinations(range(n),d):
        if any(tuple(sorted(e)) in E for e in combinations(S,2)):continue
        owner={}
        for v in range(n):
            if v in S:continue
            neighbors=[s for s in S if tuple(sorted((v,s))) in E]
            if len(neighbors)==1 and neighbors[0]<v:owner[v]=neighbors[0]
        F=list(owner)
        H={(u,v) for u,v in combinations(F,2) if tuple(sorted((u,v))) in E and owner[u]!=owner[v]}
        for t in product(range(q),repeat=len(F)):
            if all(not(t[F.index(u)] and t[F.index(v)]) for u,v in H):total+=1
    return total

def direct(n,E,q):
    d=independence_number(n,E)
    return sum(commutes(B,E,q) for S,B in rref_subspaces(n,d,q))

def mul4(a,b):
    x=0
    for i in range(2):
        if (b>>i)&1:x^=a<<i
    if x&8:x^=0b1110 # x^3 = x^2+x under x^2=x+1
    if x&4:x^=0b111  # x^2=x+1
    return x

def commutes_gf4(B,edges):
    for a,b in combinations(B,2):
        for u,v in edges:
            if mul4(a[u],b[v]) != mul4(a[v],b[u]):return False
    return True

def direct_gf4(n,E):
    d=independence_number(n,E)
    return sum(commutes_gf4(B,E) for S,B in rref_subspaces(n,d,4))

def show(n,edges,q):
    E=[tuple(sorted(e)) for e in edges]
    a=count_formula(n,E,q)
    b=direct(n,E,q)
    assert a==b,(n,E,q,a,b)
    print(f'n={n},edges={E},q={q},alpha={independence_number(n,E)},number={a}')
    return a

def main():
    total=0
    for n in range(1,5):
        edges=list(combinations(range(n),2))
        for mask in range(1<<len(edges)):
            E=[e for i,e in enumerate(edges) if mask>>i&1]
            for q in (2,3):
                a=count_formula(n,E,q);b=direct(n,E,q)
                assert a==b,(n,mask,q,a,b)
                total+=1
    for n,E in [
        (5,[(i,i+1) for i in range(4)]),
        (5,[(i,(i+1)%5) for i in range(5)]),
        (5,list(combinations(range(5),2))),
        (6,[(i,i+1) for i in range(5)]),
    ]:
        for q in (2,3):
            a=count_formula(n,E,q);b=direct(n,E,q)
            assert a==b,(n,E,q,a,b)
            total+=1
    for n in range(1,5):
        edges=list(combinations(range(n),2))
        for mask in range(1<<len(edges)):
            E=[e for i,e in enumerate(edges) if mask>>i&1]
            a=count_formula(n,E,4);b=direct_gf4(n,E)
            assert a==b,(n,E,4,a,b)
            total+=1
    for n,E in [(2,[(0,1)]),(4,[(i,i+1) for i in range(3)]),(5,[(i,(i+1)%5) for i in range(5)]),(6,[(i,i+1) for i in range(5)])]:
        show(n,E,2)
        show(n,E,3)
    triangle=[(0,1),(0,2),(1,2)]
    path=[(0,1),(1,2),(2,3)]
    for q in (2,3,4,5):
        assert count_formula(4,triangle,q)==q*q+q+1
        assert count_formula(4,path,q)==2*q+1
        if q==5:
            assert direct(4,triangle,q)==q*q+q+1
            assert direct(4,path,q)==2*q+1
            total+=2
    for perm in __import__('itertools').permutations(range(4)):
        E=[tuple(sorted((perm[u],perm[v]))) for u,v in path]
        for q in (2,3):
            assert count_formula(4,E,q)==2*q+1
    print('GRAPH_MAXIMAL_ABELIAN_SCHUBERT_OK',total)
    print('INDEPENDENCE_POLYNOMIAL_TWINS', '1+4z+3z^2',
          'K3_plus_isolate', [(q,q*q+q+1) for q in (2,3,4,5)],
          'P4',[(q,2*q+1) for q in (2,3,4,5)])
if __name__=='__main__':main()
