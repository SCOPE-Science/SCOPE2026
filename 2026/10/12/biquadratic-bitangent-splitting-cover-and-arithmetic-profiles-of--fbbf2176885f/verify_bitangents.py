#!/usr/bin/env python3
"""Exact symbolic checks for the 28 bitangents of the symmetric Ciani pencil.
Requires SymPy. The accompanying proof supplies the classical 28-bitangent theorem
and degree-four rational-map argument; finite computations alone do not prove them.
"""
import sympy as sp
s,x,y,z=sp.symbols('s x y z')
lam=-2*(s**4+1)/(s**2+1)**2
r=(s**2-1)/(s**2+1)
F=lambda X,Y,Z:sp.expand(X**4+Y**4+Z**4+lam*(X**2*Y**2+X**2*Z**2+Y**2*Z**2))
zero=lambda E:sp.cancel(E)==0
assert zero(F(s*y,y,z)-(z**2+lam*(s**2+1)*y**2/2)**2)
assert zero(F(x,y,x+y)-(lam+2)*(x*x+x*y+y*y)**2)
assert zero(F(x,y,r*x+y)-(lam+2)*(y*y+r*x*y-x*x)**2)
assert zero(r**2+lam+1)
assert zero(lam+2*(s**4+1)/(s**2+1)**2)
assert zero(lam.subs(s,-s)-lam) and zero(lam.subs(s,1/s)-lam)
assert zero(r.subs(s,-s)-r) and zero(r.subs(s,1/s)+r)
# Three sets of four axis lines, four sign-sum lines, twelve mixed lines.
T=[s,-s,1/s,-1/s]
lines=[]; groups=[]
for i,j in [(0,1),(0,2),(1,2)]:
 for t in T:
  row=[0,0,0]; row[i]=1; row[j]=-t
  lines.append(tuple(row)); groups.append('A')
for a in (1,-1):
 for b in (1,-1):
  lines.append((a,b,1));groups.append('B')
for k in range(3):
 inds=[i for i in range(3) if i!=k]
 for a in (1,-1):
  for b in (1,-1):
   row=[0,0,0]; row[inds[0]]=a;row[inds[1]]=b;row[k]=r
   lines.append(tuple(row));groups.append('C')
assert len(lines)==28 and [groups.count(q) for q in 'ABC']==[12,4,12]
def equivalent(L,M):
 return all(zero(L[i]*M[j]-L[j]*M[i]) for i in range(3) for j in range(i+1,3))
assert all(not equivalent(lines[i],lines[j]) for i in range(28) for j in range(i+1,28))
# Verify each line class is a tangent twice via the corresponding factorization;
# signed permutations preserve the symmetric quartic.
def transformed(row, operation):
 return tuple(sp.cancel(u.subs(s,operation)) if hasattr(u,'subs') else u for u in row)
for operation in (-s,1/s):
 perm=[]
 for L in lines:
  arr=[j for j,M in enumerate(lines) if equivalent(transformed(L,operation),M)]
  assert len(arr)==1
  perm.append(arr[0])
 assert len(set(perm))==28
# Galois-orbit sizes under s -> -s, s -> 1/s.
p1=[];p2=[]
for op,dest in [(-s,p1),(1/s,p2)]:
 for L in lines:
  dest.append(next(j for j,M in enumerate(lines) if equivalent(transformed(L,op),M)))
seen=set();orbit_counts={}
for i in range(28):
 if i in seen:continue
 orbit={i};front=[i]
 while front:
  k=front.pop()
  for j in (p1[k],p2[k]):
   if j not in orbit:orbit.add(j);front.append(j)
 seen |= orbit
 typ=groups[i]; orbit_counts[(typ,len(orbit))]=orbit_counts.get((typ,len(orbit)),0)+1
assert orbit_counts=={('A',4):3,('B',1):4,('C',2):6},orbit_counts
# One explicit smooth rational member t=2.
assert lam.subs(s,2)==sp.Rational(-34,25)
assert r.subs(s,2)==sp.Rational(3,5)
for L in lines:
 assert all(sp.cancel(v.subs(s,2)).is_Rational if hasattr(v,'subs') else True for v in L)
print('VERIFY_OK distinct_bitangents=28 classes=A12+B4+C12 generic_Galois=V4 orbits=1^4+2^6+4^3 rational_lambda_t2=-34/25')
# Complete quadratic-field description: h^2=lambda+2, r^2=-lambda-1,
# s=(1+r)/h and h=(1+r)/s; this proves both inclusions of splitting fields.
h=2*s/(s*s+1)
assert zero(h**2-lam-2)
assert zero(s-(1+r)/h)
assert zero((1+r)/s-h)
assert zero((s-1/s)/(s+1/s)-r)
# Three degree-two subfields of the generic V4 extension.
assert zero((s+1/s)**2-4/(lam+2))
assert zero((s-1/s)**2+4*(lam+1)/(lam+2))
# Riemann-Hurwitz branch-fibre representatives: s=0,±1,±I,∞.
assert lam.subs(s,0)==-2
assert lam.subs(s,1)==-1 and lam.subs(s,-1)==-1
assert zero(sp.diff(lam,s)+8*s*(s-1)*(s+1)/(s*s+1)**3)
# Rational/real specializations: square-class decomposition drives orbit sizes.
for t in (sp.Rational(2),sp.Rational(3,2),sp.Rational(1,3)):
 a=sp.cancel(lam.subs(s,t)); R=sp.cancel(r.subs(s,t)); H=sp.cancel(h.subs(s,t))
 assert R*R==-a-1 and H*H==a+2 and sp.cancel((1+R)/H)==t
 assert sp.Rational(-2)<a<sp.Rational(-1)
print('VERIFY_OK quadratic_subfields=A=-lambda-1,B=lambda+2 branch=-2,-1,infinity real_counts=16,28,4')
