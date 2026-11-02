"""Second exact check by modular unit-rank filtration and direct determinant.
Requires sympy only. Cubic edge lists are explicit, no other inputs.
"""
from itertools import combinations
from sympy import Matrix, factorint, prod
from verify import REPRESENTATIVES,EXPECTED

def build_reduced_laplacian(edges):
 S=list(combinations(range(8),2)); index={x:i for i,x in enumerate(S)}
 E={frozenset(p) for p in edges}; neighbors=[set() for _ in S]
 for i,(x,y) in enumerate(S):
  for z in range(8):
   if z==x or z==y:continue
   if frozenset((x,z)) in E:neighbors[i].add(index[tuple(sorted((z,y)))])
   if frozenset((y,z)) in E:neighbors[i].add(index[tuple(sorted((x,z)))])
 assert sum(map(len,neighbors))==144
 L=[[0]*27 for _ in range(27)]
 for i in range(27):
  L[i][i]=len(neighbors[i])
  for j in neighbors[i]:
   if j<27:L[i][j]-=1
 return L

def local_unit_filtration(A,p,E):
 """Over Z/p^E, peel off invertible pivots, divide residual by p.
 Count pivots at layer k => elementary divisors of valuation k.
 This algorithm never divides by nonunits, unlike general field Gaussian elimination.
 """
 B=[row[:] for row in A]; vals=[];layer=0
 while B:
  assert layer<=E,('missing nonsingular pivot',p,E)
  q=p**(E+1-layer)
  B=[[x%q for x in row] for row in B]
  n=len(B);r=0
  while r<n:
   pos=next(((i,j) for i in range(r,n) for j in range(r,n) if B[i][j]%p),None)
   if pos is None:break
   i,j=pos;B[i],B[r]=B[r],B[i]
   for z in range(n):B[z][j],B[z][r]=B[z][r],B[z][j]
   inv=pow(B[r][r],-1,q)
   for i in range(r+1,n):
    mult=B[i][r]*inv%q
    for j in range(r,n): B[i][j]=(B[i][j]-mult*B[r][j])%q
   for j in range(r+1,n):
    mult=B[r][j]*inv%q
    for i in range(r,n): B[i][j]=(B[i][j]-mult*B[i][r])%q
   r+=1
  vals.extend([layer]*r)
  assert all(B[i][j]%p==0 for i in range(r,n) for j in range(r,n))
  B=[[B[i][j]//p for j in range(r,n)] for i in range(r,n)]
  layer+=1
 return sorted(vals)

def run():
 for i,E in enumerate(REPRESENTATIVES):
  A=build_reduced_laplacian(E)
  tau=int(abs(Matrix(A).det(method='domain-ge')))
  fact=factorint(tau)
  loc={p:local_unit_filtration(A,p,e) for p,e in fact.items()}
  assert all(len(loc[p])==27 and sum(loc[p])==e for p,e in fact.items())
  factors=[int(prod(p**loc[p][j] for p in fact)) for j in range(27)]
  assert all(factors[j+1]%factors[j]==0 for j in range(26))
  assert [t for t in factors if t>1]==EXPECTED[i], (i,factors)
  print('INDEPENDENT_CLASS_%d_OK determinant=%d nontrivial=%s'%(i+1,tau,[t for t in factors if t>1]),flush=True)
 print('INDEPENDENT_UNIT_FILTRATION_CERTIFICATE_OK')
if __name__=='__main__':run()
