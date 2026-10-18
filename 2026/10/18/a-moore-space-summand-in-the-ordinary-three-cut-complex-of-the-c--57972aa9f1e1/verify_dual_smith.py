from itertools import combinations
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
n=16; gens={1,2,4,8,15}
def edge(a,b):return (a,b) if a<b else (b,a)
def aj(a,b):return a^b in gens
tr=[t for t in combinations(range(n),3) if sum(aj(a,b) for a,b in combinations(t,2))>=2]
assert len(tr)==160
edges=[e for e in combinations(range(n),2) if e[0]!=0]
assert len(edges)==105
idx={e:i for i,e in enumerate(edges)}
A=sp.zeros(105,160)
for j,(a,b,c) in enumerate(tr):
 for ee,co in [(edge(b,c),1),(edge(a,c),-1),(edge(a,b),1)]:
  if ee in idx:A[idx[ee],j]=co if ee[0] < ee[1] else -co
print('MATRIX',A.shape,flush=True)
S=smith_normal_form(A,domain=ZZ)
d=[abs(int(S[i,i])) for i in range(min(S.rows,S.cols)) if S[i,i]!=0]
from collections import Counter
print('SMITH_DIAGONAL',Counter(d),'RANK',len(d),'TORSION',d[-1],flush=True)
assert Counter(d)==Counter({1:104,2:1})
print('INDEPENDENT_VERIFY_OK')
