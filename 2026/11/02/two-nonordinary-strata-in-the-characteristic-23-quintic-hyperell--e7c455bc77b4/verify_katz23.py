#!/usr/bin/env python3
"""Exact independent finite-field checks for the genus-two pencil y²=x⁵+x+t in characteristic 23."""
from math import comb
p=23
# Expand f(x)^11 using a dictionary in exponents (x,t); independently compare with a multinomial sum.
P={(0,0):1}
for _ in range(11):
    Q={}
    for (a,b),c in P.items():
        for da,db in [(5,0),(1,0),(0,1)]:
            key=(a+da,b+db)
            Q[key]=(Q.get(key,0)+c)%p
    P=Q

def pol_at_x(n):
    return {b:c for (a,b),c in P.items() if a==n and c}

def indep_at_x(n):
    out={}
    for i in range(12):
        for j in range(12-i):
            k=11-i-j
            if 5*i+j==n:
                c=comb(11,i)*comb(11-i,j)%p
                out[k]=(out.get(k,0)+c)%p
    return {b:c for b,c in out.items() if c}

for n in (22,21,45,44):
    assert pol_at_x(n)==indep_at_x(n)
print('independent coefficients', {n: pol_at_x(n) for n in (22,21,45,44)})
assert pol_at_x(22)=={5:7,1:9}
assert pol_at_x(21)=={6:10,2:20}
assert pol_at_x(45)=={2:9}
assert pol_at_x(44)=={}
# Discriminant/resultant: smooth iff t^4 !=1. Determinant 2t^4(t^4+2).
# F_{23^2}=F_23[i], i^2=-1; 23=3 mod 4, so irreducible.
def add(a,b): return ((a[0]+b[0])%p,(a[1]+b[1])%p)
def mul(a,b): return ((a[0]*b[0]-a[1]*b[1])%p,(a[0]*b[1]+a[1]*b[0])%p)
def powe(a,n):
    r=(1,0)
    while n:
        if n&1:r=mul(r,a)
        a=mul(a,a);n//=2
    return r
zero=(0,0);one=(1,0)
roots=[];sing=[]
for a in range(p):
    for b in range(p):
        t=(a,b);t4=powe(t,4)
        if t4==(-2%p,0):roots.append(t)
        if t4==one:sing.append(t)
assert len(roots)==4 and len(sing)==4
assert len({powe(t,23) for t in roots})==4
for t in roots:
    t2=powe(t,2);t5=powe(t,5);t6=powe(t,6)
    a=add(mul((7,0),t5),mul((9,0),t))
    b=add(mul((10,0),t6),mul((20,0),t2))
    c=mul((9,0),t2)
    assert a==mul((18,0),t) and b==zero and c!=zero
    # M=[[a,0],[c,0]], transpose is Frobenius matrix H.
    # H^{(23)}H has trace a^(24) = 13 mod 23, hence one-dimensional stable image.
    assert powe(a,24)==(13,0)
# scaling t -> t/u by u^4=1 is transitive on four nonzero roots
u4=[z for x in range(p) for y in range(p) if (z:=(x,y))!=zero and powe(z,4)==one]
assert len(u4)==4
assert {mul(roots[0],z) for z in u4}==set(roots)
# F23-rational smooth fibers: only t=0 nonordinary; singular parameters are ±1.
assert set(s for s in sing if s[1]==0)=={(1,0),(22,0)}
assert all(y!=0 for x,y in roots)
print('F529 roots t^4=-2:',roots)
print('F529 singular parameters t^4=1:',sing)
print('VERIFY_OK')
