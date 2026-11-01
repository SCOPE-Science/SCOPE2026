"""Separate exact mod-two boundary rank calculation for Pappus matching complex; Python standard library only."""
import collections
N=18
J=(5,7,-7,7,-7,-5)*3
edges=sorted({tuple(sorted((i,(i+1)%N))) for i in range(N)} | {tuple(sorted((i,(i+J[i])%N))) for i in range(N)})
assert len(edges)==27
ev=[(1<<u)|(1<<v) for u,v in edges]
face=[[] for _ in range(10)]
def enumer(i,used,M,k):
 if i==27:face[k].append(M);return
 enumer(i+1,used,M,k)
 if used & ev[i]==0:enumer(i+1,used|ev[i],M|1<<i,k+1)
enumer(0,0,0,0)
assert [len(s) for s in face]==[1,27,297,1719,5643,10557,10737,5319,1026,42]
ranks=[0]*10
for k in range(1,10):
 base={m:j for j,m in enumerate(face[k-1])};piv={}
 for M in face[k]:
  x=0
  for i in range(27):
   if M>>i &1:
    x^=1<<base[M^(1<<i)]
  while x:
   a=x.bit_length()-1
   if a in piv:x^=piv[a]
   else:piv[a]=x;break
 ranks[k]=len(piv)
 print('k',k,'columns',len(face[k]),'rank',ranks[k],flush=True)
assert all(len(face[k])-ranks[k]-(ranks[k+1] if k<9 else 0)==(40 if k==6 else 0) for k in range(1,10))
print('ranks',ranks,'reducedBetti',[len(face[k])-ranks[k]-(ranks[k+1] if k<9 else 0) for k in range(1,10)])
print('HOMOLOGY_MOD2_OK')
