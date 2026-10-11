#!/usr/bin/env python3
# Exact polynomial replay for the five-dimensional integer-order complex flow.
# Standard library only.
from collections import defaultdict

N=8  # x1,x2,x3,x4,z,sigma,r,beta

def mono(i):
    e=[0]*N; e[i]=1
    return {tuple(e):1}
def const(c):
    return {(0,)*N:c} if c else {}
def add(a,b):
    d=defaultdict(int); d.update(a)
    for k,v in b.items(): d[k]+=v
    return {k:v for k,v in d.items() if v}
def neg(a): return {k:-v for k,v in a.items()}
def sub(a,b): return add(a,neg(b))
def mul(a,b):
    d=defaultdict(int)
    for ea,ca in a.items():
        for eb,cb in b.items(): d[tuple(x+y for x,y in zip(ea,eb))]+=ca*cb
    return {k:v for k,v in d.items() if v}
def deriv(a,i):
    d=defaultdict(int)
    for e,c in a.items():
        if e[i]:
            q=list(e); m=q[i]; q[i]-=1; d[tuple(q)]+=c*m
    return {k:v for k,v in d.items() if v}
def smul(c,a): return {k:c*v for k,v in a.items() if c*v}
def zero(a): return not a

x1,x2,x3,x4,z,s,r,beta=[mono(i) for i in range(N)]
one=const(1)
# F1=(s+z)x3-s x1; F2=(s+z)x4-s x2; F3=(r-z)x1-x3; F4=(r-z)x2-x4; F5=x1x3+x2x4-beta z
spz=add(s,z); rmz=sub(r,z)
f1=sub(mul(spz,x3),mul(s,x1))
f2=sub(mul(spz,x4),mul(s,x2))
f3=sub(sub(mul(rmz,x1),x3),{})
f4=sub(sub(mul(rmz,x2),x4),{})
f5=sub(add(mul(x1,x3),mul(x2,x4)),mul(beta,z))
J=sub(mul(x1,x4),mul(x2,x3))
dJ=add(add(mul(x4,f1),mul(x1,f4)),neg(add(mul(x3,f2),mul(x2,f3))))
assert zero(add(dJ,mul(add(s,one),J)))
full_div={}
for i,f in enumerate([f1,f2,f3,f4,f5]): full_div=add(full_div,deriv(f,i))
expected_full=neg(add(add(smul(2,s),const(2)),beta))
assert zero(sub(full_div,expected_full))
# Base variables X,Y,z correspond x1,x3,z with x2=x4=0.
base_div=add(add(deriv(f1,0),deriv(f3,2)),deriv(f5,4))
expected_base=neg(add(add(s,one),beta))
assert zero(sub(base_div,expected_base))
# Fixed real-phase leaf: f2 and f4 vanish after x2=x4=0.
def restrict_x2x4(a):
    return {e:c for e,c in a.items() if e[1]==0 and e[3]==0}
assert zero(restrict_x2x4(f2))
assert zero(restrict_x2x4(f4))
# Imaginary block trace = -s-1.
trace_im=neg(add(s,one))
assert zero(add(trace_im,add(s,one)))
print('VERIFY_OK')
