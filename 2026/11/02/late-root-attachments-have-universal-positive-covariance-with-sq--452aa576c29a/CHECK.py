"""Exact checks for root-degree versus squared spin sum on recursive trees."""
from fractions import Fraction
from itertools import product
from math import factorial

def predicted(n,r):
    mean=second=Fraction(1)
    cov=Fraction(0)
    profiles={}
    for j in range(2,n+1):
        q=mean-second/Fraction(j-1)
        # I_j covariance with the squared displacement at its arrival.
        profiles[j]=Fraction(2)*r*q/Fraction(j-1)
        cov=(1+Fraction(2)*r/Fraction(j-1))*cov+profiles[j]
        mean=(1+r/Fraction(j-1))*mean
        second=(1+Fraction(2)*r/Fraction(j-1))*second+1
    return mean,second,cov,profiles

def dist(i,j,p,depth):
    x=i;y=j
    while depth[x]>depth[y]:x=p[x]
    while depth[y]>depth[x]:y=p[y]
    while x!=y:x=p[x];y=p[y]
    return depth[i]+depth[j]-2*depth[x]

assertions=0
for n in range(2,9):
    for r in [Fraction(-4,5),Fraction(-1,2),Fraction(-1,7),Fraction(0),Fraction(1,7),Fraction(1,2),Fraction(4,5)]:
        totaldeg=total2=joint=Fraction(0)
        attachments=[Fraction(0)]*(n+1)
        counts=0
        for parent_tuple in product(*(range(1,k) for k in range(2,n+1))):
            parent=[0]*(n+1);depth=[0]*(n+1)
            degree=0
            for k,parent_k in enumerate(parent_tuple,2):
                parent[k]=parent_k;depth[k]=depth[parent_k]+1
                if parent_k==1:degree+=1
            second=Fraction(0)
            for i in range(1,n+1):
                for j in range(1,n+1):
                    second+=r**dist(i,j,parent,depth)
            totaldeg+=degree;total2+=second;joint+=degree*second
            for k in range(2,n+1):
                if parent[k]==1:attachments[k]+=second
            counts+=1
        assert counts==factorial(n-1);assertions+=1
        totaldeg/=counts;total2/=counts;joint/=counts
        mean,second,cov,profiles=predicted(n,r)
        assert total2==second,(n,r,total2,second);assertions+=1
        assert joint-totaldeg*total2==cov,(n,r,joint-totaldeg*total2,cov);assertions+=1
        for k in range(2,n+1):
            c=attachments[k]/counts-total2/Fraction(k-1)
            q=predicted(k-1,r)[0]-predicted(k-1,r)[1]/Fraction(k-1)
            multiplier=Fraction(1)
            for t in range(k,n):multiplier*=1+Fraction(2)*r/Fraction(t)
            expected=multiplier*Fraction(2)*r*q/Fraction(k-1)
            assert c==expected,(n,k,r,c,expected)
            assertions+=1
        if n>=4 and r:
            assert cov>0,(n,r,cov)
            assertions+=1
        if n<=3:assert cov==0;assertions+=1
# Boundary and critical-parameter symbolic checks (not asymptotic proofs).
for r in [Fraction(-4,5),Fraction(-1,2),Fraction(-1,7),Fraction(1,7),Fraction(1,2),Fraction(4,5)]:
    assert predicted(4,r)[2]==r*r*(1-r)/9
    assertions+=1
for n in [2,3,4,7,20,50]:
    r=Fraction(1,2)
    _,d,c,_=predicted(n,r)
    assert d==n*sum((Fraction(1,k) for k in range(1,n+1)),Fraction(0))
    assertions+=1
print('EXACT_ASSERTIONS',assertions)
