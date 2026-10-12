import math
import random

def dot(x,y): return x[0]*y[0]+x[1]*y[1]
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def sub(x,y): return (x[0]-y[0],x[1]-y[1])
def mul(s,x): return (s*x[0],s*x[1])
def norm(x): return math.sqrt(dot(x,x))

def pair(a,b,rho):
    return (a,0.0),(b*rho,b*math.sqrt(1-rho*rho))

def dual_derivative(g1,g2,c,w):
    g0=mul(0.5,add(g1,g2))
    dg=sub(g1,g2)
    gw=add(g2,mul(w,dg))
    R=c*norm(g0)
    return dot(dg,g0)+R*dot(dg,gw)/norm(gw)

def direct(g1,g2,c):
    g0=mul(0.5,add(g1,g2))
    if c==0: return g0
    f0=dual_derivative(g1,g2,c,0.0)
    f1=dual_derivative(g1,g2,c,1.0)
    if f0>=0:
        w=0.0
    elif f1<=0:
        w=1.0
    else:
        lo,hi=0.0,1.0
        for _ in range(80):
            mid=(lo+hi)/2
            if dual_derivative(g1,g2,c,mid)<0: lo=mid
            else: hi=mid
        w=(lo+hi)/2
    gw=add(g2,mul(w,sub(g1,g2)))
    return add(g0,mul(c*norm(g0)/norm(gw),gw))

def closed(g1,g2,c):
    a,b=norm(g1),norm(g2)
    rho=dot(g1,g2)/(a*b)
    G=math.sqrt(a*a+b*b+2*a*b*rho)
    ccd=-(b+a*rho)/G
    cbal=(a*a-b*b)/(G*(b-a*rho))
    g0=mul(0.5,add(g1,g2))
    if c<cbal:
        return add(g0,mul(c*norm(g0)/b,g2)),ccd,cbal
    delta=mul(0.5,sub(g1,g2))
    h=sub(g0,mul(dot(delta,g0)/dot(delta,delta),delta))
    e=abs(dot(delta,g0))/norm(delta)
    s=norm(h); R=c*norm(g0)
    return mul(1+math.sqrt(max(0,R*R-e*e))/s,h),ccd,cbal

random.seed(350071)
for _ in range(1200):
    a=10**random.uniform(-1,1)
    q=random.uniform(.05,.95)
    b=a*q
    rho=random.uniform(-.999,-q-1e-6)
    g1,g2=pair(a,b,rho)
    G=math.sqrt(a*a+b*b+2*a*b*rho)
    ccd=-(b+a*rho)/G
    cbal=(a*a-b*b)/(G*(b-a*rho))
    assert 0<ccd<cbal and ccd<1
    tests=[0.0,.5*ccd,ccd,min(.999,.5*(ccd+min(cbal,1)))]
    if cbal<.999: tests += [cbal,.5*(cbal+.999)]
    for c in tests:
        d,x,y=closed(g1,g2,c)
        z=direct(g1,g2,c)
        assert norm(sub(d,z))<2e-9*max(1,norm(d))
        p1,p2=dot(g1,d),dot(g2,d)
        if c<cbal-1e-10: assert p1>p2-1e-10
        if c>cbal+1e-10: assert abs(p1-p2)<2e-9*max(1,abs(p1),abs(p2))

for q in (.1,.2,1/3):
    for j in range(1,80):
        rho=-.999+j*(.999-q)/100
        if rho>=-q: break
        a,b=1.0,q
        G=math.sqrt(1+q*q+2*q*rho)
        cbal=(1-q*q)/(G*(q-rho))
        assert cbal>=1-2e-12

for _ in range(1000):
    q=random.uniform(.34,.95)
    rho=random.uniform(-.999,-q-1e-6)
    G=math.sqrt(1+q*q+2*q*rho)
    cbal=(1-q*q)/(G*(q-rho))
    crit=rho<(3*q*q-1)/(2*q)
    assert (cbal<1)==crit

for rho in (-.95,-.5,-.1,0,.7):
    g1,g2=pair(1,1,rho)
    g0=mul(.5,add(g1,g2))
    for c in (0,.1,.4,.9):
        d=direct(g1,g2,c)
        target=mul(1+c,g0)
        assert norm(sub(d,target))<2e-9

print("verification passed")
