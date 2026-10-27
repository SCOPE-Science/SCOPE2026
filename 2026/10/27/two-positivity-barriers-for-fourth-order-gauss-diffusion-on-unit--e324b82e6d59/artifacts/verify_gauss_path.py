#!/usr/bin/env python3
"""Exact identities for two-stage Gauss heat stepping on unit-conductance paths.
Run with Python 3 and SymPy.  This validates finite identities, not the
all-order asymptotic argument in the accompanying mathematical proof.
"""
import sympy as S

x = S.symbols('x', nonnegative=True)

def laplacian(n):
    a=S.zeros(n)
    for i in range(n-1):
        a[i,i]+=1;a[i+1,i+1]+=1
        a[i,i+1]-=1;a[i+1,i]-=1
    return a

def step(n,t):
    a=laplacian(n)
    num=S.eye(n)-t*a/2+t*t*a*a/12
    den=S.eye(n)+t*a/2+t*t*a*a/12
    return num*den.inv()

r=(1-x/2+x*x/12)/(1+x/2+x*x/12)
ser=S.series(r,x,0,9).removeO().expand()
assert ser.coeff(x,6)==0 and ser.coeff(x,7)==S.Rational(1,1728)
assert all(ser.coeff(x,j)==(-1)**j/S.factorial(j) for j in range(5))

p2=step(2,x)
assert S.factor(p2[0,1]-3*x/(x*x+3*x+3))==0
p3=step(3,x)
assert S.factor(p3[0,1]-4*x/(3*x*x+6*x+4))==0
assert S.factor(p3[0,2]-8*x*x*(2*x+3)/((x*x+6*x+12)*(3*x*x+6*x+4)))==0
assert S.factor(p3[1,1]-(3*x*x-2*x+4)/(3*x*x+6*x+4))==0

p4=step(4,x)
denom=2*(x*x+3*x+3)*(x**4+12*x**3+54*x*x+72*x+36)
q4=x**4-6*x**3-60*x*x-108*x-72
nums={(0,0):2*x**6+9*x**5+60*x**4+180*x**3+396*x*x+432*x+216,
      (0,1):-3*x*q4,
      (0,2):9*x*x*(x**3+6*x*x+16*x+12),
      (0,3):3*x**3*(5*x*x+18*x+12),
      (1,1):2*x**6+21*x**5+96*x**4+144*x**3+180*x*x+216*x+216,
      (1,2):3*x*(x**4+6*x**3+24*x*x+72*x+72)}
for (i,j),f in nums.items():
    assert S.factor(p4[i,j]-f/denom)==0,(i,j)
assert S.factor(p4[1,3]-p4[0,2])==0
assert S.factor(p4[2,3]-p4[0,1])==0
assert S.factor(p4[2,2]-p4[1,1])==0
assert S.factor(p4[3,3]-p4[0,0])==0
assert q4.subs(x,0)<0 and q4.subs(x,12)>0
roots=S.polys.polytools.intervals(q4,eps=S.Rational(1,10**12))
assert len([z for z,_ in roots if z[0]>0])==1
positive_roots=[z for z,_ in roots if z[0]>0]
print('P4 unique positive threshold in',positive_roots[0])

p8=step(8,S.Integer(4))
D=61423369
N=S.Matrix([
[22767445,7237548,12586536,8978304,5124384,2634048,1318656,776448],
[7237548,28116433,3629316,8732616,6487968,3808992,2091840,1318656],
[12586536,3629316,24262513,1138980,7417224,5945760,3808992,2634048],
[8978304,8732616,1138980,22947121,596772,7417224,6487968,5124384],
[5124384,6487968,7417224,596772,22947121,1138980,8732616,8978304],
[2634048,3808992,5945760,7417224,1138980,24262513,3629316,12586536],
[1318656,2091840,3808992,6487968,8732616,3629316,28116433,7237548],
[776448,1318656,2634048,5124384,8978304,12586536,7237548,22767445]])
assert D*p8==N
assert min(N)==596772
assert all(sum(N[i,j] for j in range(8))==D for i in range(8))
for n in range(2,16):
    a=laplacian(n)
    J=S.ones(n,n)/n
    pseudo=(a+J).inv()-J
    asserted=S.Rational((n-1)*(2*n-7),6*n)
    assert pseudo[0,1]==asserted
print('P8(4) minimum',min(p8),'denominator',D)
print('Taylor sign and finite exact checks: PASS')
