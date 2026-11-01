"""Exact exhaustive volume census for vertex-induced regular icosahedral subpolytopes.
Pure Python, no third-party packages. Run: python icosa_exact.py.
"""
from itertools import combinations
from math import comb
from collections import defaultdict,Counter
from functools import cmp_to_key
import json
from pathlib import Path
P=(0,1);Z=(0,0)
def add(x,y):return (x[0]+y[0],x[1]+y[1])
def sub(x,y):return (x[0]-y[0],x[1]-y[1])
def mul(x,y):return (x[0]*y[0]+x[1]*y[1], x[0]*y[1]+x[1]*y[0]+x[1]*y[1])
def sgn(x):
 a,b=x
 if b==0: return (a>0)-(a<0)
 if a==0: return (b>0)-(b<0)
 if a>0 and b>0:return 1
 if a<0 and b<0:return -1
 t=a*a+a*b-b*b
 if a<0 and b>0:return -(t>0)+(t<0)
 return (t>0)-(t<0)
def vf(x):return x[0]+x[1]*(1+5**0.5)/2
def vecsub(u,v):return tuple(sub(u[i],v[i]) for i in range(3))
def dot(u,v):
 z=Z
 for i in range(3):z=add(z,mul(u[i],v[i]))
 return z
def cross(u,v):return tuple(sub(mul(u[(i+1)%3],v[(i+2)%3]),mul(u[(i+2)%3],v[(i+1)%3])) for i in range(3))
def det(u,v,w):return dot(u,cross(v,w))
def vertex(x):return tuple((int(y),0) if y not in ['p','-p'] else (0,1 if y=='p' else -1) for y in x)
V=[]
for s in [-1,1]:
 for t in [-1,1]:V.append(vertex(['0',str(s),'p' if t==1 else '-p']))
for s in [-1,1]:
 for t in [-1,1]:V.append(vertex([str(s),'p' if t==1 else '-p','0']))
for s in [-1,1]:
 for t in [-1,1]:V.append(vertex(['p' if s==1 else '-p','0',str(t)]))
F=[[vf(z) for z in v] for v in V]

def volume_6(mask):
 ids=[i for i in range(12) if mask&(1<<i)]
 if len(ids)<4:return Z
 p0=V[ids[0]]
 if not any(sgn(det(vecsub(V[i],p0),vecsub(V[j],p0),vecsub(V[k],p0))) for i,j,k in combinations(ids[1:],3)):
  return Z
 facets=set()
 for i,j,k in combinations(ids,3):
  n=cross(vecsub(V[j],V[i]),vecsub(V[k],V[i]))
  if n==(Z,Z,Z):continue
  signs=[sgn(dot(n,vecsub(V[l],V[i]))) for l in ids]
  if max(signs)>0 and min(signs)<0:continue
  facets.add(frozenset(l for l,s in zip(ids,signs) if s==0))
 total=Z
 for facet in facets:
  ff=list(sorted(facet))
  i,j,k=ff[:3]
  n=cross(vecsub(V[j],V[i]),vecsub(V[k],V[i]))
  if n==(Z,Z,Z):raise AssertionError('collinear facet')
  for l in ids:
   ss=sgn(dot(n,vecsub(V[l],V[i])))
   if ss:
    if ss>0:n=tuple((-a,-b) for a,b in n)
    break
  # Exact angular order about the arithmetic mean of face vertices, an interior point.
  m=len(ff)
  sumf=tuple((sum(V[q][d][0] for q in ff),sum(V[q][d][1] for q in ff)) for d in range(3))
  w={q:tuple(sub((m*V[q][d][0],m*V[q][d][1]),sumf[d]) for d in range(3)) for q in ff}
  pivot=w[ff[0]]
  def orient(q,r):return sgn(dot(n,cross(w[q],w[r])))
  def half(q):
   o=sgn(dot(n,cross(pivot,w[q])))
   if o>0:return 0
   if o<0:return 1
   return 0 if sgn(dot(pivot,w[q]))>0 else 1
  def cmp(q,r):
   if q==r:return 0
   hq,hr=half(q),half(r)
   if hq!=hr:return -1 if hq<hr else 1
   o=orient(q,r)
   if not o:raise AssertionError('coinciding rays')
   return -o
  ordered=sorted(ff,key=cmp_to_key(cmp))
  # Independent exact convexity and orientation check of every sorted polygon turn.
  for t in range(len(ordered)):
   a,b,c=(ordered[(t+j)%len(ordered)] for j in range(3))
   assert sgn(dot(n,cross(vecsub(V[b],V[a]),vecsub(V[c],V[b]))))>0,(mask,facet,ordered)
  for t in range(1,len(ordered)-1):
   a,b,c=ordered[0],ordered[t],ordered[t+1]
   tri=det(V[a],V[b],V[c])
   total=add(total,tri)
 return total

