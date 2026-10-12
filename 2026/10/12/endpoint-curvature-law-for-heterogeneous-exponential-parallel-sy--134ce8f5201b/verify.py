#!/usr/bin/env python3
import math

l1,l2,t1,t2=2.0,3.0,1.5,3.5
S=l1+l2
c=l1/t1
alpha=l2-l1
A=math.sqrt(l1*l2/(t1*t2))
local_qpp=(S/2.0)*A*(A-1.0)

def F(x,a,b):
    return (-math.expm1(-a*x))*(-math.expm1(-b*x))

def f(x,a,b):
    return a*math.exp(-a*x)+b*math.exp(-b*x)-(a+b)*math.exp(-(a+b)*x)

def fp(x,a,b):
    return -a*a*math.exp(-a*x)-b*b*math.exp(-b*x)+(a+b)**2*math.exp(-(a+b)*x)

def Q(x):
    target=F(x,l1,l2)
    lo=0.0
    hi=max(c*x+1.0,1.0)
    while F(hi,t1,t2)<target:
        hi*=2.0
    for _ in range(120):
        mid=(lo+hi)/2.0
        if F(mid,t1,t2)<target:
            lo=mid
        else:
            hi=mid
    return (lo+hi)/2.0

def Qp(x):
    y=Q(x)
    return f(x,l1,l2)/f(y,t1,t2)

def Qpp(x):
    y=Q(x)
    qp=Qp(x)
    return (fp(x,l1,l2)-fp(y,t1,t2)*qp*qp)/f(y,t1,t2)

# Local expansion.
x0=1e-3
assert abs(Q(x0)/x0-A)<1.1e-4
assert abs(Qpp(x0)-local_qpp)<3e-4
assert Qpp(x0)>0.0

# Tail constants.
x=8.0
tail_q=math.exp(alpha*x)*(Q(x)-c*x)
tail_qp=math.exp(alpha*x)*(Qp(x)-c)
tail_qpp=math.exp(alpha*x)*Qpp(x)
assert abs(tail_q+1.0/t1)<2e-4
assert abs(tail_qp-alpha/t1)<3e-4
assert abs(tail_qpp+alpha*alpha/t1)<5e-4
assert Q(x)<c*x and Qp(x)>c and Qpp(x)<0.0

print(f"VERIFY_OK tail_q={tail_q:.9f} tail_qp={tail_qp:.9f} tail_qpp={tail_qpp:.9f} local_qpp={Qpp(x0):.9f}")
