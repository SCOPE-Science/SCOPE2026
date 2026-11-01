"""Independent finite rank-three first-order type recursion.

Types are built bottom-up from atomic diagrams rather than pair masks.
Run: python3 verify_ef3.py
"""
from itertools import combinations

def flags(blocks):
 V=[(p,i) for i,B in enumerate(blocks) for p in B]
 A=[[i!=j and (x[0]==y[0] or x[1]==y[1]) for j,y in enumerate(V)] for i,x in enumerate(V)]
 return A

def pair_blocks(n):return list(combinations(range(n),2))

def fano_blocks():return sorted({tuple(sorted([a,b,a^b])) for a in range(1,8) for b in range(a+1,8)})

def affine3():
 return [tuple((x,(a*x+b)%3) for x in range(3)) for a in range(3) for b in range(3)]+[tuple((x,y) for y in range(3)) for x in range(3)]

def johnson73():
 V=list(combinations(range(7),3))
 return [[i!=j and len(set(s)&set(t))==2 for j,t in enumerate(V)] for i,s in enumerate(V)]

def atomic(A,t):
 return (tuple(t[i]==t[j] for i in range(len(t)) for j in range(i+1,len(t))), tuple(A[t[i]][t[j]] for i in range(len(t)) for j in range(i+1,len(t))))

def rank3(A):
 n=len(A)
 # quantifier rank 0: atomic diagrams of triples; depth 1: pairs;
 # depth 2: singletons; depth 3: empty tuple.
 rank1=[[frozenset(atomic(A,(u,v,w)) for w in range(n)) for v in range(n)] for u in range(n)]
 rank2=[frozenset(rank1[u]) for u in range(n)]
 return frozenset(rank2)

entries={
 'pair-v3':flags(pair_blocks(3)),
 'pair-v4':flags(pair_blocks(4)),
 'pair-v6':flags(pair_blocks(6)),
 'Fano':flags(fano_blocks()),
 'affine3':flags(affine3()),
 'Johnson73':johnson73(),
}
types={k:rank3(A) for k,A in entries.items()}
assert types['pair-v3']!=types['pair-v4']
assert types['pair-v4']==types['pair-v6']
assert types['pair-v4']!=types['Fano']
assert types['pair-v3']!=types['Fano']
assert types['Fano']==types['affine3']==types['Johnson73']
for k,A in entries.items():print(k,len(A),'depth3-type-count',len(types[k]))
print('INDEPENDENT_EF3_PASS')
