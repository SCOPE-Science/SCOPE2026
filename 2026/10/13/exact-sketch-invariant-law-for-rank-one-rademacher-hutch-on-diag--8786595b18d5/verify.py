from fractions import Fraction as F
from itertools import product
from collections import Counter

def signs(n):
    return product((-1,1), repeat=n)

def estimator(a,s,z):
    n=len(a)
    S=sum(x*x for x in a)
    T=sum(x*x*x for x in a)
    p=[a[i]*s[i] for i in range(n)]
    mu=T/S
    B=[[a[i]*int(i==j)-p[i]*p[j]*(a[i]+a[j])/S+T*p[i]*p[j]/(S*S)
        for j in range(n)] for i in range(n)]
    return mu+sum(F(z[i]*z[j])*B[i][j] for i in range(n) for j in range(n))

def walk_formula(a,s,z):
    S=sum(x*x for x in a)
    T=sum(x*x*x for x in a)
    w=[s[i]*z[i] for i in range(len(a))]
    U=sum(a[i]*w[i] for i in range(len(a)))
    V=sum(a[i]*a[i]*w[i] for i in range(len(a)))
    return sum(a)+T/S-2*U*V/S+T*U*U/(S*S)

def variance_formula(a):
    S=sum(x*x for x in a)
    T=sum(x*x*x for x in a)
    mu=T/S
    return 4*sum((a[i]*a[j]/S*(mu-a[i]-a[j]))**2
                 for i in range(len(a)) for j in range(i+1,len(a)))

for values in ((1,1),(1,2),(1,2,3),(1,1,1),(1,3,5,7),(1,1,1,1,1),(1,2,3,4,5)):
    a=tuple(map(F,values))
    n=len(a)
    distribution=None
    for s in signs(n):
        scores=[]
        for z in signs(n):
            v=estimator(a,s,z)
            assert v==walk_formula(a,s,z)
            scores.append(v)
        c=Counter(scores)
        if distribution is None:
            distribution=c
        else:
            assert c==distribution
    number=sum(distribution.values())
    mean=sum(x*m for x,m in distribution.items())/number
    var=sum(m*(x-mean)**2 for x,m in distribution.items())/number
    assert mean==sum(a)
    assert var==variance_formula(a)
    assert var>0

# Two residual probes, with one sketch, must simply divide the one-probe variance by two.
for values in ((1,2),(1,2,3),(1,1,1,1)):
    a=tuple(map(F,values));n=len(a)
    s=tuple(((-1)**i) for i in range(n))
    scores=[estimator(a,s,z) for z in signs(n)]
    doubled=[(x+y)/2 for x in scores for y in scores]
    mean=sum(doubled)/len(doubled)
    var=sum((x-mean)**2 for x in doubled)/len(doubled)
    assert var==variance_formula(a)/2

for n in range(2,7):
    a=(F(1),)*n
    v=variance_formula(a)
    assert v==F(2*(n-1),n)
    for s in signs(n):
        for z in signs(n):
            w=sum(s[i]*z[i] for i in range(n))
            assert estimator(a,s,z)==F(n+1)-F(w*w,n)

c=Counter(estimator((F(1),F(1)),(1,-1),z) for z in signs(2))
assert c==Counter({F(1):2,F(3):2})
assert all(abs(x-F(2))==F(1) for x in c)
print('verification passed: exact rank-one conditional distribution and variance')
