"""Exact-rational supplementary checks for robust stratified quadratic quadrature.

The theorem for all real node positions is proved analytically in RESULT.md;
finite tests do not replace that argument.
Run: python3 verify.py (Python standard library only).
"""
from fractions import Fraction as F
from itertools import product, combinations
from random import Random

M = F(1, 2)

def lower_upper(nodes):
    nodes = sorted(nodes)
    a, b = nodes[0], nodes[-1]
    assert a <= M <= b
    upper = (M-a)*(b-M)
    pairs = [(M-u)*(v-M) for u, v in combinations(nodes, 2) if u <= M <= v]
    return min(pairs), upper  # variances above M^2

def lower_bound(m):
    return F(1, m*m) if m%2 == 0 else F(3, 4*m*m)

def upper_bound(m):
    return F((m-2)**2,4*m*m)

def witness(m):
    assert m >= 3
    x=[F(2*i+1,2*m) for i in range(m)]
    x[0]=F(1,m);x[-1]=F(m-1,m)
    assert len(set(x))==m
    assert lower_upper(x)[1] == upper_bound(m)
    x=[F(2*i+1,2*m) for i in range(m)]
    k=m//2
    if m%2==0:
        x[k-1]=F(k-1,m);x[k]=F(k+1,m)
    else:
        x[k]=F(k,m);x[k+1]=F(k+2,m)
    assert len(set(x))==m
    assert lower_upper(x)[0] == lower_bound(m)

def exact_three_weights(nodes,mean,second):
    a,b,c=nodes
    return [(second-(b+c)*mean+b*c)/((a-b)*(a-c)),
            (second-(a+c)*mean+a*c)/((b-a)*(b-c)),
            (second-(a+b)*mean+a*b)/((c-a)*(c-b))]

def positive_all_weights(nodes,var):
    m=len(nodes)
    for exp in range(2,19):
        eps=F(1,m*(2**exp))
        left=1-m*eps
        mean=(M-eps*sum(nodes))/left
        second=(M*M+var-eps*sum(t*t for t in nodes))/left
        for inds in combinations(range(m),3):
            three=[nodes[i] for i in inds]
            if len(set(three))!=3: continue
            w=exact_three_weights(three,mean,second)
            if min(w)>=0:
                weights=[eps for _ in nodes]
                for index,wi in zip(inds,w): weights[index]+=left*wi
                assert all(wi>0 for wi in weights)
                assert sum(weights)==1
                assert sum(wi*x for wi,x in zip(weights,nodes))==M
                assert sum(wi*x*x for wi,x in zip(weights,nodes))==M*M+var
                return weights
    raise AssertionError('strictly positive weight construction failed')

def main():
    for m in range(3,151): witness(m)
    # Exhaust all 2^m combinations of closed-stratum endpoints for m <= 10.
    endpoint_cases=0
    for m in range(3,11):
        for bits in product((0,1), repeat=m):
            nodes=[F(i+bits[i],m) for i in range(m)]
            lo,hi=lower_upper(nodes)
            assert lo <= lower_bound(m)
            assert hi >= upper_bound(m)
            endpoint_cases+=1
    rng=Random(20261029)
    draws=0; constructed=0
    for m in range(5,26):
        v=(lower_bound(m)+upper_bound(m))/2
        for j in range(1000):
            nodes=[F(i,m)+F(rng.randrange(1,1000000),1000000*m) for i in range(m)]
            lo,hi=lower_upper(nodes)
            assert lo <= lower_bound(m)<v<upper_bound(m)<=hi
            if m<=10 and j<20:
                positive_all_weights(nodes,v)
                constructed+=1
            draws+=1
    assert lower_bound(5)==F(3,100)
    assert upper_bound(5)==F(9,100)
    assert lower_bound(5)<F(1,12)<upper_bound(5)
    assert upper_bound(4)==F(1,16)<F(1,12)
    print('OK: sharp rational witnesses for m=3..150')
    print('OK: complete endpoint-corner enumeration:', endpoint_cases)
    print('OK: 21000 rational random interior node sets')
    print('OK: explicit all-strict-positive rational quadrature constructions:', constructed)
    print('OK: uniform measure guaranteed from 5 strata, 4 insufficient')
if __name__=='__main__': main()
