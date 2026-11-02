#!/usr/bin/env python3
"""Independent exact finite-state and asymptotic checks for private-signal star learning."""
from fractions import Fraction as Q
from functools import lru_cache
from math import comb, erf, sqrt, exp, pi

def local_error(k,p):
    q=1-p
    total=Q(0)
    for j in range(k+1):
        v=comb(k,j)*p**j*q**(k-j)
        if j*2<k: total+=v
        elif j*2==k: total+=v*q
    return total

def exact_mixture(m,p,rho):
    w=rho/(m+rho)
    value=Q(0); mass=Q(0)
    for k in range(m+1):
        value += w*local_error(k,p)
        mass += w
        if k<m: w *= Q(m-k)/(m-k-1+rho)
    assert mass==1, (m,rho,mass)
    return value

def direct_recursive(m,p,rho):
    @lru_cache(None)
    def value(correct,wrong):
        remain=m-correct-wrong
        if correct>wrong: stop=Q(0)
        elif wrong>correct: stop=Q(1)
        else: stop=1-p
        if remain==0: return stop
        denom=rho+remain
        return rho/denom*stop + Q(remain,1)/denom*(p*value(correct+1,wrong)+(1-p)*value(correct,wrong+1))
    return value(0,0)

def b(j,p):
    return sum((Q(comb(2*j+1,i))*p**i*(1-p)**(2*j+1-i) for i in range(j+1)),Q(0))

def phi(x): return exp(-x*x/2)/sqrt(2*pi)
def Phi(x): return (1+erf(x/sqrt(2)))/2

def critical_equal(alpha):
    if alpha==0: return .5
    z=2*alpha
    return Phi(-z)+(Phi(z)-.5)/z**2-phi(z)/z

checks=0
for m in range(1,17):
    for p in [Q(1,2),Q(3,5),Q(2,3),Q(3,4),Q(9,10)]:
        for rho in [Q(1,3),Q(1,2),Q(1),Q(7,3),Q(2),Q(5)]:
            a=exact_mixture(m,p,rho)
            c=direct_recursive(m,p,rho)
            assert a==c,(m,p,rho,a,c)
            checks+=1
            if rho==1:
                assert a==sum((local_error(k,p) for k in range(m+1)),Q(0))/(m+1)
                assert a==(2*sum((b(j,p) for j in range((m+1)//2)),Q(0))+(b(m//2,p) if m%2==0 else 0))/(m+1)
                checks+=2
print('exact rational recurrence comparisons:',checks)

# Direct simulation by full signal-pattern and first-activation order on small stars.
from itertools import permutations,product
for m in range(1,7):
    p=Q(3,5)
    total=Q(0)
    orders=list(permutations(range(m+1)))
    for bits in product((0,1),repeat=m+1):
        num_ones=sum(bits)
        signal_prob=p**num_ones*(1-p)**(m+1-num_ones)
        wrong_orders=0
        for order in orders:
            first_center=order.index(0)
            announced=[bits[j] for j in order[:first_center]]
            correct=sum(announced)
            wrong=len(announced)-correct
            center_correct=correct>wrong or (correct==wrong and bits[0]==1)
            wrong_orders += int(not center_correct)
        total+=signal_prob*Q(wrong_orders,len(orders))
    expected=exact_mixture(m,p,Q(1))
    assert total==expected,(m,total,expected)
print('full activation-order and signal enumeration: m=1..6 passed')

from math import lgamma, log, floor, fsum

def lower_binomial_tail(n,p,j):
    if j<0: return 0.0
    if j>=n: return 1.0
    if p==0: return 1.0
    if p==1: return 0.0
    v=exp(lgamma(n+1)-lgamma(j+1)-lgamma(n-j+1)+j*log(p)+(n-j)*log(1-p))
    terms=[v]
    for t in range(j,0,-1):
        v*=t*(1-p)/((n-t+1)*p)
        terms.append(v)
    return fsum(terms)

def pmf(n,p,j):
    return exp(lgamma(n+1)-lgamma(j+1)-lgamma(n-j+1)+j*log(p)+(n-j)*log(1-p))

def floating_mixture(m,p):
    q=1-p
    return fsum(lower_binomial_tail(k,p,(k-1)//2) if k%2 else
                lower_binomial_tail(k,p,k//2-1)+q*pmf(k,p,k//2)
                for k in range(m+1))/(m+1)
for m in [200,800,3200]:
    p=.73
    v=floating_mixture(m,p)
    target=2*p*(1-p)/(2*p-1)**2
    print('m, m*error, constant:',m,round(m*v,8),round(target,8))
    assert abs(m*v-target)<0.03
for alpha in [0,.25,.5,1,2]:
    m=2000
    p=.5+alpha/sqrt(m)
    approx=floating_mixture(m,p)
    limit=critical_equal(alpha)
    print('alpha, m=2000 error, critical limit:',alpha,round(approx,8),round(limit,8))
    assert abs(approx-limit)<0.01
print('ALL VERIFICATION CHECKS PASSED')
