from itertools import combinations

def cyc(n,i,j):
 a=abs(i-j)%n
 return min(a,n-a)

def dist(n,p,q): return cyc(n,p[0],q[0])+cyc(n,p[1],q[1])

def orbit(n,x):
 y=(x[1],x[0]);return frozenset((x,y))

def check(n,r=2):
 oo={orbit(n,(i,j)) for i in range(n) for j in range(n)}
 valid=[q for q in oo if len(q)==1 or dist(n,*tuple(q))<=r]
 def lab(q):
  x=next(iter(q))
  if len(q)==1:return 'D',x[0]
  if cyc(n,x[0],x[1])==1:
   for i in range(n):
    if q==frozenset(((i,i+1 if i+1<n else 0),(i+1 if i+1<n else 0,i))):return 'E',i
  return ('BAD',tuple(q))
 mapping={lab(q):q for q in valid}
 if r==2: assert len(mapping)==2*n and all(k[0] in ('D','E') for k in mapping)
 else: assert len(mapping)==n and all(k[0]=='D' for k in mapping)
 def ok(A,B):return all(dist(n,x,y)<=r for x in A for y in B)
 edges={frozenset((a,b)) for a,b in combinations(mapping,2) if ok(mapping[a],mapping[b])}
 triangles={frozenset(t) for t in combinations(mapping,3) if all(frozenset(p) in edges for p in combinations(t,2))}
 quadruples={frozenset(t) for t in combinations(mapping,4) if all(frozenset(p) in edges for p in combinations(t,2))}
 if r==2:
  want_edges=set()
  want_tris=set()
  for i in range(n):
   j=(i+1)%n; prev=(i-1)%n
   want_edges|={frozenset((('D',i),('D',j))),frozenset((('E',i),('E',j))),frozenset((('D',i),('E',i))),frozenset((('D',i),('E',prev)))}
   want_tris|={frozenset((('D',i),('D',j),('E',i))),frozenset((('D',i),('E',prev),('E',i)))}
  assert edges==want_edges,(n,'edges',edges^want_edges)
  assert triangles==want_tris,(n,'tris',triangles^want_tris)
  assert not quadruples,(n,'4-cliques',quadruples)
 else: assert not edges and not triangles
 return n,r,len(mapping),len(edges),len(triangles),len(quadruples)
if __name__=='__main__':
 for n in range(7,26):
  for r in (1,2):print(check(n,r))
