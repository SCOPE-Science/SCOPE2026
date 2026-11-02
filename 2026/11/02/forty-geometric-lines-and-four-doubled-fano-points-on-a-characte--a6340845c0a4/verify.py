#!/usr/bin/env python3
"""Exact line-Fano-scheme certificate for the printed six-term quartic in char 5.
Requires SymPy; all finite field and algebraic computations are exact.
"""
from collections import Counter
from itertools import combinations,product
import sympy as sp

# GF(25)=GF(5)[a]/(a^2-2); elements are u+v*a, encoded u+5*v.
Q=25
ADD=[[(x%5+y%5)%5+5*((x//5+y//5)%5) for y in range(Q)] for x in range(Q)]
MUL=[[(x%5*y%5+2*(x//5)*(y//5))%5+5*((x%5*(y//5)+(x//5)*(y%5))%5) for y in range(Q)] for x in range(Q)]
NEG=[(-(x%5))%5+5*((-(x//5))%5) for x in range(Q)]

def add(*xs):
 r=0
 for x in xs:r=ADD[r][x]
 return r

def mul(*xs):
 r=1
 for x in xs:r=MUL[r][x]
 return r

def pw(x,k):
 r=1
 while k:
  if k&1:r=MUL[r][x]
  x=MUL[x][x];k>>=1
 return r

# Equation as printed in Veniani, arXiv:1502.04510v2, Example 7.6.
def quartic(X):
 a,b,c,d=X
 return add(mul(a,a,b,c),mul(b,b,c,c),mul(a,b,b,d),
            mul(a,c,c,d),mul(a,a,d,d),mul(b,c,d,d))

def echelon(piv,vals):
 i,j=piv
 r=[[0]*4 for _ in range(2)];r[0][i]=r[1][j]=1
 free=[(0,k) for k in range(i+1,4) if k!=j]+[(1,k) for k in range(j+1,4)]
 assert len(free)==len(vals)
 for (row,col),val in zip(free,vals):r[row][col]=val
 return tuple(r[0]+r[1])

def pivot(B):
 return (next(i for i in range(4) if B[i]!=0),next(i for i in range(4) if B[4+i]!=0))

def contains_line(B):
 # Evaluations at the five distinct points (1,t), t=0,...,4, certify that
 # a polynomial of degree at most 4 in t vanishes identically.
 for t in range(5):
  X=[add(B[i],mul(t,B[4+i])) for i in range(4)]
  if quartic(X):return False
 return True

def all_lines(q):
 found=[]
 for piv in combinations(range(4),2):
  i,j=piv
  free=[(0,k) for k in range(i+1,4) if k!=j]+[(1,k) for k in range(j+1,4)]
  for vals in product(range(q),repeat=len(free)):
   B=echelon(piv,vals)
   if contains_line(B):found.append(B)
 assert len(found)==len(set(found))
 return sorted(found)

U,V=sp.symbols('U V')

def polynomials(piv,full_open=False):
 i,j=piv
 if full_open:
  free=[(row,k) for row in range(2) for k in range(4) if k not in (i,j)]
 else:
  free=[(0,k) for k in range(i+1,4) if k!=j]+[(1,k) for k in range(j+1,4)]
 sy=sp.symbols('a:'+str(len(free)))
 B=[[sp.Integer(0)]*4 for _ in range(2)];B[0][i]=B[1][j]=1
 for value,(row,col) in zip(sy,free):B[row][col]=value
 a,b,c,d=[B[0][k]*U+B[1][k]*V for k in range(4)]
 F=a*a*b*c+b*b*c*c+a*b*b*d+a*c*c*d+a*a*d*d+b*c*d*d
 P=sp.Poly(F,U,V)
 eq=[P.coeff_monomial(U**k*V**(4-k)) for k in range(5)]
 return sy,free,eq

def quotient_degree(gb,sy,cutoff=30):
 if not sy:return int(all(g.as_expr()==0 for g in gb.polys))
 LM=[p.monoms()[0] for p in gb.polys]
 if (0,)*len(sy) in LM:return 0
 bounds=[]
 for k in range(len(sy)):
  b=[m[k] for m in LM if all(m[j]==0 for j in range(len(sy)) if j!=k)]
  assert b,('not zero-dimensional',sy,LM)
  bounds.append(min(b))
 return sum(not any(all(e[k]>=m[k] for k in range(len(sy))) for m in LM)
            for e in product(*[range(b) for b in bounds]))

def poly_value(P,xx):
 val=0
 for exp,coef in P.terms():
  z=int(coef)%5
  for x,e in zip(xx,exp):z=mul(z,pw(x,e))
  val=add(val,z)
 return val

def rank5x4(A):
 A=[row[:] for row in A];h=0
 for col in range(4):
  row=next((r for r in range(h,5) if A[r][col]!=0),None)
  if row is None:continue
  A[h],A[row]=A[row],A[h]
  inv=pw(A[h][col],23)
  A[h]=[mul(inv,x) for x in A[h]]
  for r in range(5):
   if r==h:continue
   z=A[r][col]
   A[r]=[add(A[r][k],NEG[mul(z,A[h][k])]) for k in range(4)]
  h+=1
 return h

def open_chart_tangent(B):
 piv=pivot(B)
 sy,free,eq=polynomials(piv,True)
 values=[B[row*4+k] for row,k in free]
 JJ=[[sp.Poly(sp.diff(e,y),*sy,modulus=5) for y in sy] for e in eq]
 return rank5x4([[poly_value(c,values) for c in row] for row in JJ])

def truncated_local_degree(piv,N):
 sy,free,eq=polynomials(piv,True)
 mn=[sp.prod(x**n for x,n in zip(sy,e)) for e in product(range(N+1),repeat=4) if sum(e)==N]
 gb=sp.groebner(eq+mn,*sy,modulus=5,order='grevlex')
 LM=[p.LM(order='grevlex').exponents for p in gb.polys]
 if (0,0,0,0) in LM:return 0
 return sum(not any(all(e[k]>=m[k] for k in range(4)) for m in LM)
            for e in product(range(N),repeat=4) if sum(e)<N)

def main():
 assert all(add(x,NEG[x])==0 for x in range(25))
 assert all(pw(x,25)==x for x in range(25))
 assert all(mul(x,pw(x,23))==1 for x in range(1,25))
 assert pw(5,2)==2
 lines5=all_lines(5)
 lines25=all_lines(25)
 print('LINE_COUNTS_BY_FIELD',len(lines5),len(lines25))
 assert len(lines5)==4 and len(lines25)==40
 assert set(lines5)<=set(lines25)
 cellcounts=Counter(map(pivot,lines25))
 print('F25_RREF_CELL_COUNTS',sorted(cellcounts.items()))
 assert [cellcounts[p] for p in combinations(range(4),2)]==[25,9,4,0,1,1]
 chart_degrees={}
 for piv in combinations(range(4),2):
  sy,free,eq=polynomials(piv,False)
  if not sy:
   chart_degrees[piv]=int(all(sp.expand(e)==0 for e in eq))
  else:
   gb=sp.groebner(eq,*sy,order='lex',modulus=5)
   # Checking each original restricted quartic coefficient reduces to zero.
   assert all(gb.reduce(e)[1]==0 for e in eq)
   chart_degrees[piv]=quotient_degree(gb,sy)
 print('SCHUBERT_CELL_ARTIN_LENGTH_BOUNDS',sorted(chart_degrees.items()))
 assert [chart_degrees[p] for p in combinations(range(4),2)]==[26,9,4,0,1,1]
 # On the big open (0,1) cell, 25 points with quotient length 26;
 # the tangent calculation below gives an infinitesimal direction at one,
 # exhausting the possible geometric points in that cell.
 tangent=Counter(); bad=[]
 for B in lines25:
  r=open_chart_tangent(B)
  tangent[r]+=1
  if r<4:bad.append(B)
 print('FULL_OPEN_GRASSMANN_TANGENT_RANKS',dict(sorted(tangent.items())))
 assert tangent=={4:36,3:4}
 coordinate={echelon(p,(0,)*(len([k for k in range(p[0]+1,4) if k!=p[1]])+len([k for k in range(p[1]+1,4)]))) for p in [(0,1),(0,2),(1,3),(2,3)]}
 assert set(bad)==coordinate
 print('TANGENT_DEFECT_LINES',sorted(map(pivot,bad)))
 for piv in [(0,1),(0,2),(1,3),(2,3)]:
  lengths=(truncated_local_degree(piv,2),truncated_local_degree(piv,3))
  print('LOCAL_JET_LENGTHS',piv,lengths)
  assert lengths==(2,2)
 # Since each 0-dimensional local ring has length 2 modulo m^2 and m^3,
 # Nakayama gives m^2=0 and exact local length 2. All others are reduced.
 print('FANO_SCHEME_GEOMETRIC_SUPPORT',40,'SCHEME_LENGTH',40+4)
 image={B:tuple(pw(x,5) for x in B) for B in lines25}
 assert set(image.values())==set(lines25)
 seen=set();cycles=Counter()
 for B in lines25:
  if B in seen:continue
  C=B;l=0
  while C not in seen:
   seen.add(C);C=image[C];l+=1
  assert C==B
  cycles[l]+=1
 print('FROBENIUS_CYCLE_COUNTS',dict(sorted(cycles.items())))
 assert cycles=={1:4,2:18}
 print('REDUCED_LINE_ZETA_DENOMINATOR','(1-T)^4 * (1-T^2)^18')
 print('SYMPY_VERSION',sp.__version__)
 print('VERIFY_OK')
if __name__=='__main__':main()
