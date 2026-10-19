#!/usr/bin/env python3
"""Independent numerical and symbolic sanity checks for three-way short-period fold ordering.
Run: python3 verify.py. Standard library + mpmath + sympy.
Finite tests supplement, not replace, the analytic proof.
"""
import math
import cmath
import random
from fractions import Fraction
import mpmath as mp
import sympy as sp

mp.mp.dps = 65
E = mp.mpf(2)/5
H0 = mp.asin(E)/mp.pi
rt5=mp.sqrt(5)
q=( (rt5-1)/4, -(rt5+1)/4 )
s=(mp.sin(2*mp.pi/5),mp.sin(4*mp.pi/5))
assert sp.simplify((sp.cos(2*sp.pi/5)-sp.cos(4*sp.pi/5))-sp.sqrt(5)/2)==0
assert sp.simplify((sp.sin(2*sp.pi/5)**2-sp.sin(4*sp.pi/5)**2)-sp.sqrt(5)/4)==0
assert sp.simplify((sp.sin(2*sp.pi/5)**2+sp.sin(4*sp.pi/5)**2)-sp.Rational(5,4))==0

# Exhaust the five second-iterate cat-map points modulo 5.
pts=[]
for t in range(5):
 for u in range(5):
  if (4*t+3*u)%5==0 and (3*t+u)%5==0:
   pts.append((t,u))
assert sorted(pts)==sorted([(0,0),(1,2),(4,3),(2,4),(3,1)])
assert {((2*t+u)%5,(t+u)%5) for t,u in pts}==set(pts)
assert [((2*t+u)%5,(t+u)%5) for t,u in [(1,2),(2,4)]]==[(4,3),(3,1)]

# SU(1,1) matrix products from the actual complex Möbius formula.
B=mp.matrix([[1,E],[E,1]])/mp.sqrt(1-E*E)
def mat(d):
 z=mp.exp(mp.j*mp.pi*d)
 return mp.matrix([[z,0],[0,1/z]])*B

def h(mu,j,alpha):
 return mp.asin(E*mp.cos(mp.pi*mu*s[j]*mp.cos(alpha)))/mp.pi

def threshold(mu,j,alpha):
 return -mu*mp.sin(alpha)*q[j]+h(mu,j,alpha)

def threshold_fixed(mu,alpha):
 return -mu*mp.sin(alpha)+H0

def tr2(mu,j,alpha,c):
 d1=c+mu*mp.sin(alpha+2*mp.pi*(j+1)/5)
 d2=c+mu*mp.sin(alpha-2*mp.pi*(j+1)/5)
 P=mat(d2)*mat(d1)
 return P[0,0]+P[1,1],P

def tr_formula(mu,j,alpha,c):
 return 2*(mp.cos(2*mp.pi*(c+mu*mp.sin(alpha)*q[j]))+
            E*E*mp.cos(2*mp.pi*mu*mp.cos(alpha)*s[j]))/(1-E*E)

num=0
for mu in (mp.mpf('0.00001'),mp.mpf('0.02'),mp.mpf('0.1')):
 for alpha in (-mp.pi/2,mp.mpf('-.8'),mp.mpf('-.15'),mp.mpf('-.03'),mp.mpf('0'),mp.mpf('.05'),mp.mpf('.2'),mp.pi/2):
  f=threshold_fixed(mu,alpha)
  a=threshold(mu,0,alpha)
  b=threshold(mu,1,alpha)
  assert min(f,a,b)>0 and max(f,a,b)<mp.mpf('.24')
  for j in (0,1):
   c=threshold(mu,j,alpha)
   tr,P=tr2(mu,j,alpha,c)
   assert abs(tr-2)<mp.mpf('1e-58')
   assert abs(P[0,1])>mp.mpf('.1') # non-identity parabolic
   num+=2
   for delta in (mp.mpf('0'),-mp.mpf('.001'),mp.mpf('.001')):
    c2=c+delta
    tr,P=tr2(mu,j,alpha,c2)
    assert abs(tr-tr_formula(mu,j,alpha,c2))<mp.mpf('1e-58')
    assert tr.real>2 if delta<0 else (tr.real<2 if delta>0 else abs(tr.real-2)<mp.mpf('1e-58'))
    num+=2
  # check at c=0 all three driver fibers hyperbolic
  assert 0 < f and 0<a and 0<b
  for j in (0,1):
   tr,_=tr2(mu,j,alpha,0)
   assert tr.real >2
   num+=1

# Roots from explicit formulas.
def roots(mu):
 a_minus=mp.findroot(lambda x:threshold(mu,1,x)-threshold(mu,0,x),(-mp.mpf('.35'),-mp.mpf('.001')))
 a_plus=mp.findroot(lambda x:threshold(mu,0,x)-threshold_fixed(mu,x),(mp.mpf('.001'),mp.mpf('.3')))
 return a_minus,a_plus

for mu in (mp.mpf('.01'),mp.mpf('.04'),mp.mpf('.1')):
 low,high=roots(mu)
 assert -mp.pi/2<low<0<high<mp.pi/2
 for alpha in (-mp.pi/2,(low-mp.pi/2)/2,low,low/2,0,high/2,high,(high+mp.pi/2)/2,mp.pi/2):
  f=threshold_fixed(mu,alpha)
  t1=threshold(mu,0,alpha)
  t2=threshold(mu,1,alpha)
  if alpha<low-mp.mpf('1e-20'):assert t2<t1 and t2<f
  if alpha>low+mp.mpf('1e-20') and alpha<high-mp.mpf('1e-20'):assert t1<t2 and t1<f
  if alpha>high+mp.mpf('1e-20'):assert f<t1 and f<t2
  num+=3
 assert abs((threshold(mu,1,low)-threshold(mu,0,low))) < mp.mpf('1e-59')
 assert abs((threshold(mu,0,high)-threshold_fixed(mu,high))) < mp.mpf('1e-59')
 num+=2

lo,hi=roots(mp.mpf('.1'))
print('checks:',num)
print('alpha_minus(mu=0.1):',mp.nstr(lo,35))
print('alpha_plus(mu=0.1):',mp.nstr(hi,35))
print('asymptotic slopes:',mp.nstr(-E*mp.pi/(4*mp.sqrt(1-E*E)),23),mp.nstr(E*mp.pi*(1+q[0])/(2*mp.sqrt(1-E*E)),23))
print('CHECK_OK')
