"""Exact independent arithmetic check for the quadratic height-count theorem."""
from math import isqrt

def trace_power(t,d,n):
    a,b=2,t
    if n==0:return a
    if n==1:return b
    for j in range(2,n+1):a,b=b,t*b-d*a
    return b

def is_expanding(t,d):
    return (d>=2 and abs(t)<=d) or (d<=-2 and abs(t)<=abs(d)-2)

def test_source_criterion(t,d):
    if not is_expanding(t,d) or t*t==4*d:return False
    for n in (1,2,3,4,6,12):
        tr=trace_power(t,d,n)
        z=tr*tr-4*pow(d,n)
        if z<0:continue
        s=isqrt(z)
        if s*s==z and (tr+s)%2==0:return True
    return False

def count_direct(H):
    return sum(test_source_criterion(t,d) for t in range(-H,H+1) for d in range(-H,H+1))

def divisor_sum(H):
    return sum(H//j for j in range(1,H+1))

def formula(H):
    return 2*divisor_sum(H)-2*H+2*isqrt(H//2)+2*isqrt(H//3)

assert sum(is_expanding(t,d) for t in range(-2,3) for d in range(-2,3))==6
for H in range(2,66):
    N=count_direct(H)
    assert N==formula(H),(H,N,formula(H))
    E=sum(is_expanding(t,d) for t in range(-H,H+1) for d in range(-H,H+1))
    assert E==2*H*H-2,(H,E)
print('PASS 64 height boxes (H=2..65), independent integral matrix-power criterion; exact counts and expansion denominators')
for H in (2,3,4,5,10,20,50,65):print(H,formula(H),2*H*H-2)
