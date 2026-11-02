"""Exact six-node WENO-CMS conditioning checks and random finite tests.

Runs with Python 3 standard library only. Analytical estimates and all-parameter
statements are proved in RESULT.md; these tests are supplementary.
"""
from fractions import Fraction as F
from math import prod
from random import Random

X = tuple(map(F, ['0','1/4','1','2','11/4','3']))
TAU = ((0,2),(3,5),(0,1),(4,5))
EXTRA = ((1,),(4,),(2,),(3,))
H = F(1)
TARGET = F(3,2)


def linear_interp(data, pair, x):
    i,k = pair
    a,b = X[i],X[k]
    return data[i]*(b-x)/(b-a)+data[k]*(x-a)/(b-a)


def geometric_weight(pair, exponent, x=TARGET):
    radius = abs(X[pair[1]]-X[pair[0]])+H
    factors = []
    for i in pair:
        distance = abs(x-X[i])
        if distance >= radius:
            return F(0)
        factors.append((1/distance-1/radius)**exponent)
    return prod(factors)


def indicator(data,j):
    return sum((abs(data[i]-linear_interp(data,TAU[j],X[i])) for i in EXTRA[j]),F(0))/len(EXTRA[j])


def output(data,epsilon,exponent,mu):
    weights = [geometric_weight(pair,mu) for pair in TAU]
    assert sum(w>0 for w in weights)==2
    scores=[w/(epsilon+indicator(data,j))**exponent for j,w in enumerate(weights)]
    return sum((a*linear_interp(data,pair,TARGET) for a,pair in zip(scores,TAU)),F(0))/sum(scores)


def norm_lagrange(pair,x):
    i,k=pair;a,b=X[i],X[k]
    return abs((b-x)/(b-a))+abs((x-a)/(b-a))


def constants():
    active=[j for j,pair in enumerate(TAU) if geometric_weight(pair,2)>0]
    Lam=max(norm_lagrange(TAU[j],TARGET) for j in active)
    Hc=max(sum((1+norm_lagrange(TAU[j],X[i]) for i in EXTRA[j]),F(0))/len(EXTRA[j]) for j in active)
    return Lam,Hc


def test_exact():
    base=tuple(map(F,[0,0,0,1,1,1]))
    assert X==(F(0),F(1,4),F(1),F(2),F(11,4),F(3))
    assert geometric_weight(TAU[0],2)==geometric_weight(TAU[1],2)==F(1,16)
    assert geometric_weight(TAU[2],2)==geometric_weight(TAU[3],2)==0
    assert all(indicator(base,j)==0 for j in range(4))
    assert all(linear_interp(base,TAU[j],TARGET)==F(j) for j in range(2))
    Lam,Hc=constants();assert Lam==2 and Hc==2 # expected? check
    checks=0
    for t in [1,2,3,4,5]:
        for mu in [1,2,4]:
            for k in [2,3,5,7,11,13,19]:
                eps=F(1,k)
                assert output(base,eps,t,mu)==F(1,2)
                for c in [F(1,10),F(1),F(3),F(100)]:
                    delta=c*eps
                    changed=list(base);changed[1]=delta
                    expected=(1+c)**t/(1+(1+c)**t)
                    assert output(tuple(changed),eps,t,mu)==expected
                    checks+=1
    return checks


def test_global_bound():
    rng=Random(675019)
    Lam,Hc=constants()
    checks=0
    for t in [1,2,4,6]:
      for mu in [1,2,3]:
       for k in range(150):
        u=tuple(F(rng.randrange(-10,11),5) for _ in X)
        v=tuple(a+F(rng.randrange(-5,6),20) for a in u)
        B=max([abs(a) for a in u+v])
        d=max(abs(a-b) for a,b in zip(u,v))
        eps=F(rng.randrange(1,20),100)
        left=abs(output(u,eps,t,mu)-output(v,eps,t,mu))
        right=Lam*(1+F(t)*B*Hc/eps)*d
        assert left<=right,(left,right)
        checks+=1
    return checks

if __name__=='__main__':
    print('exact_checks',test_exact())
    print('bound_checks',test_global_bound())
    print('six_node_x',X)
    print('stencils',TAU,'indicator_sets',EXTRA)
    print('constant_Lambda_H',constants())
    print('PASS: exact witness, geometry, all tested perturbation scales, and bounded-data global inequality')
