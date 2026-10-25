#!/usr/bin/env python3
"""Exact representation-ring checks and independent Weyl quadrature for a sharp SU(N) character inequality."""
from collections import Counter
import math
import numpy as np
import sympy as sp

checks=0
def ck(z, msg):
 global checks
 assert z, msg
 checks += 1

def weights(N,p):
 def first(j):
  return (2*p-2*j,j)+(0,)*(N-3)
 def dual(w): return tuple(reversed(w))
 A=[first(j) for j in range(p+1)]
 B=[dual(x) for x in A]
 C=[(j,)+(0,)*(N-3)+(j,) for j in range(p+1)]
 # Each type is multiplicity-free.
 ck(len(set(A))==p+1 and len(set(B))==p+1 and len(set(C))==p+1, 'multiplicity')
 return A,B,C

def group_moment(N,p,a,b,c):
 A,B,C=weights(N,p)
 sums=Counter()
 # Counter of complex coefficients indexed by irreducible Dynkin labels.
 for w in A: sums[w]+=a*a
 for w in B: sums[w]+=b*b
 for w in C: sums[w]+=2*a*b
 sums[(0,)*(N-1)]+=c*c
 # Linear characters: χ_p and conjugate χ_p.
 chi=(p,)+(0,)*(N-2)
 chibar=(0,)*(N-2)+(p,)
 sums[chi]+=2*a*c; sums[chibar]+=2*b*c
 return sum(sp.expand(z*sp.conjugate(z)) for z in sums.values())

def formula(N,p,a,b,c):
 A=a*sp.conjugate(a);B=b*sp.conjugate(b);C=c*sp.conjugate(c)
 base=(p+1)*(A*A+B*B+4*A*B)+C*C+4*C*(A+B)+4*sp.re(c*c*sp.conjugate(a*b))
 if N==4: return sp.expand(base+2*sp.re(a*a*sp.conjugate(b*b)))
 if N>=5: return sp.expand(base)
 # SU(3) extra collisions between Sym^p and its dual + χ, χbar
 out=base+4*sp.re(a*a*sp.conjugate(b*c))+4*sp.re(b*b*sp.conjugate(a*c))
 if p%3==0:
  out+=(a+b)**2*sp.conjugate((a+b)**2)-(A*A+B*B+4*A*B)
 return sp.expand(out)

samples=[(sp.Integer(1),sp.Integer(2),sp.Integer(3)),
         (sp.Integer(1)+sp.I,2-sp.I,3+2*sp.I),
         (sp.Integer(-2)+3*sp.I,3-sp.I,-1+sp.I),
         (sp.Integer(0),sp.Integer(1),sp.Integer(2)),
         (sp.Integer(1),sp.Integer(0),sp.Integer(0))]
for N in range(3,9):
 for p in range(1,13):
  A,B,C=weights(N,p)
  for x,y,Z in samples:
   ck(sp.simplify(group_moment(N,p,x,y,Z)-formula(N,p,x,y,Z))==0,
      f'group identity N={N},p={p},sample={x,y,Z}')
  # Verify every overlap by direct Dynkin-weight intersection.
  aa=set(A);bb=set(B);cc=set(C)
  if N==3 and p%3==0:
   ex={(2*p//3,2*p//3)}
   ck(aa&bb==ex and aa&cc==ex and bb&cc==ex,'SU3 triple overlap')
  elif N==3:
   ck(not (aa&bb or aa&cc or bb&cc),'SU3 no triple')
  elif N==4:
   ck(aa&bb=={(0,p,0)} and not aa&cc and not bb&cc,'SU4 overlap')
  else:
   ck(not(aa&bb or aa&cc or bb&cc),'higher-rank disjointness')
  chi=(p,)+(0,)*(N-2);chibar=(0,)*(N-2)+(p,)
  if N==3:
   ck(chibar in aa and chi in bb and chi not in cc and chibar not in cc,'SU3 linear collision')
  else:
   ck(chi not in (aa|bb|cc) and chibar not in (aa|bb|cc),'no other linear collision')

r,p,d=sp.symbols('r p d',positive=True)
K=sp.Rational(3,2)*(p+1)+sp.Rational(5,2)*d
F=(K+2*sp.sqrt(2)*r+6*r*r+r**4)/(1+r*r)**2
poly=4*r**3+3*sp.sqrt(2)*r**2+(3*p+5*d-3)*r-sp.sqrt(2)
ck(sp.simplify(sp.diff(F,r)*(1+r*r)**3+2*poly)==0,'cubic derivative identity')
A,B,C=sp.symbols('A B C',real=True,nonnegative=True)
# Exactly sharp rank-dependent stability identities for the c=0 problem.
ck(sp.simplify(sp.Rational(3,2)*(p+1)*(A+B)**2-(p+1)*(A*A+B*B+4*A*B) -sp.Rational(1,2)*(p+1)*(A-B)**2)==0,'balance defect')

for pp in range(1,21):
 dd=int(pp%3==0)
 polynomial=sp.Poly(poly.subs({p:pp,d:dd}),r)
 roots=sp.nroots(polynomial,maxsteps=100)
 pos=[complex(t).real for t in roots if abs(complex(t).imag)<1e-9 and complex(t).real>0]
 ck(len(pos)==1,'single positive root')
 rr=pos[0]; gain=float(F.subs({p:pp,d:dd,r:rr})-K.subs({p:pp,d:dd}))
 ck(gain>0 and rr>0,'strict gain')

# Independent finite-grid Weyl-integration tests. Periods here are chosen above
# all frequencies in the Laurent integrand for these examples.
def h_poly(e,p):
 h=[np.ones(e.shape[1],complex)]+[np.zeros(e.shape[1],complex) for _ in range(p)]
 for z in e:
  for j in range(1,p+1):h[j]+=z*h[j-1]
 return h[p]

def weyl(N,p,aa,bb,cc,L):
 grid=np.indices((L,)*(N-1),dtype=np.int16).reshape(N-1,-1)
 z=np.exp(2j*np.pi*grid/L)
 z=np.vstack([z,1/np.prod(z,axis=0)])
 chi=h_poly(z,p)
 f=abs(aa*chi+bb*np.conj(chi)+cc)**4
 for i in range(N):
  for j in range(i+1,N):f*=abs(z[i]-z[j])**2
 return float(f.mean()/math.factorial(N))
for N,p,L in [(3,1,29),(3,2,29),(3,3,40),(4,1,27),(4,2,29),(5,1,17)]:
 a,b,c=(1+1j), (2-1j), (1-2j)
 got=weyl(N,p,a,b,c,L)
 exact=complex(formula(N,p,1+sp.I,2-sp.I,1-2*sp.I))
 ck(abs(got-exact.real) < 2e-8 and abs(exact.imag)<1e-10,
    f'Weyl check {N,p}: {got} vs {exact}')
print(f'PASS: {checks} exact overlap, formula, calculus, algebra and independent finite-grid Weyl quadrature assertions')
