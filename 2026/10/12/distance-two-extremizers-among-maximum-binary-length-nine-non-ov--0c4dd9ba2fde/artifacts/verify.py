from itertools import product,combinations
n=9
words=[''.join(p) for p in product('01', repeat=n)]
def bifix_free(w):
 return all(w[:k]!=w[n-k:] for k in range(1,n))
V=[w for w in words if bifix_free(w)]
idx={w:i for i,w in enumerate(V)}
N=len(V)
# compatibility: two words can coexist iff no proper prefix of either equals suffix of either, all cross directions.
def compat(a,b):
 for k in range(1,n):
  if a[:k]==b[n-k:] or b[:k]==a[n-k:]: return False
 return True
adj=[0]*N
for i in range(N):
 for j in range(i+1,N):
  if compat(V[i],V[j]):
   adj[i]|=1<<j;adj[j]|=1<<i
print('N',N,'edges',sum(x.bit_count() for x in adj)//2)
# enumerate maximum cliques using BronKerbosch with target 14 and canonical ordering straightforward DFS intersection increasing indices
T=14; sols=[];nodes=0
allmask=(1<<N)-1
# degeneracy? simple recursive with candidate mask upper bound

def dfs(chosen,cand,last):
 global nodes
 nodes+=1
 if len(chosen)==T:
  sols.append(tuple(chosen));return
 if len(chosen)+cand.bit_count()<T:return
 # choose vertices ascending; cand already > last
 while cand:
  if len(chosen)+cand.bit_count()<T:return
  b=cand&-cand; cand-=b; v=b.bit_length()-1
  dfs(chosen+[v], cand & adj[v], v)
# symmetry orientation: every nonoverlap binary code all words must same first bit? compatibility implies prefix1 cannot equal suffix1 among any words, so sets split first 0 last1 or first1 last0. enumerate all directly.
dfs([],allmask,-1)
print('sols',len(sols),'nodes',nodes)

def hd(a,b):return sum(x!=y for x,y in zip(a,b))
from collections import Counter
mind=Counter(); maxd=99; good=[]
for s in sols:
 ws=[V[i] for i in s]
 d=min(hd(a,b) for a,b in combinations(ws,2))
 mind[d]+=1
print('mindist dist',mind)
best=max(mind);good=[tuple(sorted(V[i] for i in s)) for s in sols if min(hd(V[i],V[j]) for i,j in combinations(s,2))==best]
print('best',best,'count',len(good))
def compc(c):return tuple(sorted(''.join('1' if x=='0' else '0' for x in w) for w in c))
def revc(c):return tuple(sorted(w[::-1] for w in c))
def cr(c):return compc(revc(c))
S=set(good);seen=set();orbs=[]
for c in S:
 if c in seen:continue
 o={c,compc(c),revc(c),cr(c)}
 assert o<=S
 seen|=o;orbs.append(o)
print('orbits',len(orbs),Counter(map(len,orbs)))
for f,name in [(compc,'comp'),(revc,'rev'),(cr,'cr')]:print(name,sum(f(c)==c for c in S))
for sz in sorted(set(map(len,orbs))):
 reps=sorted(min(o) for o in orbs if len(o)==sz)
 print('size',sz,'num',len(reps),'first',reps[0])
