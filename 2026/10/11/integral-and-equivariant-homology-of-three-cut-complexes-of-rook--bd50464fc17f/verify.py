#!/usr/bin/env python3
"""Self-contained small-case tests of the ordinary three-cut complex of Cartesian products of cliques."""
from itertools import combinations, permutations, product
from math import comb

def signperm(a):
 return -1 if sum(a[i]>a[j] for i in range(len(a)) for j in range(i+1,len(a)))%2 else 1

def fixed_cycles(a):
 return sum(a[i]==i for i in range(len(a)))

def two_cycles(a):
 return sum(i<a[i] and a[a[i]]==i for i in range(len(a)))

def rank2(cols):
 pivots={}
 for v in cols:
  while v:
   p=v.bit_length()-1
   if p in pivots: v^=pivots[p]
   else: pivots[p]=v; break
 return len(pivots)

def calc(m,n,character=False):
 N=m*n
 v=tuple(product(range(m),range(n)))
 adjacency=lambda i,j: v[i][0]==v[j][0] or v[i][1]==v[j][1]
 connected_triples=[]
 for q in combinations(range(N),3):
  connected_triples.append((sum(adjacency(i,j) for i,j in combinations(q,2))>=2,q))
 good={}
 cut={}
 for mask in range(1<<N):
  # avoid circular reasoning: directly evaluate all disconnected vertex triples
  no_bad=True
  for connected,t in connected_triples:
   if not connected and all(mask>>x&1 for x in t):no_bad=False;break
  good[mask]=no_bad
 for mask in range(1<<N):
  complement=((1<<N)-1)^mask
  cut[mask]=not good[complement]
 maxima=[]
 for mask in good:
  if good[mask] and not any(good.get(mask|(1<<i),False) for i in range(N) if not mask>>i&1):maxima.append(mask)
 expected={sum(1<<(i*n+j) for j in range(n)) for i in range(m)}
 expected|={sum(1<<(i*n+j) for i in range(m)) for j in range(n)}
 expected|={sum(1<<(i*n+j) for i in ii for j in jj) for ii in combinations(range(m),2) for jj in combinations(range(n),2)}
 expected={x for x in expected if not any(x!=y and x&y==x for y in expected)}
 assert set(maxima)==expected,(m,n,'facets')
 b=comb(m,2)*comb(n,2)-(m-1)*(n-1)
 # direct rank of full chain complex over F2 for dual Gamma, independent of long exact sequence
 faces={d:[] for d in range(-1,N)}
 for mask in good:
  if not good[mask]:continue
  d=mask.bit_count()-1
  faces[d].append(mask)
 bd={}
 for d in range(0,N):
  if not faces[d]:continue
  cod={s:i for i,s in enumerate(faces[d-1])}
  cols=[]
  for s in faces[d]:
   p=0
   for i in range(N):
    if s>>i&1:p^=1<<cod[s^(1<<i)]
   cols.append(p)
  bd[d]=rank2(cols)
 bets={d:len(faces[d])-bd.get(d,0)-bd.get(d+1,0) for d in faces if faces[d]}
 assert all(q == (b if d==2 else 0) for d,q in bets.items()), (m,n,b,bets)
 print("BETTI_CHECK",m,n,b,"computed",bets)
 print('FACES_OK',m,n,'GammaF',[(d,len(faces[d])) for d in faces if faces[d]],'Betti',bets)
 if character:
  # independent direct signed Lefschetz on Alexander dual Delta3
  assert m*n<=12
  perms1=list(permutations(range(m)))
  perms2=list(permutations(range(n)))
  accepted=[mask for mask,is_face in cut.items() if is_face and mask]
  testcnt=0
  for a,c in product(perms1,perms2):
   mapping=[a[i]*n+c[j] for i,j in v]
   trace=0
   for mask in accepted:
    ids=[i for i in range(N) if mask>>i&1]
    ims=[mapping[i] for i in ids]
    if set(ids)!=set(ims):continue
    sortedims=sorted(ims)
    order=[sortedims.index(x) for x in ims]
    trace+=(-1 if len(ids)%2==0 else 1)*signperm(order)
   trace-=1  # reduced Euler-Lefschetz: subtract empty-face contribution
   predicted=(comb(fixed_cycles(a),2)-two_cycles(a))*(comb(fixed_cycles(c),2)-two_cycles(c))-(fixed_cycles(a)-1)*(fixed_cycles(c)-1)
   signv=signperm(a)**n*signperm(c)**m
   expectedtrace=(-1)**(N-5)*signv*predicted
   assert trace==expectedtrace,(m,n,a,c,trace,expectedtrace)
   testcnt+=1
  print('CHARACTER_OK',m,n,testcnt)
for p in [(2,3),(3,3),(3,4)]:calc(*p,character=True)
print('VERIFY_OK')
