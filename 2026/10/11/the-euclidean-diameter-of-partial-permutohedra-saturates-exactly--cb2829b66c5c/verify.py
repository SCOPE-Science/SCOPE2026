#!/usr/bin/env python3
from itertools import combinations, permutations

def source_vertices(m,n):
    out=[]
    p=min(m,n)
    for k in range(p+1):
        vals=tuple(range(n-k+1,n+1))
        for supp in combinations(range(m),k):
            for perm in permutations(vals):
                v=[0]*m
                for i,x in zip(supp,perm):
                    v[i]=x
                out.append(tuple(v))
    return out

def S(n,k):
    return sum((n-r)**2 for r in range(k))

def formula2(m,n):
    s=min(m,2*n)
    a=s//2
    b=s-a
    return S(n,a)+S(n,b),a,b

def classify(u,v,m,n,a,b):
    su={i for i,x in enumerate(u) if x}
    sv={i for i,x in enumerate(v) if x}
    if su & sv:
        return False
    U=sorted((u[i] for i in su))
    V=sorted((v[i] for i in sv))
    A=list(range(n-a+1,n+1))
    B=list(range(n-b+1,n+1))
    return (U==A and V==B) or (U==B and V==A)

cases=0
maximizers=0
for m in range(1,6):
    for n in range(1,6):
        V=source_vertices(m,n)
        want,a,b=formula2(m,n)
        best=-1
        pairs=[]
        for i,u in enumerate(V):
            for v in V[i+1:]:
                d2=sum((x-y)**2 for x,y in zip(u,v))
                if d2>best:
                    best=d2
                    pairs=[(u,v)]
                elif d2==best:
                    pairs.append((u,v))
        if len(V)==1:
            best=0
            pairs=[]
        assert best==want,(m,n,best,want)
        for u,v in pairs:
            assert classify(u,v,m,n,a,b),(m,n,u,v,a,b)
        # Construct one predicted pair and check it is present and maximizing.
        s=min(m,2*n)
        supp_a=list(range(a))
        supp_b=list(range(a,a+b))
        u=[0]*m
        v=[0]*m
        for i,x in zip(supp_a,range(n-a+1,n+1)):
            u[i]=x
        for i,x in zip(supp_b,range(n-b+1,n+1)):
            v[i]=x
        assert tuple(u) in V and tuple(v) in V
        assert sum((x-y)**2 for x,y in zip(u,v))==want
        cases+=1
        maximizers+=len(pairs)

# Saturation identity.
for n in range(1,30):
    sat=n*(n+1)*(2*n+1)//3
    for m in range(2*n,2*n+8):
        want,_,_=formula2(m,n)
        assert want==sat

print(f"VERIFY_OK partial-permutohedron-diameter cases={cases} maximizing_pairs={maximizers} saturation=yes")
