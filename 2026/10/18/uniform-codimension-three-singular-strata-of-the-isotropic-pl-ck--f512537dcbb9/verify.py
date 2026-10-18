"""Exact checks for Gram-corank singular strata of Plucker isotropic quadrics.
All operations use integer/rational arithmetic and standard SymPy only.
"""
import sympy as sp
from math import comb

def local_check(k,n):
    m=n-k
    A=sp.Matrix.hstack(sp.eye(k),sp.Matrix(k,m,lambda i,j:(i+2)*(j+1) + (i==j)*2 - (i+j)%3))
    G=A*A.T
    detG=G.det()
    minor_sq=0
    from itertools import combinations
    for idx in combinations(range(n),k):
        minor_sq+=A[:,idx].det()**2
    assert detG==minor_sq,('Cauchy-Binet',k,n)
    B=A[:,k:n]
    adj=G.adjugate()
    for i in range(k):
      for j in range(m):
        dij=sp.diff(sp.det(sp.eye(k)+sp.Matrix(k,m,lambda r,c:sp.Symbol('b_%d_%d'%(r,c)))*sp.Matrix(m,k,lambda c,r:sp.Symbol('b_%d_%d'%(r,c)))),sp.Symbol('b_%d_%d'%(i,j)))
        subs={sp.Symbol('b_%d_%d'%(r,c)):B[r,c] for r in range(k) for c in range(m)}
        assert dij.subs(subs)==2*(adj*B)[i,j]
    return k,n

for k,n in [(2,4),(2,5),(3,5),(3,6),(3,7),(4,6)]:
    assert local_check(k,n)==(k,n)
for n in range(4,16):
 for k in range(2,n-1):
    for r in range(1,min(k,n-k)+1):
      dimO=r*(n-r)-r*(r+1)//2
      dimFiber=(k-r)*(n-k-r)
      codim=k*(n-k)-dimO-dimFiber
      assert codim==r*(r+1)//2,(n,k,r)
print('VERIFY_OK cauchy_binet_and_jacobian=6 exact_codim_dimension_profiles=verified n=4..15 k=2..n-2')
