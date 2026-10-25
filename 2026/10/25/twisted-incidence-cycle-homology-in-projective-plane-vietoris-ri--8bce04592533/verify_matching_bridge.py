#!/usr/bin/env python3
"""Independent character comparison of Fano scale-two Rips and Heawood matching homology.

Builds the 336 graph symmetries, all flag-matchings, all finite-chain
boundary ranks, all eight order-seven subgroups and their conjugation action.
No nonstandard libraries or external data are used.
"""
from itertools import product
from collections import Counter

points=range(1,8)
flags=[(p-1,l+6) for p in points for l in points if ((p&l).bit_count()%2)==0]
assert len(flags)==21
edges_index={frozenset(e):i for i,e in enumerate(flags)}

G0=[]
for a,b,c in product(points,repeat=3):
 def apply(x):return (a if x&1 else 0)^(b if x&2 else 0)^(c if x&4 else 0)
 if len({apply(x) for x in points})!=7:continue
 lines=[]
 for n in points:
  cand=[v for v in points if all((v&apply(x)).bit_count()%2 == (n&x).bit_count()%2 for x in points)]
  assert len(cand)==1
  lines.append(cand[0]+6)
 G0.append(tuple([apply(x)-1 for x in points]+lines))
assert len(G0)==168
j=tuple([i+7 if i<7 else i-7 for i in range(14)])
G=G0+[tuple(j[h[i]] for i in range(14)) for h in G0]
assert len(set(G))==336
ident=tuple(range(14))

def compose(g,h):return tuple(g[h[i]] for i in range(14))
def inv(g):
 res=[0]*14
 for i,v in enumerate(g):res[v]=i
 return tuple(res)
def power(g,k):
 p=ident
 for _ in range(k):p=compose(g,p)
 return p

def order(g):
 for n in range(1,15):
  if power(g,n)==ident:return n
 raise AssertionError

subgroups=set()
for g in G0:
 if order(g)==7:
  subgroups.add(frozenset(power(g,k) for k in range(7)))
assert len(subgroups)==8

# Exhaust every simplex of the ordinary matching complex.
matchings=[0]
for edge_num,(u,v) in enumerate(flags):
 for m in tuple(matchings):
  if any(((m>>e)&1) and ({u,v}&set(flags[e])) for e in range(edge_num)):
   continue
  matchings.append(m|(1<<edge_num))
assert len(set(matchings))==len(matchings)==3462
nonempty=[m for m in matchings if m]
bydim={}
for m in nonempty:bydim.setdefault(m.bit_count()-1,[]).append(m)
assert [len(bydim[i]) for i in range(7)]==[21,168,644,1218,1050,336,24]

def rank2(columns):
 basis={}
 for col in columns:
  while col:
   bit=col.bit_length()-1
   if bit in basis:col^=basis[bit]
   else:
    basis[bit]=col
    break
 return len(basis)

boundary_ranks=[]
for k in range(1,7):
 row={m:i for i,m in enumerate(bydim[k-1])}
 columns=[]
 for m in bydim[k]:
  c=0
  for i in range(21):
   if (m>>i)&1:c^=1<<row[m^(1<<i)]
  columns.append(c)
 boundary_ranks.append(rank2(columns))
assert boundary_ranks==[20,148,496,722,312,24]
# These ranks saturate the rational upper bounds by the chain-complex
# dimension inequalities. Hence reduced rational homology is Q^16 in degree 4.


def Lef_matching(g):
 perm=[edges_index[frozenset((g[u],g[v]))] for u,v in flags]
 total=-1  # reduced: subtract ordinary H0 contribution
 for m in nonempty:
  im=0
  vv=[i for i in range(21) if (m>>i)&1]
  for i in vv:im|=1<<perm[i]
  if im!=m:continue
  flips=sum(perm[vv[i]]>perm[vv[t]] for i in range(len(vv)) for t in range(i+1,len(vv)))
  total+=(-1)**(len(vv)-1+flips)
 return total


def Wtrace(g):
 inverse=inv(g)
 fixed=0
 for subgroup in subgroups:
  image=frozenset(compose(compose(g,h),inverse) for h in subgroup)
  assert image in subgroups
  if image==subgroup:fixed+=1
 # Matching H4 = trivial + (reduced eight-Sylow permutation T) + W,
 # so W character = matching_H4 - 1 - (fixed-1).
 return Lef_matching(g)-fixed

def ripsH2trace(g):
 fixedflags=0
 for u,v in flags:
  if {g[u],g[v]}=={u,v}:fixedflags+=1
 preserves=g[0]<7
 if preserves:
  return fixedflags - sum(g[i]==i for i in range(14))+1
 return fixedflags-1

char_counts=Counter()
for g in G:
 a,b=Wtrace(g),ripsH2trace(g)
 assert a==b,(a,b,g)
 char_counts[a]+=1
assert char_counts==Counter({0:147,-1:112,1:48,2:28,8:1})
print('HEAWOOD_RIPS_MATCHING_CHARACTER_BRIDGE_OK',len(nonempty),len(G),len(subgroups),boundary_ranks)
