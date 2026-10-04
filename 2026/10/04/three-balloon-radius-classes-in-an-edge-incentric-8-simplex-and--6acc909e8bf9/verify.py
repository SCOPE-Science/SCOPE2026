#!/usr/bin/env python3
from fractions import Fraction as F
from decimal import Decimal, getcontext

# Univariate polynomials, coefficient list low-to-high, over Q.
def trim(p):
    p=list(p)
    while len(p)>1 and p[-1]==0: p.pop()
    return p
def add(a,b):
    n=max(len(a),len(b)); r=[F(0) for _ in range(n)]
    for i,x in enumerate(a): r[i]+=x
    for i,x in enumerate(b): r[i]+=x
    return trim(r)
def neg(a): return [-x for x in a]
def sub(a,b): return add(a,neg(b))
def mul(a,b):
    r=[F(0) for _ in range(len(a)+len(b)-1)]
    for i,x in enumerate(a):
        for j,y in enumerate(b): r[i+j]+=x*y
    return trim(r)
def scale(a,s): return trim([x*s for x in a])
def powp(a,n):
    r=[F(1)]; q=a[:]
    while n:
        if n&1: r=mul(r,q)
        q=mul(q,q); n//=2
    return r
def evalp(p,x):
    y=F(0)
    for a in reversed(p): y=y*x+a
    return y
def divrem(a,b):
    a=trim(a); b=trim(b); q=[F(0)]*max(1,len(a)-len(b)+1)
    while len(a)>=len(b) and any(a):
        k=len(a)-len(b); t=a[-1]/b[-1]; q[k]+=t
        a=sub(a,[F(0)]*k+scale(b,t))
    return trim(q),trim(a)

def C(n): return [F(n)]
B=[F(0),F(1)]
P=[F(4875),F(-18250),F(-5901),F(816),F(136)]
Cnum=[F(332475),F(692955),F(-47192),F(-10744)]
c=scale(Cnum,F(1,372560))

# H1 and H2 after c=c(b).
H1=add(add(add(add(add(add(neg(mul(powp(B,2),c)),neg(powp(B,2))),scale(mul(B,powp(c,2)),3)),scale(mul(B,c),4)),scale(B,-5)),scale(powp(c,2),3)),scale(c,-5))
H2=C(0)
terms=[(-9,mul(powp(B,3),c)),(-9,powp(B,3)),(23,mul(powp(B,2),powp(c,2))),(20,mul(powp(B,2),c)),(-1,powp(B,2)),(-5,mul(B,powp(c,3))),(28,mul(B,powp(c,2))),(4,mul(B,c)),(-5,B),(-5,powp(c,3)),(3,powp(c,2)),(-5,c)]
for k,p in terms: H2=add(H2,scale(p,k))
A=[F(-59018575),F(-174872335),F(9637368),F(2546328)]
Bpoly=[F(-11936394528025),F(-53690303071570),F(-48108539657769),F(479231239776),F(286367804048),F(74570064256),F(9119249344)]
assert H1 == scale(mul(P,A),F(1,138800953600))
assert H2 == scale(mul(P,Bpoly),F(1,10342336654643200))

# Isolating signs.
lo=F(247953648,10**9); hi=F(247953649,10**9)
plo=evalp(P,lo); phi=evalp(P,hi)
assert plo>0 and phi<0
# P' < 0 on (0,1) via 544+2448-18250 < 0 and -11802 b < 0.
assert 544+2448-18250 < 0

# M^2-7N, substitute c(b), reduce modulo P.
M=add(add(C(1),scale(B,3)),scale(c,5))
N=add(add(C(1),scale(powp(B,2),3)),scale(powp(c,2),5))
Q=sub(powp(M,2),scale(N,7))
_,Qrem=divrem(Q,P)
expected=scale([F(22782),F(-82717),F(-3584),F(1224)],F(1,18628))
assert Qrem==expected
assert F(7515,4)>0

# Auxiliary root s=-bc/(b+c+bc): verify e3=0 algebraically after clearing denominator.
den=add(add(B,c),mul(B,c))
snum=neg(mul(B,c))
# e3 for roots 1,b,c,s = bc + s(b+c+bc), cleared: bc*den+snum*(b+c+bc)=0.
e3clear=add(mul(mul(B,c),den),mul(snum,den))
assert all(x==0 for x in trim(e3clear))

# Coefficient conditions are exactly H1=H2=0 at a root of P, already certified by factorizations.
# Positivity bounds used in prose.
assert F(6,25) < lo < hi < F(1,4)
cminus1_lower= -F(10744,64)-F(47192,16)+F(692955*6,25)-F(40085)
assert cminus1_lower==F(4924273,40) and cminus1_lower>0
qnum_lower=-F(3584,16)-F(82717,4)+F(22782)
assert qnum_lower==F(7515,4) and qnum_lower>0

# Decimal diagnostic bisection and c value.
getcontext().prec=50
def Pd(x):
    return Decimal(136)*x**4+Decimal(816)*x**3-Decimal(5901)*x**2-Decimal(18250)*x+Decimal(4875)
a=Decimal(lo.numerator)/Decimal(lo.denominator); z=Decimal(hi.numerator)/Decimal(hi.denominator)
for _ in range(140):
    m=(a+z)/2
    if Pd(m)>0: a=m
    else: z=m
bd=(a+z)/2
cd=(-Decimal(10744)*bd**3-Decimal(47192)*bd**2+Decimal(692955)*bd+Decimal(332475))/Decimal(372560)
print('VERIFY_OK')
print('b', bd)
print('c', cd)
print('P(lo)>0', plo>0, 'P(hi)<0', phi<0)
print('exact_factorizations', True)
print('exact_existence_remainder', True)
