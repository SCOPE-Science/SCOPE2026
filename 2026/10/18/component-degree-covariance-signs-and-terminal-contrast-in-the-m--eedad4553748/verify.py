"""Exact finite verification for component/degree-count covariances of the Moran forest.

The independent sampler directly enumerates each older-vertex attachment choice.
No third-party dependencies are required. Finite tests are not a proof of limits.
"""
from fractions import Fraction as F
from itertools import product
from math import comb, e


def binom_p(k, r, m):
    if k < 0 or not 0 <= r <= k:
        return F(0)
    return F(comb(k, r), m ** r) * F(m - 1, m) ** (k - r)


def degree_cov_formula(n, r):
    if n == 2 or r > n - 1 or r < 0:
        return F(0)
    m = n - 1
    total = F(0)
    for k in range(1, m + 1):
        aa = (m-k)*(m-1)+F(k*(k-1),2)
        bb = F((m-k)*(k+1),2)
        a = binom_p(k-1, r, m)-binom_p(k-1, r-1, m)
        b = binom_p(k-1, r-1, m)-binom_p(k-1, r-2, m)
        total += F(k,m**3)*(aa*a+bb*b)
    return total


def degree_one_simplified(n):
    if n <= 3:
        return F(0)
    m=n-1; a=F(m-1,m)
    return -sum((F(k*(m-k)*(m-k-1)*(2*m-k-1),2*m**4)*a**(k-2)
                 for k in range(1,m-1)),F(0))


def terminal_cov_formula(n):
    if n == 2: return F(0)
    m=n-1; a=F(m-1,m)
    return sum((F(k*(k-1),2*m*m)*a**(k-1) for k in range(2,m+1)),F(0))


def enumerated_covariances(n):
    m=n-1
    total=m**m
    choices=[[u for u in range(1,n+1) if u!=v] for v in range(2,n+1)]
    accum=[0]*(n+1)
    cross=[0]*(n+1)
    ksum=zsum=kzsum=0
    for us in product(*choices):
        indeg=[0]*n;outdeg=[0]*n
        for v,u in enumerate(us,2):
            if u<v:
                indeg[v-1]=1;outdeg[u-1]+=1
        num_components=n-sum(indeg)
        num_terminals=outdeg.count(0)
        histogram=[0]*(n+1)
        for d_in,d_out in zip(indeg,outdeg):
            histogram[d_in+d_out]+=1
        ksum+=num_components;zsum+=num_terminals;kzsum+=num_components*num_terminals
        for r in range(n+1):
            accum[r]+=histogram[r]
            cross[r]+=num_components*histogram[r]
    result=[F(c,total)-F(ksum*count,total*total)
            for c,count in zip(cross,accum)]
    terminal=F(kzsum,total)-F(ksum*zsum,total*total)
    return result,terminal


def float_cov_limits(n):
    m=n-1; a=1-1/m
    cov_terminal=sum(k*(k-1)/(2*m*m)*a**(k-1) for k in range(2,m+1))
    cov_one=-sum(k*(m-k)*(m-k-1)*(2*m-k-1)/(2*m**4)*a**(k-2)
                 for k in range(1,m-1))
    return cov_terminal/n,cov_one/n


def main():
    asserts=0
    for n in range(2,9):
        empirical, terminal=enumerated_covariances(n)
        for r in range(n+1):
            assert degree_cov_formula(n,r)==empirical[r], (n,r)
            asserts+=1
        assert terminal_cov_formula(n)==terminal,(n,'terminal')
        asserts+=1
        assert sum(empirical)==0,(n,'degree-class conservation')
        asserts+=1
        print('exhaustive',n,(n-1)**(n-1),'cov_deg_one',empirical[1],
              'cov_terminal',terminal)
    for n in range(3,71):
        assert degree_cov_formula(n,1)==degree_one_simplified(n),n
        assert degree_cov_formula(n,0)>0,n
        assert (degree_cov_formula(n,1)<0)==(n>=4),n
        for r in range(2,n):
            assert degree_cov_formula(n,r)<0,(n,r)
            asserts+=1
        asserts+=3
    for n in (201,501,1001,5001):
        positive,negative=float_cov_limits(n)
        assert abs(positive-(1-5/(2*e)))<1/n,(n,positive)
        assert abs(negative-(4-11/e))<1/n,(n,negative)
        asserts+=2
        print('asymptotic_scale',n,positive,negative)
    print('VERIFY_OK exact/numeric assertions',asserts)

if __name__=='__main__':
    main()
