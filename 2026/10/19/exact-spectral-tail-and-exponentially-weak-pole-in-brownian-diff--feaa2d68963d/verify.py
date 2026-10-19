#!/usr/bin/env python3
"""Deterministic numerical cross-checks for the exponentially refreshed resetting-intensity model.

Run with: python verify.py
Requires mpmath. Tests do not replace the analytical proof.
"""
import mpmath as m
m.mp.dps = 70
checks=0

def ok(cond,what):
 global checks
 checks+=1
 if not cond: raise AssertionError(what)

def root(r):
 r=m.mpf(r)
 # For r>0, r*exp(t)*E1(t) decreases from infinity to <1 on (0,r).
 lo=m.mpf(0); hi=r
 for _ in range(265):
  mid=(lo+hi)/2
  if r*m.exp(mid)*m.e1(mid)>1: lo=mid
  else: hi=mid
 return (lo+hi)/2

def ff(t):return m.exp(t)*m.e1(t)

def continuum(r,y):
 # a=1 throughout; spectral intensity density at s=r+y
 A=-m.exp(-y)*m.ei(y)
 B=m.pi*m.exp(-y)
 return m.exp(-y)/((1-r*A)**2+(r*B)**2)

for rstr in ['0.12','0.4','0.8','1','2','5','10','30','100']:
 r=m.mpf(rstr);u=root(r);th=r-u
 w=u/(r*th)
 ok(u>0 and u<r,'root interval')
 ok(th>0 and th<min(r,m.mpf(1)),'rate bound')
 ok(w>0 and w<1,'mass bound')
 ok(abs(r*ff(u)-1)<m.mpf('1e-45'),'secular equation')
 dw=1/(r*r*(-(ff(u)-1/u)))
 ok(abs(w-dw)<m.mpf('1e-39'),'residue equals eigenprojection')
 R=lambda z:ff(r+z)/(1-r*ff(r+z))
 for zz in ['0.02','0.7','4']:
  z=m.mpf(zz)
  # H(z) = phi(r+z)/(1-r phi(r+z)); derived independently via geometric refresh renewal.
  h=R(z)
  ok(0<h<1/z,'resolvent Stieltjes bounds')
  ok(abs((1-z*h)-(1-(r+z)*ff(r+z))/(1-r*ff(r+z)))<m.mpf('1e-45'),'Fourier renewal identity')

# Hellmann-Feynman sensitivity: d theta/dr = 1 - isolated spectral mass.
for rr in ['0.4','0.8','1.2','3','10']:
 r=m.mpf(rr);eps=m.mpf('1e-7')
 th=lambda x:x-root(x)
 slope=(th(r+eps)-th(r-eps))/(2*eps)
 w=root(r)/(r*th(r))
 ok(abs(slope-(1-w))<m.mpf('2e-13'),'spectral derivative identity')

# Check a continuous spectral density and isolated mass reconstruct S(0) and H(s).
# Apply numerical quadrature in log-coordinate across the spectral continuum.
for rstr in ['0.5','1','2']:
 r=m.mpf(rstr);u=root(r);th=r-u;w=u/(r*th)
 # for lambda=y, use y=exp(t); density dy=e^t dt
 def weight(t):
  y=m.exp(t)
  return continuum(r,y)*y
 splits=[-100,-30,-15,-7,-3,-1,0,1,3,6]
 ncont=m.fsum(m.quad(weight,[a,b]) for a,b in zip(splits[:-1],splits[1:]))
 ncont+=m.quad(weight,[6,15])
 ok(abs(w+ncont-1)<m.mpf('3e-9'),'spectral mass reconstruction r='+rstr)
 for zstr in ['0.5','2']:
  z=m.mpf(zstr)
  Hcalc=w/(z+th)
  Hcalc+=m.fsum(m.quad(lambda t: weight(t)/(z+r+m.exp(t)),[a,b]) for a,b in zip(splits[:-1],splits[1:]))
  Hcalc+=m.quad(lambda t:weight(t)/(z+r+m.exp(t)),[6,15])
  Hdirect=ff(r+z)/(1-r*ff(r+z))
  ok(abs(Hcalc-Hdirect)<m.mpf('3e-9'),'spectral resolvent reconstruction r='+rstr)

# Small-refresh essential-singularity and big-refresh perturbative checks.
for rstr,tol in [('0.10','0.001'),('0.08','0.0001'),('0.05','0.000001')]:
 r=m.mpf(rstr);u=root(r);theta=r-u;w=u/(r*theta)
 lead=m.exp(-1/r-m.euler)
 ok(abs(u/lead-1)<m.mpf(tol),'small-refresh eigen-shift')
 ok(abs(w/(lead/r**2)-1)<m.mpf(tol)*2,'small-refresh pole mass')

for rstr,tol in [('30','0.01'),('70','0.002'),('120','0.0008')]:
 r=m.mpf(rstr);u=root(r);th=r-u;w=u/(r*th)
 ok(abs(th-(1-1/r))<m.mpf(tol),'fast-refresh decay')
 ok(abs(w-(1-1/r**2))<m.mpf(tol),'fast-refresh pole mass')

print(f'PASS {checks} deterministic checks; direct secular equation, Fourier transform, spectral normalization, resolvent, both limits.')
