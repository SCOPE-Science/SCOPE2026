"""Exact verification of labeled outdegree–leaf-count covariance in uniform recursive trees.
Only the uniform independent-parent model is used. Standard library only.
"""
from fractions import Fraction
from itertools import product
from math import factorial


def predicted(n,i):
    if i == 1:
        return Fraction(n-2,2*(n-1))
    N,t=n-1,i-1
    h=sum((Fraction(1,j) for j in range(t+1,N+1)),Fraction(0))
    return Fraction((N-t)*(N-2),2*N*N)-Fraction(t,N)*h


def exhaustive(n):
    total=factorial(n-1)
    d=[0]*n; dl=[0]*n; leaves_total=0
    for choices in product(*(range(1,j) for j in range(2,n+1))):
        deg=[0]*(n+1)
        for parent in choices: deg[parent]+=1
        leaves=sum(deg[i]==0 for i in range(2,n+1))
        leaves_total+=leaves
        for i in range(1,n+1):
            d[i-1]+=deg[i]
            dl[i-1]+=deg[i]*leaves
    for i in range(1,n+1):
        covariance=Fraction(dl[i-1],total)-Fraction(d[i-1]*leaves_total,total*total)
        assert covariance==predicted(n,i), (n,i,covariance,predicted(n,i))
    return n


if __name__=='__main__':
    for n in range(2,10):
        exhaustive(n)
        print('exhaustive parent arrays passed n=',n)
    for n in range(4,301):
        signs=[]
        for i in range(2,n):
            c=predicted(n,i)
            signs.append(1 if c>0 else (0 if c==0 else -1))
        assert signs==sorted(signs,reverse=True)
        assert signs[-1]==-1
        if n>=7: assert signs[0]==1
        else: assert signs[0]<0
    print('exact harmonic sign-order and n=7 onset verified for 4<=n<=300')
