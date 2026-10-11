#!/usr/bin/env python3
# Exact polynomial verification for the transformed-height identity.
VARS = ("a","b","f","g","x","y","z")
N=len(VARS)
def C(n): return {(0,)*N:int(n)} if n else {}
def X(i):
    e=[0]*N; e[i]=1; return {tuple(e):1}
def add(p,q):
    r=dict(p)
    for m,c in q.items():
        r[m]=r.get(m,0)+c
        if r[m]==0: del r[m]
    return r
def neg(p): return {m:-c for m,c in p.items()}
def sub(p,q): return add(p,neg(q))
def mul(p,q):
    r={}
    for m,c in p.items():
        for n,d in q.items():
            k=tuple(m[i]+n[i] for i in range(N))
            r[k]=r.get(k,0)+c*d
    return {m:c for m,c in r.items() if c}
def scale(k,p): return {m:k*c for m,c in p.items() if k*c}
a,b,f,g,x,y,z=[X(i) for i in range(N)]
two=C(2)
xdot=mul(a,sub(y,x))
zdot=add(neg(mul(b,z)),add(mul(f,mul(x,x)),mul(g,mul(x,y))))
lhs=sub(mul(mul(two,a),zdot),mul(mul(two,g),mul(x,xdot)))
# -b(2az-gx^2) + (2a(f+g)-bg)x^2
term1=neg(mul(b,sub(mul(mul(two,a),z),mul(g,mul(x,x)))))
knum=sub(mul(mul(two,a),add(f,g)),mul(b,g))
rhs=add(term1,mul(knum,mul(x,x)))
assert lhs==rhs, (lhs,rhs)
print("VERIFY_OK")
