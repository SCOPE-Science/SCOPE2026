from itertools import product
from collections import defaultdict,Counter
LENS=range(1,8)

def local(l,p=0,c=0):return (l,c,p)
def nextv(v):
 l,c,p=v
 return(l,c,(p+1)%l)
def predv(v):
 l,c,p=v
 return(l,c,(p-1)%l)
def edge(a,b):return nextv(a)==b

def pair_type(counts,x,y):
 # atomic: equality and loops and directed pair edges
 a=(int(x==y),int(edge(x,x)),int(edge(y,y)),int(edge(x,y)),int(edge(y,x)))
 cand=set()
 for z in (nextv(x),predv(x),nextv(y),predv(y)):
  if z != x and z != y:cand.add(z)
 def pat(z):
  return (int(edge(x,z)) | (int(edge(z,x))<<1) | (int(edge(y,z))<<2) | (int(edge(z,y))<<3) | (int(edge(z,z))<<4))
 mask=0
 for z in cand:mask|=1<<pat(z)
 no_loop=sum(counts[l-1]*l for l in range(2,8))
 exclusions={x,y}|cand
 excl_nonloop=sum(v[0]>=2 for v in exclusions)
 if no_loop>excl_nonloop:mask |=1<<0
 no_fixed=counts[0]
 excl_fixed=sum(v[0]==1 for v in {x,y})
 if no_fixed>excl_fixed:mask |=1<<16
 return(a,mask)

def type3(counts):
 out=[]
 for l in LENS:
  if counts[l-1]==0:continue
  x=local(l)
  pairs={pair_type(counts,x,x)}
  for d in range(1,l):pairs.add(pair_type(counts,x,local(l,d)))
  for m in LENS:
   if counts[m-1] and (m!=l or counts[l-1]>=2):
    y=local(m,0,1 if m==l else 0)
    pairs.add(pair_type(counts,x,y))
  out.append(frozenset(pairs))
 return frozenset(out)


def direct(cycles):
 succ=[]
 for l in cycles:
  base=len(succ);succ.extend(base+(i+1)%l for i in range(l))
 N=len(succ)
 def ep(x,y):return succ[x]==y
 def sigpair(x,y):
  atom=(int(x==y),int(ep(x,x)),int(ep(y,y)),int(ep(x,y)),int(ep(y,x)))
  patterns=0
  for z in range(N):
   if z==x or z==y:continue
   pat=(int(ep(x,z))|(int(ep(z,x))<<1)|(int(ep(y,z))<<2)|(int(ep(z,y))<<3)|(int(ep(z,z))<<4))
   patterns |=1<<pat
  return atom,patterns
 return frozenset(frozenset(sigpair(x,y) for y in range(N)) for x in range(N))

def expand(counts):
 return [l for l,c in enumerate(counts,1) for _ in range(c)]



def census():
    from itertools import product
    import csv
    best={};all_short=set(); all_18=set(); classified=0; checked=0
    for counts in product(range(4),repeat=7):
        if not any(counts):continue
        classified+=1
        typ=type3(counts)
        n=sum((i+1)*x for i,x in enumerate(counts))
        if typ not in best or (n,counts)<best[typ]:best[typ]=(n,counts)
        if n<=19:
            all_short.add(typ)
            assert typ==direct(expand(counts)),counts
            checked+=1
        if n<=18:all_18.add(typ)
    assert classified==16383 and len(best)==143
    assert len(all_short)==143 and len(all_18)==142 and checked==731
    maximum=max(n for n,c in best.values())
    assert maximum==19
    champions=[c for n,c in best.values() if n==19]
    assert champions==[(3,2,1,1,1,0,0)],champions
    witnesses=sorted(best.values())
    with open('minimal_representatives.csv','w',newline='',encoding='utf-8') as f:
        w=csv.writer(f)
        w.writerow(['minimum_vertices','cycles_length_1','cycles_length_2','cycles_length_3','cycles_length_4','cycles_length_5','cycles_length_6','cycles_length_7'])
        for n,c in witnesses:w.writerow((n,)+c)
    print('Canonical vectors:',classified)
    print('Rank-three theory classes:',len(best))
    print('Representatives of order at most 19 checked independently:',checked)
    print('Distinct types on order at most 18:',len(all_18))
    print('Sharp maximum minimum-representative order:',maximum)
    print('Unique minimum representative of order 19, cycle counts 1..7:',champions[0])
    return best

def checks():
    from random import Random
    rng=Random(1729)
    samples=[(1,0,0,0,0,0,0),(0,1,0,0,0,0,0),(0,0,1,0,0,0,0),(0,0,0,1,0,0,0),(0,0,0,0,1,0,0),(0,0,0,0,0,1,0),(0,0,0,0,0,0,1),(3,2,1,1,1,0,0),(3,3,3,3,3,3,3)]
    for _ in range(500):
        counts=tuple(rng.randrange(4) for _ in range(7))
        if any(counts):samples.append(counts)
    for v in samples:assert direct(expand(v))==type3(v),v
    for n in (7,8,9,10,11,13,17,23,29):
        assert direct([n])==direct([7])
    for m in (3,4,5,7):assert direct([3]*m)==direct([3]*3)
    print('Direct independent spot checks:',len(samples))
    print('Long-cycle/copy truncation spot checks: passed')

if __name__=='__main__':
    census()
    checks()
