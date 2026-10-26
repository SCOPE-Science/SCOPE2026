#!/usr/bin/env python3
"""Finite exact arithmetic checks for coloured Ewens permutations.

No finite check is a proof of asymptotic first-order convergence.
"""
from fractions import Fraction
from itertools import permutations, product
from math import factorial

def rising(x,n):
    v=1
    for j in range(n):
        v*=x+j
    return v

def cycles(p):
    n=len(p); seen=set(); answer=[]
    for i in range(n):
        if i not in seen:
            v=i; path=[]
            while v not in seen:
                seen.add(v); path.append(v); v=p[v]
            answer.append(path)
    return answer

def run_count(p, marks, k):
    out=0
    for i in range(len(p)):
        v=i; traversed=set(); good=True
        for j in range(k):
            if v in traversed or not marks[v]:
                good=False; break
            traversed.add(v); v=p[v]
        if good:out+=1
    return out

def expected_run_formula(n,theta,p,k):
    # The cycle length of a distinguished vertex has Ewens probability
    # theta*(n-1)!/(n-l)! * (theta)_(n-l)/(theta)_n.
    prob_long=1-Fraction(sum(theta*factorial(n-1)*rising(theta,n-l)//factorial(n-l)
                              for l in range(1,k)), rising(theta,n))
    return n*p**k*prob_long

cases=0; counts=0; normals=0
for theta in (1,2):
    for n in range(1,7):
        denom=rising(theta,n)*3**n
        total=0
        sums=[0]*min(n,4)
        for perm in permutations(range(n)):
            c=len(cycles(perm)); ew=theta**c
            total+=ew
            for bits in product((0,1),repeat=n):
                w=ew*2**(n-sum(bits))
                for k in range(1,min(n,4)+1):
                    sums[k-1]+=w*run_count(perm,bits,k)
                cases+=1
        assert total==rising(theta,n), (theta,n,total)
        normals+=1
        for k,num in enumerate(sums,1):
            got=Fraction(num,denom)
            expected=expected_run_formula(n,theta,Fraction(1,3),k)
            assert got==expected,(theta,n,k,got,expected)
            counts+=1
# Verify that a long 2-colour cycle with <=2 marked points has the
# correct rooted-radius-2 neighbourhood multiplicities under rotation.
checks=0
for n in (13,17):
    for a in range(n):
        for b in range(a+1,n):
            R={a,b}
            classes={}
            for i in range(n):
                pattern=tuple(int((i+j)%n in R) for j in range(-2,3))
                classes[pattern]=classes.get(pattern,0)+1
            assert sum(classes.values())==n
            if min((b-a)%n,(a-b)%n)>4:
                # Each marked point is locally isolated, with exactly
                # five root positions whose radius-two ball sees it.
                assert classes.get((0,0,0,0,0),0)==n-10
            checks+=1
print('EWENS_SPARSE_FINITE_OK',cases,counts,normals,checks)
