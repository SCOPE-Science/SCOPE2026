#!/usr/bin/env python3
"""Reproduce the 96-node Galois-invariant Weil-divisor certificate.

Requires SymPy >= 1.13; exact coefficients are in Q(i).
The formulas and node parameters are given by Burek, arXiv:2610.01276v1,
Appendices A--B and Section 7. No external data or network is used.
"""
import sympy as s
v,t=s.symbols('v t'); I=s.I
A=lambda z:z**8+14*z**4+1
B=lambda z:z*(z**4-1)
C=lambda z:z**12-33*z**8-33*z**4+1
sec={}
for label,u in [('P',s.Integer(2)),('Q',2*I)]:
 m=B(u)*B(v); z=B(u)*t+B(v)/t
 a=[-18*(1+I)*(u*v+I),18*(1+I)*(u*v+I),18*(1-I)*(u*v-I),18*(1-I)*(u+I*v),-18*(1+I)*(u-I*v),s.Integer(0)]
 b=[-3*(5*u**4*v**4-u**4-v**4+24*I*u**3*v**3-24*u**2*v**2-24*I*u*v+5),0,
 -3*(5*u**4*v**4-u**4-v**4-24*I*u**3*v**3-24*u**2*v**2+24*I*u*v+5),
 3*(u**4*v**4-5*u**4-5*v**4-24*I*u**3*v+24*u**2*v**2+24*I*u*v**3+1),
 3*(u**4*v**4-5*u**4-5*v**4+24*I*u**3*v+24*u**2*v**2-24*I*u*v**3+1),
 3*(u**4*v**4+u**4+v**4+6*u**4*v**2+6*u**2*v**4-12*u**2*v**2+6*u**2+6*v**2+1)]
 b[1]=b[0]
 for j in [0,1,5]:
  aa=s.expand(a[j]); bb=s.expand(b[j]); cc=s.expand(aa**3/108); dd=s.expand((3*aa**2*bb-11664*m-cc**2)/108)
  x=s.expand(t**2*(aa*z+bb)); y=s.expand(t**3*(54*z**2+cc*z+dd))
  sec[label+str(j+1)]=(x,y)


# Exact polynomial identity for each section graph on the Weierstrass hypersurface.
for name,(xx,yy) in sec.items():
    f=-27*481*A(v)*t**4
    h=2916*(30**4*t**10+B(v)**4*t**2)+54*(-4879)*C(v)*t**6
    assert s.expand(yy**2-xx**3-f*xx-h) == 0, name

import sympy as s,sys
from fractions import Fraction as F
v,t=s.symbols('v t'); I=s.I
class G:
 def __init__(self,a=0,b=0):
  if isinstance(a,G):self.a,self.b=a.a,a.b;return
  self.a,self.b=F(a),F(b)
 def __add__(self,other):
  o=g(other);return G(self.a+o.a,self.b+o.b)
 __radd__=__add__
 def __neg__(self):return G(-self.a,-self.b)
 def __sub__(self,other):return self+-g(other)
 def __rsub__(self,other):return g(other)+-self
 def __mul__(self,other):
  o=g(other);return G(self.a*o.a-self.b*o.b,self.a*o.b+self.b*o.a)
 __rmul__=__mul__
 def inv(self):
  den=self.a*self.a+self.b*self.b;return G(self.a/den,-self.b/den)
 def __truediv__(self,other):return self*g(other).inv()
 def __pow__(self,n):
  assert n>=0
  out=G(1);cur=self
  while n:
   if n&1:out=out*cur
   cur=cur*cur;n//=2
  return out
 def __eq__(self,other):
  o=g(other);return self.a==o.a and self.b==o.b
 def __hash__(self):return hash((self.a,self.b))
 def __repr__(self):return f'({self.a},{self.b})'
 def conj(self):return G(self.a,-self.b)
