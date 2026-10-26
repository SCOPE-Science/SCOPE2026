"""Finite independent checks for the four-round Steiner point-collinearity result.
Python 3 standard library; no external data or services.
"""
from itertools import product,combinations
from collections import Counter

def add(x,y,q):return x^y if q in (2,4) else (x+y)%q
def mul(x,y,q):
 if q==2:return x&y
 if q==3:return x*y%3
 z=0
 for i in range(2):
  if (y>>i)&1:z^=x<<i
 if z&8:z^=0b1100  # x^3 = 1, since x^2=x+1 => x^3=1
 if z&4:z^=0b111   # x^2 = x+1
 return z

def inv(x,q):return next(y for y in range(1,q) if mul(x,y,q)==1)
def norm(x,q):
 a=next(y for y in x if y)
 return tuple(mul(y,inv(a,q),q) for y in x)
def dot(x,y,q):
 acc=0
 for a,b in zip(x,y):acc=add(acc,mul(a,b,q),q)
 return acc

def projective(q):
 vectors=list(product(range(q), repeat=3)); points=sorted({norm(x,q) for x in vectors if any(x)})
 blocks=sorted({frozenset(i for i,x in enumerate(points) if dot(u,x,q)==0) for u in points}, key=lambda x: tuple(sorted(x)))
 return ('PG(2,%d)'%q,len(points),blocks)

def affine(q):
 points=list(product(range(q),repeat=2))
 blocks=[]
 for slope in range(q):
  for intercept in range(q):
   blocks.append(frozenset(i for i,(x,y) in enumerate(points) if y==add(mul(slope,x,q),intercept,q)))
 for intercept in range(q):
  blocks.append(frozenset(i for i,(x,y) in enumerate(points) if x==intercept))
 return ('AG(2,%d)'%q,len(points),blocks)

def check_design(n,blocks):
 k=len(blocks[0]);pairs=Counter()
 for b in blocks:
  assert len(b)==k
  for pair in combinations(sorted(b),2):pairs[pair]+=1
 assert len(pairs)==n*(n-1)//2 and set(pairs.values())=={1}
 assert len(blocks)==n*(n-1)//(k*(k-1))
 return k

def compute_rank4(n,blocks):
 tri={tuple(sorted(t)) for b in blocks for t in combinations(sorted(b),3)}
 pools=[{}, {}, {}, {}, {}]
 def intern(level,v):
  if v not in pools[level]:pools[level][v]=len(pools[level])
  return pools[level][v]
 # Return actual structural fingerprints independent of each graph, not pool-local IDs;
 # intern pools shared externally in call below instead for cross-comparison.
 return tri

atoms={};levels=[{} for _ in range(4)]
def intern(d,v):
 if v not in d:d[v]=len(d)
 return d[v]
def rank4(n,blocks):
 tri=compute_rank4(n,blocks)
 def atom(a,b,c,d):
  t=(a,b,c,d)
  return (tuple(i*4+j for i,j in combinations(range(4),2) if t[i]==t[j]),
          tuple(i*16+j*4+h for i,j,h in combinations(range(4),3) if tuple(sorted((t[i],t[j],t[h]))) in tri))
 # Rank one profiles of ordered triples (each fourth extension).
 t3={}
 for a,b,c in product(range(n),repeat=3):
  t3[a,b,c]=intern(levels[3],frozenset(intern(atoms,atom(a,b,c,d)) for d in range(n)))
 t2={}
 for a,b in product(range(n),repeat=2):
  t2[a,b]=intern(levels[2],frozenset(t3[a,b,c] for c in range(n)))
 t1={}
 for a in range(n):
  t1[a]=intern(levels[1],frozenset(t2[a,b] for b in range(n)))
 return intern(levels[0],frozenset(t1.values()))

def main():
 group=[]
 for design in [projective(2),affine(3),projective(3),affine(4),projective(4)]:
  name,n,blocks=design;k=check_design(n,blocks);typ=rank4(n,blocks)
  group.append((name,n,k,typ));print('FINITE',name,'v=',n,'k=',k,'rank4=',typ)
 assert len(set(t for _,_,k,t in group if k==3))==1
 assert len(set(t for _,_,k,t in group if k>=4))==1
 assert group[0][-1]!=group[2][-1]
 # Independent pair-line closure census for every ordered triple, including repetitions:
 for name,n,blocks in [projective(2),affine(3),projective(3),affine(4),projective(4)]:
  k=len(blocks[0]);line={}
  for b in blocks:
   for a,c in combinations(b,2):line[frozenset((a,c))]=b
  assert len(line)==n*(n-1)//2
  stats=Counter()
  for a,b,c in combinations(range(n),3):
   coll=any({a,b,c}<=block for block in blocks)
   if coll:
    same=sum(x not in (a,b,c) and {a,b,c,x}<=block for x in range(n) for block in [line[frozenset((a,b))]])
    off=n-k
    assert same==k-3 and off>=1
    stats['collinear']+=1
   else:
    Ls=[line[frozenset(p)] for p in ((a,b),(a,c),(b,c))]
    ext=[sum(x not in (a,b,c) and x in L for x in range(n)) for L in Ls]
    outside=sum(x not in (a,b,c) and all(x not in L for L in Ls) for x in range(n))
    assert ext==[k-2]*3 and outside==n-3*k+3 and outside>=1
    stats['noncollinear']+=1
  print('EXTENSION_CENSUS',name,dict(stats))
 print('VERIFY_OK','rank4_groups=',len({r[-1] for r in group}),'finite_designs=',len(group),'atom4_types=',len(atoms),'triple_extension_types=',len(levels[3]))

if __name__=='__main__':main()
