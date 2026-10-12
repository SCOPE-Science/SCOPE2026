import math
import random

def dot(x,y):
    return sum(a*b for a,b in zip(x,y))

def add(x,y):
    return [a+b for a,b in zip(x,y)]

def mul(s,x):
    return [s*a for a in x]

def norm(x):
    return math.sqrt(dot(x,x))

def pair(a,b,rho):
    return [a,0.0],[b*rho,b*math.sqrt(1.0-rho*rho)]

def weights(a,b,rho):
    s=math.sqrt(1.0+rho)
    return 1.0/(a*s),1.0/(b*s)

random.seed(350074)

for _ in range(5000):
    a=10.0**random.uniform(-2.0,2.0)
    b=10.0**random.uniform(-2.0,2.0)
    rho=random.uniform(-0.995,0.995)
    g1,g2=pair(a,b,rho)
    al1,al2=weights(a,b,rho)
    # Exact source equations.
    lhs1=dot(g1,g1)*al1+dot(g1,g2)*al2
    lhs2=dot(g2,g1)*al1+dot(g2,g2)*al2
    assert abs(lhs1-1.0/al1) < 2e-10*max(1.0,abs(lhs1))
    assert abs(lhs2-1.0/al2) < 2e-10*max(1.0,abs(lhs2))

    # Pure independent magnitude changes: fresh solve leaves direction unchanged up to scale.
    s1=10.0**random.uniform(-2.0,2.0)
    s2=10.0**random.uniform(-2.0,2.0)
    h1=mul(s1,g1); h2=mul(s2,g2)
    bl1,bl2=weights(s1*a,s2*b,rho)
    dfresh=add(mul(bl1,h1),mul(bl2,h2))
    target=mul(1.0/math.sqrt(1.0+rho),add(mul(1.0/a,g1),mul(1.0/b,g2)))
    assert norm([x-y for x,y in zip(dfresh,target)]) < 3e-10

    # Stale direction signs match the analytic criteria.
    dstale=add(mul(al1,h1),mul(al2,h2))
    p1=dot(h1,dstale); p2=dot(h2,dstale)
    if rho>=0.0:
        assert p1>0.0 and p2>0.0
    else:
        q=s1/s2
        safe=(-rho < q < -1.0/rho)
        assert (p1>0.0 and p2>0.0)==safe
        if q < -rho:
            assert p1<0.0 and p2>0.0
        if q > -1.0/rho:
            assert p1>0.0 and p2<0.0

# Exact boundary cases for several conflicts.
for rho in (-0.95,-0.8,-0.5,-0.2):
    a,b=2.0,3.0
    g1,g2=pair(a,b,rho)
    al1,al2=weights(a,b,rho)
    for q,which in ((-rho,1),(-1.0/rho,2)):
        h1=mul(q,g1); h2=g2
        d=add(mul(al1,h1),mul(al2,h2))
        p1=dot(h1,d); p2=dot(h2,d)
        if which==1:
            assert abs(p1)<2e-12 and p2>0.0
        else:
            assert p1>0.0 and abs(p2)<2e-12

# Log formulation is equivalent in the conflict regime.
for rho in (-0.99,-0.7,-0.3,-0.05):
    radius=-math.log(-rho)
    for z in (-1.2*radius,-0.5*radius,0.0,0.5*radius,1.2*radius):
        q=math.exp(z)
        assert ((-rho<q<-1.0/rho) == (abs(z)<radius))

print('verification passed')
