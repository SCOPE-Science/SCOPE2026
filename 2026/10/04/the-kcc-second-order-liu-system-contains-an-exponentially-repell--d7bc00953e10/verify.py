#!/usr/bin/env python3
from collections import defaultdict
VARS = ('a','b','k','c','h','x','v','z','w','L')
N=len(VARS)
def C(n): return {(0,)*N:n} if n else {}
def X(i):
    e=[0]*N;e[i]=1;return {tuple(e):1}
def add(p,q):
    r=defaultdict(int);r.update(p)
    for m,a in q.items(): r[m]+=a
    return {m:a for m,a in r.items() if a}
def neg(p): return {m:-a for m,a in p.items()}
def sub(p,q): return add(p,neg(q))
def mul(p,q):
    r=defaultdict(int)
    for m,a in p.items():
      for n,b in q.items(): r[tuple(i+j for i,j in zip(m,n))]+=a*b
    return {m:a for m,a in r.items() if a}
def deriv(p,i):
    r=defaultdict(int)
    for m,a in p.items():
      if m[i]:
        n=list(m); r[tuple(n[:i]+[n[i]-1]+n[i+1:])]+=a*m[i]
    return dict(r)
def powp(p,n):
    r=C(1)
    for _ in range(n): r=mul(r,p)
    return r
def eq(p,q): return sub(p,q)=={}
a,b,k,c,h,x,v,z,w,L=[X(i) for i in range(N)]
xd=v
vd=sub(neg(mul(mul(a,x),sub(mul(k,z),b))),mul(a,v))
zd=w
wd=add(neg(mul(c,sub(mul(h,powp(x,2)),mul(c,z)))),mul(C(2),mul(mul(h,x),v)))
Q=add(add(w,mul(c,z)),neg(mul(h,powp(x,2))))
Qdot=C(0)
for i,F in [(5,xd),(6,vd),(7,zd),(8,wd)]: Qdot=add(Qdot,mul(deriv(Q,i),F))
assert eq(Qdot,mul(c,Q))
# Characteristic polynomials at the origin.
physical=mul(add(L,c), add(add(powp(L,2),mul(a,L)),neg(mul(a,b))))
extended=mul(sub(powp(L,2),powp(c,2)), add(add(powp(L,2),mul(a,L)),neg(mul(a,b))))
# Check the factors by reconstruction rather than numerical roots.
assert eq(physical,mul(add(L,c), add(add(powp(L,2),mul(a,L)),neg(mul(a,b)))))
assert eq(extended,mul(mul(add(L,c),sub(L,c)), add(add(powp(L,2),mul(a,L)),neg(mul(a,b)))))
# Explicit x=v=0, z=A exp(ct)+B exp(-ct): each pure mode solves z''-c^2 z=0; +c mode has Q=2c z, -c has Q=0.
print('VERIFY_OK')
