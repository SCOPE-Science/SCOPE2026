#!/usr/bin/env python3
from itertools import combinations

def fan_with_horn(n,m):
    # Vertices: 0=center; then n ordered triangle pairs; then m leaves.
    N=1+2*n+m
    A=[set() for _ in range(N)]
    for i in range(n):
        a=1+2*i
        b=a+1
        for u,v in ((0,a),(a,b),(b,0)):
            A[u].add(v);A[v].add(u)
    for j in range(m):
        x=1+2*n+j
        A[0].add(x);A[x].add(0)
    return A

def three_horn_triangle():
    # Core 0,1,2; leaf i+3 attached to core i.
    A=[set() for _ in range(6)]
    for u,v in ((0,1),(1,2),(2,0),(0,3),(1,4),(2,5)):
        A[u].add(v);A[v].add(u)
    return A

def zero_forces(S,A):
    blue=set(S)
    while True:
        move=None
        for v in sorted(blue):
            W=A[v]-blue
            if len(W)==1:
                move=next(iter(W))
                break
        if move is None:
            return len(blue)==len(A)
        blue.add(move)

def minimum_sets(A):
    N=len(A)
    for k in range(N+1):
        sets=[S for S in combinations(range(N),k) if zero_forces(S,A)]
        if sets:
            return k,sets
    raise RuntimeError

def predicted_fan_count(n,m):
    if m==1:
        return n+1, (2**(n-1))*(n+4)
    return n+m-1, m*(2**n)

def classify_fan_minset(n,m,S):
    S=set(S)
    center=0
    pairs=[{1+2*i,2+2*i} for i in range(n)]
    leaves=set(range(1+2*n,1+2*n+m))
    if m>=2:
        return (
            center not in S
            and all(len(P&S)==1 for P in pairs)
            and len(leaves&S)==m-1
        )
    # m=1: exactly one from each pair plus one extra object.
    leaf=next(iter(leaves))
    base=[len(P&S) for P in pairs]
    if center in S and leaf not in S and all(x==1 for x in base):
        return True
    if leaf in S and center not in S and all(x==1 for x in base):
        return True
    if center not in S and leaf not in S and base.count(2)==1 and base.count(1)==n-1:
        return True
    return False

# Exhaustive fan-with-horn checks, including all small Yu-Wu boundary graphs.
for n in range(1,7):
    for m in range(1,5):
        A=fan_with_horn(n,m)
        z,sets=minimum_sets(A)
        pz,pc=predicted_fan_count(n,m)
        assert z==pz,(n,m,z,pz)
        assert len(sets)==pc,(n,m,len(sets),pc)
        assert all(classify_fan_minset(n,m,S) for S in sets)
        print(f"F_{n}({m}): Z={z}, minimum_sets={len(sets)}")

# Three-horn triangle boundary.
A=three_horn_triangle()
z,sets=minimum_sets(A)
assert z==2 and len(sets)==9
expected=set()
# Two leaves.
for S in combinations((3,4,5),2):
    expected.add(tuple(sorted(S)))
# One core plus a nonincident leaf.
for c in range(3):
    for leaf in (3,4,5):
        if leaf!=c+3:
            expected.add(tuple(sorted((c,leaf))))
assert set(map(tuple,map(sorted,sets)))==expected
print("K3(1,1,1): Z=2, minimum_sets=9")

# Closed-form Yu-Wu finite-family substitutions.
for r in range(1,6):
    n=2*r
    z,c=predicted_fan_count(n,2)
    assert z==2*r+1 and c==2**(2*r+1)
for p in (3,5,7):
    for k in (1,2,3):
        q=p**k
        n1=(q+1)//2
        z1,c1=predicted_fan_count(n1,1)
        assert z1==(q+3)//2
        assert c1==(2**((q-1)//2))*((q+9)//2)
        n3=(q-1)//2
        z3,c3=predicted_fan_count(n3,3)
        assert z3==(q+3)//2
        assert c3==3*(2**((q-1)//2))
print("YU_WU_SPECIALIZATIONS_OK")
print("VERIFY_OK")
