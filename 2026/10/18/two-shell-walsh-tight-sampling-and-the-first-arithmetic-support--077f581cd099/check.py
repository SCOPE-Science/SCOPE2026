#!/usr/bin/env python3
"""Exact finite checks for the two-Hamming-shell first-Walsh-band sampling theorem."""
from fractions import Fraction
from itertools import product
from math import comb

def admissible_pairs(n):
    for s in range(1, n+1):
        if n % s: continue
        t = n // s
        if (n-s)%2 or (n+t)%2 or (n+t)//2>n: continue
        yield s,t,(n-s)//2,(n+t)//2

def analytic_gram(n,s,t):
    a=Fraction(t,s+t)
    mu=(a*s+(1-a)*(-t))/n
    tau=(a*(s*s-n)+(1-a)*(t*t-n))/(n*(n-1))
    return mu,tau

for n in range(3,11):
    pairs=list(admissible_pairs(n))
    assert bool(pairs)==(n%2==1 or n%4==0)
    for s,t,k,l in pairs:
        assert s*t==n and analytic_gram(n,s,t)==(0,0)
        if n<=8:
            beta=Fraction(t,s+t)
            data=[]
            for bits in product((1,-1),repeat=n):
                h=bits.count(-1)
                weight=(beta/Fraction(comb(n,k))) if h==k else ((1-beta)/Fraction(comb(n,l)) if h==l else Fraction(0))
                if weight:data.append((bits,weight))
            assert sum((w for _,w in data),Fraction(0))==1
            for i in range(-1,n):
                for j in range(-1,n):
                    g=sum((w*(1 if i==-1 else x[i])*(1 if j==-1 else x[j]) for x,w in data),Fraction(0))
                    assert g==(1 if i==j else 0),(n,s,t,i,j,g)

def candidate_count(n,s):
    t=n//s
    return comb(n,(n-s)//2)+comb(n,(n-t)//2)

previous=[]
for n in range(3,52,2):
    divs=[s for s in range(1,n+1,2) if n%s==0]
    pairs=sorted((candidate_count(n,s),s,n//s) for s in divs)
    base=comb(n,(n-1)//2)+1
    if pairs[0][0] < base:previous.append((n,pairs[0],base))
assert previous==[(51,(244362982488625,3,17),247959266474053)]
assert candidate_count(51,3)==244362982488625
assert candidate_count(51,1)==247959266474053
# Infinite improvement along n=51+6j. For n=6k+3, R_k=C(n,n/3)/C(n,(n-1)/2)
# R_(k+1)/R_k = 9(3k+2)(3k+4)^2(3k+5)/(16(2k+3)^2(4k+3)(4k+5)) < 3/4
# since 3/4 - ratio = 3(13k^4+65k^3+138k^2+144k+60)/(16(2k+3)^2(4k+3)(4k+5)) > 0.
# Also (3/4)/(n+3) < 1/(n+9) for n>15.
def mul(a,b):
    r=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):r[i+j]+=x*y
    return r

def prod(*factors):
    r=[1]
    for a in factors:r=mul(r,a)
    return r

def sub(a,b):
    r=[0]*max(len(a),len(b))
    for i,x in enumerate(a):r[i]+=x
    for i,x in enumerate(b):r[i]-=x
    return r

# 3/4 - RR = [12(2k+3)^2(4k+3)(4k+5) - 9(3k+2)(3k+4)^2(3k+5)] /
#                  [16(2k+3)^2(4k+3)(4k+5)]
left=sub([12*x for x in prod([3,2],[3,2],[3,4],[5,4])],
         [9*x for x in prod([2,3],[4,3],[4,3],[5,3])])
assert left==[3*z for z in [60,144,138,65,13]]
assert candidate_count(51,3)<candidate_count(51,1)
print('PASS: exact Walsh Gram checks through n=8, all parity/divisor profile checks through n=10')
print('PASS: all odd dimensions 3..49 prefer the extremal-center construction; first strict interior gain is 51')
print('PASS: symbolic strict-contraction factor for every n=51+6j')
print('n51 optimal sites:',candidate_count(51,3),'baseline:',candidate_count(51,1))
