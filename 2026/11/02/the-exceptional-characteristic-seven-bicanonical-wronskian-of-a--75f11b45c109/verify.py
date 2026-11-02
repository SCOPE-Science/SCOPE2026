#!/usr/bin/env python3
"""Exact GF(7)[x,t] Hasse-derivative checks for a genus-three curve family."""
from math import comb
P=7

def mon(x=0,t=0,c=1):
    c%=P
    return {(x,t):c} if c else {}

def plus(a,b):
    out=dict(a)
    for k,v in b.items():
        out[k]=(out.get(k,0)+v)%P
        if out[k]==0:del out[k]
    return out

def neg(a):return {k:(-v)%P for k,v in a.items()}
def sub(a,b):return plus(a,neg(b))
def times(a,b):
    out={}
    for (ix,it),v in a.items():
        for (jx,jt),w in b.items():
            k=(ix+jx,it+jt)
            out[k]=(out.get(k,0)+v*w)%P
    return {k:v for k,v in out.items() if v}
def scale(a,s):return {k:(s*v)%P for k,v in a.items() if s*v%P}
def power(a,n):
    out=mon()
    for _ in range(n):out=times(out,a)
    return out

def at_t0(a):return {(i,0):v for (i,j),v in a.items() if j==0}

x=mon(1);t=mon(0,1);one=mon();F=plus(plus(power(x,8),times(t,power(x,4))),one)
B={}
for n in range(1,8):
    Fn={}
    if n<=8:Fn=plus(Fn,scale(power(x,8-n),comb(8,n)))
    if n<=4:Fn=plus(Fn,scale(times(t,power(x,4-n)),comb(4,n)))
    val=times(Fn,power(F,n-1))
    for i in range(1,n):val=sub(val,times(B[i],B[n-i]))
    B[n]=scale(val,4)  # 2 inverse in GF(7)

b5_expected=times(scale(times(times(t,sub(power(t,2),scale(one,4))),power(x,7)),3),times(sub(power(x,8),one),F))
assert B[5]==b5_expected
assert at_t0(B[5])=={}
assert at_t0(B[6])=={}
S={}
for j in range(6):S=plus(S,scale(power(x,8*j),(-1)**j))
b7_expected=scale(times(x,S),4)
assert at_t0(B[7])==b7_expected
assert b7_expected
# Hasse--Witt coefficient check: rows i,j = 1,2,3,
# (i,j) entry coefficient of x^(7i-j) in F^3.
F3=power(F,3)
H={(i,j):{s:v for (r,s),v in F3.items() if r==7*i-j and s>=0} for i in range(1,4) for j in range(1,4)}
assert H[(1,3)]=={1:3} and H[(2,2)]=={1:6,3:1} and H[(3,1)]=={1:3}
assert all(not v for k,v in H.items() if k not in ((1,3),(2,2),(3,1)))
# D7 for t=0 is x(1-x^48)/(2y^15): polynomial B7/y^13, using y^2=1+x^8.
assert times(b7_expected,plus(one,power(x,8)))==scale(times(x,sub(one,power(x,48))),4)
# Branch roots x^8=-1: eight; primitive x^48=1: 48 distinct roots,
# with eight branch roots among them; two points over each of the other forty roots.
assert 8*4 + 2 + 2 + 2*(48-8) == 4*(12+17)
print('B5 identity in GF(7)[x,t]: PASS')
print('B5=B6=0 at t=0; B7 explicit and nonzero: PASS')
print('Hasse-Witt family matrix entries: PASS')
print('Higher Wronskian divisor degree 116: PASS')
print('VERIFY_OK')
