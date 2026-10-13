#!/usr/bin/env python3
from itertools import combinations

def fib(n):
    a,b=0,1
    for _ in range(n):
        a,b=b,a+b
    return a

def antiregular_graph(m):
    N=[set() for _ in range(m)]
    for i in range(1,m+1):
        for j in range(i+1,m+1):
            if i+j>=m+1:
                N[i-1].add(j-1)
                N[j-1].add(i-1)
    return N

def zero_forces(C,N):
    blue=set(C)
    while True:
        move=None
        for v in sorted(blue):
            W=N[v]-blue
            if len(W)==1:
                move=next(iter(W))
                break
        if move is None:
            return len(blue)==len(N)
        blue.add(move)

def ready(C,N):
    blue=set(C)
    return zero_forces(C,N) and any(N[v] <= blue for v in blue)

def stats(m):
    N=antiregular_graph(m)
    z=None; a=0
    for k in range(m+1):
        A=[C for C in combinations(range(m),k) if zero_forces(C,N)]
        if A:
            z=k; a=len(A); break
    rho=None; b=0
    for k in range(m+1):
        A=[C for C in combinations(range(m),k) if ready(C,N)]
        if A:
            rho=k; b=len(A); break
    return z,a,rho,b

def annihilator_mod(x,p,ell):
    mod=p**ell
    return frozenset(r for r in range(mod) if (r*x)%mod==0)

def compressed_mod_graph(p,ell):
    mod=p**ell
    elems=list(range(mod))
    def unit(x): return x%p!=0
    zd=[x for x in elems if x!=0 and not unit(x)]
    classes={}
    for x in zd:
        a=annihilator_mod(x,p,ell)
        classes.setdefault(a,[]).append(x)
    reps=[min(v) for v in classes.values()]
    def val(x):
        i=0
        while x%p==0:
            i+=1; x//=p
        return i
    reps=sorted(reps,key=val)
    N=[set() for _ in reps]
    for i,x in enumerate(reps):
        for j in range(i+1,len(reps)):
            if (x*reps[j])%mod==0:
                N[i].add(j);N[j].add(i)
    return reps,N

for m in range(1,13):
    z,a,rho,b=stats(m)
    if m==1:
        assert (z,a,rho,b)==(1,1,1,1)
        print("m=1: K1 boundary, Z=1, min_sets=1, mr=0")
        continue
    assert z==m//2
    assert rho==z+1
    if m%2==0:
        assert a==fib(m+1)
        assert b==fib(m)
    else:
        assert a==2*fib(m-1)
        assert b==2*fib(m-2)
    if m>=4:
        z0,a0,r0,b0=stats(m-2)
        assert a==2*a0+b0
        assert b==a0+b0
    print(f"m={m}: Z={z}, min_sets={a}, ready_min={rho}, ready_sets={b}, mr={m-z}")

for p in (2,3):
    for ell in range(2,7):
        reps,N=compressed_mod_graph(p,ell)
        A=antiregular_graph(ell-1)
        assert len(reps)==ell-1
        assert N==A
        vals=[]
        for x in reps:
            y=x;i=0
            while y%p==0:
                i+=1;y//=p
            vals.append(i)
        assert vals==list(range(1,ell))
        print(f"Z/{p}^{ell}: classes={len(reps)}, valuations={vals}, anti_regular=A_{ell-1}")

print("VERIFY_OK")
