#!/usr/bin/env python3
"""Characteristic-seven Hasse matrix, line factors, and exhaustive algebraic depth certificate."""
import sympy as S

a,b,x=S.symbols('a b x')
def red(f,*var):return S.Poly(S.expand(f),*(var or (a,b)),modulus=7).as_expr()
def zero(f,*var):return S.Poly(S.expand(f),*(var or (a,b)),modulus=7).is_zero
f=S.expand((x**4-a*x**2+1)*(x**4-b*x**2+1))
c=S.Poly(S.expand(f**3),x)
h=lambda n:c.nth(n)
M=S.Matrix(3,3,lambda i,j:h(7*(i+1)-(j+1)))
assert all(zero(M[i,j]-(0 if (i+j)%2 else h(7*(i+1)-(j+1)))) for i in range(3) for j in range(3))
P=S.Matrix([[1,0,1],[0,1,0],[1,0,-1]])
H0=h(12);Hp=h(6)-h(4);Hm=h(6)+h(4)
D=P.inv()*M*P-S.diag(Hm,H0,Hp)
assert all(zero(D[i,j]) for i in range(3) for j in range(3))
s=a+b;q=a*b
H0_expected=q**3-q**2-q*s**2-3*q-3*s**2-1
assert zero(H0-H0_expected)
plus=[(a+b+4),(a-2*b-2),(a-4*b-6)]
minus=[(a+b-4),(a-2*b+2),(a-4*b+6)]
assert zero(Hp+plus[0]*plus[1]*plus[2])
assert zero(Hm+minus[0]*minus[1]*minus[2])
# Each H0-line intersection is explicitly split over F7; a high-multiplicity
# root is on the excluded diagonal/singular-branch boundary.
plus_b=[-a-4,4*(a-2),2*(a-6)]
minus_b=[-a+4,4*(a+2),2*(a+6)]
restricted=[
 [-a*(a-3)*(a+2)**4,(a-3)*(a+2)**4*(a+3),(a-1)*(a+2)**4*(a+3)],
 [-a*(a-2)**4*(a+3),(a-3)*(a-2)**4*(a+3),(a-3)*(a-2)**4*(a+1)]
]
for k,Bs in enumerate([plus_b,minus_b]):
 for i,be in enumerate(Bs):
  assert zero(H0.subs(b,be)-restricted[k][i],a)
  # All roots in the affine line are in F7: split into these linear factors.
  fac=S.factor_list(S.Poly(H0.subs(b,be),a,modulus=7).as_expr(),modulus=7)[1]
  assert all(S.Poly(poly,a,modulus=7).degree()==1 for poly,exp in fac)
# Pairs of cross-family Hasse-line equations: intersection at a unique F7
# point or parallel. Same-family lines meet only at excluded singular points.
for group in [plus,minus]:
 for u in range(3):
  for v in range(u+1,3):
   roots=[(i,j) for i in range(7) for j in range(7) if red(group[u].subs({a:i,b:j}))==0 and red(group[v].subs({a:i,b:j}))==0]
   assert roots in [[(5,5)],[(2,2)]]
for f0 in plus:
 for f1 in minus:
  det=S.Poly(f0,a,b).coeff_monomial(a)*S.Poly(f1,a,b).coeff_monomial(b)-S.Poly(f0,a,b).coeff_monomial(b)*S.Poly(f1,a,b).coeff_monomial(a)
  if det%7:
   pts=[(i,j) for i in range(7) for j in range(7) if not(f0.subs({a:i,b:j})%7) and not(f1.subs({a:i,b:j})%7)]
   assert len(pts)==1
# The algebraic rank-at-most-one locus is exhausted by F7 points,
# because every pairwise intersection of H0, Hplus, Hminus is over F7.
smooth=lambda aa,bb: aa not in (2,5) and bb not in (2,5) and aa!=bb
loci={0:[],1:[],2:[],3:[]}
for aa in range(7):
 for bb in range(7):
  if not smooth(aa,bb):continue
  rk=sum(int(int(H.subs({a:aa,b:bb}))%7!=0) for H in (H0,Hp,Hm))
  loci[rk].append((aa,bb))
assert list(map(lambda t:len(loci[t]),range(4)))==[2,12,6,0]
assert loci[0]==[(3,4),(4,3)]
assert sorted(loci[1])==[(0,3),(0,4),(1,3),(1,4),(3,0),(3,1),(3,6),(4,0),(4,1),(4,6),(6,3),(6,4)]
print('HOWE_7_SYMBOLIC_OK ranks_on_F7=',[len(loci[r]) for r in range(4)])
