"""Exact finite-sample checks for disjoint multinomial absolute differences.
All recorded scientific assertions are proved independently of this finite checker.
"""
from fractions import Fraction as F
from math import factorial
from itertools import product

def g(m, t):
    return sum((abs(2*j-m) * F(factorial(m),factorial(j)*factorial(m-j))
                * t**j * (1-t)**(m-j) for j in range(m+1)), F(0))

def exact_cov(n, a, b, c, d):
    p, q = a+b, c+d
    assert all(z>0 for z in (a,b,c,d)) and p+q<=1
    gp=[g(i,b/p) for i in range(n+1)]
    gq=[g(j,d/q) for j in range(n+1)]
    m1=m2=m12=F(0)
    for i in range(n+1):
        for j in range(n+1-i):
            k=n-i-j
            w=F(factorial(n), factorial(i)*factorial(j)*factorial(k))*p**i*q**j*(1-p-q)**k
            m1+=w*gp[i]; m2+=w*gq[j]; m12+=w*gp[i]*gq[j]
    return m12-m1*m2

cases=[
    ('both balanced unequal blocks',(F(1,8), F(1,8), F(1,4), F(1,4))),
    ('one balanced one biased',(F(1,10),F(1,10),F(1,10),F(3,10))),
    ('both biased',(F(1,10),F(2,10),F(3,10),F(1,10))),
    ('four categories exactly',(F(1,8),F(1,8),F(1,8),F(5,8))),
    ('very unequal pair',(F(1,16),F(3,16),F(2,16),F(5,16))),
    ('uniform five categories',(F(1,5),F(1,5),F(1,5),F(1,5)))
]
count=0
for name,params in cases:
    for n in range(1,13):
        z=exact_cov(n,*params)
        assert z<0, (name,n,z)
        count+=1
print('PASS: '+str(count)+' exact negative-covariance checks across six multinomial laws and N=1..12.')
print('N=1 identity: Cov = -(a+b)(c+d).')
for name,params in cases[:3]:
    print(name,'N=12 exact covariance =',str(exact_cov(12,*params)))
