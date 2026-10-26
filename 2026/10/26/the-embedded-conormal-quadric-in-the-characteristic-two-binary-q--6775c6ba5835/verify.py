#!/usr/bin/env python3
"""Exact GF(2) polynomial and Hilbert-numerator checks for a binary quadratic resultant."""
from itertools import permutations, combinations
from collections import defaultdict

def const(n, c=1):
    return {tuple([0]*n): c % 2} if c % 2 else {}

def var(n,i):
    e=[0]*n;e[i]=1;return {tuple(e):1}

def add(*ps):
    out={}
    for p in ps:
        for e,c in p.items():
            if c%2:
                out[e]=out.get(e,0)^1
                if not out[e]:del out[e]
    return out

def mul(*ps):
    out=const(len(next(iter(ps[0]))) if ps[0] else 6)
    for p in ps:
        new={}
        for e,c in out.items():
            for f,d in p.items():
                t=tuple(x+y for x,y in zip(e,f))
                new[t]=new.get(t,0)^(c*d%2)
                if not new[t]:del new[t]
        out=new
    return out

def deriv(p,i):
    out={}
    for e,c in p.items():
        if e[i]%2:
            q=list(e);q[i]-=1;out[tuple(q)]=c
    return out

def shift(p, e):
    return {tuple(x+y for x,y in zip(k,e)):v for k,v in p.items()}

def lead(p):
    return max(p,key=lambda e:(sum(e),tuple(-x for x in e[::-1])))

def divides(e,f):return all(a<=b for a,b in zip(e,f))

def reduce(p, gb):
    p=dict(p);rem={}
    while p:
        m=lead(p)
        for g in gb:
            l=lead(g)
            if divides(l,m):
                p=add(p,shift(g,tuple(x-y for x,y in zip(m,l))))
                break
        else:
            rem[m]=1;del p[m]
    return rem

def subst(p,maps):
    n=len(next(iter(maps[0])))
    out={}
    for e,c in p.items():
        cur=const(n,c)
        for i,power in enumerate(e):
            for _ in range(power):cur=mul(cur,maps[i])
        out=add(out,cur)
    return out

v=[var(6,i) for i in range(6)]
a,b,c,d,e,f=v
u=add(mul(a,e),mul(b,d))
w=add(mul(a,f),mul(c,d))
z=add(mul(b,f),mul(c,e))
R=add(mul(w,w),mul(u,z))
M=[[a,b,c,{}],[{},a,b,c],[d,e,f,{}],[{},d,e,f]]
det={}
for perm in permutations(range(4)):
    det=add(det,mul(*[M[i][perm[i]] for i in range(4)]))
assert det==R, 'Sylvester determinant mismatch'
ordered=[mul(e,z),mul(e,w),mul(e,u),mul(b,z),mul(b,w),mul(b,u)]
assert [deriv(R,i) for i in range(6)]==ordered,'gradient mismatch'
G=[mul(w,w)]+ordered
assert all(not reduce(add(shift(gi,tuple(x-y for x,y in zip(lcm,li))),shift(gj,tuple(x-y for x,y in zip(lcm,lj)))),G)
               for gi,gj in combinations(G,2)
               for li,lj in [(lead(gi),lead(gj))]
               for lcm in [tuple(max(x,y) for x,y in zip(li,lj))]),'Buchberger criterion failed'
lead_m=[lead(g) for g in G]
num=defaultdict(int);num[0]=1
for n in range(1,len(G)+1):
    for part in combinations(lead_m,n):
        lcm=tuple(max(x[i] for x in part) for i in range(6))
        num[sum(lcm)]+=(-1)**n
num={k:v for k,v in num.items() if v}
assert num=={0:1,3:-6,4:6,6:-1},('Hilbert numerator',num)
# Affine-coordinate identity, setting a=1, e=d*b+U, f=d*c+V.
B,C,D,U,V=[var(5,i) for i in range(5)]
aff=subst(R,[const(5),B,C,D,add(mul(D,B),U),add(mul(D,C),V)])
assert aff==add(mul(V,V),mul(B,U,V),mul(C,U,U)),'local normal form mismatch'
# T = k[a,c,d,f]/(af+cd), H_T=(1+t)/(1-t)^3.
# Conormal excess t^2 H_T+t (H_T-1/(1-t)^2) = t^2(3+t)/(1-t)^3.
print('VERIFY_OK: Sylvester determinant, six partial derivatives, 21 Buchberger S-polynomials,')
print('GF2 Hilbert numerator 1-6t^3+6t^4-t^6, local normal form V^2+BUV+CU^2')
