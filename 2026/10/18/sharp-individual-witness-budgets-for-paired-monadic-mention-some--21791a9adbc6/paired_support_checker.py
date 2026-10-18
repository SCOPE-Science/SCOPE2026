from itertools import combinations
from math import comb

def down_from(T,n):
 return frozenset(s for s in range(1<<n) if any(s&t==s for t in T))
def maxfac(K):
 return frozenset(a for a in K if not any(a!=b and a&b==a for b in K))
def pair(T,n):
 M=(1<<n)-1
 return (down_from(T,n),down_from([M^t for t in T],n))

def inspect(n):
 worlds=1<<n
 seq={}
 for b in range(1,1<<worlds):
  T=frozenset(i for i in range(worlds) if b>>i&1)
  q=pair(T,n)
  v=len(T)
  if q not in seq or len(seq[q])>v:seq[q]=T
 assert seq
 distribution={}
 for (K,L),T in seq.items():
  F=maxfac(K); G=maxfac(L); H=frozenset(((1<<n)-1)^b for b in G)
  assert len(T)==len(F|H),(n,K,L,T,F,H)
  assert all(any(h&a==h for h in H) for a in F)
  assert all(any(h&a==h for a in F) for h in H)
  distribution[len(T)]=distribution.get(len(T),0)+1
 M=max(map(len,seq.values()))
 expected=sorted((comb(n,k) for k in range(n+1)), reverse=True)
 bound=sum(expected[:2])
 assert M==bound,(n,M,bound)
 print(f'worlds={n}, joint_semantic_pairs={len(seq)}, witness_min_distribution={sorted(distribution.items())}, max_min_witnesses={M}, 2Sperner_bound={bound}')
for n in (1,2,3,4):inspect(n)
print('PAIR_CLASSIFICATION_CHECK_OK')
