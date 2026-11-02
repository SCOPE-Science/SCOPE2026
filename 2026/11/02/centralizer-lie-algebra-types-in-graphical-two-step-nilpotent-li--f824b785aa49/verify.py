#!/usr/bin/env python3
"""Direct finite-field bracket checks and six-vertex graph comparison."""
from itertools import combinations, product
from collections import Counter
from math import comb

def graph(edges,n):return {tuple(sorted(e)) for e in edges},set(range(n))
def components(S,E):
    out=[];R=set(S)
    while R:
        t={R.pop()};todo=list(t)
        while todo:
            v=todo.pop()
            for e in E:
                if v in e:
                    w=e[0] if e[1]==v else e[1]
                    if w in R:R.remove(w);t.add(w);todo.append(w)
        out.append(t)
    return out

def info(S,E,V):
    N=set(S)
    for i,j in E:
        if i in S:N.add(j)
        if j in S:N.add(i)
    U=V-N
    return U,components(S,E),sum(set(e)<=U for e in E)

def bracket(a,b,E,p):
    return tuple((a[i]*b[j]-a[j]*b[i])%p for i,j in sorted(E))

def direct_check(n,p):
    tests=0
    pairs=list(combinations(range(n),2));V=set(range(n))
    for emask in range(1<<len(pairs)):
        E={e for j,e in enumerate(pairs) if emask>>j&1}
        for x in product(range(p),repeat=n):
            S={i for i in V if x[i]};U,cc,k=info(S,E,V)
            # Explicit kernel basis: one weighted vector per S component, one basis vector per U.
            B=[]
            for C in cc:B.append([x[i] if i in C else 0 for i in range(n)])
            for u in U:B.append([1 if i==u else 0 for i in range(n)])
            for y in B:assert not any(bracket(x,y,E,p)),('not centralizing',E,x,y)
            # Independence: disjoint nonempty supports and singleton U, hence exact nullity.
            assert len(B)==len(cc)+len(U)
            # Bracket image of a basis is spanned by distinct standard edge symbols.
            used=set()
            for i in range(len(B)):
                for j in range(i):
                    z=bracket(B[i],B[j],E,p)
                    assert sum(v!=0 for v in z)<=1
                    used|={e for e,v in zip(sorted(E),z) if v}
            assert len(used)==k,(E,x,len(used),k)
            assert used=={e for e in E if set(e)<=U}
            tests+=1
    return tests

def signatures(E,n):
    V=set(range(n));a=Counter()
    for s in range(1<<n):
        S={i for i in V if s>>i&1};U,C,derived=info(S,E,V)
        rank=n-len(C)-len(U)
        for j in range(len(S)+1):
            a[(j,rank)]+=(-1)**(len(S)-j)*comb(len(S),j)
    return +a

def witness(E,q):
    V=set(range(6));total=0
    for mask in range(1<<6):
        S={i for i in V if mask>>i&1};U,C,k=info(S,E,V)
        if k==5:total+=(q-1)**len(S)
    return total*(q**len(E))

A={tuple(map(int,t)) for t in ('01','02','03','04','14','23','35')}
B={tuple(map(int,t)) for t in ('04','05','13','14','23','24','34')}
assert signatures(A,6)==signatures(B,6)
for q in (2,3,4,7):
    assert witness(A,q)==0
    assert witness(B,q)==q**7*(q-1)
checks=sum(direct_check(n,p) for n in (3,4) for p in (2,3))
print('GRAPH_LIE_CENTRALIZER_TYPE_OK',checks,'FORMAL_POLYNOMIAL_IDENTICAL',True)
