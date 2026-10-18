#!/usr/bin/env python3
"""Independent exact checks for uniform finite-prefix multiplicative golden-mean words.
No external dependencies. Finite tests corroborate, but do not prove, asymptotic limits.
"""
from fractions import Fraction
from math import floor, log2, sqrt

LIMIT=90
A=[1,2]; B=[0,1]; C=[0,1]
for k in range(2,LIMIT+1):
    A.append(A[k-1]+A[k-2])
    B.append(B[k-1]+B[k-2]+A[k-2])
    C.append(C[k-1]+C[k-2]+2*B[k-2]+A[k-2])

def lengths(n):
    return [1+(n//i).bit_length()-1 for i in range(1,n+1,2)]

def moments_independent(n):
    ll=lengths(n)
    mean=sum((Fraction(B[k],A[k]) for k in ll),Fraction())
    var=sum((Fraction(C[k],A[k])-Fraction(B[k]**2,A[k]**2) for k in ll),Fraction())
    count=1
    for k in ll:count*=A[k]
    return count,mean,var

def moments_brute(n):
    count=s1=s2=0
    for word in range(1<<n):
        if any((word>>(i-1))&1 and (word>>(2*i-1))&1 for i in range(1,n//2+1)):
            continue
        k=word.bit_count()
        count+=1;s1+=k;s2+=k*k
    m=Fraction(s1,count)
    return count,m,Fraction(s2,count)-m*m

exact_checks=0
for n in range(1,19):
    a=moments_brute(n)
    b=moments_independent(n)
    assert a==b, (n,a,b)
    exact_checks+=1

for k in range(1,LIMIT+1):
    assert A[k]>0 and 0<=B[k]<=k*A[k]
    assert C[k]*A[k]>=B[k]*B[k]

K=65
alpha=sum((Fraction(B[k],A[k])/2**(k+1) for k in range(1,K+1)),Fraction())
sig2=sum((Fraction(C[k],A[k])-Fraction(B[k]*B[k],A[k]*A[k]))/2**(k+1) for k in range(1,K+1))
alpha_tail=Fraction(K+2,2**(K+1))
sig2_tail=Fraction(K*K+4*K+6,2**(K+3))
assert float(alpha_tail)<1e-16 and float(sig2_tail)<1e-15
assert sum((Fraction(B[k],A[k])/2**(k+1) for k in range(1,6)),Fraction()) == Fraction(1667,4992)
assert Fraction(1667,4992)>Fraction(1,3)
phi=(1+sqrt(5))/2
s=phi**-2
beta=2*s/(2+s)
assert beta<1/3
assert abs(beta-2/(4+sqrt(5)))<1e-14

# Exact dyadic-orbit squared-length sum bound used by the concentration proof.
for n in range(1,2000):
    assert sum(x*x for x in lengths(n))<=6*n

# Verify the finite golden-mean uniform first-symbol law and the Parry limit.
for k in (4,8,12,20,35):
    # first symbol 1 forces next 0, leaving a legal length k-2 suffix
    first_one=Fraction(A[k-2],A[k])
    assert abs(float(first_one)-s)<4*(phi**(-2*k+1))

# Finite means and variances are numerically approaching the analytic series.
for n in (300,1000,10000):
    count,mean,var=moments_independent(n)
    assert abs(float(mean/n)-float(alpha))<3/n**0.7
    assert abs(float(var/n)-float(sig2))<3/n**0.7

print("VERIFY_OK: 18 exact independent full-word enumerations; 1999 concentration bounds; 5 local Perron-cylinder tests")
print("alpha in [%.16f, %.16f]"%(float(alpha),float(alpha+alpha_tail)))
print("sigma2 in [%.16f, %.16f]"%(float(sig2),float(sig2+sig2_tail)))
print("beta = %.16f, gap = %.16f"%(beta,float(alpha)-beta))
