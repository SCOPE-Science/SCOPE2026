import math
import random

def closed_m(t,b1,G):
    a=(1.0-b1)/(1.0+b1)
    return ((-1.0)**(t-1))*a*G*(1.0-(-b1)**t)

def run_adamomentum(b1,b2,eps,G,T):
    m=0.0
    v=0.0
    out=[]
    for t in range(1,T+1):
        g=(1.0 if t%2 else -1.0)*G
        m=b1*m+(1.0-b1)*g
        v=b2*v+(1.0-b2)*m*m+eps
        mh=m/(1.0-b1**t)
        vh=v/(1.0-b2**t)
        u=mh/math.sqrt(vh)
        out.append((t,g,m,v,mh,vh,u))
    return out

def limits(b1,b2,eps,G):
    a=(1.0-b1)/(1.0+b1)
    d=eps/(1.0-b2)
    am=a*abs(G)/math.sqrt(a*a*G*G+d)
    raw=a*abs(G)/math.sqrt(G*G+d)
    return a,d,am,raw,am/raw

random.seed(350058)

# Exact first-moment transient and asymptotic AdaMomentum response.
for _ in range(500):
    b1=random.uniform(0.0,0.98)
    b2=random.uniform(0.0,0.999)
    eps=10.0**random.uniform(-12.0,-3.0)
    G=random.choice((-1.0,1.0))*10.0**random.uniform(-2.0,2.0)
    out=run_adamomentum(b1,b2,eps,G,5000)
    for t,g,m,v,mh,vh,u in out[:50]:
        assert abs(m-closed_m(t,b1,G)) <= 2e-12*max(1.0,abs(m))
    a,d,am,raw,ratio=limits(b1,b2,eps,G)
    last=out[-1]
    assert abs(last[5]-(a*a*G*G+d)) <= 2e-8*max(1.0,a*a*G*G+d)
    assert abs(abs(last[6])-am) <= 2e-7*max(1.0,am)

# Raw-gradient control is exact after bias correction.
for _ in range(500):
    b1=random.uniform(0.0,0.98)
    b2=random.uniform(0.0,0.999)
    eps=10.0**random.uniform(-12.0,-3.0)
    G=10.0**random.uniform(-2.0,2.0)
    vr=0.0
    d=eps/(1.0-b2)
    for t in range(1,100):
        vr=b2*vr+(1.0-b2)*G*G+eps
        vrhat=vr/(1.0-b2**t)
        assert abs(vrhat-(G*G+d)) <= 3e-12*max(1.0,G*G+d)

# Restoration factor is increasing with signal magnitude and tends to 1/a.
for b1 in (0.1,0.5,0.9,0.99):
    b2=0.999
    eps=1e-8
    vals=[]
    for G in (1e-6,1e-4,1e-2,1.0,100.0):
        a,d,am,raw,r=limits(b1,b2,eps,G)
        vals.append(r)
    assert all(y>x for x,y in zip(vals,vals[1:]))
    assert vals[-1] < 1.0/a
    assert abs(vals[-1]-1.0/a) < 2e-3*(1.0/a)

# Zero damping cancels first-moment attenuation exactly.
for b1 in (0.0,0.2,0.5,0.9,0.99):
    a=(1.0-b1)/(1.0+b1)
    for b2 in (0.0,0.5,0.999):
        A,D,am,raw,r=limits(b1,b2,0.0,3.0)
        assert abs(am-1.0) < 2e-15
        assert abs(raw-a) < 2e-15
        assert abs(r-1.0/a) < 2e-13

# Widely used beta1=0.9 gives a factor 19 in the signal-dominated limit.
b1=0.9
a=(1.0-b1)/(1.0+b1)
assert abs(a-1.0/19.0) < 1e-15
assert abs(1.0/a-19.0) < 1e-13

# Source-table beta values and epsilon: crossover scale.
b2=0.999
eps=1e-8
Gc=math.sqrt(eps/(1.0-b2))/a
assert abs(Gc-0.060083275543199186) < 2e-15
_,_,am,_,_=limits(b1,b2,eps,Gc)
assert abs(am-1.0/math.sqrt(2.0)) < 2e-14

print("verification passed")
