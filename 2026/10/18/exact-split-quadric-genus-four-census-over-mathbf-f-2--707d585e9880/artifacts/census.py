from pathlib import Path
ROOT = Path(__file__).resolve().parent
from collections import Counter,defaultdict
from itertools import product
from sieve import mul,IRR

def binary_poly_mul(p,q):
 z=0
 for i in range(4):
  if p>>i&1:
   for j in range(4):
    if q>>j&1:z^=1<<(i+j)
 return z

def linpow(a,b,n):
 P=1
 for i in range(n):
  P=binary_poly_mul(P,(a|(b<<1)))
 return P
# binary_poly_mul currently loops only i,j<4 but deg results for n<=3 okay

def trans(a,b,c,d):
 return [binary_poly_mul(linpow(a,b,3-i),linpow(c,d,i)) for i in range(4)]
G=[(a,b,c,d) for a,b,c,d in product((0,1),repeat=4) if (a*d+b*c)%2==1]
assert len(G)==6
Id=(1,0,0,1)
perms=[]
for U,V,sw in product(G,G,(False,True)):
 T=trans(*U);S=trans(*V)
 mapcol=[]
 for i in range(4):
  for j in range(4):
   v=0
   for k in range(4):
    if T[i]>>k&1:
     for l in range(4):
      if S[j]>>l&1:
       a,b=(l,k) if sw else (k,l)
       v^=1<<(4*a+b)
   mapcol.append(v)
 perms.append(mapcol)

def apply(m,col):
 z=0
 while m:
  bb=m&-m;z^=col[bb.bit_length()-1];m^=bb
 return z

pts=[(1,0),(0,1),(1,1)]
pointmask=[]
for X,Y in product(pts,pts):
 v=0
 for i in range(4):
  for j in range(4):
   v|=((X[0]**(3-i)*X[1]**i*Y[0]**(3-j)*Y[1]**j)&1)<<(4*i+j)
 pointmask.append(v)

def points(m):return sum((m&p).bit_count()%2==0 for p in pointmask)

smooth=[int(x) for x in open(ROOT / "sieve_survivors.txt")];st=set(smooth)
assert len(perms)==72 and len(set(tuple(c) for c in perms))==72
assert all(apply(m,p) in st for m in smooth for p in perms)
print('total smooth',len(smooth),'group',len(perms),'group preserves?',True)
print('rational hist',dict(sorted(Counter(map(points,smooth)).items())))
seen=set();orbitcnt=Counter();orbits=[];stab=Counter();
for m in smooth:
 if m in seen:continue
 orbit={apply(m,p) for p in perms}
 assert orbit<=st
 size=len(orbit)
 assert 72%size==0
 seen.update(orbit)
 x=points(m)
 orbitcnt[x]+=1;stab[72//size]+=1
 orbits.append((m, x,size,72//size))
print('orbits',len(orbits),'stabilizers',dict(sorted(stab.items())))
with open(ROOT / "orbit_representatives.tsv",'w') as f:
 f.write('\n'.join('\t'.join(map(str,row)) for row in orbits))
print('orbit count by rational points',dict(sorted(orbitcnt.items())))
assert len(seen)==len(smooth)

# incidence pattern of smooth curves as 3x3 grid (bitmask of rational points): more refined orbit type
pattern=Counter();pattern_orbit=Counter();strat=defaultdict(list)
for m in smooth:
 b=sum(((m&v).bit_count()%2==0)<<idx for idx,v in enumerate(pointmask))
 pattern[b]+=1
for m,r,size,h in orbits:
 b=sum(((m&v).bit_count()%2==0)<<idx for idx,v in enumerate(pointmask))
 pattern_orbit[b]+=1
# classify incidence sets via automorphism group induced action on 9 grid cells
pointindex={p:i for i,p in enumerate(pts)}
pointp=[]
for T in G:
 def app(x):
  a,b,c,d=T
  xx=((a*x[0]+b*x[1])%2,(c*x[0]+d*x[1])%2)
  return pointindex[xx]
 pointp.append(tuple(map(app,pts)))
patclass={};patweights=Counter();
for b in range(512):
 if b in patclass:continue
 orb=set()
 for PU,PV,sw in product(pointp,pointp,(False,True)):
  q=0
  for i in range(3):
   for j in range(3):
    if b>>(3*i+j)&1:
     v=(3*PV[j]+PU[i]) if sw else (3*PU[i]+PV[j])
     q|=1<<v
  orb.add(q)
 rep=min(orb)
 for q in orb:patclass[q]=rep
patcounts=Counter();
for b,n in pattern.items():patcounts[patclass[b]]+=n
print('incidence pattern orbit classes',len(patcounts));print('patterns',[(format(b,'09b'),b.bit_count(),n,len([q for q in range(512) if patclass[q]==b])) for b,n in sorted(patcounts.items(), key=lambda z:(z[0].bit_count(),z[0]))]);
with open(ROOT / "stats.txt",'w') as f:
 f.write('total_smooth='+str(len(smooth))+'\n');f.write('rational_hist='+str(dict(sorted(Counter(map(points,smooth)).items())))+'\n');f.write('orbit_hist='+str(dict(sorted(orbitcnt.items())))+'\n');f.write('stabilizers='+str(dict(sorted(stab.items())))+'\n');f.write('pattern_class='+str(dict(sorted(patcounts.items())))+'\n')
