import math
import random

def dot(x,y):
    return sum(a*b for a,b in zip(x,y))

def norm(x):
    return math.sqrt(dot(x,x))

def add(x,y):
    return [a+b for a,b in zip(x,y)]

def mul(a,x):
    return [a*z for z in x]

def cosine(x,y):
    return dot(x,y)/(norm(x)*norm(y))

def pair(c,tau,A,B):
    theta=math.acos(c)
    gamma=math.acos(tau)
    g1=[A,0.0]
    g2=[B*math.cos(theta),B*math.sin(theta)]
    lam=math.sin(theta-gamma)/math.sin(gamma)
    g1p=add(g1,mul((A/B)*lam,g2))
    g2p=add(g2,mul((B/A)*lam,g1))
    return g1,g2,g1p,g2p,theta,gamma

random.seed(350074)

# Randomized exact identities and norm-ratio independence.
for _ in range(5000):
    c=random.uniform(-0.999,0.999)
    tau=random.uniform(c+1e-7,0.999999)
    A=10.0**random.uniform(-3,3)
    B=10.0**random.uniform(-3,3)
    g1,g2,g1p,g2p,theta,gamma=pair(c,tau,A,B)
    assert abs(cosine(g1p,g2)-tau) < 2e-10
    assert abs(cosine(g2p,g1)-tau) < 2e-10
    final=cosine(g1p,g2p)
    formula=math.cos(theta-2.0*gamma)
    algebra=c*(2.0*tau*tau-1.0)+2.0*tau*math.sqrt((1.0-c*c)*(1.0-tau*tau))
    assert abs(final-formula) < 3e-10
    assert abs(final-algebra) < 3e-10

# Half-angle target gives exact parallelism; one-third-angle target gives final cosine = requested target.
for c in (-0.95,-0.7,-0.2,0.0,0.4,0.8,0.97):
    theta=math.acos(c)
    tstar=math.cos(theta/2.0)
    teq=math.cos(theta/3.0)
    for A,B in ((1.0,1.0),(0.3,7.0),(12.0,0.2)):
        _,_,p,q,_,_=pair(c,tstar,A,B)
        assert abs(cosine(p,q)-1.0) < 3e-10
        _,_,p,q,_,_=pair(c,teq,A,B)
        assert abs(cosine(p,q)-teq) < 3e-10

# Strict two-branch behavior and comparison with requested target.
for c in (-0.9,-0.4,0.2,0.7):
    theta=math.acos(c)
    tstar=math.cos(theta/2.0)
    teq=math.cos(theta/3.0)
    ts1=[c+(tstar-c)*k/20.0 for k in range(1,20)]
    cs1=[math.cos(theta-2*math.acos(t)) for t in ts1]
    assert all(cs1[i] < cs1[i+1] for i in range(len(cs1)-1))
    ts2=[tstar+(0.999999-tstar)*k/20.0 for k in range(1,20)]
    cs2=[math.cos(theta-2*math.acos(t)) for t in ts2]
    assert all(cs2[i] > cs2[i+1] for i in range(len(cs2)-1))
    for t in [c+(teq-c)*0.2,c+(teq-c)*0.7]:
        assert math.cos(theta-2*math.acos(t)) > t
    for t in [teq+(0.999999-teq)*0.2,teq+(0.999999-teq)*0.7]:
        assert math.cos(theta-2*math.acos(t)) < t

# Extreme target returns final mutual cosine to the original value.
for c in (-0.8,-0.1,0.5,0.9):
    theta=math.acos(c)
    vals=[math.cos(theta-2*math.acos(t)) for t in (0.99,0.9999,0.99999999)]
    assert abs(vals[-1]-c) < 5e-4

print("verification passed")
