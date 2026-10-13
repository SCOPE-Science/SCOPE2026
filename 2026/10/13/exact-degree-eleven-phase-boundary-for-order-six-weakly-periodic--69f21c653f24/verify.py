#!/usr/bin/env python3
from fractions import Fraction as F
from math import gcd

# ascending coefficient lists
def trim(p):
    p=list(p)
    while len(p)>1 and p[-1]==0: p.pop()
    return p

def add(p,q):
    n=max(len(p),len(q)); r=[F(0)]*n
    for i in range(n): r[i]=(p[i] if i<len(p) else 0)+(q[i] if i<len(q) else 0)
    return trim(r)
def neg(p): return [-c for c in p]
def sub(p,q): return add(p,neg(q))
def mul(p,q):
    r=[F(0)]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q): r[i+j]+=a*b
    return trim(r)
def scale(p,c): return trim([c*x for x in p])
def power(p,n):
    r=[F(1)]; b=p
    while n:
        if n&1:r=mul(r,b)
        b=mul(b,b); n//=2
    return r
def deriv(p): return trim([F(i)*p[i] for i in range(1,len(p))] or [F(0)])
def divmod_poly(p,q):
    p=trim(p); q=trim(q); r=p[:]; out=[F(0)]*max(1,len(p)-len(q)+1)
    while len(r)>=len(q) and not (len(r)==1 and r[0]==0):
        d=len(r)-len(q); c=r[-1]/q[-1]; out[d]=c
        for i,b in enumerate(q): r[d+i]-=c*b
        r=trim(r)
    return trim(out),trim(r)
def evalp(p,x):
    y=F(0)
    for c in reversed(p): y=y*x+c
    return y
def sgn(v): return (v>0)-(v<0)
def sturm(p):
    s=[trim(p),deriv(p)]
    while not (len(s[-1])==1 and s[-1][0]==0):
        _,r=divmod_poly(s[-2],s[-1]); r=neg(r)
        if len(r)==1 and r[0]==0: break
        s.append(r)
    return s
def variations(signs):
    s=[x for x in signs if x]
    return sum(s[i]!=s[i-1] for i in range(1,len(s)))
def V_at(S,x): return variations([sgn(evalp(p,x)) for p in S])
def V_inf(S): return variations([sgn(p[-1]) for p in S])
def count_interval(p,lo,hi):
    S=sturm(p); return V_at(S,lo)-V_at(S,hi)
def count_to_inf(p,lo):
    S=sturm(p); return V_at(S,lo)-V_inf(S)

# J(x) and P(a), ascending
J=[-9,-18,72,30,-174,-60,120,62,-25,-26,0,4]
P=[-6912,0,-4032,2880,7579,3680,3278,-4996,-2817,160,384,256]

# Critical relation from G_x=0: a=N/D.
x=[F(0),F(1)]
N=add(add(scale(power(x,4),5),scale(power(x,2),-12)),[F(3)])
D=add(scale(power(x,3),4),scale(x,-6))

# Exact substitution identity D^2 G(x,N/D) = -J(x).
D2=power(D,2)
left=[F(0)]
# G=x^5-a x^4-4x^3+3a x^2+3x+a^2-a
left=add(left,mul(power(x,5),D2))
left=add(left,neg(mul(mul(N,D),power(x,4))))
left=add(left,scale(mul(power(x,3),D2),-4))
left=add(left,scale(mul(mul(N,D),power(x,2)),3))
left=add(left,scale(mul(x,D2),3))
left=add(left,power(N,2))
left=add(left,neg(mul(N,D)))
assert trim(left)==trim(neg(J))

# Exact elimination identity: D^11 P(N/D) is divisible by J.
num=[F(0)]
for i,ci in enumerate(P):
    term=mul(power(N,i), power(D,11-i))
    num=add(num,scale(term,ci))
_,rem=divmod_poly(num,J)
assert rem==[F(0)]

xi_lo=F(207717459,100000000)
xi_hi=F(207717460,100000000)
a_lo=F(1894515,1000000)
a_hi=F(1894516,1000000)
assert count_to_inf(J,F(2))==1
assert count_interval(J,xi_lo,xi_hi)==1
assert sgn(evalp(J,xi_lo))==-1 and sgn(evalp(J,xi_hi))==1
assert count_interval(P,a_lo,a_hi)==1
assert sgn(evalp(P,a_lo))==-1 and sgn(evalp(P,a_hi))==1

def amap(t):
    return (5*t**4-12*t**2+3)/(4*t**3-6*t)
# a'(x)=(10x^6-21x^4+18x^2+9)/(2x^2(2x^2-3)^2)>0 for x>2.
assert a_lo < amap(xi_lo) < amap(xi_hi) < a_hi
# positivity of derivative numerator for x>=2: set y=x^2>=4; q(y)=10y^3-21y^2+18y+9,
# q(4)>0 and q'(y)=30y^2-42y+18 has negative discriminant and positive leading coefficient.
assert 10*4**3-21*4**2+18*4+9>0
assert (-42)**2-4*30*18 < 0

# Irreducibility of P mod 41 (Rabin criterion; degree 11 is prime).
pmod=41
def mtrim(p):
    p=[int(c)%pmod for c in p]
    while len(p)>1 and p[-1]==0:p.pop()
    return p
def madd(p,q):
    n=max(len(p),len(q)); r=[0]*n
    for i in range(n):r[i]=((p[i] if i<len(p) else 0)+(q[i] if i<len(q) else 0))%pmod
    return mtrim(r)
def msub(p,q): return madd(p,[(-c)%pmod for c in q])
def mmul(p,q):
    r=[0]*(len(p)+len(q)-1)
    for i,a0 in enumerate(p):
        for j,b0 in enumerate(q):r[i+j]=(r[i+j]+a0*b0)%pmod
    return mtrim(r)
def mdivmod(p,q):
    r=mtrim(p); q=mtrim(q); out=[0]*max(1,len(r)-len(q)+1); inv=pow(q[-1],-1,pmod)
    while len(r)>=len(q) and not (len(r)==1 and r[0]==0):
        d=len(r)-len(q); c=r[-1]*inv%pmod; out[d]=c
        for i,b0 in enumerate(q):r[d+i]=(r[d+i]-c*b0)%pmod
        r=mtrim(r)
    return mtrim(out),r
def mmod(p,f): return mdivmod(p,f)[1]
def mpowmod(base,e,f):
    r=[1]; b=mmod(base,f)
    while e:
        if e&1:r=mmod(mmul(r,b),f)
        b=mmod(mmul(b,b),f);e//=2
    return r
def mgcd(a,b):
    a=mtrim(a);b=mtrim(b)
    while not (len(b)==1 and b[0]==0):
        _,r=mdivmod(a,b);a,b=b,r
    inv=pow(a[-1],-1,pmod);return [(c*inv)%pmod for c in a]
Pm=[int(c)%pmod for c in P]
X=[0,1]
h1=msub(mpowmod(X,pmod,Pm),X)
assert mgcd(Pm,h1)==[1]
hn=msub(mpowmod(X,pmod**11,Pm),X)
assert mmod(hn,Pm)==[0]
assert gcd(*[abs(int(c)) for c in P if c])==1

print('VERIFY_OK J_gt2=1 J_tight=1 P_tight=1 elimination=exact irreducible_mod41=1')
