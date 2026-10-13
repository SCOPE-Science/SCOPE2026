import itertools
import math
import random

rng = random.Random(350066)

def exact_distribution_moments(g):
    d = len(g)
    M = max(abs(x) for x in g)
    if M == 0.0:
        return [0.0]*d, 0.0, 0.0
    p = [abs(x)/M for x in g]
    mean = [0.0]*d
    second = 0.0
    err = 0.0
    for bits in itertools.product((0, 1), repeat=d):
        prob = 1.0
        q = []
        for x, pi, bi in zip(g, p, bits):
            prob *= pi if bi else (1.0-pi)
            sgn = 0.0 if x == 0.0 else (1.0 if x > 0.0 else -1.0)
            q.append(M*sgn*bi)
        for i, qi in enumerate(q):
            mean[i] += prob*qi
        second += prob*sum(qi*qi for qi in q)
        err += prob*sum((qi-xi)**2 for qi,xi in zip(q,g))
    return mean, second, err

def ratio(g):
    M=max(abs(x) for x in g)
    l1=sum(abs(x) for x in g)
    l2=sum(x*x for x in g)
    return 0.0 if l2 == 0.0 else M*l1/l2

def sharp_ratio(d):
    return (math.sqrt(d)+1.0)/2.0

def extremizer(d):
    if d == 1:
        return [1.0]
    t=1.0/(math.sqrt(d)+1.0)
    return [1.0]+[t]*(d-1)

# Exact distribution replay.
for d in range(1,9):
    for _ in range(40):
        g=[rng.uniform(-2.0,2.0) for _ in range(d)]
        if max(abs(x) for x in g) < 1e-12:
            continue
        mean, second, err = exact_distribution_moments(g)
        M=max(abs(x) for x in g)
        expected_second=M*sum(abs(x) for x in g)
        norm2=sum(x*x for x in g)
        for a,b in zip(mean,g):
            assert abs(a-b) < 3e-12*max(1.0,abs(b))
        assert abs(second-expected_second) < 5e-12*max(1.0,expected_second)
        assert abs(err-(expected_second-norm2)) < 5e-12*max(1.0,err,norm2)

# Equality family and sharp variance constant.
for d in list(range(1,101))+[256,1024]:
    g=extremizer(d)
    r=ratio(g)
    assert abs(r-sharp_ratio(d)) < 2e-13*max(1.0,r)
    omega=r-1.0
    target=(math.sqrt(d)-1.0)/2.0
    assert abs(omega-target) < 2e-13*max(1.0,target)

# Random vectors never beat the proved constant.
for d in (2,3,5,10,25,100):
    sr=sharp_ratio(d)
    for _ in range(5000):
        g=[rng.expovariate(1.0)*(1 if rng.random()<0.5 else -1) for _ in range(d)]
        assert ratio(g) <= sr*(1+2e-13)

# Direct objective expectation by enumeration.
for d in range(1,9):
    L=1.7
    for _ in range(30):
        x=[rng.uniform(-2.0,2.0) for _ in range(d)]
        if max(abs(z) for z in x)<1e-12:
            continue
        h=rng.uniform(0.01,1.5)
        eta=h/L
        g=[L*z for z in x]
        M=max(abs(z) for z in g)
        p=[abs(z)/M for z in g]
        f0=0.5*L*sum(z*z for z in x)
        expf=0.0
        for bits in itertools.product((0,1), repeat=d):
            prob=1.0
            q=[]
            for gi,pi,bi in zip(g,p,bits):
                prob *= pi if bi else (1-pi)
                sgn=1.0 if gi>0 else (-1.0 if gi<0 else 0.0)
                q.append(M*sgn*bi)
            xp=[xi-eta*qi for xi,qi in zip(x,q)]
            expf += prob*0.5*L*sum(z*z for z in xp)
        target=f0*(1-2*h+h*h*ratio(x))
        assert abs(expf-target)<8e-12*max(1.0,abs(target),f0)

# Sharp descent boundary and minimax step.
for d in (1,2,3,9,10,25,100):
    R=sharp_ratio(d)
    boundary=2.0/R
    hstar=1.0/R
    worst=lambda h: 1-2*h+R*h*h
    assert worst(0.999*boundary) < 1.0
    assert abs(worst(boundary)-1.0) < 5e-14
    assert worst(1.001*boundary) > 1.0
    target=(math.sqrt(d)-1)/(math.sqrt(d)+1)
    assert abs(worst(hstar)-target)<5e-14

assert abs((math.sqrt(9)-1)/2-1.0)<1e-15
assert (math.sqrt(10)-1)/2>1.0

print("verification passed")
