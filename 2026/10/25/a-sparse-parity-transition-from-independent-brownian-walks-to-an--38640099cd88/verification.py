"""Independent finite-state checks for sparse Boolean parity transforms.
Scientific status: finite checks only; the functional limit is proved analytically.
"""
from fractions import Fraction
from math import comb, ceil, log
from itertools import product

def p_n(n,theta_num,theta_den):
    return Fraction(1,2 ** (ceil(Fraction(n*theta_num,theta_den))+2))

def parity_mean(k,p):
    return (1-2*p)**(2**k)

count=0
for a,b in [(1,4),(1,2),(3,4),(5,4)]:
    for n in range(1,7):
        p=p_n(n,a,b)
        for k in range(n+1):
            total=sum(Fraction(comb(2**k,j))*p**j*(1-p)**(2**k-j)*(-1)**j for j in range(2**k+1))
            assert total==parity_mean(k,p)
            count+=1
for n in range(1,4):
    p=p_n(n,1,2)
    subsets=[tuple(j for j in range(n) if mask&(1<<j)) for mask in range(2**n)]
    for xi in product([-1,1],repeat=n):
        neg={j for j,x in enumerate(xi) if x==-1}
        active=[i for i,K in enumerate(subsets) if all(j in neg for j in K)]
        k=len(neg)
        assert len(active)==2**k
        mean=Fraction(0)
        for beta in product([0,1],repeat=2**n):
            wt=p**sum(beta)*(1-p)**(2**n-sum(beta))
            z=(-1)**sum(beta[i] for i in active)
            mean+=wt*z
        assert mean==parity_mean(k,p)
        count+=1
print('PASS',count,'exact-rational parity and model assertions')
