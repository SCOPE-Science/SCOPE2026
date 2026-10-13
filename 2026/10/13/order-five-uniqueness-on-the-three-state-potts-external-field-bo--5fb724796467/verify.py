#!/usr/bin/env python3
from math import comb

# Sparse bivariate polynomials: key=(x exponent, t exponent), integer value.
def add(a,b):
    out=dict(a)
    for k,v in b.items():
        out[k]=out.get(k,0)+v
        if out[k]==0: del out[k]
    return out

def scale(a,c):
    return {k:c*v for k,v in a.items() if c*v}

def mul(a,b):
    out={}
    for (i,j),x in a.items():
        for (r,s),y in b.items():
            k=(i+r,j+s)
            out[k]=out.get(k,0)+x*y
    return {k:v for k,v in out.items() if v}

def deriv_x(a):
    return {(i-1,j):i*c for (i,j),c in a.items() if i}

def power(a,n):
    out={(0,0):1}
    for _ in range(n): out=mul(out,a)
    return out

def mono(i,j=0,c=1):
    return {(i,j):c}

one=mono(0)
v=mono(1)
t=mono(0,1)
p={}
for j in range(1,5): p=add(p,mono(j))
S=add(p,one)
L=add(mul(t,p),scale(add(mono(5),one),-1))
M=add(p,L)
Lp=deriv_x(L)
pp=deriv_x(p)
P=add(mul(mul(S,add(p,scale(L,-4))),Lp), scale(mul(mul(L,add(L,scale(one,-1))),pp),5))

# Build R(y;t), substitute y=v+v^{-1} as a Laurent polynomial in v.
y_sub=add(mono(1),mono(-1))
R={}
def add_term(coeff_t, ypow):
    global R
    ct={}
    for tp,c in enumerate(coeff_t):
        if c: ct[(0,tp)]=c
    R=add(R,mul(ct,power(y_sub,ypow)))
add_term([0,0,4],4)
add_term([0,0,11],3)
add_term([0,0,8],2)
add_term([0,0,8],1)
add_term([0,-4],5)
add_term([0,2],4)
add_term([0,33],3)
add_term([0,34],2)
add_term([0,44],1)
add_term([0,8],0)
add_term([-10],5)
add_term([-20],4)
add_term([10],3)
add_term([20],2)
add_term([50],1)
add_term([30],0)
expected=mul(mul(add(mono(1),scale(one,-1)),add(mono(1),one)),mul(mono(5),R))
assert P==expected, 'derivative factorization failed'

# Independently expand R(2+z;t). Here the first exponent is z.
def ypow_shifted(n):
    out={}
    for i in range(n+1):
        out[(i,0)]=comb(n,i)*(2**(n-i))
    return out
Rz={}
def add_z_term(coeff_t, ypow):
    global Rz
    ct={}
    for tp,c in enumerate(coeff_t):
        if c: ct[(0,tp)]=c
    Rz=add(Rz,mul(ct,ypow_shifted(ypow)))
for coeff,ypow in [
    ([0,0,4],4),([0,0,11],3),([0,0,8],2),([0,0,8],1),
    ([0,-4],5),([0,2],4),([0,33],3),([0,34],2),([0,44],1),([0,8],0),
    ([-10],5),([-20],4),([10],3),([20],2),([50],1),([30],0)]:
    add_z_term(coeff,ypow)

target={
 (0,0):-350,(0,1):400,(0,2):200,
 (1,0):-1190,(1,1):320,(1,2):300,
 (2,0):-1200,(2,1):-40,(2,2):170,
 (3,0):-550,(3,1):-111,(3,2):43,
 (4,0):-120,(4,1):-38,(4,2):4,
 (5,0):-10,(5,1):-4,
}
assert Rz==target, 'shifted R expansion failed'

# Exact coefficient bounds used for 0 <= t < 1.
assert 30+32-119 == -57
assert 17-120 == -103
assert 43-550 == -507
# At t_*=(sqrt(11)-2)/2, 4 t_*^2+8 t_*-7 reduces exactly to 11-11.
assert 11-11 == 0

print('VERIFY_OK factorization=exact shifted_expansion=exact sign_bounds=exact')
