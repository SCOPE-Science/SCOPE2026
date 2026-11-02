"""Standalone exact-rational checks for the finite herding identification theorem.

Run using Python 3 standard library: python check.py.
The finite checks are corroboration of the proof, not a replacement for it.
"""
from fractions import Fraction as Q
from random import Random


def stationary(N, a, b, h):
    weights = [Q(1)]
    for k in range(N):
        birth = (N-k)*(a+h*k)
        death = (k+1)*(b+h*(N-k-1))
        assert birth > 0 and death > 0
        weights.append(weights[-1]*birth/death)
    Z = sum(weights)
    return [w/Z for w in weights]


def observable_moments(N, a, b, h, p):
    A=a+b
    r=a/A
    V=N*r*(1-r)*(A+N*h)/(A+h)
    m=p*N*r
    s=p*p*V
    v=s+m*(1-p)
    return m,v,s


def inverse(N, m, v, c1, c2, A):
    s=c1*c1/c2
    p=1-(v-s)/m
    r=m/(N*p)
    R=s/(p*m-m*m/N)
    return p, A*r, A*(1-r), A*(R-1)/(N-R), R


def identified_sizes(m, v, c1, c2, cutoff):
    s=c1*c1/c2
    p=1-(v-s)/m
    L=(s+m*m)/(p*m)
    U=m*m/(p*m-s) if p*m>s else None
    sizes=[N for N in range(2,cutoff+1) if N>L and (U is None or N<U)]
    return p,L,U,sizes

rng=Random(70129)
tests=0
for N in range(2,13):
    for run in range(100):
        a=Q(rng.randint(1,15),rng.randint(1,15))
        b=Q(rng.randint(1,15),rng.randint(1,15))
        h=Q(rng.randint(1,15),rng.randint(1,15))
        p=Q(rng.randint(1,10),11)
        weights=stationary(N,a,b,h)
        M=sum(k*w for k,w in enumerate(weights))
        V=sum((k-M)**2*w for k,w in enumerate(weights))
        m,v,s=observable_moments(N,a,b,h,p)
        A=a+b
        # Taking the lag to be (log 2)/A gives exact covariance multipliers.
        c1,c2=s/Q(2),s/Q(4)
        assert sum(weights)==1; tests+=1
        assert M==N*a/A; tests+=1
        assert V==s/(p*p); tests+=1
        assert v==p*p*V+m*(1-p); tests+=1
        pp,aa,bb,hh,R=inverse(N,m,v,c1,c2,A)
        assert (pp,aa,bb,hh)==(p,a,b,h); tests+=1
        assert 1<R<N; tests+=1
        pp2,L,U,sizes=identified_sizes(m,v,c1,c2,80)
        assert pp2==p and N in sizes; tests+=1
        assert all((L<j) and (U is None or j<U) for j in sizes); tests+=1
        assert all(j not in sizes for j in range(2,81) if not (L<j and (U is None or j<U))); tests+=1

cases=[
    (4,Q(1),Q(2),Q(1),Q(3,4),Q(1),Q(9,8),Q(7,16),Q(7,32),Q(5,2),None),
    (4,Q(9),Q(1),Q(1,100),Q(3,4),Q(27,10),Q(175797,200200),Q(20331,200200),Q(20331,400400),Q(3704,1001),Q(6006,1501)),
]
for N,a,b,h,p,em,ev,ec1,ec2,eL,eU in cases:
    m,v,s=observable_moments(N,a,b,h,p)
    c1,c2=s/Q(2),s/Q(4)
    assert (m,v,c1,c2)==(em,ev,ec1,ec2); tests+=1
    pp,L,U,sizes=identified_sizes(m,v,c1,c2,100)
    assert (pp,L,U)==(p,eL,eU); tests+=1
    assert (sizes==[4] if eU is not None else sizes==list(range(3,101))); tests+=1
    for j in sizes:
        p2,a2,b2,h2,R=inverse(j,m,v,c1,c2,a+b)
        assert p2==p and min(a2,b2,h2)>0; tests+=1
        assert observable_moments(j,a2,b2,h2,p)==(m,v,s); tests+=1

print(f"PASS: {tests} exact-rational assertions, 1100 detailed-balance distributions, and 2 boundary examples")
