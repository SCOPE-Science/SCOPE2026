#!/usr/bin/env python3
"""Reproduce the two-marker contiguous minimal-absent-word classification.
Python standard library only. Run: python maw_two_markers_checker.py
"""
from itertools import product
import random

def predicted(a,b,c):
    M=max(a,b,c)
    K=max(b,min(a,c))
    A={'0'*(M+1)}
    A.update('1'+'0'*k+'1' for k in range(K+1) if k!=b)
    if c>max(a,b):A.add('0'*(max(a,b)+1)+'1')
    if a>max(b,c):A.add('1'+'0'*(max(b,c)+1))
    if a>b and c>b:A.add('0'*(b+1)+'1'+'0'*(b+1))
    if a<b and c<b:A.add('0'*(a+1)+'1'+'0'*(c+1))
    if a<b<=c:A.add('0'*(a+1)+'1'+'0'*b+'1')
    if c<b<=a:A.add('1'+'0'*b+'1'+'0'*(c+1))
    if a>=b and c>=b:A.add('1'+'0'*b+'1'+'0'*b+'1')
    return A

def independent_factors(w):
    return {w[i:j] for i in range(len(w)+1) for j in range(i,len(w)+1)}

def independent_maws(w):
    F=independent_factors(w)
    candidate={'0','1'}
    for f in F:
        if f:
            candidate.update(ch+f for ch in '01')
    return {s for s in candidate if s not in F and (len(s)==1 or (s[:-1] in F and s[1:] in F))}

def formula_count(a,b,c):
    m=max(a,b,c)
    K=max(b,min(a,c))
    return (1+K + (c>max(a,b))+(a>max(b,c))
            +((a>b and c>b) or (a<b and c<b))
            +(a>=b and c>=b)+(a<b<=c)+(c<b<=a))

def gen_coeff(s):
    return sum(formula_count(a,b,s-a-b) for a in range(s+1) for b in range(s-a+1))

def generating_coefficient_direct(s):
    # Derived rational GF G(z)=(2+5z+2z^2+2z^3-4z^4)/[(1-z)^4(1+z)(1+z+z^2)].
    # Multiply by (1-z)^4(1+z)(1+z+z^2)=(1-z)^3(1-z^2)(1-z^3)/(1-z)?
    from math import comb
    def inv_1minus4(m):return comb(m+3,3) if m>=0 else 0
    # 1/[(1-z)^4(1+z)(1+z+z^2)] = 1/[(1-z)^2(1-z^2)(1-z^3)]
    def base(n):
        if n<0:return 0
        return sum(n-2*j-3*k+1 for j in range(n//2+1) for k in range((n-2*j)//3+1))
    return 2*base(s)+5*base(s-1)+2*base(s-2)+2*base(s-3)-4*base(s-4)

def main():
    tested=0
    for a,b,c in product(range(11),repeat=3):
        w='0'*a+'1'+'0'*b+'1'+'0'*c
        actual=independent_maws(w)
        predicted_set=predicted(a,b,c)
        assert actual==predicted_set,(a,b,c, actual-predicted_set,predicted_set-actual)
        assert len(actual)==formula_count(a,b,c),(a,b,c)
        tested+=1
    rng=random.Random(20261023)
    for _ in range(200):
        a,b,c=(rng.randrange(0,160) for i in range(3))
        w='0'*a+'1'+'0'*b+'1'+'0'*c
        assert independent_maws(w)==predicted(a,b,c),(a,b,c)
        tested+=1
    for s in range(0,32):
        assert gen_coeff(s)==generating_coefficient_direct(s),(s,gen_coeff(s),generating_coefficient_direct(s))
    for n in range(6,90):
        best=[];mx=0
        for a in range(n-1):
            for b in range(n-1-a):
                c=n-2-a-b
                k=formula_count(a,b,c)
                if k>mx:mx=k;best=[(a,b,c)]
                elif k==mx:best.append((a,b,c))
        assert mx==n and best==[(0,n-2,0)],(n,mx,best)
    print(f'PASS: {tested} independent MAW-set comparisons, 32 GF coefficients, exact maxima for n=6..89')

if __name__=='__main__':main()
