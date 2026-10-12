#!/usr/bin/env python3
from math import isqrt

LIMIT = 100_000


def factor(n):
    out=[]
    d=2
    while d*d<=n:
        if n%d==0:
            e=0
            while n%d==0:
                n//=d; e+=1
            out.append((d,e))
        d = 3 if d==2 else d+2
    if n>1: out.append((n,1))
    return out


def tau_from_factor(f):
    t=1
    for _,e in f: t*=e+1
    return t


def rep_p_x2_minus_8y2(p):
    # Regression search only; the proof in RESULT.md is symbolic.
    # The sqrt(p) search range comfortably covers every tested p.
    for y in range(isqrt(p)+1):
        z=p+8*y*y
        x=isqrt(z)
        if x*x==z:
            return x,y
    return None


def witness(n):
    N=8*n+1
    f=factor(N)
    t=tau_from_factor(f)
    if t%4==0:
        return None
    odd=[(p,e) for p,e in f if e%2]
    if not odd:
        x=isqrt(N)
        assert x*x==N and x%2==1
        m=(x-1)//2
        assert m*(m+1)//2==n
        return m,0,"square"
    assert len(odd)==1
    p,e=odd[0]
    assert e%4==1
    assert p%8==1
    v=1
    for q,a in f:
        if q==p:
            v*=q**((a-1)//2)
        else:
            assert a%2==0
            v*=q**(a//2)
    rep=rep_p_x2_minus_8y2(p)
    assert rep is not None, (n,p)
    A,B=rep
    X=A*v
    Y=B*v
    assert X*X-8*Y*Y==N
    assert X%2==1
    m=(X-1)//2
    assert m*(m+1)//2-Y*Y==n
    return m,Y,"one-odd-exponent"

count=0
branch_square=0
branch_unique=0
for n in range(LIMIT+1):
    N=8*n+1
    f=factor(N)
    if tau_from_factor(f)%4 != 0:
        count+=1
        w=witness(n)
        assert w is not None
        if w[2]=="square": branch_square+=1
        else: branch_unique+=1

print("VERIFY_OK")
print(f"n_range=0..{LIMIT}")
print(f"exceptional_inputs={count}")
print(f"square_branch={branch_square}")
print(f"unique_odd_exponent_branch={branch_unique}")
