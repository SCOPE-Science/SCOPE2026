#!/usr/bin/env python3
from fractions import Fraction
from itertools import product, combinations
from math import comb

def deletion_ball_two(x):
    n=len(x)
    return {x[:i]+x[i+1:j]+x[j+1:] for i,j in combinations(range(n),2)}

def run_lengths(x):
    out=[]
    i=0
    while i<len(x):
        j=i+1
        while j<len(x) and x[j]==x[i]:
            j+=1
        out.append(j-i)
        i=j
    return out

def run_formula(x):
    L=run_lengths(x)
    R=len(L)
    I=sum(1 for j,a in enumerate(L) if a==1 and 0<j<R-1)
    E=sum(1 for j,a in enumerate(L) if a==1 and (j==0 or j==R-1))
    return comb(R+1,2)-2*I-E

def target_mean(n):
    return Fraction(n*n+n+2,8)

def target_var(n):
    return Fraction((n-1)*(n-2)*(2*n-3),32)

total_words=0
for n in range(2,13):
    vals=[]
    for bits in product('01', repeat=n):
        x=''.join(bits)
        v=len(deletion_ball_two(x))
        assert v==run_formula(x), (n,x,v,run_formula(x))
        vals.append(v)
    total_words += len(vals)
    mean=Fraction(sum(vals),len(vals))
    var=Fraction(sum(v*v for v in vals),len(vals))-mean*mean
    assert mean==target_mean(n),(n,mean,target_mean(n))
    assert var==target_var(n),(n,var,target_var(n))

for n in range(3,201):
    m=n-1
    walsh=Fraction(m*(m-1)*(m-1),16)+Fraction(comb(m,2),16)
    closed=Fraction(m*(m-1)*(2*m-1),32)
    assert walsh==closed==target_var(n),(n,walsh,closed,target_var(n))

print(f"VERIFY_OK words={total_words} n=2..12 walsh_n<=200")
