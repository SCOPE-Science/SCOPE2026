#!/usr/bin/env python3
from itertools import product
from collections import Counter, defaultdict

def qint(m,q):
    return (q**m-1)//(q-1)

def canon(v,q):
    for x in v:
        if x%q:
            inv=pow(x,-1,q)
            return tuple((inv*y)%q for y in v)
    raise ValueError("zero vector")

def projective_points(n,q):
    seen=set()
    for v in product(range(q), repeat=n):
        if any(v):
            seen.add(canon(v,q))
    return sorted(seen)

def dot(x,y,q):
    return sum(a*b for a,b in zip(x,y))%q

def quotient_graph(n,q):
    P=projective_points(n,q)
    flags=[(p,h) for p in P for h in P if dot(p,h,q)==0]
    idx={f:i for i,f in enumerate(flags)}
    A=[set() for _ in flags]
    for i,(p,h) in enumerate(flags):
        for j in range(i+1,len(flags)):
            r,k=flags[j]
            if dot(h,r,q)==0 and dot(k,p,q)==0:
                A[i].add(j); A[j].add(i)
    return flags,A

def formula(n,q):
    a=qint(n-1,q); b=qint(n-2,q); c=qint(n-3,q)
    T=a+(a-1)*b
    degQ=T-1
    lam_same=a+(b-1)*b-2
    lam_cross=(q+1)*b+(b-q-1)*c-2
    fullN=(q-1)*qint(n,q)*a
    fullD=(q-1)*T-1
    return a,b,c,T,degQ,lam_same,lam_cross,fullN,fullD

def classify_edge(f,g):
    p,h=f; r,k=g
    if p==r: return "same_point"
    if h==k: return "same_hyperplane"
    return "cross"

for n,q in [(3,2),(3,3),(4,2),(4,3),(5,2)]:
    flags,A=quotient_graph(n,q)
    a,b,c,T,degQ,ls,lc,fullN,fullD=formula(n,q)
    assert len(flags)==qint(n,q)*a
    assert set(map(len,A))=={degQ}
    counts=defaultdict(set)
    edge_counts=Counter()
    for i in range(len(flags)):
        for j in A[i]:
            if i<j:
                typ=classify_edge(flags[i],flags[j])
                counts[typ].add(len(A[i]&A[j]))
                edge_counts[typ]+=1
    assert counts["same_point"]=={ls}
    assert counts["same_hyperplane"]=={ls}
    if n==3:
        assert not counts["cross"]
    else:
        assert counts["cross"]=={lc}
        assert ls-lc==q*c*((q-1)*c+1)>0
    assert fullN==(q-1)*len(flags)
    assert fullD==(q-1)*(degQ+1)-1
    print("case",n,q,"flags",len(flags),"qdeg",degQ,
          "same",ls,"cross",lc if n>=4 else "absent",
          "full_vertices",fullN,"full_degree",fullD,
          "edge_types",dict(edge_counts))

# Direct matrix check for the first higher-dimensional boundary M_4(F_2).
def outer(u,f,q):
    return tuple(tuple((a*b)%q for b in f) for a in u)

def mmul(A,B,q):
    n=len(A)
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(n))%q
                       for j in range(n)) for i in range(n))

n=q=2  # reset immediately below; keeps linter-simple integer names
n=4; q=2
P=projective_points(n,q)
matrices={}
for u in P:
    for f in P:
        if dot(u,f,q)==0:
            M=outer(u,f,q)
            assert mmul(M,M,q)==tuple(tuple(0 for _ in range(n)) for _ in range(n))
            matrices[M]=(u,f)
assert len(matrices)==qint(4,2)*qint(3,2)==105
items=list(matrices.items())
for i,(A,(p,h)) in enumerate(items):
    for j in range(i+1,len(items)):
        B,(r,k)=items[j]
        commute=mmul(A,B,q)==mmul(B,A,q)
        geometry=(dot(h,r,q)==0 and dot(k,p,q)==0)
        assert commute==geometry

print("VERIFY_OK")
