"""Reproducibility checks for a fixed-depth unit-hopping wealth model.

Only ordinary mathematical computations: finite checks do not prove asymptotic claims.
"""
from fractions import Fraction as Q
from itertools import combinations
from math import comb, exp, factorial, log
import random


def compositions(total, count):
    if count == 1:
        yield (total,)
    else:
        for first in range(total + 1):
            for rest in compositions(total-first, count-1):
                yield (first,) + rest


def multinomial_prob(counts, p):
    m = sum(counts)
    out = Q(factorial(m))
    for k, pr in zip(counts,p):
        out *= pr ** k / factorial(k)
    return out


def expected_values_enum(p,m):
    L=len(p)
    assert sum(p)==1
    eg=Q(0)
    ev=Q(0)
    total=Q(0)
    for x in compositions(m,L):
        w=multinomial_prob(x,p)
        total+=w
        eg+= w * Q(sum(abs(x[i]-x[j]) for i,j in combinations(range(L),2)),L*m)
        ev+= w * Q(sum(z==0 for z in x),L)
    assert total==1
    return eg,ev


def expected_values_formula(p,m):
    L=len(p)
    vacancy=sum((1-x)**m for x in p)/L
    g=Q(0)
    for i,j in combinations(range(L),2):
        s=p[i]+p[j]
        q=p[i]/s
        pair=Q(0)
        for n in range(m+1):
            bin1=comb(m,n)*s**n*(1-s)**(m-n)
            inner=sum(comb(n,k)*q**k*(1-q)**(n-k)*abs(2*k-n) for k in range(n+1))
            pair+=bin1*inner
        g+=pair/(L*m)
    return g,vacancy


def check_exact_stationarity():
    r=[Q(1),Q(2),Q(4)]
    p=[x/sum(r) for x in r]
    for m in (2,4,6):
        for x in compositions(m,3):
            px=multinomial_prob(x,p)
            for i,j in ((0,1),(1,0),(1,2),(2,1),(2,0),(0,2)):
                if x[i]==0: continue
                y=list(x); y[i]-=1; y[j]+=1; y=tuple(y)
                py=multinomial_prob(y,p)
                out=px*x[i]*min(Q(1),r[j]/r[i])/2
                back=py*y[j]*min(Q(1),r[i]/r[j])/2
                assert out==back, (m,x,i,j,out,back)
        e1=expected_values_enum(p,m)
        e2=expected_values_formula(p,m)
        assert e1==e2,(m,e1,e2)
        print('exact detailed balance and Gini/vacancy formula',m,tuple(str(x) for x in e1))
    for m in (2,5,9):
        for p in ([Q(1,3)]*3,[Q(1,7),Q(2,7),Q(4,7)], [Q(2,7),Q(2,7),Q(3,7)]):
            assert expected_values_enum(p,m)==expected_values_formula(p,m)
        unequal=expected_values_enum([Q(1,7),Q(2,7),Q(4,7)],m)
        balanced=expected_values_enum([Q(2,7),Q(2,7),Q(3,7)],m)
        assert all(a>b for a,b in zip(unequal,balanced))
        print('strict pair-balancing Gini and vacancy',m,tuple(str(a-b) for a,b in zip(unequal,balanced)))
    assert expected_values_enum([Q(1,7),Q(2,7),Q(4,7)],1)==(Q(2,3),Q(2,3))


def expected_float_moments(p,m):
    L=len(p)
    vac=sum((1-v)**m for v in p)/L
    g=0.0
    for i,j in combinations(range(L),2):
        s=p[i]+p[j]
        q=p[i]/s
        for n in range(m+1):
            weight=comb(m,n)*s**n*(1-s)**(m-n)
            g+=weight*sum(comb(n,k)*q**k*(1-q)**(n-k)*abs(2*k-n) for k in range(n+1))/(L*m)
    return g,vac


def check_temperature_order():
    phi=[0.0,0.25,0.7,1.0]
    for m in (2,5,12):
        seq=[]
        for T in (0.09,0.15,0.3,0.8,2.0,50.0):
            a=[exp((v-max(phi))/T) for v in phi]
            p=[w/sum(a) for w in a]
            seq.append((T,)+expected_float_moments(p,m))
        assert all(seq[i][1]>seq[i+1][1]+1e-12 and seq[i][2]>seq[i+1][2]+1e-12 for i in range(len(seq)-1)),seq
        print('temperature ordered',m,[(t,round(g,9),round(v,9)) for t,g,v in seq])


def check_empirical_poisson():
    random.seed(1710)
    L=6000
    m=3
    T=0.4
    phi=[random.random() for _ in range(L)]
    weights=[exp(u/T) for u in phi]
    norm=sum(weights)
    p=[w/norm for w in weights]
    c=T*(exp(1/T)-1)
    # E_{phi}[e^-lambda(phi)] via midpoint quadrature, not sample fitting.
    F0=sum(exp(-m*exp((k+0.5)/10000/T)/c) for k in range(10000))/10000
    # Empirical stationary occupancy with M independent samples from p.
    counts=[0]*L
    # random.choices is an explicit multinomial sampler.
    for i in random.choices(range(L),weights=weights,k=m*L):
        counts[i]+=1
    obs=counts.count(0)/L
    assert abs(obs-F0)<0.04,(obs,F0)
    print('finite-L vacancy vs Poisson-mixture prediction',L,obs,F0)


if __name__=='__main__':
    check_exact_stationarity()
    check_temperature_order()
    check_empirical_poisson()
    print('ALL_FINITE_CHECKS_PASSED')
