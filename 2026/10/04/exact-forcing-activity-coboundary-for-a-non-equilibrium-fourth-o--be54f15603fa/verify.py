#!/usr/bin/env python3
from fractions import Fraction as Q

N=10  # x,y,z,w,a,b,c,e,f,g

def mono(i):
    e=[0]*N; e[i]=1; return {tuple(e):Q(1)}
def const(q): return {(0,)*N:Q(q)} if q else {}
def add(*ps):
    out={}
    for p in ps:
        for m,c in p.items():
            out[m]=out.get(m,Q(0))+c
            if out[m]==0: del out[m]
    return out
def neg(p): return {m:-c for m,c in p.items()}
def scale(p,s): return {m:c*Q(s) for m,c in p.items() if c*Q(s)}
def mul(p,q):
    out={}
    for m,c in p.items():
        for n,d in q.items():
            k=tuple(m[i]+n[i] for i in range(N))
            out[k]=out.get(k,Q(0))+c*d
    return {m:c for m,c in out.items() if c}
def diff(p,i):
    out={}
    for m,c in p.items():
        if m[i]:
            k=list(m); k[i]-=1; k=tuple(k)
            out[k]=out.get(k,Q(0))+c*m[i]
    return out

def lie(p,F):
    return add(*(mul(diff(p,i),F[i]) for i in range(4)))

x,y,z,w,a,b,c,e,f,g=[mono(i) for i in range(N)]
x2=mul(x,x); y2=mul(y,y); xy=mul(x,y); xz=mul(x,z)
F=[y,z,w, add(neg(mul(a,w)), mul(b,x2), neg(mul(c,y2)), mul(e,xy), mul(f,xz), g)]
Phi=add(w,mul(a,z),scale(mul(e,x2),Q(-1,2)),neg(mul(f,xy)))
target=add(mul(b,x2),neg(mul(add(c,f),y2)),g)
assert lie(Phi,F)==target
B=Q(7,10); CF=Q(99,50); G=Q(23,20)
assert B/CF==Q(35,99)
assert G/CF==Q(115,198)
print('VERIFY_OK')
