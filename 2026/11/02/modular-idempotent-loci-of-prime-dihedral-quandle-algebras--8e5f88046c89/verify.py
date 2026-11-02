#!/usr/bin/env python3
"""Finite-field tests for the modular dihedral-quandle idempotent theorem."""
from itertools import product
from math import comb, lcm

PRIMES=(3,5,7,11,13,17,19,23,31)

def mul(a,b,p):
    c=[0]*p
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b):
                if i+j<p:
                    c[i+j]=(c[i+j]+x*y)%p
    return c

def sigma_matrix(a,p):
    a%=p
    y=[comb(a,k)%p if k<=a else 0 for k in range(p)]
    y[0]=0
    power=[1]+[0]*(p-1)
    matrix=[[0]*(p-1) for _ in range(p-1)]
    for j in range(p-1):
        power=mul(power,y,p)
        for i in range(1,p): matrix[i-1][j]=power[i]
    return matrix

def nullspace(matrix,p):
    m=len(matrix[0]); a=[row[:] for row in matrix]
    pivots=[];row=0
    for j in range(m):
        pivot=next((i for i in range(row,len(a)) if a[i][j]%p),None)
        if pivot is None:continue
        a[pivot],a[row]=a[row],a[pivot]
        inv=pow(a[row][j],-1,p)
        a[row]=[(v*inv)%p for v in a[row]]
        for i in range(len(a)):
            if i!=row and a[i][j]:
                c=a[i][j]
                a[i]=[(x-c*y)%p for x,y in zip(a[i],a[row])]
        pivots.append(j);row+=1
        if row==len(a):break
    out=[]
    for free in range(m):
        if free in pivots:continue
        v=[0]*m;v[free]=1
        for i,j in enumerate(pivots):v[j]=(-a[i][free])%p
        out.append(v)
    return out

def exponential(h,p):
    result=[1]+[0]*(p-1);power=result[:];inverse_factorial=1
    for j in range(1,p):
        power=mul(power,h,p)
        inverse_factorial=inverse_factorial*pow(j,-1,p)%p
        result=[(a+inverse_factorial*b)%p for a,b in zip(result,power)]
    return result

def t_to_x(t,p):
    result=[0]*p
    for j,c in enumerate(t):
        for i in range(j+1):
            result[i]=(result[i]+c*comb(j,i)*(-1)**(j-i))%p
    return result

def square_quandle(v,p):
    out=[0]*p
    for i,a in enumerate(v):
        if a:
            for j,b in enumerate(v):
                if b:out[(2*j-i)%p]=(out[(2*j-i)%p]+a*b)%p
    return out

def order_2(p):
    j=1
    while pow(2,j,p)!=1:j+=1
    return j

for p in PRIMES:
    a=sigma_matrix(p-1,p);b=sigma_matrix(2,p)
    matrix=[[(a[i][j]+b[i][j]-(i==j))%p for j in range(p-1)] for i in range(p-1)]
    kernel=nullspace(matrix,p)
    expected=(p-1)//lcm(2,order_2(p))
    assert len(kernel)==expected,(p,len(kernel),expected)
    if p in (17,31):
        for vector in kernel:
            f=t_to_x(exponential([0]+vector,p),p)
            assert square_quandle(f,p)==f
            assert sum(f)%p==1
            assert sum(x!=0 for x in f)>1
        print('NONBASIS_WITNESS',p, 'dimension',expected)
    print('LINEAR_KERNEL_OK',p,expected)

for p in (3,5):
    counts={0:0,1:0}
    for vector in product(range(p),repeat=p):
        if square_quandle(vector,p)==list(vector):
            assert sum(vector)%p in (0,1)
            counts[sum(vector)%p]+=1
    assert counts=={0:1,1:p},(p,counts)
    print('EXHAUSTIVE_OK',p,p**p,'idempotents',sum(counts.values()))
print('MODULAR_DIHEDRAL_IDEMPOTENT_OK')
