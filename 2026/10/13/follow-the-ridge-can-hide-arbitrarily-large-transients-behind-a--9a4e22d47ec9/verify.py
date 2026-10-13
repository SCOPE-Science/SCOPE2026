import math
import random

def fr_step(x,y,h,c,b,ex,ey):
    a=h-b*b/c
    gx=a*x+b*y
    gy=b*x-c*y
    xn=x-ex*gx
    yn=y+ey*gy-ex*(b/c)*gx
    return xn,yn

def closed(t,x0,y0,h,c,b,ex,ey):
    e0=y0-(b/c)*x0
    p=1-ex*h
    q=1-ey*c
    e=(q**t)*e0
    if t==0:
        x=x0
    elif abs(p-q)>1e-11:
        x=(p**t)*x0-ex*b*((p**t-q**t)/(p-q))*e0
    else:
        x=(p**t)*x0-ex*b*t*(p**(t-1))*e0
    y=e+(b/c)*x
    return x,y

random.seed(350092)

# Moderate ranges avoid irrelevant floating cancellation in h-b^2/c.
for _ in range(2000):
    h=random.uniform(0.7,3.0)
    c=random.uniform(0.7,3.0)
    b=random.uniform(-2.5,2.5)
    ex=random.uniform(0.03,1.7/h)
    ey=random.uniform(0.03,1.7/c)
    x0=random.uniform(-2,2)
    y0=random.uniform(-2,2)
    x,y=x0,y0
    p=1-ex*h
    q=1-ey*c
    for t in range(1,8):
        e=y-(b/c)*x
        xn,yn=fr_step(x,y,h,c,b,ex,ey)
        en=yn-(b/c)*xn
        assert abs(en-q*e)<2e-9*max(1,abs(en),abs(q*e))
        assert abs(xn-(p*x-ex*b*e))<2e-9*max(1,abs(xn))
        cx,cy=closed(t,x0,y0,h,c,b,ex,ey)
        assert abs(xn-cx)<2e-8*max(1,abs(cx))
        assert abs(yn-cy)<2e-8*max(1,abs(cy))
        x,y=xn,yn

# Repeated-root resonance: eigenvalues fixed, amplification diverges.
h=2.0
c=3.0
r=0.4
ex=(1-r)/h
ey=(1-r)/c
vals=[]
for b in (1.0,3.0,10.0,30.0,100.0):
    p=1-ex*h
    q=1-ey*c
    assert abs(p-r)<1e-14 and abs(q-r)<1e-14
    x1,y1=fr_step(0.0,1.0,h,c,b,ex,ey)
    formula=((1-r)*b/h)**2 + (r-(1-r)*b*b/(h*c))**2
    direct=x1*x1+y1*y1
    assert abs(direct-formula)<2e-9*max(1,formula)
    vals.append(direct)
assert all(vals[i+1]>vals[i] for i in range(len(vals)-1))
assert vals[-1]>1e6

# Jordan closed form at resonance.
b=4.7
x0=-0.2
y0=0.8
e0=y0-(b/c)*x0
for t in range(12):
    x,y=closed(t,x0,y0,h,c,b,ex,ey)
    expected=(r**t)*x0 if t==0 else (r**t)*x0-ex*b*t*(r**(t-1))*e0
    assert abs(x-expected)<2e-12

# Defining-paper example f=-3x^2+4xy-y^2.
a=-6.0
b=4.0
c=2.0
h=a+b*b/c
assert abs(h-2.0)<1e-14
eta=0.2
assert abs((1-eta*h)-(1-eta*c))<1e-14

print("verification passed")
