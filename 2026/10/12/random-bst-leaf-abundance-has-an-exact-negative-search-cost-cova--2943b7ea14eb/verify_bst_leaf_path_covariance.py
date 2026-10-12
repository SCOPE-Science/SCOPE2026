#!/usr/bin/env python3
from fractions import Fraction
from itertools import permutations
from math import factorial

def H(n):
    return sum((Fraction(1,k) for k in range(1,n+1)), Fraction(0))

def target_EL(n):
    if n==0: return Fraction(0)
    if n==1: return Fraction(1)
    return Fraction(n+1,3)

def target_EP(n):
    if n==0: return Fraction(0)
    return 2*(n+1)*H(n)-4*n

def target_cov(n):
    if n<2: return Fraction(0)
    return -Fraction((n-2)*(n+3),9*n)

def target_varL(n):
    if n<=2: return Fraction(0)
    if n==3: return Fraction(2,9)
    return Fraction(2*(n+1),45)

def bst_stats(p):
    n=len(p)
    left=[-1]*(n+1)
    right=[-1]*(n+1)
    root=p[0]
    path=0
    for x in p[1:]:
        cur=root
        depth=0
        while True:
            depth+=1
            if x<cur:
                if left[cur]==-1:
                    left[cur]=x
                    path+=depth
                    break
                cur=left[cur]
            else:
                if right[cur]==-1:
                    right[cur]=x
                    path+=depth
                    break
                cur=right[cur]
    leaves=sum(1 for x in p if left[x]==-1 and right[x]==-1)
    return leaves,path

def run():
    permutations_checked=0
    mean_checks=0
    covariance_checks=0
    variance_checks=0
    slope_checks=0
    recurrence_checks=0

    for n in range(1,10):
        N=factorial(n)
        sL=sP=sL2=sLP=0
        for p in permutations(range(1,n+1)):
            L,P=bst_stats(p)
            sL+=L; sP+=P; sL2+=L*L; sLP+=L*P
        permutations_checked+=N
        EL=Fraction(sL,N); EP=Fraction(sP,N)
        assert EL==target_EL(n)
        assert EP==target_EP(n)
        mean_checks+=2
        varL=Fraction(sL2,N)-EL*EL
        assert varL==target_varL(n)
        variance_checks+=1
        cov=Fraction(sLP,N)-EL*EP
        assert cov==target_cov(n)
        covariance_checks+=1
        if n>=4:
            assert cov/varL==-Fraction(5,2)*Fraction((n-2)*(n+3),n*(n+1))
            slope_checks+=1

    c=[Fraction(0)]*301
    v=[Fraction(0)]*301
    for n in range(2,301):
        EL=target_EL(n); EP=target_EP(n)
        cross=Fraction(0); between=Fraction(0)
        for k in range(n):
            r=n-1-k
            A=target_EL(k)+target_EL(r)
            B=target_EP(k)+target_EP(r)+(n-1)
            cross+=(A-EL)*(B-EP)/n
            between+=(A-EL)*(A-EL)/n
        c[n]=Fraction(2,n)*sum(c[:n])+cross
        v[n]=Fraction(2,n)*sum(v[:n])+between
        assert c[n]==target_cov(n)
        assert v[n]==target_varL(n)
        recurrence_checks+=2

    print(
        'VERIFY_OK '
        f'permutations_checked={permutations_checked} '
        f'mean_checks={mean_checks} '
        f'covariance_checks={covariance_checks} '
        f'variance_checks={variance_checks} '
        f'slope_checks={slope_checks} '
        f'recurrence_checks={recurrence_checks}'
    )

if __name__=='__main__':
    run()
