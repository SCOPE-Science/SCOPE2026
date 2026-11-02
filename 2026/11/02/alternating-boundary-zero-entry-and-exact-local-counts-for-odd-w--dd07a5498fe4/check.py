"""Exact rational checks for the odd weighted Bergman boundary-crossing identity.
Run with Python 3 and no third-party packages. The proof is analytical; this
script tests its algebra and representative exact sign brackets.
"""
from fractions import Fraction as F
from math import comb

def add(a,b): return (a[0]+b[0], a[1]+b[1])
def mul(a,b): return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def cmul(c,a): return (c*a[0],c*a[1])
def power(a,n):
    r=(F(1),F(0))
    for _ in range(n): r=mul(r,a)
    return r

def A(j): return F(1,4*j+1)+F(2,4*j+2)+F(2,4*j+3)
def S_blocks(k): return sum(((-4)**j*A(j) for j in range(k)),F(0))
def S_binomial(m):
    # Im(1+it)^(m-1)/t integrated over t in (0,1)
    return sum((F((-1)**ell*comb(m-1,2*ell+1),2*ell+1)
                for ell in range(m//2)),F(0))

def numerator_imag_over_i(m,beta,r):
    # For z=ir, J_beta(z)/i is twice the imaginary part of
    # (1+ir)^m H_beta(ir), H_beta(z) = sum beta*(-z)^j C(m-1,j)/(j+beta).
    z=(F(0),r); H=(F(0),F(0))
    for j in range(m):
        coeff=F(comb(m-1,j)*(-1)**j)*beta/(F(j)+beta)
        H=add(H,cmul(coeff,power(z,j)))
    return 2*mul(power((F(1),r),m),H)[1]

checks=0
for k in range(1,13):
    m=4*k
    s1=S_blocks(k);s2=S_binomial(m)
    assert s1==s2,(k,s1,s2);checks+=1
    assert s1 != 0 and (s1>0)==(k%2==1);checks+=1
    # Independently compute beta-derivative of J_beta at z=i via h(i).
    h=(F(0),F(0))
    for j in range(1,m):
        h=add(h,cmul(F(comb(m-1,j)*(-1)**j,j),power((F(0),F(1)),j)))
    assert h[1]==-s1;checks+=1
    assert 2*s1/m == -2*h[1]/m;checks+=1
for j in range(1,20):
    assert 4*A(j+1)>A(j);checks+=1
assert 4*A(1)>A(0);checks+=1
assert S_blocks(1)==F(8,3);checks+=1
assert S_blocks(2)==F(-64,105);checks+=1
assert F(2,8)*S_blocks(2)==-F(16,105);checks+=1
for k in range(1,5):
    m=4*k; b=-F(1,100000)
    left=F(999,1000); middle=F(1); right=F(1001,1000)
    v0=numerator_imag_over_i(m,b,middle)
    vlo=numerator_imag_over_i(m,b,left)
    vhi=numerator_imag_over_i(m,b,right)
    if k%2: assert vlo*v0<0,(k, 'inward sign bracket')
    else: assert vhi*v0<0,(k,'outward sign bracket')
    checks+=1
print(f'PASS: {checks} exact rational assertions; k=1..12 derivative and sign; four exact root brackets.')
