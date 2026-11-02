#!/usr/bin/env python3
"""Exact arithmetic check for hard-core crown precision theorem.
All calculations use rational arithmetic and finite integer polynomial arithmetic.
The mathematical sign proof is stated separately in RESULT.md.
"""
from fractions import Fraction
from itertools import product

CHECKS=0
def ck(x,msg='assertion'):
    global CHECKS
    CHECKS+=1
    if not x: raise AssertionError(msg)

def trim(p):
    while len(p)>1 and not p[-1]:p.pop()
    return p

def add(a,b):
    return trim([(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))])

def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return trim(c)

def scale(a,k):return trim([k*v for v in a])
def sub(a,b):return add(a,scale(b,-1))
def powp(a,n):
    r=[1]
    for _ in range(n):r=mul(r,a)
    return r

def inverse(A):
    n=len(A);m=[[Fraction(x) for x in row]+[Fraction(i==j) for j in range(n)] for i,row in enumerate(A)]
    for k in range(n):
        pos=next(i for i in range(k,n) if m[i][k]);m[k],m[pos]=m[pos],m[k]
        q=m[k][k];m[k]=[v/q for v in m[k]]
        for i in range(n):
            if i==k:continue
            c=m[i][k]
            if c:m[i]=[v-c*w for v,w in zip(m[i],m[k])]
    return [row[n:] for row in m]

# Factorizations of E_n, where sign of Q_(a_i,b_i) = sign E_n.
Ps={
  3:[-1,-3],
  4:[-3,-18,-8,4,1],
  5:[-24,28,124,117,49,11,1],
  6:[20,80,520,1400,1945,1640,921,356,91,14,1],
}
x=[0,1];t=[1,1]
for n in range(2,7):
    h=powp(t,n-2)
    z=add(sub(scale(mul(powp(t,2),h),2),[1]),scale(powp(x,2),n))
    r=add(mul(t,h),x)
    k=sub(mul(add(mul(h,add([1],scale(x,n))),scale(x,2)),z),scale(mul(x,powp(r,2)),2*n))
    j=sub(mul(add(mul(h,add([1],scale(x,n-1))),scale(x,2)),z),scale(mul(x,powp(r,2)),2*(n-1)))
    E=sub(mul(mul(h,add([1],scale(x,n))),j),mul(mul(add([1],scale(x,n-1)),add(h,scale(x,2))),k))
    expected=([0] if n==2 else mul(scale(powp(x,5 if n in (3,4,6) else 6),-2 if n==3 else 2),([1,3] if n==3 else Ps[n])))
    # At n=3, E=-2*x^5*(3*x+1); compare with that positive factor convention.
    ck(E==expected,('polynomial identity',n,E,expected))
    ck(z[0]==1,('partition function constant',n))

# Independent enumeration over all 2^(2n) binary assignments.
for n in range(2,7):
  for lam in (Fraction(1,5),Fraction(1,2),Fraction(1),Fraction(3),Fraction(10)):
    v=2*n;Z=Fraction(0);first=[Fraction(0)]*v;second=[[Fraction(0)]*v for _ in range(v)]
    for mask in range(1<<(2*n)):
      if any((mask>>i&1) and (mask>>(n+j)&1) for i in range(n) for j in range(n) if i!=j):continue
      w=lam**mask.bit_count();Z+=w
      inds=[i for i in range(v) if mask>>i&1]
      for i in inds:
        first[i]+=w
        for j in inds:second[i][j]+=w
    t=1+lam
    expected_z=2*t**n-1+n*lam**2
    ck(Z==expected_z,('Z',n,lam))
    p=(lam*t**(n-1)+lam**2)/Z
    u=lam**2*t**(n-2)/Z
    vv=lam**2/Z
    for i in range(v):
      ck(first[i]/Z==p,('mean',n,lam,i))
      for j in range(v):
        exp=(p if i==j else u if (i<n)==(j<n) else vv if (i-j)%n==0 else Fraction(0))
        ck(second[i][j]/Z==exp,('second',n,lam,i,j))
    C=[[second[i][j]/Z-(first[i]*first[j])/(Z*Z) for j in range(v)] for i in range(v)]
    Q=inverse(C)
    for i in range(v):
      for j in range(v):
        ck(sum(Q[i][k]*C[k][j] for k in range(v))==int(i==j),('matrix inverse',n,lam,i,j))
    h=t**(n-2)
    K=(h*(1+n*lam)+2*lam)*Z -2*n*lam*(t*h+lam)**2
    J=(h*(1+(n-1)*lam)+2*lam)*Z -2*(n-1)*lam*(t*h+lam)**2
    E=h*(1+n*lam)*J-(h+2*lam)*(1+(n-1)*lam)*K
    ck(K>0 and Z>0 and h>0,('denominator',n,lam))
    derived=Z*E/(2*lam*h*(1+n*lam)*(h+2*lam)*K)
    ck(Q[0][n]==derived,('precision formula',n,lam))
    cov=vv-p*p
    if n>=3:ck(cov<0,('matched covariance',n,lam))
    ck((Q[0][n]>0)==(E>0),('sign precision',n,lam))
    for i in range(n):ck(Q[i][n+i]==Q[0][n],('matched symmetry',n,lam,i))
print('PASS:',CHECKS,'exact finite checks (symbolic polynomial identity plus exhaustive binary state sums)')
