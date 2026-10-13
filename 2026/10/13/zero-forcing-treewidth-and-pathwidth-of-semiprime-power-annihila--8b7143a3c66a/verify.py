#!/usr/bin/env python3
from itertools import combinations

def abstract_graph(a):
    V=[("A",i) for i in range(1,a+1)]+[("B",j) for j in range(a)]
    N={v:set() for v in V}
    for x,y in combinations(V,2):
        adj=(x[0]=="A" and y[0]=="B" and x[1]+y[1]>=a) or (x[0]=="B" and y[0]=="A" and x[1]+y[1]>=a) or (x[0]=="B" and y[0]=="B" and x[1]+y[1]>=a)
        if adj: N[x].add(y); N[y].add(x)
    return V,N

def zero_forces(S,N):
    blue=set(S)
    while True:
        if len(blue)==len(N): return True
        move=None
        for v in sorted(blue):
            w=N[v]-blue
            if len(w)==1: move=next(iter(w)); break
        if move is None: return False
        blue.add(move)

def exact_Z(a):
    V,N=abstract_graph(a)
    for k in range(len(V)+1):
        c=sum(1 for S in combinations(V,k) if zero_forces(S,N))
        if c: return k,c

def claimed_sequence(a):
    V,N=abstract_graph(a); blue={("A",i) for i in range(1,a)}; seq=[]
    for i in range(1,a):
        s=("A",i); t=("B",a-i); assert N[s]-blue=={t}; blue.add(t); seq.append((s,t))
    s=("B",1); t=("A",a); assert N[s]-blue=={t}; blue.add(t); seq.append((s,t))
    s=("A",a); t=("B",0); assert N[s]-blue=={t}; blue.add(t); seq.append((s,t))
    assert len(blue)==2*a; return seq

def minor_certificate(a):
    V,N=abstract_graph(a); C=[{("A",i),("B",a-i)} for i in range(1,a+1)]
    for B in C:
        x,y=tuple(B); assert y in N[x]
    for i in range(a):
        for j in range(i+1,a): assert any(y in N[x] for x in C[i] for y in C[j])
    return C

def divisors(n): return [d for d in range(1,n+1) if n%d==0]
def direct_graph(p,q,a):
    n=p**a*q; D=[d for d in divisors(n) if 1<d<n]; N={d:set() for d in D}
    for d,e in combinations(D,2):
        if (d*e)%n==0: N[d].add(e); N[e].add(d)
    return n,D,N

def compare_direct(p,q,a):
    n,D,Nd=direct_graph(p,q,a); V,Na=abstract_graph(a)
    f={("A",i):p**i for i in range(1,a+1)}; f.update({("B",j):p**j*q for j in range(a)})
    assert sorted(f.values())==sorted(D)
    for x,y in combinations(V,2): assert ((f[y] in Nd[f[x]])==(y in Na[x]))
    return n,len(D)

for a in range(2,31): assert len(claimed_sequence(a))==a+1 and len(minor_certificate(a))==a
print("symbolic forcing and K_a-minor certificates: a=2..30 OK")
for a in range(2,9):
    z,c=exact_Z(a); assert z==a-1; print(f"a={a}: exact Z={z}, minimum_sets={c}")
for p,q,a in [(2,3,2),(2,5,4),(3,5,5),(5,7,3)]:
    n,v=compare_direct(p,q,a); print(f"Z/{n}Z: direct ideal-product graph has {v} vertices and matches the abstract graph")
V,N=abstract_graph(1); assert len(V)==2 and all(len(N[v])==1 for v in V) and exact_Z(1)[0]==1
print("a=1 boundary: K2 with Z=1")
print("VERIFY_OK")
