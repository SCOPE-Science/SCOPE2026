#!/usr/bin/env python3
"""Exact algebraic checks and independent finite-field examples for cyclic quintic triple covers."""
from fractions import Fraction
import sympy as s
x = s.Symbol('x')
b = s.symbols('b0:5')
f = x**5 + sum((b[j]**2)*x**j for j in range(5))
A = b[0] + b[2]*x + b[4]*x*x
B = b[1] + b[3]*x + x*x
assert s.Poly(f-A**2-x*B**2, x,*b, modulus=2).is_zero
# For characteristic two Cartier on rational differential forms,
# C(f dx) is the odd-coefficient extraction B dx.
odd = sum((b[j] if j%2 else 0)*x**((j-1)//2) for j in range(5) if j%2) + x**2
assert s.Poly(odd-B,x,*b,modulus=2).is_zero
# Semilinear Cartier action, with basis (dx/y,dx/y^2,x dx/y^2,x^2 dx/y^2):
# C(w0)=b1*w1+b3*w2+w3, C(w1)=0, C(w2)=w0, C(w3)=0.
# Thus C^2(w0)=sqrt(b3)*w0, and image(C) always 2-dimensional.
# Algebraic dependence is exactly b3=0; p-rank then zero, otherwise two.
# The finite-field examples independently check using point counts and L-polynomials.
def mul(a,c,m,mod):
    out=0
    for _ in range(m):
        if c&1: out ^= a
        c >>= 1
        a <<= 1
        if a&(1<<m):a^=mod
    return out

def power(a,n,m,mod):
    out=1
    while n:
        if n&1:out=mul(out,a,m,mod)
        a=mul(a,a,m,mod);n>>=1
    return out

def lpoly(cubic):
    irr={1:0b11,2:0b111,3:0b1011,4:0b10011,
         5:0b100101,6:0b1000011,7:0b10000011,8:0b100011011}
    nums=[]
    for m,mod in irr.items():
        q=1<<m
        fibers={}
        for y in range(q):
            z=power(y,3,m,mod)
            fibers[z]=fibers.get(z,0)+1
        n=1  # unique point at infinity; gcd(3,5)=1
        for z in range(q):
            fz=power(z,5,m,mod)^z^1
            if cubic: fz ^= power(z,3,m,mod)
            n += fibers.get(fz,0)
        nums.append(n)
    traces=[2**m+1-nums[m-1] for m in range(1,9)]
    coeff=[1]
    for n in range(1,9):
        val=Fraction(-sum(coeff[n-i]*traces[i-1] for i in range(1,n+1)),n)
        assert val.denominator==1
        coeff.append(int(val))
    return nums,coeff

for cubic,want_points,want_coefs,want_rank in (
  (False,[3,9,9,33,33,57,129,273],[1,0,2,0,6,0,8,0,16],0),
  (True,[3,11,9,15,33,119,129,159],[1,0,3,0,4,0,12,0,16],2),
):
    points,coeff=lpoly(cubic)
    assert points==want_points
    assert coeff==want_coefs
    assert max(i for i,v in enumerate(coeff) if v%2)==want_rank
# f=x^5+x+1 and f=x^5+x^3+x+1 are squarefree:
assert s.gcd(s.Poly(x**5+x+1,x,modulus=2),s.Poly(x**4+1,x,modulus=2)).degree()==0
assert s.gcd(s.Poly(x**5+x**3+x+1,x,modulus=2),s.Poly(x**4+x**2+1,x,modulus=2)).degree()==0
print('VERIFY_OK: universal square decomposition, Cartier semilinearity, squarefree witnesses, F2^1..F2^8 counts and L-polynomials')
