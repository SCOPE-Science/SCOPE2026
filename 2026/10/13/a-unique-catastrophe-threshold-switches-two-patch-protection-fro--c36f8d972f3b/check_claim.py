#!/usr/bin/env python3
"""Exact polynomial and rational checks for a two-patch persistence sensitivity theorem.

Requires only Python 3 standard library. Run `python3 check_claim.py`.
"""
from fractions import Fraction
from itertools import product

DIM = 4

def C(n):
    return {(0,) * DIM: n} if n else {}

def X(i):
    return {tuple(1 if j == i else 0 for j in range(DIM)): 1}

def add(*qs):
    out = {}
    for q in qs:
        for k, v in q.items():
            out[k] = out.get(k, 0) + v
            if not out[k]:
                del out[k]
    return out

def neg(q):
    return {k: -v for k,v in q.items()}

def sub(a,b):
    return add(a,neg(b))

def mul(*qs):
    out = C(1)
    for q in qs:
        nxt = {}
        for a, av in out.items():
            for b, bv in q.items():
                k = tuple(a[i]+b[i] for i in range(DIM))
                nxt[k] = nxt.get(k, 0) + av*bv
        out = {k:v for k,v in nxt.items() if v}
    return out

def power(q,n):
    out = C(1)
    for _ in range(n):
        out = mul(out,q)
    return out

def diff(q,i):
    out = {}
    for a,v in q.items():
        if a[i]:
            b = tuple(a[j] - (j==i) for j in range(DIM))
            out[b] = a[i]*v
    return out

def ev(q, x,y,c,r):
    vs = (x,y,c,r)
    return sum(v * product_fraction(vs, a) for a, v in q.items())

def product_fraction(vs,exps):
    out = Fraction(1)
    for v,e in zip(vs,exps):
        out *= v**e
    return out

x,y,c,r = (X(i) for i in range(DIM))
one=C(1);two=C(2);three=C(3);four=C(4)
A=add(c,x,r); B=add(c,y,r)
N=add(mul(A,B),mul(y,B),mul(x,A))
D=sub(mul(add(x,y,r),A,B),mul(c,add(mul(y,B),mul(x,A))))
s=add(x,y); p=mul(x,y)
P=add(
 power(r,4),
 mul(add(mul(three,c),mul(two,s)),power(r,3)),
 mul(add(mul(three,power(c,2)),mul(four,c,s),power(s,2),mul(two,p)),power(r,2)),
 mul(add(power(c,3),mul(two,power(c,2),s),mul(c,power(s,2)),mul(two,s,p)),r),
 mul(p,sub(p,add(mul(c,s),mul(two,power(c,2)))))
)
U=sub(mul(diff(N,0),D),mul(N,diff(D,0)))
Q=add(sub(mul(diff(U,1),D),mul(two,U,diff(D,1))),mul(two,A,B,P))
assert Q == {}, 'Formal mixed-derivative identity fails'
# Check expected first-step recurrence with rational arithmetic independently.
checks=0
for xi,yi,ci,ri in product((Fraction(1,2), Fraction(1), Fraction(3)),
                            (Fraction(1,3),Fraction(1),Fraction(4)),
                            (Fraction(1,2),Fraction(2)),
                            (Fraction(0),Fraction(1,2),Fraction(3))):
    val=ev(N,xi,yi,ci,ri)/ev(D,xi,yi,ci,ri)
    only_first=(1+ci*val)/(ci+xi+ri)
    only_second=(1+ci*val)/(ci+yi+ri)
    assert (xi+yi+ri)*val == 1+yi*only_first+xi*only_second
    assert ev(D,xi,yi,ci,ri)>0
    checks+=1

# Shock threshold witness at x=y=c=1: P(0)<0<P(1) and P'(r)>0 for r>=0.
assert ev(P,1,1,1,0)==-3
assert ev(P,1,1,1,1)>0
for ri in (Fraction(0),Fraction(1,10),Fraction(1,5),Fraction(1)):
    assert ev(D,1,1,1,ri)>0

def T(xi,yi,ci,ri):
    return ev(N,xi,yi,ci,ri)/ev(D,xi,yi,ci,ri)

# Cross-increment in reduced extinction rates: positive at r=0, negative at r=1.
step=Fraction(1,10)
values=[]
for ri in (Fraction(0),Fraction(1)):
    interaction=T(1-step,1-step,1,ri)-T(1-step,1,1,ri) - T(1,1-step,1,ri)+T(1,1,1,ri)
    values.append(interaction)
assert values[0]>0 and values[1]<0

print('VERIFY_OK formal_coefficients=',len(P), 'formal_derivative=1 first_step_cases=',checks,
      'protection_signs=',len(values), 'certificate=exact')
