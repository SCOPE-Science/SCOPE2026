"""Reproducibility checks for local-minimum/isolated-point covariance.
Standard library only. Run: python verify.py
"""
from fractions import Fraction as F
from itertools import permutations
from math import comb, factorial, exp, log
from random import Random

def positive_power(z, p):
    return max(F(0), z) ** p

def q_distribution(n, r):
    # Inclusion-exclusion for the Dirichlet(1,...,1) simplex.
    probs=[]
    for k in range(n+1):
        probs.append(comb(n,k)*sum(((-1)**j)*comb(n-k,j)*positive_power(1-(k+j)*r,n-1)
                      for j in range(n-k+1)))
    return probs

def conditional_cov(n,k):
    return -F(k*(k-1)*(n-k)*(n-k-1),3*(n-1)*(n-2)*(n-3))

def closed_cov(n,r):
    return -F(n,3)*(positive_power(1-2*r,n-1)-2*positive_power(1-3*r,n-1)+positive_power(1-4*r,n-1))

nperm=0; checks=0
for n in range(5,9):
    arr=[(0,0,0) for _ in range(n+1)]
    m2=0
    for a in permutations(range(n)):
        m=sum(a[i]<a[(i-1)%n] and a[i]<a[(i+1)%n] for i in range(n))
        m2+=m*m
        for k in range(n+1):
            h=[int(a[i]>=n-k) for i in range(n)]
            c=sum(h[i]*h[(i+1)%n] for i in range(n))
            x,y,z=arr[k]
            arr[k]=(x+m,y+c,z+m*c)
        nperm+=1
    count=factorial(n)
    assert F(m2,count)-F(n*n,9)==F(2*n,45)
    checks+=1
    for k,(sm,sk,smk) in enumerate(arr):
        assert F(sm,count)==F(n,3)
        assert F(smk,count)-F(sm,count)*F(sk,count)==conditional_cov(n,k), (n,k)
        checks+=2
    for r in [F(0),F(1,20),F(1,12),F(1,7),F(1,5),F(2,5),F(1,2),F(3,5)]:
        probs=q_distribution(n,r)
        assert sum(probs)==1 and all(p>=0 for p in probs), (n,r,probs)
        cv=sum(probs[k]*conditional_cov(n,k) for k in range(n+1))
        assert cv==closed_cov(n,r),(n,r,cv,closed_cov(n,r))
        checks+=2
    print('checked n=',n,'permutations=',count)
for x in (-1.0,0.,1.0):
    n=40000
    r=(log(n)+x)/(2*n)
    observed=-(n/3)*sum(c*(max(0,1-j*r)**(n-1)) for c,j in [(1,2),(-2,3),(1,4)])
    target=-exp(-x)/3
    assert abs(observed-target)<0.07, (x,observed,target)
    checks+=1
rng=Random(20261011)
for n in range(5,11):
    for _ in range(1500):
        pts=sorted(rng.random() for i in range(n))
        gaps=[(pts[(i+1)%n]-pts[i])%1 for i in range(n)]
        neighbor=[]
        for i in range(n):
            ds=[min(abs(pts[i]-pts[j]),1-abs(pts[i]-pts[j])) if i!=j else float('inf') for j in range(n)]
            neighbor.append(min(range(n),key=lambda j:ds[j]))
        m_near=sum(neighbor[i]==j and neighbor[j]==i for i in range(n) for j in range(i+1,n))
        m_gap=sum(gaps[i]<min(gaps[(i-1)%n],gaps[(i+1)%n]) for i in range(n))
        assert m_near==m_gap,(n,pts,m_near,m_gap)
        checks+=1
        for r in (0.02,0.1,0.25,0.49):
            k_near=sum(all(min(abs(pts[i]-pts[j]),1-abs(pts[i]-pts[j]))>r for j in range(n) if j!=i) for i in range(n))
            k_gap=sum(gaps[(i-1)%n]>r and gaps[i]>r for i in range(n))
            assert k_near==k_gap,(n,r,pts,k_near,k_gap)
            checks+=1
print('VERIFY_OK permutations=',nperm,'checks=',checks)

