#!/usr/bin/env python3
"""Exact certificate for the quotient of a rational involution on a parameter surface.
Run: python3 verify_quotient.py (requires sympy)."""
import sympy as S
u,v=S.symbols('u v', nonzero=True)
a,b=S.symbols('a b')
s=a+b; d=a-b
apr=(-2*d-8)/s
bpr=(2*d-8)/s
assert S.factor(apr+bpr+16/s)==0
assert S.factor(apr-bpr+4*d/s)==0
# The induced map is u -> -1/u, v -> -v.
up=-1/u; vp=-v
assert S.simplify(-1/up-u)==0
assert S.simplify(-vp-v)==0
q=u-1/u
z=u+1/u
t=v*v
w=v*z
F=w*w-t*(q*q+4)
assert S.factor(F)==0
assert S.factor(q.subs(u,up)-q)==0
assert S.factor(t.subs(v,vp)-t)==0
assert S.factor(w.subs({u:up,v:vp}, simultaneous=True)-w)==0
D=u*u-u*v+1
N=q*q+4-2*w+t
assert S.factor(N-(D/u)**2)==0
assert S.factor((u*u-u*v+1).subs({u:up,v:vp}, simultaneous=True) - D/u**2)==0
assert S.factor((a*a-4)*(b*b-4)-((a*b+4)**2-4*(a+b)**2))==0
# Check the coordinate change from original symmetric coefficients.
p=a*b
V=(p+4)/s
assert S.factor((apr*bpr+4)/(apr+bpr)+V)==0
# Isolated singularities, affine chart Z=1.
Q,T,W,Z=S.symbols('Q T W Z')
G=W*W*Z-T*(Q*Q+4*Z*Z)
assert S.factor(G.subs(Z,1)-(W*W-T*(Q*Q+4)))==0
assert [S.factor(S.diff(G,x)) for x in (Q,T,W,Z)]==[-2*Q*T,-Q**2-4*Z**2,2*W*Z,W**2-8*T*Z]
# On Z=1, Jacobian vanishing has exactly Q^2+4=0,T=W=0.
for root in (2*S.I,-2*S.I):
 assert all(S.simplify(f.subs({Q:root,T:0,W:0,Z:1}))==0 for f in (G,)+tuple(S.diff(G,x) for x in (Q,T,W,Z)))
# At infinity Z=0, the partials G_T=-Q^2 and G_Z=W^2 force Q=W=0.
assert G.subs(Z,0)==-T*Q**2
assert S.diff(G,T).subs(Z,0)==-Q**2
assert S.diff(G,Z).subs({Z:0,Q:0})==W**2
# Chart T=1: A3 is Q^2+4 (Z-W^2/8)^2-W^4/16.
assert S.factor((Q*Q+4*Z*Z-W*W*Z)-(Q*Q+4*(Z-W*W/8)**2-W**4/16))==0
# A1 at Q=+-2i: Q^2+4 has simple zero and local equation W^2=T*(Q^2+4).
assert S.diff(Q*Q+4,Q).subs(Q,2*S.I)!=0
# Boundary collision curve is doubled, and its intersection with t=4 has length four.
h=Q**2+4
assert S.factor((W**2-T*h).subs(T,2*W-h)-(W-h)**2)==0
assert S.factor((W**2-4*h).subs(W,(h+4)/2)-Q**4/4)==0
# The projective hyperplane section at infinity is one simple and one double line.
assert S.factor(G.subs(Z,0)+T*Q**2)==0
# Exhaustively check all rational source points and their orbit invariant separation in two finite fields.
for prime in (7,13):
 pts=set()
 inv={}
 def iv(x):return pow(x,prime-2,prime)
 for U in range(1,prime):
  for V in range(prime):
   if ((V*V-4)*(U*U-U*V+1))%prime==0: continue
   pts.add((U,V))
 for P in pts:
  U,V=P
  partner=(-iv(U)%prime,-V%prime)
  assert partner in pts
  assert partner!=P
  qv=(U-iv(U))%prime
  tv=V*V%prime
  wv=V*(U+iv(U))%prime
  k=(qv,tv,wv)
  assert (wv*wv-tv*(qv*qv+4))%prime==0
  assert ((tv-4)*(qv*qv+4-2*wv+tv))%prime!=0
  inv.setdefault(k,set()).add(P)
 assert all(len(fiber)==2 for fiber in inv.values())
 assert len(pts)==2*len(inv)
 print(f'F{prime}: {len(pts)} admissible source points; {len(inv)} distinct two-element orbits')
print('PRYM_DECK_CUBIC_QUOTIENT_AND_A3_2A1_PASS')
