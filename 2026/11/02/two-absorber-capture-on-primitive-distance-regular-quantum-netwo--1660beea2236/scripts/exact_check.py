#!/usr/bin/env python3
"""Exact rational spectral-projector check for Petersen and odd graph O4."""
import itertools
import sympy as sp

def kneser(n,k):
  v=list(itertools.combinations(range(n),k))
  A=sp.zeros(len(v))
  for i,U in enumerate(v):
    for j,V in enumerate(v):
      if i!=j and not set(U)&set(V):A[i,j]=1
  return A

def check(n,k,spectrum):
 A=kneser(n,k);N=A.rows;I=sp.eye(N)
 P=[]
 for lam in spectrum:
  q=I
  for mu in spectrum:
   if mu!=lam:q=q*(A-mu*I)/(lam-mu)
  assert q*q==q and A*q==lam*q
  P.append(q)
 assert sum(P,sp.zeros(N))==I
 mult=[sp.trace(E) for E in P]
 print(f'KG({n},{k}) size={N}, eigenvalues={spectrum}, multiplicities={mult}')
 for z in range(1, k+1):
  # BFS distances
  verts=list(itertools.combinations(range(n),k))
  dist=[999]*N;dist[0]=0;todo=[0]
  for u in todo:
   for w in range(N):
    if A[u,w] and dist[w]==999:dist[w]=dist[u]+1;todo.append(w)
  ws=[u for u in range(N) if dist[u]==z]
  if not ws:continue
  cos=[sp.factor(E[0,ws[0]]/E[0,0]) for E in P]
  assert all(E[0,w]/E[0,0]==c for E,c in zip(P,cos) for w in ws)
  print('distance',z,'cosines',cos,'positive minors',[(1-c*c) for c in cos[1:]])
  assert all(abs(c)<1 for c in cos[1:])
 print('EXACT CHECK PASSED')
if __name__=='__main__':
 check(5,2,[3,1,-2]);check(7,3,[4,2,-1,-3])
