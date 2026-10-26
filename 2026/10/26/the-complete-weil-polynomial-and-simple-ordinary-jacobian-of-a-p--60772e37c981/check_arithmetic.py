#!/usr/bin/env python3
"""Exact polynomial checks for a smooth plane-filling sextic over F_3."""
from math import gcd

N = [13, 21, 34, 73, 288, 708, 2253, 6529, 19681, 58236]
p = [0] + [3**m + 1 - N[m-1] for m in range(1,11)]
c = [1]
for k in range(1, 11):
    a = -sum(c[k-i]*p[i] for i in range(1, k+1))
    assert a % k == 0
    c.append(a//k)
c += [3**(10-k)*c[k] for k in range(9,-1,-1)]
assert c == [1,9,46,173,527,1377,3198,6775,13353,24841,44020,
             74523,120177,182925,259038,334611,384183,378351,
             301806,177147,59049]

def trim(a):
    a=list(a)
    while a and a[-1]==0:
        a.pop()
    return a

def add(a,b,p):
    r=[0]*max(len(a),len(b))
    for i in range(len(r)):
        r[i]=((a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0))%p
    return trim(r)

def sub(a,b,p):
    r=[0]*max(len(a),len(b))
    for i in range(len(r)):
        r[i]=((a[i] if i<len(a) else 0)-(b[i] if i<len(b) else 0))%p
    return trim(r)

def mul(a,b,p):
    if not a or not b: return []
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]=(c[i+j]+x*y)%p
    return trim(c)

def divrem(a,b,p):
    assert b
    a=trim(a); db=len(b)-1; lead=pow(b[-1],-1,p)
    while len(a)>db:
        coef=a[-1]*lead%p; off=len(a)-len(b)
        for i,bi in enumerate(b):a[off+i]=(a[off+i]-coef*bi)%p
        a=trim(a)
    return a

def poly_gcd(a,b,p):
    while b: a,b=b,divrem(a,b,p)
    if not a:return []
    z=pow(a[-1],-1,p)
    return [(v*z)%p for v in a]

def powmod(a,n,f,p):
    ans=[1]
    while n:
        if n&1:ans=divrem(mul(ans,a,p),f,p)
        a=divrem(mul(a,a,p),f,p);n>>=1
    return ans

# Projective smoothness: on Z=1 the common gradient zeroes imply
# x=y^4(y+1) and G(y)=y^16(y+1)^5-1=0.
Y=[0,1]; ONE=[1]
yp1=[1,1]
# Construct actual polynomials without reducing high powers.
def monom(i,co=1):return [0]*i+[co]
G=sub(mul(monom(16),mul(mul(yp1,yp1,3),mul(mul(yp1,yp1,3),yp1,3),3),3),[1],3)
R=add(add(sub([],monom(18),3),monom(12),3),sub([],add(monom(4),monom(3),3),3),3)
# Recompute the affine equation after the gradient substitution, not just the gcd.
xsub=mul(monom(4),yp1,3)
x3=mul(mul(xsub,xsub,3),xsub,3)
x5=mul(mul(x3,xsub,3),xsub,3)
y3=monom(3)
y5=monom(5)
Fsub=add(add(add(add(add(mul(x5,Y,3),x5,3),sub([],mul(x3,y3,3),3),3),x3,3),xsub,3),sub(y5,y3,3),3)
assert divrem(Fsub,G,3)==R
assert poly_gcd(G,R,3)==[1]
print('SMOOTHNESS_GCD_OK')

# Irreducibility modulo 23: Rabin's exact criterion for degree 20.
f=[v%23 for v in c]
assert len(f)==21 and f[-1]
T=[0,1]
for proper in (4,10):
    b=powmod(T,23**proper,f,23)
    assert poly_gcd(f,sub(b,T,23),23)==[1]
assert powmod(T,23**20,f,23)==T
print('MOD23_IRREDUCIBLE_OK')
assert c[10]%3==1
print('ORDINARY_OK')
print('L_COEFFICIENTS=',c)
print('VERIFY_ARITHMETIC_OK')
