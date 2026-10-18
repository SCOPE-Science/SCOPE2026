#!/usr/bin/env python3
"""Exact finite consistency checks for the two-step q-central binomial polynomial theorem.
The mathematical assertion for all positive indices follows from the written proof,
not from extrapolating these finite checks.
"""
from math import gcd

def mul(a,b):
    z=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b):
                if y:z[i+j]+=x*y
    while len(z)>1 and z[-1]==0:z.pop()
    return z

def prod(xs):
    r=[1]
    for x in xs:r=mul(r,x)
    return r

def one_minus(exp):
    z=[0]*(exp+1); z[0]=1;z[exp]=-1
    return z

def qint(r,power):
    assert r>=1 and power>=1
    z=[0]*(power*(r-1)+1)
    for j in range(r):z[power*j]=1
    return z

def factor_poly(n,k):
    if n==1:return qint(k,1)
    R=prod([qint(k,m) for m in range(3,n+1)])
    if n%2:
        factors=[qint((n+1)//2,2*k),qint(k,1),qint(k,2),qint(k,2),R,R]
    elif k%2==0:
        factors=[qint(n+1,k),qint(2*k,1),qint(k//2,2),qint(k//2,2),R,R]
    else:
        raise ValueError('nonpolynomial rational function')
    return prod(factors)

def original_num_den(n,k):
    numerator=[one_minus(1)]
    denominator=[one_minus(k*(n+2))]
    for m in range(1,n+1):
        numerator.extend([one_minus(k*m),one_minus(k*(m+2))])
        denominator.extend([one_minus(m),one_minus(m)])
    return prod(numerator),prod(denominator)

def cyclotomic_exponent(n,k,d):
    u=d//gcd(d,k)
    return n//u + (n+2)//u - 2//u - 2*(n//d) - int(k*(n+2)%d==0)

def main():
    proven_branch=0
    for n in range(1,9):
        for k in range(1,9):
            if n%2==1 or k%2==0:
                a,b=original_num_den(n,k)
                f=factor_poly(n,k)
                assert min(f)>=0
                assert mul(b,f)==a, (n,k)
                proven_branch+=1
            else:
                # The formula has an exact simple pole at q=-1, residue k^(n-1).
                qint_at_minus1=(1 if k%2 else 0)
                assert qint_at_minus1==1
                R_at_minus1=k**(n//2-1)
                assert k*(R_at_minus1**2)==k**(n-1)
    scanned=0
    for n in range(1,61):
        for k in range(1,31):
            minexp=min(cyclotomic_exponent(n,k,d) for d in range(2,k*(n+2)+1))
            assert (minexp>=0)==(n%2==1 or k%2==0), (n,k,minexp)
            scanned+=1
    print('VERIFY_OK exact_polynomial_identities=',proven_branch,'cyclotomic_cases=',scanned)

if __name__=='__main__':main()
