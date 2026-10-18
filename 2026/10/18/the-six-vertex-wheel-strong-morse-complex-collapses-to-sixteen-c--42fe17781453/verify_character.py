"""Independent simplicial chain enumeration, mod-two homology, dihedral traces.

The chain character uses signed permutations of oriented simplices; the
resulting Lefschetz numbers recover the rational homology character.
"""
import itertools
from collections import defaultdict

rim = tuple(range(5))
V = tuple(range(6))
E = {frozenset((i,(i+1)%5)) for i in rim} | {frozenset((i,5)) for i in rim}
adj = {v:set() for v in V}
for edge in E:
 u,v=tuple(edge)
 adj[u].add(v);adj[v].add(u)

facets=[]
for order in itertools.permutations(V):
  prefix=[];f=[]
  for u in order:
    previous=[v for v in prefix if frozenset((u,v)) in E]
    if len(previous)==1:f.append((u,previous[0]))
    prefix.append(u)
  facets.append(tuple(f))
levels=defaultdict(set)
for f in facets:
 for size in range(0,len(f)+1):
  for sub in itertools.combinations(f,size):levels[size].add(tuple(sorted(sub)))
assert {k:len(v) for k,v in levels.items()} == {0:1,1:20,2:55,3:20}

def rank_mod_two(cols):
  pivots={};rank=0
  for val in cols:
    while val:
      k=val.bit_length()-1
      if k not in pivots:
        pivots[k]=val;rank+=1;break
      val ^= pivots[k]
  return rank

ranks={}
for k in (1,2,3):
  prev={face:i for i,face in enumerate(sorted(levels[k-1]))}
  cols=[]
  for face in sorted(levels[k]):
    bitset=0
    for i in range(k):
      boundary=face[:i]+face[i+1:]
      bitset ^= (1<<prev[boundary])
    cols.append(bitset)
  ranks[k]=rank_mod_two(cols)
assert ranks=={1:1,2:19,3:20},ranks
assert {k-1:len(levels[k])-ranks.get(k,0)-ranks.get(k+1,0) for k in (1,2,3)}=={0:0,1:16,2:0}

def permutation_sign(ordered, mapped):
 positions = {z:i for i,z in enumerate(ordered)}
 indices=[positions[x] for x in mapped]
 return -1 if sum(indices[i]>indices[j] for i in range(len(indices)) for j in range(i+1,len(indices)))%2 else 1

values={}
for reflected in (0,1):
  for shift in rim:
    def perm(x):return 5 if x==5 else (shift-x if reflected else shift+x)%5
    chain=[]
    for k in (1,2,3):
      val=0
      for ordered in levels[k]:
        mapped=tuple((perm(u),perm(v)) for u,v in ordered)
        if set(mapped)==set(ordered):
          val += permutation_sign(ordered,mapped)
      chain.append(val)
    lefschetz=chain[0]-chain[1]+chain[2]
    trace_h1=1-lefschetz
    values[(reflected,shift)]=(tuple(chain),trace_h1)
assert values[(0,0)] == ((20,55,20),16)
assert all(values[(0,j)]==((0,0,0),1) for j in range(1,5))
assert all(values[(1,j)]==((2,-3,0),-4) for j in rim)
print('independent enumerator: simplices including empty = 96')
print('mod-two simplicial boundary ranks:',ranks)
print('reduced mod-two Betti numbers (0,1,2): (0,16,0)')
print('D5 rational H1 traces: identity 16, four nonidentity rotations 1, five reflections -4')
print('D5 rational module: 4 copies reflection sign plus 3 copies rational standard 4-dimensional module')
print('full D5-fixed H1 dimension: 0')