def run():
 tab=defaultdict(Counter);counts=Counter();total6={}
 for mask in range(1<<12):
  k=mask.bit_count();v=volume_6(mask)
  assert v[0]==0 and v[1]==0 or sgn(v)>=0
  counts[(k,v)]+=1;tab[k][v]+=1
 sums={k:(sum(v[0]*cnt for v,cnt in d.items()),sum(v[1]*cnt for v,cnt in d.items())) for k,d in tab.items()}
 assert sum(sum(d.values()) for d in tab.values())==4096
 assert all(sum(tab[k].values())==comb(12,k) for k in range(13))
 assert len(set(v for k,v in counts))==29
 assert all(v==Z for k in range(4) for v in tab[k])
 assert tab[4][Z]==75 and tab[5][Z]==12
 assert all(v!=Z for k in range(6,13) for v in tab[k])
 assert tab[12]==Counter({(40,40):1})
 # Coplanar configurations have two explicit geometric sources.
 zero4={frozenset(i for i in range(12) if mask>>i&1) for mask in range(1<<12)
        if mask.bit_count()==4 and volume_6(mask)==Z}
 zero5={frozenset(i for i in range(12) if mask>>i&1) for mask in range(1<<12)
        if mask.bit_count()==5 and volume_6(mask)==Z}
 adjacent={i:frozenset(j for j in range(12) if j!=i and dot(vecsub(V[j],V[i]),vecsub(V[j],V[i]))==(4,0)) for i in range(12)}
 assert all(len(q)==5 for q in adjacent.values())
 assert zero5==set(adjacent.values()) and len(zero5)==12
 opposite=[frozenset((i,j)) for i in range(12) for j in range(i+1,12)
           if all(add(V[i][d],V[j][d])==Z for d in range(3))]
 assert len(opposite)==6
 antipodal_planes={a|b for a,b in combinations(opposite,2)}
 ring_quads={frozenset(c) for ring in adjacent.values() for c in combinations(sorted(ring),4)}
 assert len(antipodal_planes)==15 and len(ring_quads)==60
 assert not (antipodal_planes & ring_quads)
 assert zero4==antipodal_planes|ring_quads and len(zero4)==75
 assert all(a%4==0 and b%4==0 and a>=0 and b>=0 for d in tab.values() for a,b in d)
 print('sum of volumes in six-times units (a+b phi):',sums)
 print('distinct volume levels:',len(set(v for k,v in counts)))
 for k in sorted(tab):
  print(k, sorted([(v[0],v[1],cnt) for v,cnt in tab[k].items()],key=cmp_to_key(lambda x,y:sgn(sub((x[0],x[1]),(y[0],y[1]))))))
 out={'coordinates':[ [list(z) for z in p] for p in V],
      'volume_spectrum':{str(k): [[a,b,c] for (a,b),c in sorted(tab[k].items(),key=cmp_to_key(lambda x,y:sgn(sub(x[0],y[0]))))] for k in tab},
      'sum_6vol':{str(k):list(v) for k,v in sums.items()}}
 target=Path(__file__).with_name('volume_spectrum.json')
 if target.exists():
  with target.open(encoding='utf-8') as f: expected=json.load(f)
  assert out==expected, 'Volume spectrum mismatch'
 else:
  print('No reference spectrum was supplied; exact census completed without table comparison.')
 print('ALL_EXACT_4096_SUBPOLYTOPE_CHECKS_PASSED')
 return out
if __name__=='__main__':run()
