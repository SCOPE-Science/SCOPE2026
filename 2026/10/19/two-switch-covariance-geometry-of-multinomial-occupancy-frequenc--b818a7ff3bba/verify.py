"""Standalone exact covariance verifier for multinomial occupancy frequencies.
Requires Python 3 standard library only. This checks finite cases, not the analytic theorem.
"""
from itertools import product
from fractions import Fraction as F
from math import comb, factorial, prod

def fall(n,r): return prod(range(n-r+1,n+1))
def exact_uniform(m,n,j,k):
    ej=F(m*comb(n,j)*(m-1)**(n-j),m**n)
    ek=F(m*comb(n,k)*(m-1)**(n-k),m**n)
    joint=F(m*(m-1)*factorial(n)*(m-2)**(n-j-k),factorial(j)*factorial(k)*factorial(n-j-k)*m**n)
    return joint-ej*ek

def enumerate_uniform(m,n,j,k):
    u=v=w=0
    for word in product(range(m),repeat=n):
        counts=[word.count(t) for t in range(m)]
        a=counts.count(j);b=counts.count(k)
        u+=a;v+=b;w+=a*b
    return F(w,m**n)-F(u*v,m**(2*n))

def ratio_sign(m,n,j,k):
    s=j+k
    lhs=fall(n,s)*(m-2)**(n-s)*m**(n-1)
    rhs=fall(n,j)*fall(n,k)*(m-1)**(2*n-s-1)
    return (lhs>rhs)-(lhs<rhs)

checks=0
for m in (3,4,5):
    for n in range(3,8):
        if m**n>40000:continue
        for j in range(1,min(n,4)):
            for k in range(j+1,min(n,5)):
                if j+k>n:continue
                c=exact_uniform(m,n,j,k)
                assert c==enumerate_uniform(m,n,j,k)
                assert (c>0)-(c<0)==ratio_sign(m,n,j,k)
                checks+=1

phases=0
for m in range(3,10):
    for j in range(1,7):
        for k in range(j+1,9):
            seq=[]
            for n in range(j+k,90):
                v=ratio_sign(m,n,j,k)
                if v and (not seq or v!=seq[-1]): seq.append(v)
                phases+=1
            assert seq in ([-1],[1],[-1,1],[1,-1],[-1,1,-1]),(m,j,k,seq)

p=[F(1,32),F(15,32),F(16,32)]
def heterogeneous(n):
    mean1=sum((n*x*(1-x)**(n-1) for x in p),F(0))
    mean2=sum((comb(n,2)*x*x*(1-x)**(n-2) for x in p),F(0))
    joint=sum((n*comb(n-1,2)*p[i]*p[j]**2*(1-p[i]-p[j])**(n-3)
               for i in range(3) for j in range(3) if i!=j),F(0))
    return joint-mean1*mean2
expected={3:1,4:-1,9:1,10:-1}
for n,z in expected.items():
    c=heterogeneous(n)
    assert (c>0)-(c<0)==z
print('PASS: exact word enumerations',checks,'phase-sign tests',phases,'heterogeneous checkpoints',expected)
