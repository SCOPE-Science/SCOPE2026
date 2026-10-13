import math
import random

def closed_ratio(t,b1):
    if b1 == 0.0:
        return 1.0
    a=(1.0-b1)/(1.0+b1)
    return a*(1.0-(-b1)**t)/(1.0-b1**t)

def replay(T,b1,b2,nu1,nu2,G,eps):
    m=0.0
    v=0.0
    rows=[]
    for t in range(1,T+1):
        g=G if t%2 else -G
        m=b1*m+(1.0-b1)*g
        v=b2*v+(1.0-b2)*g*g
        mhat=m/(1.0-b1**t) if b1 != 1.0 else m
        vhat=v/(1.0-b2**t) if b2 != 1.0 else v
        num=(1.0-nu1)*g+nu1*mhat
        den=math.sqrt((1.0-nu2)*g*g+nu2*vhat)+eps
        rows.append((t,g,m,v,mhat,vhat,num,den,abs(num/den)))
    return rows

random.seed(350067)

# Exact moments, parity law, and second-moment erasure.
for _ in range(1000):
    b1=random.uniform(0.0,0.999)
    b2=random.uniform(0.0,0.999)
    nu1=random.uniform(0.0,1.0)
    nu2=random.uniform(0.0,1.0)
    G=random.choice((-1.0,1.0))*10.0**random.uniform(-2.0,2.0)
    eps=10.0**random.uniform(-12.0,-2.0)
    rows=replay(40,b1,b2,nu1,nu2,G,eps)
    a=(1.0-b1)/(1.0+b1)
    for t,g,m,v,mhat,vhat,num,den,u in rows:
        ratio=mhat/g
        assert abs(ratio-closed_ratio(t,b1)) <= 3e-12*max(1.0,abs(ratio))
        assert abs(vhat-G*G) <= 3e-10*max(1.0,G*G)
        assert abs(den-(abs(G)+eps)) <= 3e-10*max(1.0,abs(G)+eps)
        if t%2==0:
            assert abs(ratio-a) <= 3e-12
        q=num/g
        assert q > 0.0 or abs(q) < 1e-14

# Odd factors decrease; even factors equal the asymptotic value.
for b1 in (0.1,0.5,0.9,0.95,0.999):
    for nu1 in (0.0,0.3,0.7,0.8,1.0):
        qinf=(1.0-nu1)+nu1*(1.0-b1)/(1.0+b1)
        rows=replay(101,b1,0.98,nu1,0.37,2.0,1e-8)
        odd=[]
        for t,g,m,v,mhat,vhat,num,den,u in rows:
            q=num/g
            if t%2==0:
                assert abs(q-qinf) < 3e-12
            else:
                odd.append(q)
        assert all(y <= x + 1e-14 for x,y in zip(odd,odd[1:]))
        assert odd[-1] >= qinf-1e-14
        assert abs(odd[0]-1.0) < 3e-12

# Sharp beta1 -> 1 floor.
for nu1 in (0.1,0.5,0.8,1.0):
    b1=1.0-1e-10
    qinf=(1.0-nu1)+nu1*(1.0-b1)/(1.0+b1)
    assert abs(qinf-(1.0-nu1)) < 1e-9

# WMT16 source setting.
nu1=0.8
b1=0.95
nu2=0.7
b2=0.98
qinf=(1.0-nu1)+nu1*(1.0-b1)/(1.0+b1)
assert abs(qinf-0.22051282051282048) < 1e-15

# Changing second-moment parameters does not change any update magnitude.
baseline=[r[-1] for r in replay(100,b1,0.98,nu1,0.7,3.0,1e-6)]
for b2x,nu2x in ((0.0,0.0),(0.5,0.2),(0.999,1.0),(0.7,0.93)):
    vals=[r[-1] for r in replay(100,b1,b2x,nu1,nu2x,3.0,1e-6)]
    for x,y in zip(vals,baseline):
        assert abs(x-y) < 2e-10

print("verification passed")
