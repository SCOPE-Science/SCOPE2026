#!/usr/bin/env python3
from itertools import combinations

def abstract_graph():
    V=[(i,j) for i in range(3) for j in range(3)
       if (i,j) not in {(0,0),(2,2)}]
    N={v:set() for v in V}
    for x,y in combinations(V,2):
        if x[0]+y[0]>=2 and x[1]+y[1]>=2:
            N[x].add(y); N[y].add(x)
    return V,N

def force_sequence(S,V,N):
    blue=set(S)
    seq=[]
    while len(blue)<len(V):
        move=None
        for v in V:
            if v in blue:
                white=N[v]-blue
                if len(white)==1:
                    move=(v,next(iter(white)))
                    break
        if move is None:
            return None
        seq.append(move)
        blue.add(move[1])
    return seq

def polynomial(V,N):
    out={}
    mins=[]
    for k in range(len(V)+1):
        count=0
        for S in combinations(V,k):
            seq=force_sequence(S,V,N)
            ok=(seq is not None)
            if k==len(V):
                ok=True
            if ok:
                count+=1
                if k==2:
                    mins.append(tuple(sorted(S)))
        if count:
            out[k]=count
    return out,sorted(mins)

def check_path_decomposition(V,N,bags):
    assert set().union(*map(set,bags))==set(V)
    for x,y in combinations(V,2):
        if y in N[x]:
            assert any(x in B and y in B for B in bags),(x,y)
    for v in V:
        loc=[i for i,B in enumerate(bags) if v in B]
        assert loc==list(range(min(loc),max(loc)+1)),(v,loc)
    return max(len(B) for B in bags)-1

def divisors(n):
    return [d for d in range(1,n+1) if n%d==0]

def direct_ring(p,q):
    n=p*p*q*q
    D=[d for d in divisors(n) if 1<d<n]
    N={d:set() for d in D}
    for d,e in combinations(D,2):
        if (d*e)%n==0:
            N[d].add(e); N[e].add(d)
    model={(0,1):q,(0,2):q*q,(1,0):p,(1,1):p*q,
           (1,2):p*q*q,(2,0):p*p,(2,1):p*p*q}
    V,A=abstract_graph()
    assert sorted(model.values())==sorted(D)
    for x,y in combinations(V,2):
        assert ((model[y] in N[model[x]]) == (y in A[x]))
    return n,len(D)

V,N=abstract_graph()
assert len(V)==7
poly,mins=polynomial(V,N)
expected={2:4,3:24,4:33,5:21,6:7,7:1}
assert poly==expected,(poly,expected)
expected_mins=sorted([
    ((0,1),(0,2)),
    ((0,1),(1,1)),
    ((1,0),(1,1)),
    ((1,0),(2,0)),
])
assert mins==expected_mins,(mins,expected_mins)
print("zero forcing polynomial:",poly)
print("minimum zero forcing sets:",mins)

for S in expected_mins:
    seq=force_sequence(S,V,N)
    assert seq is not None and len(seq)==5
    print("forcing sequence",S,":",seq)

bags=[
    {(0,1)},
    {(0,1),(0,2)},
    {(0,1),(0,2),(2,1)},
    {(0,2),(2,0),(2,1)},
    {(1,2),(2,0),(2,1)},
    {(1,0),(1,2),(2,1)},
    {(1,1),(1,2),(2,1)},
]
pw_upper=check_path_decomposition(V,N,bags)
assert pw_upper==2
cycle=[(0,2),(2,0),(1,2),(2,1)]
for i in range(4):
    assert cycle[(i+1)%4] in N[cycle[i]]
assert cycle[2] not in N[cycle[0]]
assert cycle[3] not in N[cycle[1]]
print("width-2 path decomposition OK; induced C4 OK")

for p,q in [(2,3),(2,5),(3,5),(5,7)]:
    n,c=direct_ring(p,q)
    assert c==7
    print(f"Z/{n}Z direct ideal-product graph OK: {c} vertices")

assert sum(poly.values())==90
print("all 128 subsets classified; 90 are zero forcing")
print("VERIFY_OK")
