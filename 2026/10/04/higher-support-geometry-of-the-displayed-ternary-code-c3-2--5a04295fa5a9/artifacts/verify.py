#!/usr/bin/env python3
import itertools,collections,math,json
from pathlib import Path
C=json.loads((Path(__file__).resolve().parent/"certificate.json").read_text())
G=[[1,0,0,0,2,1,1,2,0,1,0,0,1,2,1,0,1,1,1,0,0,2,2],[0,1,0,0,2,2,2,1,2,0,0,2,1,1,1,1,1,0,0,2,0,1,1],[0,0,1,0,2,1,0,1,2,1,1,2,0,2,2,2,0,1,0,0,2,0,2],[0,0,0,1,0,2,0,2,1,1,1,2,2,2,0,1,1,0,1,2,1,0,2],[0,0,0,0,1,1,1,1,0,2,1,1,2,0,0,1,0,1,1,1,2,2,2]]
def rank(A):
 A=[r[:] for r in A];rr=0
 for c in range(len(A[0])):
  p=next((i for i in range(rr,len(A)) if A[i][c]%3),None)
  if p is None:continue
  A[rr],A[p]=A[p],A[rr];iv=pow(A[rr][c]%3,-1,3);A[rr]=[iv*x%3 for x in A[rr]]
  for i in range(len(A)):
   if i!=rr and A[i][c]%3:
    f=A[i][c]%3;A[i]=[(A[i][j]-f*A[rr][j])%3 for j in range(len(A[0]))]
  rr+=1
 return rr
assert rank(G)==5
gram=[[sum(G[i][c]*G[j][c] for c in range(23))%3 for j in range(5)] for i in range(5)]
assert rank(gram)==5
W=collections.Counter()
for a in itertools.product(range(3),repeat=5):
 w=[sum(a[i]*G[i][j] for i in range(5))%3 for j in range(23)];W[sum(x!=0 for x in w)]+=1
assert {str(k):v for k,v in sorted(W.items())}==C["ordinary_weight_distribution"]
def subs(d):
 for piv in itertools.combinations(range(5),d):
  P=set(piv);free=[(i,c) for i,p in enumerate(piv) for c in range(p+1,5) if c not in P]
  for vals in itertools.product(range(3),repeat=len(free)):
   B=[[0]*5 for _ in range(d)]
   for i,p in enumerate(piv):B[i][p]=1
   for (i,c),v in zip(free,vals):B[i][c]=v
   yield B
S={};H=[]
for d in range(1,6):
 ctr=collections.Counter()
 for B in subs(d):
  s=sum(any(sum(B[r][i]*G[i][j] for i in range(5))%3 for r in range(d)) for j in range(23));ctr[s]+=1
 S[str(d)]={str(k):v for k,v in sorted(ctr.items())};H.append(min(ctr))
assert H==C["generalized_hamming_weights"] and S==C["support_spectra"]
def canon(v):
 for x in v:
  if x:return tuple(pow(x,-1,3)*y%3 for y in v)
pc=collections.defaultdict(list)
for j in range(23):pc[canon(tuple(G[i][j] for i in range(5)))].append(j+1)
assert len(pc)==22 and [(c,p) for c,p in pc.items() if len(p)>1]==[((1,2,0,0,1),[7,22])]
A=[W.get(i,0) for i in range(24)]
def K(j,i):return sum((-1)**s*2**(j-s)*math.comb(i,s)*math.comb(23-i,j-s) for s in range(max(0,j-(23-i)),min(j,i)+1))
D=[sum(A[i]*K(j,i) for i in range(24))//243 for j in range(6)]
assert D==C["dual"]["first_coefficients"]==[1,0,2,22,650,4574]
print("VERIFY_OK")
