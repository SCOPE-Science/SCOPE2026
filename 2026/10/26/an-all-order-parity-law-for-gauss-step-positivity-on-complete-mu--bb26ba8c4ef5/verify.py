#!/usr/bin/env python3
"""Exact-rational checks for Gauss-step positivity on multipartite Laplacians.

Finite checks supplement the analytic proof; they do not establish the
statements for all stage counts or graph orders.
"""
from fractions import Fraction
from math import factorial
from itertools import combinations
from sympy import Matrix, eye, zeros, Rational


def q_coefficients(s):
    return [Fraction(factorial(s)*factorial(2*s-k), factorial(2*s)*factorial(s-k)*factorial(k)) for k in range(s+1)]


def eval_poly(cs, z, flip=False):
    y = z*0
    for k, c in enumerate(cs):
        y += Rational(c.numerator, c.denominator)*((-z)**k if flip else z**k)
    return y


def multipartite_laplacian(parts):
    n=sum(parts)
    L=zeros(n,n)
    class_of=sum(([i]*size for i,size in enumerate(parts)),[])
    for i,j in combinations(range(n),2):
        if class_of[i]!=class_of[j]:
            L[i,i]+=1;L[j,j]+=1;L[i,j]-=1;L[j,i]-=1
    return L,class_of


def matrix_polynomial(cs, A, flip=False):
    n=A.rows
    B=zeros(n,n)
    power=eye(n)
    for k,c in enumerate(cs):
        B+=(Rational(c.numerator,c.denominator)*(-1 if (flip and k%2) else 1))*power
        power=power*A
    return B

# Exact coefficient and quotient-ratio inequalities, finite stress checks.
coeff_cases=0
for s in range(1,41):
    cs=q_coefficients(s)
    assert cs[0]==1 and cs[1]==Fraction(1,2)
    ratios=[]
    for i in range((s+1)//2):
        if 2*i+1<=s:
            ratio=cs[2*i]/cs[2*i+1]
            assert ratio==Fraction((2*i+1)*(2*s-2*i),s-2*i)
            ratios.append(ratio)
    assert all(a<b for a,b in zip(ratios,ratios[1:]))
    coeff_cases+=1

# Direct polynomial-matrix expression versus exact spectral projectors.
parts_cases=[(1,1,1),(1,2),(2,2),(2,3),(1,2,2),(1,1,3),
             (1,2,3),(2,2,2),(3,3),(2,1,1,2),(4,1)]
stages=[1,2,3,4,5,6,8]
steps=[Fraction(1,4),Fraction(2,1),Fraction(9,1)]
checks=0
strict_checks=0
for parts in parts_cases:
    L,cls=multipartite_laplacian(parts)
    n=L.rows
    for s in stages:
        cs=q_coefficients(s)
        for h in steps:
            z=Rational(h.numerator,h.denominator)
            A=z*L
            U=matrix_polynomial(cs,A,True)
            V=matrix_polynomial(cs,A,False)
            T=V.inv()*U
            Rn=eval_poly(cs,z*n,True)/eval_poly(cs,z*n)
            for i in range(n):
                q=n-parts[cls[i]]
                Ri=eval_poly(cs,z*q,True)/eval_poly(cs,z*q)
                for j in range(n):
                    if cls[i]!=cls[j]:
                        expected=(1-Rn)/n
                    else:
                        expected=(1-Rn)/n+(Rn-Ri)/parts[cls[i]]
                        if i==j: expected+=Ri
                    assert T[i,j]==expected,(parts,s,h,i,j,T[i,j],expected)
                    if i!=j:
                        assert T[i,j]>0,(parts,s,h,i,j,T[i,j])
                        strict_checks+=1
                    elif s%2==0:
                        assert T[i,j]>0,(parts,s,h,i,j,T[i,j])
                        strict_checks+=1
                assert sum(T[i,j] for j in range(n))==1
            checks+=1

# Direct large-step obstruction at odd stages and n >= 3.
for s in [1,3,5,7,9]:
    cs=q_coefficients(s)
    n=5
    Rn=eval_poly(cs,10**6*n,True)/eval_poly(cs,10**6*n)
    diag=(1+4*Rn)/5
    assert diag<0

print('verification_passed')
print('coefficient_stage_counts',coeff_cases)
print('exact_matrix_cases',checks)
print('strict_matrix_entries_checked',strict_checks)
print('large_step_odd_cases',5)
