#!/usr/bin/env python3
"""Exact check of second-order anchored-path Green-function and leader placement theorem."""
from fractions import Fraction
from itertools import product
import sympy as sp

def F(l):
    assert l>=0
    return Fraction(l*(l+1)*(l*(l+1)+1),6)

def C(p):
    return Fraction(p*(p+1)*(2*p+1),6)

def g(l):
    return Fraction(2*l**3+l,3)

def closed(n,h,k,x):
    x=Fraction(x)
    base=F(k-1)+F(n-k)
    if k<=h:
        p=n-h; d=h-k+1
    else:
        p=h; d=k-h
    return base + 2*(x-1)*(p*p*(d-1)+C(p)) + (x-1)**2*p*p

def direct(n,h,k,x):
    x=Fraction(x)
    L=sp.zeros(n)
    for i in range(n-1):
        w=sp.Rational(x.denominator,x.numerator) if i==h-1 else sp.Integer(1)
        L[i,i]+=w;L[i+1,i+1]+=w;L[i,i+1]-=w;L[i+1,i]-=w
    I=[v for v in range(n) if v!=k-1]
    K=L.extract(I,I)
    A=K.inv()
    return Fraction(sp.trace(A*A))

def winners(n,h,x):
    v=[closed(n,h,k,x) for k in range(1,n+1)]
    m=min(v)
    return [i+1 for i,y in enumerate(v) if y==m]

def predicted(n,h,x):
    if h==n-h: return [h,h+1]
    if h>n-h:
        return [n+1-k for k in reversed(predicted(n,n-h,x))]
    def t(k): return 1+(g(n-k)-g(k))/(2*h*h)
    ans=[]
    for k in range(h+1,n+1):
        ok1=(k==h+1 or x<=t(k-1))
        ok2=(k==n or x>=t(k))
        if ok1 and ok2: ans.append(k)
    return ans

xs=[Fraction(1,31),Fraction(1,5),Fraction(1,2),Fraction(1),Fraction(7,5),Fraction(4),Fraction(40)]
count_matrix=0;count_winners=0;count_ties=0
for n in range(3,11):
    for h in range(1,n):
        for x in xs:
            for k in range(1,n+1):
                got=direct(n,h,k,x)
                want=closed(n,h,k,x)
                assert got==want,(n,h,k,x,got,want)
                count_matrix+=1
            got=winners(n,h,x)
            want=predicted(n,h,x)
            assert got==want,(n,h,x,got,want)
            count_winners+=1
for n in range(3,55):
    for h in range(1,n):
        ts = [1+(g(n-k)-g(k))/(2*h*h) for k in range(h+1,n)] if h<n-h else []
        for x in xs+[t for t in ts if t>0]:
            got=winners(n,h,x)
            want=predicted(n,h,x)
            assert got==want,(n,h,x,got,want)
            if len(got)>1: count_ties+=1
            count_winners+=1
print('exact_grounded_laplacian_matrix_checks:', count_matrix)
print('exact_global_leader_classification_checks:',count_winners)
print('tie_cases:',count_ties)
print('example n=12 h=4:')
for x in [Fraction(1,5),Fraction(1),Fraction(5),Fraction(10),Fraction(100)]:
 print(f'  resistance={x}, optimal_leaders={winners(12,4,x)}, minimum_J={min(closed(12,4,k,x) for k in range(1,13))}')
print('PASS')
