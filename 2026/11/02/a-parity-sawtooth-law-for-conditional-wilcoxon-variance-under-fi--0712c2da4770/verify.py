#!/usr/bin/env python3
"""Exact checks for conditional rank-sum variance and parity-sawtooth theorem.
Requires Python >=3.9 and SymPy. No network, inputs or random seed required.
Finite enumeration corroborates; symbolic identities and the accompanying
algebraic positivity proof establish the all-size conclusions.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations
import sympy as S

checks = 0

def confirm(condition, description):
    global checks
    if not condition:
        raise AssertionError(description)
    checks += 1

A,B,r,x,y = S.symbols('a b r x y', integer=True)
Ve = A*B*(2*A*B*r+4*A*B-(A+B)*(r*r+r-2)+r*r-r)/(12*r*(r+1))
def W(a,b):
    return a*b*(2*a*b-(a+b)*r+a-3*b+r-1)/(12*(r+1))
Vo = S.factor(((A-r)*W(A,B)+(B-r)*W(B,A))/(A+B-2*r))

def bilinear_variance(a,b,p,q,t,h,k):
    alpha=a*(a-p)/(p*p*(p+1))
    beta=b*(b-q)/(q*q*(q+1))
    return (b/q)**2*alpha*(p*h-t*t)+(a/p)**2*beta*(q*k-t*t)+alpha*beta*(p*q*t-p*h-q*k+t*t)

t=r*(r+1)/2
h=r*(r+1)*(2*r+1)/6
confirm(S.cancel(Ve-bilinear_variance(A,B,r,r,t,h,h)-A*A*B*B/(4*r*r))==0,'even conditional formula')
confirm(S.cancel(W(A,B)-bilinear_variance(A,B,r+1,r,t,h,h))==0,'odd conditional formula')

# Every displayed strict inequality reduces to a polynomial with nonnegative
# integer coefficients after translating to feasible, nonnegative x,y.
DeltaEven = S.factor(Ve-Ve.subs(r,r+1))
DeltaLeft = S.factor(Ve-Vo)
DeltaRight = S.factor(Ve.subs(r,r+1)-Vo)
DeltaOdd = S.factor(Vo-Vo.subs(r,r+1))
expected_even=A*B*(A*B*r+4*A*B+2*A+2*B-r)/(6*r*(r+1)*(r+2))
expected_left=A*B*(A+B)*(2*A*B-(A+B)*(r-1)-2*r)/(6*r*(r+1)*(A+B-2*r))
G=A*B*(A+B+2*r+8)-(r+1)*(A+B)**2-(2*r-1)*(A+B)-2*r
expected_right=A*B*G/(6*(r+1)*(r+2)*(A+B-2*r))
H=(x**3*y+x*y**3+2*x*x*y*y
   +(r+2)*(x**3+y**3)+(3*r+4)*(x*x*y+x*y*y)
   +(r*r+2*r)*(x*x+y*y)+(2*r*r+12*r+8)*x*y
   +(2*r*r+4*r)*(x+y))
expected_odd=A*B*H/(6*(r+1)*(r+2)*(A+B-2*r)*(A+B-2*r-2))
confirm(S.cancel(DeltaEven-expected_even)==0,'even parity difference identity')
confirm(S.cancel(DeltaLeft-expected_left)==0,'odd vs preceding even identity')
confirm(S.cancel(DeltaRight-expected_right)==0,'odd vs next even identity')
confirm(S.cancel(DeltaOdd-expected_odd.subs({x:A-r-1,y:B-r-1}))==0,'odd parity difference identity')
confirm(S.cancel(G.subs({A:r+1+x,B:r+1+y})-(x*x*y+x*y*y+(4*r+10)*x*y+(r*r+6*r+8)*(x+y)+2*r*r+8*r+8))==0,'right positivity')
confirm(S.cancel((2*A*B-(A+B)*(r-1)-2*r).subs({A:r+x,B:r+y})-(r*(x+y)+2*x*y+x+y))==0,'left positivity')


def predicted(a,b,k):
    a=int(a); b=int(b); k=int(k); r=k//2
    if k%2==0:
        return Fraction(a*b*(2*a*b*r+4*a*b-(a+b)*(r*r+r-2)+r*r-r),12*r*(r+1))
    def w(i,j):
        return Fraction(i*j*(2*i*j-(i+j)*r+i-3*j+r-1),12*(r+1))
    return Fraction((a-r)*w(a,b)+(b-r)*w(b,a),a+b-2*r)

# Independent whole-word enumeration, including all compositions of size 2..15.
for n in range(2,16):
    for a in range(1,n):
        b=n-a
        classes=defaultdict(list)
        for selected in combinations(range(n),a):
            bits=[0]*n
            for pos in selected: bits[pos]=1
            runs=1+sum(bits[j]!=bits[j-1] for j in range(1,n))
            one_prefix=0
            U=0
            for bit in bits:
                if bit: one_prefix+=1
                else: U+=one_prefix
            classes[runs].append(U)
        for k,values in classes.items():
            mean=Fraction(sum(values),len(values))
            var=sum((Fraction(val)-mean)**2 for val in values)/len(values)
            confirm(mean==Fraction(a*b,2),f'mean a={a} b={b} k={k}')
            confirm(var==predicted(a,b,k),f'variance a={a} b={b} k={k}')
        # Adjacent inequalities compare only existing run counts.
        for k in sorted(classes):
            if k%2:
                if k-1 in classes:
                    confirm(predicted(a,b,k-1)>predicted(a,b,k),f'left trough {a},{b},{k}')
                if k+1 in classes:
                    confirm(predicted(a,b,k+1)>predicted(a,b,k),f'right trough {a},{b},{k}')
            if k+2 in classes:
                confirm(predicted(a,b,k)>predicted(a,b,k+2),f'parity decrease {a},{b},{k}')

# Much larger all-feasible parameter grid (not an infinite proof).
for a in range(1,36):
    for b in range(1,36):
        maxruns=2*min(a,b)+(1 if a!=b else 0)
        for k in range(2,maxruns+1):
            z=predicted(a,b,k)
            confirm(z>=0,f'nonnegative variance {a},{b},{k}')
            if k+2<=maxruns:
                confirm(z>predicted(a,b,k+2),f'parity decrease {a},{b},{k}')
            if k%2 and k+1<=maxruns:
                confirm(predicted(a,b,k+1)>z,f'right trough {a},{b},{k}')
            if k%2:
                confirm(predicted(a,b,k-1)>z,f'left trough {a},{b},{k}')
print(f'PASS {checks} exact checks; includes complete words through length 15 and symbolic identities')
