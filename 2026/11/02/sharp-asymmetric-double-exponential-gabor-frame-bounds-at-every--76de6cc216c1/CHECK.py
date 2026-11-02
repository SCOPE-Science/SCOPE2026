#!/usr/bin/env python3
"""Direct numerical and rational checks of exact asymmetric exponential Gabor bounds."""
import cmath
import math
from fractions import Fraction

COUNT = 0

def check(test, label):
    global COUNT
    if not test:
        raise AssertionError(label)
    COUNT += 1

def bounds(a, b, q):
    assert a > 0 and b > 0 and q >= 3
    ua = [math.exp(-a*l)/(1+math.exp(-a*q)) for l in range(q)]
    vb = [math.exp(-b*(q-l))/(1+math.exp(-b*q)) for l in range(q)]
    U=sum(v*v for v in ua)
    V=sum(v*v for v in vb)
    W=sum(u*v for u,v in zip(ua,vb))
    t=( (b-a)*W+math.sqrt((a-b)**2*W**2+4*a*b*U*V) )/(2*b*V)
    x=math.log(t)/(a+b)
    A=q*(U*math.exp(-2*a*x)+V*math.exp(2*b*x)-2*W*math.exp((b-a)*x))
    up=[math.exp(-a*l)/(1-math.exp(-a*q)) for l in range(q)]
    vp=[math.exp(-b*(q-l))/(1-math.exp(-b*q)) for l in range(q)]
    B=q*sum((u+v)**2 for u,v in zip(up,vp))
    return A,B,x

def Zak(a,b,x,w,terms=300):
    val=0j
    for n in range(-terms,terms+1):
        c=x+n
        g=math.exp(-a*c) if c>=0 else math.exp(b*c)
        val+=g*cmath.exp(-2j*math.pi*n*w)
    return val

def eig(a,b,q,x,w):
    return sum(abs(Zak(a,b,x,w+j/q))**2 for j in range(q))

def poly(a,b,q,x,w):
    z=cmath.exp(-2j*math.pi*q*w)
    sa=math.exp(-a*q)
    sb=math.exp(-b*q)
    vals=[]
    for l in range(q):
        c=x+l
        P=math.exp(-a*c)/(1-sa*z)+math.exp(-b*(q-c))/(z-sb)
        vals.append(P)
    return q*sum(abs(z)**2 for z in vals)

for q in (3,4,5,8):
 for a,b in ((0.3,0.7),(1.4,0.5),(0.9,0.9),(2.7,1.2),(0.1,3.1)):
    A,B,x0=bounds(a,b,q)
    check(0<x0<1, 'interior critical point')
    check(0<A<B, 'nondegenerate bounds')
    check(abs(eig(a,b,q,x0,0.5/q)-A)<2e-8*max(1,A), 'independent Zak min')
    check(abs(eig(a,b,q,0,0)-B)<2e-8*max(1,B), 'independent Zak max')
    check(abs(poly(a,b,q,x0,0.5/q)-A)<2e-10*max(1,A), 'polyphase identity min')
    check(abs(poly(a,b,q,0,0)-B)<2e-10*max(1,B), 'polyphase identity max')
    for ix in range(17):
      x=ix/16
      for iw in range(17):
         w=iw/(16*q)
         v=poly(a,b,q,x,w)
         check(A-1e-8<=v<=B+1e-8,'global spectral enclosure')
         if ix in (0,8,16) and iw in (0,8,16):
             check(abs(v-eig(a,b,q,x,w))<2e-8*max(1,v),'infinite Zak independent')
    check(abs(poly(a,b,q,0,0)-poly(a,b,q,1,0))<1e-10, 'endpoint periodicity')
    check(abs(poly(a,b,q,0,0.5/q)-poly(a,b,q,1,0.5/q))<1e-10, 'endpoint periodicity anti')

# Exact rational polyphase identity for unequal exponents at integer spatial site x=0.
# Choose e^(-a)=1/2 and e^(-b)=1/3; all samples are rational.
for q in range(3,12):
    ra=Fraction(1,2); rb=Fraction(1,3)
    for l in range(q):
       # symbolic at z=+1, -1: correct sums of both positive and negative tails
       for sign in (+1,-1):
          left=ra**l/(1-ra**q*sign)+rb**(q-l)/(sign-rb**q)
          series1=sum((ra**(l+j*q))*sign**j for j in range(30))
          series2=sum((rb**(j*q-l))*sign**(-j) for j in range(1,30))
          check(abs(float(left)-(float(series1)+float(series2)))<1e-14,'rational infinite tails')

print('CHECK_OK assertions='+str(COUNT))
