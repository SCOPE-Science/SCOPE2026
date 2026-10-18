"""Independent exact enumeration and asymptotic recurrence checks for weighted recursive-tree path lengths."""
from fractions import Fraction as F
from itertools import product
from math import log, isclose


def moments_exact(weights):
    n=len(weights)
    W=[sum(weights[:k],F(0)) for k in range(1,n+1)]
    probs=[None,F(1)]+[weights[k-1]/W[k-1] for k in range(2,n+1)]
    expectation=F(0); second=F(0); mass=F(0)
    for choices in product(*(range(1,k) for k in range(2,n+1))):
        depths=[0]*(n+1); density=F(1)
        for child,parent in zip(range(2,n+1),choices):
            depths[child]=depths[parent]+1
            density*=weights[parent-1]/W[child-2]
        total=sum(depths)
        mass+=density; expectation+=density*total; second+=density*total*total
    assert mass==1
    v=F(0); predicted=F(0)
    for j in range(2,n+1):
        p=probs[j-1]  # past attachment fraction
        if j>=3:
            v=(1-p*p)*v+p*(1-p)
        pj=probs[j]
        predicted+=(1+(n-j)*pj)**2*v
    assert second-expectation**2==predicted, (second-expectation**2,predicted)
    return expectation, predicted


def recurrence_variance(beta,c,n):
    v=0.; ans=0.
    for j in range(2,n+1):
        if j>2:
            pprev=c*(j-1)**(-beta)
            v=(1-pprev*pprev)*v+pprev*(1-pprev)
        pj=c*j**(-beta)
        ans+=(1+(n-j)*pj)**2*v
    return ans


def leading_coeff(beta,c):
    if beta < 2/3:
        return 2*c**3/((1-beta)*(2-3*beta)*(3-3*beta)*(4-3*beta))
    if beta == 2/3:
        return 3*c**3
    return None

if __name__=='__main__':
    weights=[F(j,1) for j in range(1,8)]
    for n in range(3,8):
        mu,var=moments_exact(weights[:n])
        print('exact enumeration n=',n,'mean=',mu,'variance=',var)
    print('asymptotic recurrence ratios:')
    for beta in (0.55, 2/3, 0.8):
        c=0.6
        for n in (10000,100000):
            var=recurrence_variance(beta,c,n)
            if beta<2/3: scale=n**(4-3*beta)*leading_coeff(beta,c)
            elif beta==2/3: scale=n*n*log(n)*leading_coeff(beta,c)
            else: scale=n*n
            print('beta',beta,'n',n,'Var/scale',var/scale)
        assert recurrence_variance(beta,c,100000)>0
    print('All exact finite checks passed.')