def g(z):
 if isinstance(z,G):return z
 if isinstance(z,(int,F)):return G(z)
 z=s.expand(z)
 return G(F(str(s.re(z))),F(str(s.im(z))))
GG=G(0,1)
raw=sec
# polynomials = terms (v exponent,t exponent,Gaussian coeff)
polys={}
for k,(x,y) in raw.items():
 polys[k]=[]
 for expr in [x,y]:
  po=s.Poly(expr,v,t,extension=I)
  terms=[]
  for exps,c in po.terms():
   terms.append((exps[0],exps[1],g(c)))
  polys[k].append(terms)
 for j,label in enumerate(['x','y']):
  polys[k+'bar'] = polys.get(k+'bar',[])
  polys[k+'bar'].append([(a,b,c.conj()) for a,b,c in polys[k][j]])
def ev(p,vv,tt,dv=0,dt=0):
 out=G();vp=[G(1)];tp=[G(1)]
 maxa=max(e[0] for e in p);maxb=max(e[1] for e in p)
 for a in range(maxa):vp.append(vp[-1]*vv)
 for b in range(maxb):tp.append(tp[-1]*tt)
 for a,b,c in p:
  if a<dv or b<dt:continue
  cc=c
  if dv:cc=cc*a
  if dt:cc=cc*b
  out=out+cc*vp[a-dv]*tp[b-dt]
 return out
# 24 table rows from full primary appendix
rows=[
 (-3,-2-2*I),(-2,-1),((-4-3*I)/5,(-26+18*I)/125),((-4+3*I)/5,(-26-18*I)/125),((-3-4*I)/5,(-26-18*I)/125),((-3+4*I)/5,(-26+18*I)/125),(-s.Rational(1,2),-s.Rational(1,8)),(-s.Rational(1,3),(-2-2*I)/27),(-3*I,-2-2*I),(-2*I,-1),(-I/2,-s.Rational(1,8)),(-I/3,(-2-2*I)/27),
 (I/3,(-2-2*I)/27),(I/2,-s.Rational(1,8)),(2*I,-1),(3*I,-2-2*I),(s.Rational(1,3),(-2-2*I)/27),(s.Rational(1,2),-s.Rational(1,8)),((3-4*I)/5,(-26+18*I)/125),((3+4*I)/5,(-26-18*I)/125),((4-3*I)/5,(-26-18*I)/125),((4+3*I)/5,(-26+18*I)/125),(2,-1),(3,-2-2*I)
]
def A(z):return z**8+14*z**4+1
def B(z):return z*(z**4-1)
def C(z):return z**12-33*z**8-33*z**4+1
assert s.expand(A(v)**3-C(v)**2-108*B(v)**4)==0
factors=(v**4-16)*(16*v**4-1)*(v**4-81)*(81*v**4-1)*(25*v**4-14*v**2+25)*(25*v**4+14*v**2+25)
assert s.expand(481**3*B(v)**4-30**4*A(v)**3+factors)==0
for vv,tt in rows:
 V=g(vv);T=g(tt)
 assert T**4==C(V)/G(-4879),(vv,tt,T**4,C(V)/G(-4879))
 assert G(481)**3*B(V)**4-G(30)**4*A(V)**3==0
assert len({g(vv) for vv,_ in rows})==24
# build row info of node and all section incidence & derivatives
S=sorted(polys)
nodeinfo=[]
assert s.expand(A(v)**3-C(v)**2-108*B(v)**4)==0
factors=(v**4-16)*(16*v**4-1)*(v**4-81)*(81*v**4-1)*(25*v**4-14*v**2+25)*(25*v**4+14*v**2+25)
assert s.expand(481**3*B(v)**4-30**4*A(v)**3+factors)==0
for vv,tt in rows:
 V=g(vv);T=g(tt)
 for jj in range(4):
  t0=T*(GG**jj)
  x0=G(3*481**2)*C(V)*t0**2/(G(-4879)*A(V))
  inc={}
  for nm in S:
   x,y=polys[nm]
   if ev(x,V,t0)==x0 and ev(y,V,t0)==0:
    inc[nm]=[(ev(x,V,t0,dv=1),ev(x,V,t0,dt=1)),(ev(y,V,t0,dv=1),ev(y,V,t0,dt=1))]
  if not inc:print('UNCOVERED',V,t0);sys.exit(1)
  nodeinfo.append({'v':V,'t':t0,'cover':inc})
