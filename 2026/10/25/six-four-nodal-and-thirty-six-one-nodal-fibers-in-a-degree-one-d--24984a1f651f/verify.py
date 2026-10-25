#!/usr/bin/env python3
"""Exact arithmetic certificate for a degree-one del Pezzo pencil."""

def trim(a):
    a=list(a)
    while len(a)>1 and a[-1]==0: a.pop()
    return a

def add(a,b):
    c=[0]*max(len(a),len(b))
    for i,x in enumerate(a): c[i]+=x
    for i,x in enumerate(b): c[i]+=x
    return trim(c)

def neg(a): return [-x for x in a]
def sub(a,b): return add(a,neg(b))
def scale(a,k): return trim([k*x for x in a])
def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return trim(c)
def power(a,n):
    r=[1]
    while n:
        if n&1: r=mul(r,a)
        a=mul(a,a);n//=2
    return r

def deriv(a):return trim([i*a[i] for i in range(1,len(a))] or [0])

def modp(a,p):return trim([x%p for x in a])
def gcdp(a,b,p):
    a,b=modp(a,p),modp(b,p)
    while b!=[0]:
        r=a[:]
        while r!=[0] and len(r)>=len(b):
            shift=len(r)-len(b)
            coef=(r[-1]*pow(b[-1],-1,p))%p
            for i,x in enumerate(b):r[i+shift]=(r[i+shift]-coef*x)%p
            r=trim(r)
        a,b=b,r
    if a==[0]:return [0]
    return modp(scale(a,pow(a[-1],-1,p)),p)

t=[0,1]
h=add(add(power(t,6),t),[1])
Q=sub(add(scale(power(t,3),256),scale(power(h,2),1728)),[27])
a,b,c=Q,scale(power(t,2),144),scale(t,27)
# Norm in Z[T]/(T^3+16) of a+b*T+c*T^2.
Fdet=add(sub(add(power(a,3),scale(mul(mul(a,b),c),48)),scale(power(b,3),16)),scale(power(c,3),256))
Fpublished=add(sub(add(power(Q,3),scale(mul(Q,power(t,3)),186624)),scale(power(t,6),47775744)),scale(power(t,3),5038848))
assert Fdet==Fpublished and len(Fdet)-1==36
assert Fdet[-1]==1728**3
for poly1,poly2 in ((Fdet,deriv(Fdet)),(Fdet,h),(h,deriv(h)),(h,sub(scale(power(t,3),256),[27]))):
    assert gcdp(poly1,poly2,5)==[1]
# In the quartic A(s,t)=s^4+s+t, simultaneous A=A_s=0 implies 256 t^3=27.
# H(t) does not meet that discriminant and all relevant roots are simple.
print('VERIFY_OK: degree 36; exact cubic norm; four coprimality certificates modulo 5')
