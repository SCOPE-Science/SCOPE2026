#!/usr/bin/env python3
from fractions import Fraction
import math

def variance_ints(lo, hi):
    vals=list(range(lo,hi+1))
    n=len(vals)
    mean=Fraction(sum(vals),n)
    return sum((Fraction(x)-mean)**2 for x in vals)/n

for k in range(2,201):
    lhs=Fraction(k**3,4)-variance_ints(1,k-1)-k*variance_ints(0,k-1)
    rhs=Fraction(k*(2*k*k-k+3),12)
    assert lhs==rhs,(k,lhs,rhs)
    assert rhs>0


def lam(k,l2,s):
    t=math.exp(s)
    s1=sum(t**j for j in range(1,k))
    s0=sum(t**j for j in range(k))
    return (l2+1)*(1+t**k)**k/(s1*s0**k)


def branch(k,l2,s):
    t=math.exp(s)
    c=(l2+1)/sum(t**j for j in range(1,k))
    a=(t**k)*c
    L=lam(k,l2,s)
    r1=a-L*((1+l2+a)/(a+c))**k
    r2=c-L*((1+l2+c)/(a+c))**k
    return a,c,L,max(abs(r1),abs(r2))

worst_res=0.0
worst_contrast=0.0
cases=0
for k in (2,3,4,7,12):
    for l2 in (0.2,1.0,3.5):
        for s in (0.05,0.1):
            a,c,L,res=branch(k,l2,s)
            scale=max(1.0,abs(a),abs(c))
            worst_res=max(worst_res,res/scale)
            contrast=(a-c)/(a+c)
            exact=math.tanh(k*s/2.0)
            worst_contrast=max(worst_contrast,abs(contrast-exact))
            cases+=1
assert worst_res < 1e-9,worst_res
assert worst_contrast < 1e-12,worst_contrast
print(f"VERIFY_OK exact_variances=199 cases={cases} max_residual={worst_res:.3e} max_contrast_identity={worst_contrast:.3e}")
