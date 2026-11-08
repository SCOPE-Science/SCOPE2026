#!/usr/bin/env python3
"""Finite exact coefficient checks for the critical Gaussian kernel identity.
Not a substitute for the operator-theoretic proof.
"""
from fractions import Fraction as Q
from math import factorial, comb

def hermite(n):
    # Physicists' Hermite polynomial H_n, coefficient dictionary.
    ans={}
    for j in range(n//2+1):
        power=n-2*j
        ans[power]=ans.get(power,0)+(-1)**j*factorial(n)*2**power//(factorial(j)*factorial(power))
    return ans

def double_factorial_odd(k):
    a=1
    for j in range(1,k+1): a*=2*j-1
    return a

def gaussian_entry(m,n,t):
    # The critical Bargmann-multiplier kernel coefficient of z^m conj(w)^n.
    if (m-n)%2: return Q(0)
    hm,hn=hermite(m),hermite(n)
    poly={}
    for p,a in hm.items():
        for q,b in hn.items():
            poly[p+q]=poly.get(p+q,0)+a*b
    summ=Q(0)
    for p,a in poly.items():
        assert p%2==0
        k=p//2
        summ+=Q(a*double_factorial_odd(k),2**k)*(1-t)**k
    sign=1 if ((m-n)//2)%2==0 else -1
    return sign*summ/Q(2**((m+n)//2)*factorial(m)*factorial(n))

def gram_entry(m,n,t):
    rho2=1-t
    val=Q(0)
    for j in range(min(m,n)+1):
        if (m-j)%2 or (n-j)%2: continue
        p=(m-j)//2; q=(n-j)//2
        val+=rho2**j*(t/2)**(p+q)/Q(factorial(j)*factorial(p)*factorial(q))
    return val

count=0
for t in (Q(1,9),Q(1,4),Q(2,5),Q(1,2),Q(3,4),Q(7,8)):
    for m in range(11):
        for n in range(11):
            x=gram_entry(m,n,t);y=gaussian_entry(m,n,t)
            assert x==y,(m,n,t,x,y)
            count+=1
    assert (1-t)>0
    count+=1
print('CRITICAL_FOCK_BARGMANN_PASS',count,'exact coefficient assertions')