assert {nm:sum(nm in o['cover'] for o in nodeinfo) for nm in S} == {nm:32 for nm in S}
assert min(len(o['cover']) for o in nodeinfo)==2 and max(len(o['cover']) for o in nodeinfo)==10
# equal tangent gradients for same ruling; nonzero determinant = same ruling; rank1 diff => opposite.
def class_sign(r0,r):
 d00=r[0][0]-r0[0][0];d01=r[0][1]-r0[0][1]
 d10=r[1][0]-r0[1][0];d11=r[1][1]-r0[1][1]
 return +1 if d00*d11-d01*d10!=0 or (d00==0 and d01==0 and d10==0 and d11==0) else -1
allrow=[]; iscounter=[]
for idx,o in enumerate(nodeinfo):
 inc=o['cover'];basis=next(iter(inc));rf=inc[basis]
 signs={nm:class_sign(rf,r) for nm,r in inc.items()}
 # Repeat with a distinct reference plane, to check invariance of absolute classes.
 last=next(reversed(inc))
 signs_alt={nm:class_sign(inc[last],r) for nm,r in inc.items()}
 assert signs_alt=={nm:signs[nm]*signs[last] for nm in inc}
 # test consistency of relative sign among all pairs
 for n,r in inc.items():
  for m,rm in inc.items():
   expected=signs[n]*signs[m]
   actual=class_sign(r,rm)
   if expected!=actual:print('BAD RULING',idx,n,m,expected,actual);sys.exit(1)
 col={k:signs.get(k,0)+signs.get(k+'bar',0) for k in sorted(raw)}
 iscounter.append(col)
 allrow.append((o['v'],o['t'],basis,signs,col))
missing=[(i,v,t,co) for i,(v,t,b,ss,co) in enumerate(allrow) if not any(co.values())]
assert not missing
# The divisor is the sum of all twelve section graphs: all six norm weights are one.
weights={k:1 for k in sorted(raw)}
vals=[sum(c[k]*weights[k] for k in weights) for c in iscounter]
print('local divisor signs distribution',{z:sum(s.sign(v)==z for v in vals) for z in [-1,0,1]}, 'min abs',min(map(abs,vals)))

import json
data={'weights':weights,'rows':[{'v':str(v),'t':str(t),'sections':sg,'norm':co,'weighted_class':int(vv)} for (v,t,b,sg,co),vv in zip(allrow,vals)]}
from pathlib import Path
certificate=Path(__file__).with_name('certificate.json')
expected=json.loads(certificate.read_text(encoding='utf-8'))
assert data == expected
assert len({row['v'] for row in data['rows']}) == 24
assert len({(row['v'],row['t']) for row in data['rows']}) == 96
node_map={(row['v'],row['t']):row for row in data['rows']}
for p in nodeinfo:
    cp=(str(p['v'].conj()),str(p['t'].conj()))
    assert cp in node_map
    orig=node_map[(str(p['v']),str(p['t']))]
    assert abs(orig['weighted_class'])==abs(node_map[cp]['weighted_class'])
assert all(abs(x['weighted_class']) in (2,4) for x in data['rows'])
assert sum(abs(x['weighted_class'])==2 for x in data['rows']) == 64
assert sum(abs(x['weighted_class'])==4 for x in data['rows']) == 32
print('CLASS_HISTOGRAM: 64 points with absolute local class 2; 32 points with absolute class 4.')
print('VERIFY_OK: 96 distinct nodes, 12 section graphs, full rank-two ruling test, nonzero Galois norms.')
