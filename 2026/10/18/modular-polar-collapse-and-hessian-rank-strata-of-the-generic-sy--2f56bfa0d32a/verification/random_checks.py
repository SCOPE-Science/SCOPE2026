#!/usr/bin/env python3
"""Finite spot checks over F2 of the polar base and pointwise Hessian ranks."""
import random
import sympy as s
from check_hessian import setup, det_rank_mod

def run(n, samples):
 pairs,x,A,f,H,g=setup(n)
 fn=s.lambdify(x,list(H),'math')
 an=s.lambdify(x,list(A),'math')
 gn=s.lambdify(x,g,'math')
 rng=random.Random(n*143)
 for v in samples:
  Am=s.Matrix(n,n,[z%2 for z in an(*v)])
  Hm=s.Matrix(len(x),len(x),[z%2 for z in fn(*v)])
  d=det_rank_mod(Am,2); h=det_rank_mod(Hm,2)
  induced_alt=None
  if d==n-1:
   # all principal (n-2)-minors of an invertible restriction vanish iff induced quotient alternating
   # Equivalently, the diagonal of the adjugate of a nonsingular (n-1)-dimensional sub-block
   inds=next(comb for comb in __import__('itertools').combinations(range(n),n-1) if det_rank_mod(Am.extract(comb,comb),2)==n-1)
   Bi=Am.extract(inds,inds)
   induced_alt=all(int(Bi.adjugate()[i,i])%2==0 for i in range(n-1))
  expect= n-(n%2) if d==n else (0 if induced_alt else 2) if d==n-1 else 2 if d==n-2 else 0
  assert h==expect,(n,v,d,h,expect)
  base = all(int(z)%2==0 for z in gn(*v))
  alternating=(all(v[k]==0 for k,(i,j) in enumerate(pairs) if i==j))
  assert base == (d<=n-2 or (n%2==0 and alternating)),(n,v,d,base)
 print('spot n=',n,'tested=',len(samples),'OK')

if __name__=='__main__':
 for n in (3,4):
  rng=random.Random(n)
  M=n*(n+1)//2
  vlist=[tuple((mask>>i)&1 for i in range(M)) for mask in range(1<<M)] if n==3 else [tuple(rng.randrange(2) for _ in range(M)) for _ in range(150)]
  run(n,vlist)
 print('FINITE_SPOTS_OK')
