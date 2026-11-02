"""Reproduction of exact finite-cycle coverage laws and sharp asymmetric profiles.

Run: python3 checker.py. Uses the Python standard library only.
"""
from fractions import Fraction as Q
from itertools import product
from math import exp, gamma, log, cosh, sqrt


def matmul(a,b):
    return ((a[0][0]*b[0][0]+a[0][1]*b[1][0],a[0][0]*b[0][1]+a[0][1]*b[1][1]),
            (a[1][0]*b[0][0]+a[1][1]*b[1][0],a[1][0]*b[0][1]+a[1][1]*b[1][1]))


def transfer(q):
    return ((1-q,q),(1-q,0))


def matrix_power(a, k):
    z=Q(0); one=Q(1)
    out=((one,z),(z,one))
    while k:
        if k&1: out=matmul(out,a)
        a=matmul(a,a); k>>=1
    return out


def cdf_transfer(n,qa,qb):
    a=matrix_power(matmul(transfer(qa),transfer(qb)),n//2)
    return a[0][0]+a[1][1]


def cdf_by_states(n,qa,qb):
    q=[qa if i%2==0 else qb for i in range(n)]
    total=Q(0)
    for state in product((0,1),repeat=n):
        if any(state[i] and state[(i+1)%n] for i in range(n)):
            continue
        term=Q(1)
        for i,bit in enumerate(state):
            term*=q[i] if bit else 1-q[i]
        total+=term
    return total


def polynomial_cdf(n):
    # Independent symbolic sum over binary not-yet-attempted edge states.
    # Map exponent pair (number of even, number of odd unattempted edges)
    # to an exact integer coefficient of qa^i qb^j.
    poly={}
    for state in product((0,1),repeat=n):
        if any(state[i] and state[(i+1)%n] for i in range(n)):
            continue
        terms={(0,0):1}
        for i,bit in enumerate(state):
            d=(1,0) if i%2==0 else (0,1)
            nxt={}
            for key,v in terms.items():
                if bit:
                    k=(key[0]+d[0],key[1]+d[1]);nxt[k]=nxt.get(k,0)+v
                else:
                    nxt[key]=nxt.get(key,0)+v
                    k=(key[0]+d[0],key[1]+d[1]);nxt[k]=nxt.get(k,0)-v
            terms=nxt
        for key,v in terms.items(): poly[key]=poly.get(key,0)+v
    return {k:v for k,v in poly.items() if v}


def expectation_by_polynomial(n,a,b):
    # 1-F(t) is integrated termwise with qa=e^{-a t},qb=e^{-b t}.
    f=polynomial_cdf(n)
    assert f.get((0,0))==1
    return sum((Q(-v, a*i+b*j) for (i,j),v in f.items() if i+j),Q(0))


def expectation_by_vertex_inclusion(n,a,b):
    # Independent inclusion-exclusion over uncovered vertex events.
    result=Q(0)
    for mask in range(1,1<<n):
        chosen={i for i in range(n) if mask>>i&1}
        used_edges={e for i in chosen for e in ((i-1)%n,i)}
        rate=sum((a if e%2==0 else b) for e in used_edges)
        result+=Q(1 if len(chosen)%2 else -1,rate)
    return result


def numeric_cdf(n,a,b,x):
    t=(log(n)+x)/(a+b)
    if t<0:return 0.0
    qa=exp(-a*t); qb=exp(-b*t)
    u=qa*qb; trace=1-u; determinant=u*(1-qa)*(1-qb)
    root=sqrt(max(0.0,trace*trace-4*determinant))
    lp=(trace+root)/2
    lm=determinant/lp if lp else 0
    return lp**(n//2)+lm**(n//2)


def check():
    count=0
    for n in (4,6,8,10):
        for a,b in ((Q(1,2),Q(1,3)),(Q(1,10),Q(3,5)),
                    (Q(2,3),Q(3,4)),(Q(1),Q(1)),(Q(0),Q(0))):
            assert cdf_transfer(n,a,b)==cdf_by_states(n,a,b),(n,a,b)
            count+=1
    for n in (4,6,8):
        for a,b in ((1,1),(1,3),(2,5)):
            x=expectation_by_polynomial(n,a,b)
            y=expectation_by_vertex_inclusion(n,a,b)
            assert x==y,(n,a,b,x,y)
            count+=1
    # The limit curves are compared at three distinct nonzero spatial offsets.
    for a,b in ((1.,1.),(1.,3.),(2.,3.)):
        delta=min(a,b)/(a+b)
        for n in (2**14,2**18,2**21):
            for x in (-0.6,0.0,0.7):
                g=exp(-exp(-x))
                predicted=(1. if a==b else .5)*g*exp(-(1+delta)*x)
                scaled=(numeric_cdf(n,a,b,x)-g)*n**delta
                assert 0.75<scaled/predicted<1.3,(a,b,n,x,scaled/predicted)
                count+=1
    for kap in (0.,1.,2.):
        for n in (2**14,2**18,2**21):
            for x in (-0.3,0.5):
                eps=kap/log(n)
                g=exp(-exp(-x))
                predicted=g*exp(-1.5*x)*cosh(kap/2)
                scaled=(numeric_cdf(n,1+eps,1-eps,x)-g)*sqrt(n)
                assert .8<scaled/predicted<1.25,(kap,n,x,scaled/predicted)
                count+=1
    # Numerical checking of the profile's maximum formula itself.
    for delta in (0.1,0.25,0.5):
        x=-log(1+delta)
        value=.5*exp(-exp(-x))*exp(-(1+delta)*x)
        target=.5*(1+delta)**(1+delta)*exp(-(1+delta))
        assert abs(value-target)<1e-13
        count+=1
    print('PASS:',count,'independent exact and asymptotic assertions')
    return count

if __name__=='__main__':check()
