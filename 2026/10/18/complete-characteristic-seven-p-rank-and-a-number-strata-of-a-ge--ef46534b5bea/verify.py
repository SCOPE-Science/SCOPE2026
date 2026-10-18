#!/usr/bin/env python3
"""Exact characteristic-seven invariant-stratum verification; Python 3 and SymPy."""
import sympy as S
s,p,x=S.symbols('s p x')
F=x**8+s*x**6+(p+2)*x**4+s*x**2+1
Hf=S.Poly(S.expand(F**3),x)
get=lambda i: S.Poly(Hf.coeff_monomial(x**i),s,p,modulus=7).as_expr()
M=S.Matrix([[get(7*i-j) for j in (1,2,3)] for i in (1,2,3)])
A=(p+3)*((p+1)*(p+2)-s*s)
B=(s-4)*(s*s+s-2-p)
C=(s+4)*(s*s-s-2-p)
red=lambda f: S.Poly(S.expand(f),s,p,modulus=7).as_expr()
quartic0=(x*x+S.Symbol('a')*x+1)*(x*x+S.Symbol('b')*x+1)
a,b=S.symbols('a b')
def symm(e):
 ex, rem,_=S.symmetrize(e,[a,b],formal=True)
 assert rem==0
 return S.expand(ex.subs({S.Symbol('s1'):s,S.Symbol('s2'):p}))
q0=(x*x+a*x+1)*(x*x+b*x+1)
qm=(x*x+a-2)*(x*x+b-2)
qp=(x*x+a+2)*(x*x+b+2)
for q,h in [(q0,A),(qm,B),(qp,C)]:
 coef=S.Poly(S.expand(q**3),x).coeff_monomial(x**6)
 assert red(symm(coef)-h)==0, (coef,h)
print('ELLIPTIC_HASSE_FACTORIZATIONS_OK')
# The direct genus-three Cartier-Manin determinant gives an independent matrix check.
D=red(M.det())
prod=red(A*B*C)
ratios=[]
for ss in range(7):
 for pp in range(7):
  vv=int(prod.subs({s:ss,p:pp}))%7
  if vv: ratios.append(int(D.subs({s:ss,p:pp}))%7*pow(vv,-1,7)%7)
assert len(set(ratios))==1 and ratios
r=ratios[0]
assert red(D-r*prod)==0
print('GENUS_THREE_MATRIX_DETERMINANT_OK', 'scalar=',r)
# For a smooth parameter chart, no other geometric common zeros exist.
# Elimination resultants are over GF(7); factorization gives all possible s.
for label,fx,fy,wanted in [
 ('AB',A,B,[(0,5),(2,4),(4,0)]),
 ('AC',A,C,[(0,5),(5,4),(3,0)]),
 ('BC',B,C,[(0,5),(4,3),(3,3)])]:
 R=S.Poly(S.resultant(fx,fy,p),s,modulus=7)
 fac=S.factor_list(R)[1]
 cand={(-int(q.all_coeffs()[-1])%7) for q,m in fac if q.degree()==1}
 assert cand=={ss for ss,pp in wanted},(label,cand,wanted)
 found=[]
 for ss in cand:
  # At each resultant root the univariate gcd captures *all* geometric p-roots.
  gx=S.Poly(fx.subs(s,ss),p,modulus=7)
  gy=S.Poly(fy.subs(s,ss),p,modulus=7)
  gg=S.gcd(gx,gy)
  coef,factors=S.factor_list(gg)
  assert all(t.degree()==1 for t,m in factors),(label,ss,factors)
  for t,m in factors:
   pp=(-int(t.all_coeffs()[-1])*pow(int(t.all_coeffs()[0])%7,-1,7))%7
   if int(((s*s-4*p)*(p*p+p+3*s*s+2)).subs({s:ss,p:pp}))%7: found.append((ss,pp))
 assert sorted(found)==sorted(wanted),(label,found,wanted)
 print(label,'common smooth candidates',wanted,'elimination',[(str(t.as_expr()),m) for t,m in fac])
# All seven candidates are on smooth locus and have precisely the claimed ranks.
U=(s*s-4*p)*(p*p+p+3*s*s+2)
rank2=[(2,4),(4,0),(5,4),(3,0),(4,3),(3,3)]
rank3=[(0,5)]
for ss,pp in rank2+rank3:
 values=[int(red(h).subs({s:ss,p:pp}))%7 for h in (A,B,C)]
 assert int(U.subs({s:ss,p:pp}))%7
 zero_count=sum(z==0 for z in values)
 assert zero_count==(3 if (ss,pp)==(0,5) else 2)
 print('EXCEPTION',ss,pp,'a-number',zero_count,'p-rank',3-zero_count)
# Check that all multiple Hasse intersections in the smooth chart are transverse.
for ss,pp in rank2+rank3:
 vanishing=[f for f in (A,B,C) if int(f.subs({s:ss,p:pp}))%7==0]
 for i in range(len(vanishing)):
  for j in range(i+1,len(vanishing)):
   ff,gg=vanishing[i],vanishing[j]
   minor=S.diff(ff,s)*S.diff(gg,p)-S.diff(ff,p)*S.diff(gg,s)
   assert int(minor.subs({s:ss,p:pp}))%7!=0,(ss,pp,i,j)
print('TRANSVERSE_ALL_SEVEN_INTERSECTIONS_OK')
# For all GF7 points on U, confirm the ranks via a direct genus-three Cartier matrix.
def rankmod7(v):
 ar=[[int(t)%7 for t in row] for row in v]
 k=0
 for j in range(len(ar[0])):
  z=next((i for i in range(k,len(ar)) if ar[i][j]),None)
  if z is None:continue
  ar[k],ar[z]=ar[z],ar[k]; w=pow(ar[k][j],-1,7)
  ar[k]=[t*w%7 for t in ar[k]]
  for i in range(len(ar)):
   if i!=k:
    r0=ar[i][j];ar[i]=[(u-r0*v)%7 for u,v in zip(ar[i],ar[k])]
  k+=1
 return k
counts={0:0,1:0,2:0,3:0}
for ss in range(7):
 for pp in range(7):
  if int(U.subs({s:ss,p:pp}))%7==0: continue
  num=sum(int(red(h).subs({s:ss,p:pp}))%7==0 for h in (A,B,C))
  Mval=M.subs({s:ss,p:pp}).tolist()
  assert rankmod7(Mval)==3-num,(ss,pp,num,Mval)
  counts[num]+=1
print('GF7_RANK_COUNTS',counts)
print('VERIFY_OK')
