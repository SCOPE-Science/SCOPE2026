"""Complementary robber-survival recursion on the symplectic generalized quadrangle."""
from itertools import combinations,combinations_with_replacement,product
from functools import reduce

def omega(x,y):
 x0=[x>>i&1 for i in range(4)];y0=[y>>i&1 for i in range(4)]
 return (x0[0]*y0[2]+x0[2]*y0[0]+x0[1]*y0[3]+x0[3]*y0[1])%2
L={frozenset({a,b,a^b}) for a in range(1,16) for b in range(a+1,16) if omega(a,b)==0}
L=sorted(L,key=lambda z:tuple(sorted(z)))
assert len(L)==15
adj=[set() for _ in range(30)]
for j,ss in enumerate(L):
 for a in ss:
  adj[a-1].add(j+15);adj[j+15].add(a-1)
N=[x|{i} for i,x in enumerate(adj)]
allmask=(1<<30)-1

def solve(k,rounds=3):
 states=list(combinations_with_replacement(range(30),k)); pos={s:i for i,s in enumerate(states)}
 moves=[[pos[tuple(sorted(z))] for z in set(product(*(N[a] for a in s)))] for s in states]
 occupied=[reduce(lambda m,a:m|(1<<a),s,0) for s in states]
 losing=[allmask^m for m in occupied]
 counts=[sum(m.bit_count() for m in losing)]
 won=[i for i,z in enumerate(losing) if z==0]
 for t in range(1,rounds+1):
  escape=[]
  for C in range(len(states)):
   q=allmask^occupied[C]
   for C2 in moves[C]:
    possible=0
    remaining=losing[C2]
    while remaining:
     low=remaining & -remaining
     rv=low.bit_length()-1
     for r in N[rv]:possible|=1<<r
     remaining-=low
    q &= possible & (allmask^occupied[C2])
    if not q:break
   escape.append(q)
  losing=escape
  counts.append(sum(m.bit_count() for m in losing))
  won=[i for i,z in enumerate(losing) if z==0]
 return counts,[states[i] for i in won]

if __name__=='__main__':
 for k in (1,2,3):
  counts,won=solve(k,3)
  assert counts=={1:[870,780,780,780],2:[13050,10530,10530,10530],3:[134850,98280,93720,73440]}[k]
  print('k',k,'losing-state-counts',counts,'unconditionally winning initial triples count',len(won))
  if k==3:
   import sys
   from itertools import combinations
   win=set(won)
   projective={tuple(sorted([a-1,b-1,(a^b)-1])) for a,b in combinations(range(1,16),2)}
   print('projective-2-subspaces',len(projective),'winning-point-subsets',len([x for x in won if x[2]<15]),'equal?',{x for x in win if x[2]<15}==projective)
   line_wins={x for x in win if x[0]>=15}
   print('line_wins',len(line_wins))
   ncon=nreg=0
   for ss in combinations(range(15,30),3):
    sets=[L[x-15] for x in ss]
    concurrent=len(set.intersection(*map(set,sets)))==1
    disjoint=all(not set(sets[i])&set(sets[j]) for i,j in ((0,1),(0,2),(1,2)))
    transversals=sum(all(set(L[y-15])&set(a) for a in sets) for y in range(15,30) if y not in ss)
    if ss in line_wins:
     assert concurrent or disjoint and transversals==3
     ncon+=int(concurrent);nreg+=int(disjoint)
    else: assert not concurrent and not (disjoint and transversals==3)
   print('concurrent',ncon,'reguli',nreg)

   import hashlib
   seq="\n".join(",".join(map(str,C)) for C in sorted(win))+"\n"
   assert hashlib.sha256(seq.encode()).hexdigest()=="422e6ea22043c57643838985dc011c76221708a837c123f32282bb65c4d9353d"
   print("VERIFY_OK")
