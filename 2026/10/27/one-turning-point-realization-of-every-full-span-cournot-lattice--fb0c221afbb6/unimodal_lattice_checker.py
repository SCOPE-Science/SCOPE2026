"""Exact-rational checks of finite input/output identities for a Cournot construction.
The infinite omega-limit assertion rests on the mathematical proof, not this checker.
"""
from fractions import Fraction as Q
from random import Random

def T(x):
    return 2*x if x<=Q(1,2) else 2*(1-x)

def interp(nodes, x):
    assert nodes[0][0] <= x <= nodes[-1][0]
    for (a,fa),(b,fb) in zip(nodes,nodes[1:]):
        if a<=x<=b:
            return fa+(x-a)*(fb-fa)/(b-a)
    raise AssertionError(x)

def build(p,q):
    m=len(p)
    d=2**(2*m)+1
    orbit=[Q(2**(i+1),d) for i in range(2*m)]
    xp=[Q(0), *orbit[::2], Q(1)]
    xq=[Q(0), *orbit[1::2], Q(1)]
    np=list(zip(xp, [Q(0),*p,Q(1)]))
    nq=list(zip(xq, [Q(0),*q,Q(1)]))
    h=lambda x:interp(np,x)
    k=lambda x:interp(nq,x)
    hi=lambda x:interp([(b,a) for a,b in np],x)
    ki=lambda x:interp([(b,a) for a,b in nq],x)
    f=lambda x:k(T(hi(x)))
    g=lambda x:h(T(ki(x)))
    return orbit,h,k,f,g,hi,ki

rng=Random(20261022)
cases=0
points=0
for m in range(1,7):
 for example in range(30):
    pp=sorted(rng.sample(range(1,300),m))
    qq=sorted(rng.sample(range(1,300),m))
    p=[Q(x,300) for x in pp]
    q=[Q(x,300) for x in qq]
    orbit,h,k,f,g,hi,ki=build(p,q)
    assert len(set(orbit))==2*m
    assert all(T(orbit[i])==orbit[(i+1)%(2*m)] for i in range(2*m))
    assert all(f(p[i])==q[i] for i in range(m))
    assert all(g(q[i])==p[(i+1)%m] for i in range(m))
    for j in range(31):
       x=Q(j,30)
       assert f(x)==k(T(hi(x))) and g(x)==h(T(ki(x)))
       assert g(f(x))==h(T(T(hi(x))))
       assert f(g(x))==k(T(T(ki(x))))
       points+=1
    assert f(Q(0))==0 and f(Q(1))==0 and g(Q(0))==0 and g(Q(1))==0
    assert f(h(Q(1,2)))==1 and g(k(Q(1,2)))==1
    cases+=1
print(f'CHECKS_PASS {cases} configurations; {points} exact-rational composition tests; orbit and unimodal-endpoint identities verified')
