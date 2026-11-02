#!/usr/bin/env python3
"""Independent finite exact checks for a finite Mallows fixed-position theorem.
Only Python's standard library is used; no randomness or floating-point decisions.
"""
from collections import Counter
from fractions import Fraction
from itertools import permutations
from math import factorial, comb

checks = 0

def check(cond, note):
    global checks
    checks += 1
    if not cond:
        raise AssertionError(note)

def add(*ps):
    z = [0]*max(map(len,ps))
    for p in ps:
        for k,v in enumerate(p): z[k] += v
    return tuple(z)

def mul(a,b):
    z=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): z[i+j]+=x*y
    return tuple(z)

def shift(p,n):
    return (0,)*n+tuple(p)

def qbinom(n,k):
    if k<0 or k>n: return (0,)
    if k==0 or k==n: return (1,)
    return add(qbinom(n-1,k),shift(qbinom(n-1,k-1),n-k))

def qfact(n):
    result=(1,)
    for m in range(1,n+1):result=mul(result,(1,)*m)
    return result

def predicted(n,i):
    a,b=i-1,n-i
    result=(0,)
    for j in range(min(a,b)+1):
        result=add(result,shift(mul(qbinom(a,j),qbinom(b,j)),j*j+2*j))
    return mul(mul(qfact(a),qfact(b)),result)

def evalpoly(p,q):
    x=Fraction(0)
    for coeff in reversed(p):x=x*q+coeff
    return x

# Completely independent enumeration of permutations and their inversions.
for n in range(2,9):
    hist=[Counter() for _ in range(n)]
    for sigma in permutations(range(1,n+1)):
        inv=sum(sigma[a]>sigma[b] for a in range(n) for b in range(a+1,n))
        for i,v in enumerate(sigma):
            if v==i+1:hist[i][inv]+=1
    for i in range(1,n+1):
        p=predicted(n,i)
        observed=tuple(hist[i-1][k] for k in range(max(len(p),max(hist[i-1])+1)))
        check(observed[:len(p)]==p,('enumeration',n,i))
        check(all(x==0 for x in observed[len(p):]),('degree',n,i))
        check(sum(p)==factorial(n-1),('normalization',n,i))
        check(p==predicted(n,n+1-i),('reflection',n,i))

# Exact finite-q likelihood ratio and monotonic diagonal comparison.
Q=(Fraction(1,5),Fraction(1,2),Fraction(3,4),Fraction(1),
   Fraction(5,4),Fraction(2),Fraction(4))
for n in range(2,19):
    polynomials=[predicted(n,i) for i in range(1,n+1)]
    for q in Q:
        z=evalpoly(qfact(n),q)
        probabilities=[evalpoly(p,q)/z for p in polynomials]
        for i in range(n):
            check(probabilities[i]==probabilities[n-1-i],('symmetry',n,i,q))
        for i in range(1,n):
            a,b=i-1,n-i
            x,y=probabilities[i-1:i+1]
            if b>a+1:
                check((y>x) if q>1 else ((y<x) if q<1 else (y==x)),('strict',n,i,q))
            elif b==a+1:
                check(x==y,('middle tie',n,i,q))
        if q==1:
            for p in probabilities: check(p==Fraction(1,n),('uniform',n,q))

# Independent q-tilted binary words: probability of crossing count J.
for m in range(2,10):
    for a in range(m+1):
        b=m-a
        for q in Q:
            weights=Counter()
            from itertools import combinations
            for choice in combinations(range(m),a):
                chosen=set(choice)
                j=sum(v>=a for v in chosen)
                cross=sum(x<y and x not in chosen and y in chosen for x in range(m) for y in range(m))
                weights[j]+=q**cross
            normal=sum(weights.values(),Fraction(0))
            pred=Counter()
            for j in range(min(a,b)+1):
                pred[j]=q**(j*j)*evalpoly(qbinom(a,j),q)*evalpoly(qbinom(b,j),q)
            denom=evalpoly(qbinom(m,a),q)
            for j in range(min(a,b)+1):
                check(weights[j]/normal==pred[j]/denom,('q-hypergeom',m,a,j,q))
            check(normal==denom,('q-Vandermonde',m,a,q))

# Direct proof-relevant ratio test independent of permutation enumeration.
for q in Q:
    for a in range(0,15):
        for b in range(a+2,18):
            old=[q**(j*j)*evalpoly(qbinom(a,j),q)*evalpoly(qbinom(b,j),q) for j in range(a+1)]
            new=[q**(j*j)*evalpoly(qbinom(a+1,j),q)*evalpoly(qbinom(b-1,j),q) for j in range(a+2)]
            for j in range(a):
                check(new[j+1]*old[j]>new[j]*old[j+1],('strict MLR',a,b,j,q))
            check(new[a+1]>0,('expanded support',a,b,q))

print('PASS',checks,'exact assertions')
