#!/usr/bin/env python3
"""Numerical integration and algebraic-identity consistency checks for the spherical-cap spectrum."""
import mpmath as mp
mp.mp.dps = 65
count=0

def close(a,b,tol=mp.mpf('2e-49')):
 global count
 assert mp.fabs(a-b)<tol*(1+mp.fabs(a)+mp.fabs(b)),(a,b)
 count+=1

def rho_const(d):
 return mp.gamma(mp.mpf(d)/2)/(mp.sqrt(mp.pi)*mp.gamma(mp.mpf(d-1)/2))

def vals(d,c):
 x=lambda t:t*t
 F={
 'A':lambda t: d*x(t),
 'B':lambda t:mp.mpf(d)/(d-1)*(1-x(t)),
 'C':lambda t:mp.mpf(d+2)/(2*(d-1))*(d*x(t)-1)**2,
 'D':lambda t:mp.mpf(d*(d+2))/(d-1)*x(t)*(1-x(t)),
 'E':lambda t:mp.mpf(d*(d+2))/((d-1)*(d+1))*(1-x(t))**2}
 K=rho_const(d)
 v={k:2*K*mp.quad(lambda t:f(t)*(1-t*t)**(mp.mpf(d-3)/2),[c,1]) for k,f in F.items()}
 return v

for d in [3,4,5,7,10,25]:
 k=rho_const(d)
 c1=1/mp.sqrt(d);c2=mp.sqrt(d+2)/d
 assert 0<c1<c2<1
 count+=1
 for c in [mp.mpf('0.06'),c1*mp.mpf('0.8'),c1,(c1+c2)/2,c2,(1+c2)/2,mp.mpf('0.99')]:
  V=vals(d,c)
  A,B,C,D,E=[V[k] for k in 'ABCDE']
  m=mp.mpf(d-1)/2
  close(C-A,k*c*(1-c*c)**m*(d*d*c*c-(d+2))/(d-1))
  close(C-D,k*(d+2)*c*(1-c*c)**m*(d*c*c-1)/(d-1))
  close(A-D,2*k*d*c**3*(1-c*c)**m/(d-1))
  assert A>D>B and D>E
  count+=1
  top=max(A,C)
  eps=mp.mpf('1e-48')
  if c<c2 and mp.fabs(c-c2)>eps:close(top,A)
  if c>c2 and mp.fabs(c-c2)>eps:close(top,C)
  if c<c1 and mp.fabs(c-c1)>eps:close(max(C,D,B,E),D)
  if c>c1 and c<c2:close(max(C,D,B,E),C)
  if c>c2:close(max(A,D,B,E),A)
  if mp.fabs(c-c1)<eps:close(C,D)
  if mp.fabs(c-c2)<eps:close(C,A)
  # Trace of cap compression equals dimension times cap measure.
  trace=A+(d-1)*B+C+(d-1)*D+((d-2)*(d+1)//2)*E
  cap=2*k*mp.quad(lambda t:(1-t*t)**(mp.mpf(d-3)/2),[c,1])
  dim=d+(d+2)*(d-1)//2
  close(trace,dim*cap)
 print('d=',d,'thresholds',mp.nstr(c1,12),mp.nstr(c2,12))
print('PASS',count,'assertions')
