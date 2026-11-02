#!/usr/bin/env python3
"""Exact rational certificate for the one-pointed linear-Hodge denominator witness cutoff.

No external packages, network, precomputed rational tables, or floating-point arithmetic.
Run: python3 verify.py
"""
from fractions import Fraction as F
from math import comb, factorial, lcm
from itertools import combinations
import json

GMAX = 10

def add(P, Q):
    R=[F(0)]*max(len(P),len(Q))
    for i,x in enumerate(P):R[i]+=x
    for i,x in enumerate(Q):R[i]+=x
    return R

def mul(P, Q, n=GMAX):
    R=[F(0)]*min(len(P)+len(Q)-1, n+1)
    for i,x in enumerate(P):
        for j,y in enumerate(Q):
            if i+j<len(R):R[i+j]+=x*y
    return R

def bernoulli(n):
    B=[F(1)]
    for m in range(1,n+1):
        B.append(-sum((F(comb(m+1,j))*B[j] for j in range(m)),F(0))/F(m+1))
    return B

# Method A: Bernoulli-logarithm exponential recurrence.
def by_logarithm():
    B=bernoulli(2*GMAX)
    c=[F(0)]+[F((-1)**(j-1))*B[2*j]/(2*j*factorial(2*j))
                   for j in range(1,GMAX+1)]
    Q=[[F(1)]]
    for g in range(1,GMAX+1):
        a=[F(0)]*(g+1)
        for j in range(1,g+1):
            for i,coeff in enumerate(Q[g-j]):
                a[i+1]+=F(j,g)*c[j]*coeff
        Q.append(a)
    # x -> x+1 converts coefficient polynomial to the actual Hodge integral series.
    return [[sum((coeff*comb(k,i) for k,coeff in enumerate(Q[g]) if k>=i),F(0))
             for i in range(g+1)] for g in range(GMAX+1)]

# Method B: independent formal sine division followed by integer exponentiation
# and Newton interpolation from P_g(r-1) for 1 <= r <= g+1.
def by_sine_interpolation():
    s=[F((-1)**j,2**(2*j)*factorial(2*j+1)) for j in range(GMAX+1)]
    a=[F(1)]
    for n in range(1,GMAX+1):
        a.append(-sum((s[j]*a[n-j] for j in range(1,n+1)),F(0)))
    powers=[[F(1)]+[F(0)]*GMAX]
    for r in range(1,GMAX+2):
        powers.append(mul(powers[-1],a))
    # Build binomial(x,k) in the monomial basis.
    binoms=[[F(1)]]
    for k in range(1,GMAX+1):
        binoms.append([z/F(k) for z in mul(binoms[-1],[F(-(k-1)),F(1)])])
    out=[[F(1)]]
    for g in range(1,GMAX+1):
        values=[powers[r][g] for r in range(1,g+2)]
        differences=[]
        while values:
            differences.append(values[0])
            values=[values[j+1]-values[j] for j in range(len(values)-1)]
        poly=[F(0)]*(g+1)
        for k,delta in enumerate(differences):
            for i,b in enumerate(binoms[k]):poly[i]+=delta*b
        out.append(poly)
    return out

def is_prime(p):
    return p>=2 and all(p%d for d in range(2,int(p**0.5)+1))

def vp(m,p):
    z=0
    while m%p==0 and m:
        z+=1;m//=p
    return z

def minkowski(g):
    d=2*g
    T=1
    exps={}
    for p in range(2,d+2):
        if not is_prime(p):continue
        den=p-1; e=0
        while den<=d:
            e+=d//den;den*=p
        if e:exps[p]=e;T*=p**e
    return T,exps

A=by_logarithm()
B=by_sine_interpolation()
assert A==B, 'The independent rational constructions disagree.'

# The entire classification for g <= 10 is verified without assuming any
# denominator identity: compute lcm of all actual coefficients and compare
# with the independently computed Minkowski number.
expected_w=[None,1,1,2,2,1,2,2,2,2,3]
expected_examples={1:(0,),2:(0,),3:(0,1),4:(0,1),5:(1,),
                   6:(0,2),7:(0,3),8:(0,2),9:(0,3),10:(0,1,3)}
records=[]
for g in range(1,GMAX+1):
    den=[q.denominator for q in A[g]]
    T,exps=minkowski(g)
    assert lcm(*den)==T,(g,'incorrect denominator equality')
    winning=None
    for k in range(1,len(den)+1):
        for idx in combinations(range(len(den)),k):
            if lcm(*(den[i] for i in idx))==T:
                winning=idx;break
        if winning is not None:break
    assert len(winning)==expected_w[g]
    witness=expected_examples[g]
    assert lcm(*(den[i] for i in witness))==T
    records.append({'g':g,'Minkowski_T_2g':str(T),'witness_indices':list(witness),
                    'minimal_number':len(winning),'denominators':[str(v) for v in den]})

# Lower bound at g=10: for prime-power maxima 3^14,5^6,19,
# the eligible coefficient-index sets are pairwise disjoint.
g=10; T,exps=minkowski(g); den=[x.denominator for x in A[g]]
cover={p:[i for i,d in enumerate(den) if vp(d,p)==exps[p]] for p in (3,5,19)}
assert exps[3]==14 and exps[5]==6 and exps[19]==1
assert cover=={3:[3,4,9,10],5:[1,5],19:[0,2]}
assert not (set(cover[3]) & set(cover[5]) or set(cover[3]) & set(cover[19]) or set(cover[5]) & set(cover[19]))
print('VERIFY_OK; independent rational series match; all genus 1..10 minima verified; genus-ten disjoint prime-support obstruction verified.')
print(json.dumps({'classification':records,'genus10_cover':{str(p):z for p,z in cover.items()},
                  'genus10_values':[
                    {'i':i,'numerator':str(q.numerator),'denominator':str(q.denominator)}
                    for i,q in enumerate(A[10])]},indent=2))
