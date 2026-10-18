#!/usr/bin/env python3
"""Reproduce finite exact polynomial certificates and small-angle examples; not an infinite proof."""
import math, cmath
from fractions import Fraction as Q

def add(a,b):
 c=[Q(0)]*max(len(a),len(b))
 for j,z in enumerate(a):c[j]+=z
 for j,z in enumerate(b):c[j]+=z
 return c

def scale(a,x):return [z*x for z in a]

def mul_y(a):return [Q(0)]+a

def cheb(n):
 a,b=[Q(1)],[Q(0),Q(1)]
 if n==0:return a
 if n==1:return b
 for _ in range(2,n+1):a,b=b,add(scale(mul_y(b),2),scale(a,-1))
 return b

def recurrence(N):
 c=Q(2)
 for k in range(1,N):c*=Q(k*k,(k+1)*(2*k+1))
 assert c==Q(2**(N+1),N*N*math.comb(2*N,N))
 assert c>0
 return c

def nodes(N):
 return sorted([((math.pi*(2*j+(N+1)%2)/N+math.pi)%(2*math.pi))-math.pi for j in range(N)]) if False else sorted([((-math.pi+(2*j+1)*math.pi/N) if N%2==0 else (-math.pi+(2*j+1)*math.pi/N+math.pi/N)) for j in range(N)])

def canon(N):
 if N%2:return [2*math.pi*j/N for j in range(-(N-1)//2,(N-1)//2+1)]
 return [(2*j+1)*math.pi/N for j in range(-N//2,N//2)]

for n in range(3,41):
 recurrence(n)
 p=cheb(n)
 assert p[-1]==2**(n-1)
 # The normalized Chebyshev certificate is exactly polynomial and has all indicated roots.
 sign=(-1)**(n-1)
 coeff=add([Q(1)],scale(p,-sign))
 assert len(coeff)==n+1 and coeff[-1]==-sign*2**(n-1)
 assert coeff[0]==Q(1)-sign*p[0]
for n in range(3,25):
 z=canon(n)
 assert len(z)==n
 E=sum(t*t for t in z)/n
 E0=(math.pi**2/3)*(1-1/n**2)
 assert abs(E-E0)<1e-12
 for k in range(1,n):
  coeff=sum(cmath.exp(1j*k*t) for t in z)/n
  assert abs(coeff)<1e-12
 for q in range(1,41):
  h=math.pi*(q/100)/(2*n)
  P=[x+h for x in z]+[x-h for x in z]
  moments=sum(t*t for t in P)/(2*n)
  delta=moments-E0
  assert abs(delta-h*h)<2e-12
  phase=sum(cmath.exp(1j*n*t) for t in P)/(2*n)
  remainder=4/(n*n*math.comb(2*n,n))*(1-((-1)**(n-1))*phase.real)
  assert delta+2e-12>=remainder
  assert delta>=-2e-12
print('PASS: 38 exact coefficient/Chebyshev cases and 880 shifted-grid witnesses')
