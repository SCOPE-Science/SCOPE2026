#!/usr/bin/env python3
from fractions import Fraction
import math

# Polynomials are coefficient lists in ascending powers.
def trim(a):
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a

def add(a,b):
    n=max(len(a),len(b)); out=[Fraction(0) for _ in range(n)]
    for i,x in enumerate(a): out[i]+=x
    for i,x in enumerate(b): out[i]+=x
    return trim(out)

def scale(a,s): return trim([x*s for x in a])
def mul(a,b):
    out=[Fraction(0) for _ in range(len(a)+len(b)-1)]
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j]+=x*y
    return trim(out)

def power(a,n):
    r=[Fraction(1)]
    for _ in range(n): r=mul(r,a)
    return r

def shift(k,coef=1): return [Fraction(0)]*k+[Fraction(coef)]
def sub(a,b): return add(a,scale(b,Fraction(-1)))
def evalp(a,x):
    r=Fraction(0)
    for coef in reversed(a): r=r*x+coef
    return r

def deriv(a): return [a[i]*i for i in range(1,len(a))] or [Fraction(0)]
def divrem(a,b):
    a=trim(a[:]); b=trim(b[:])
    if len(a)<len(b): return [Fraction(0)],a
    q=[Fraction(0)]*(len(a)-len(b)+1)
    while len(a)>=len(b) and any(a):
        k=len(a)-len(b); t=a[-1]/b[-1]; q[k]=t
        a=sub(a,shift(k,0)) if False else a
        for j,v in enumerate(b): a[j+k]-=t*v
        trim(a)
    return trim(q),trim(a)
def negrem(a,b):
    return scale(divrem(a,b)[1],Fraction(-1))
def signs_at(seq,x):
    vals=[]
    for p in seq:
        v=evalp(p,x)
        if v>0: vals.append(1)
        elif v<0: vals.append(-1)
    return sum(vals[i]!=vals[i-1] for i in range(1,len(vals)))
def sturm_count(p,a,b):
    seq=[trim(p[:]),trim(deriv(p))]
    while not (len(seq[-1])==1 and seq[-1][0]==0):
        r=negrem(seq[-2],seq[-1])
        if len(r)==1 and r[0]==0: break
        seq.append(r)
    return signs_at(seq,a)-signs_at(seq,b)

C=shift(1)
P=add(scale(shift(5),-20),add(scale(shift(3),24),scale(shift(1),-5)))
Q=add(scale(shift(6),100),add(scale(shift(4),-120),add(scale(shift(2),30),[-1])))
P2=power(P,2); P3=power(P,3)
EY=[Fraction(0)]
for term in [scale(mul(shift(4),P),4),scale(mul(shift(3),P2),8),scale(shift(3),-4),scale(mul(shift(2),P),-3),scale(mul(shift(1),P2),-4),scale(shift(1),2),scale(P3,3),scale(P,-2)]: EY=add(EY,term)
EX=[Fraction(0)]
for term in [scale(shift(5),20),scale(mul(shift(4),P),16),scale(shift(3),-25),scale(mul(shift(2),P),-16),mul(shift(1),P2),scale(shift(1),6),scale(P,2)]: EX=add(EX,term)
cm1=add(C,[-1]); cp1=add(C,[1])
quart=add(scale(shift(4),60),add(scale(shift(2),-32),[3]))
facY=scale(mul(mul(mul(mul(C,power(cm1,2)),power(cp1,2)),quart),Q),-4)
facX=scale(mul(mul(mul(C,power(cm1,2)),power(cp1,2)),Q),4)
assert EY==facY
assert EX==facX

a=Fraction(93,100); b=Fraction(47,50)
assert evalp(Q,a)<0<evalp(Q,b)
assert sturm_count(Q,a,b)==1

# Numerical diagnostic bisection within the certified interval.
def qf(x): return 100*x**6-120*x**4+30*x**2-1
lo=float(a); hi=float(b)
for _ in range(200):
    mid=(lo+hi)/2
    if qf(mid)>0: hi=mid
    else: lo=mid
c=(lo+hi)/2
d=-20*c**5+24*c**3-5*c
x=3*math.acos(c)/math.pi
y=math.sqrt(3)*math.acos(d)/math.pi
assert 0<d<1
assert d+4*c**3-3*c>0
assert abs(x-0.3558473606263811208579681)<5e-15
assert abs(y-0.4255359610370576630888604)<5e-15
assert abs(500*d**6-600*d**4+186*d**2-5)<5e-12
print('VERIFY_OK')
print('c = %.16f' % c)
print('d = %.16f' % d)
print('x = %.16f' % x)
print('y = %.16f' % y)
