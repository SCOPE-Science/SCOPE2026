"""Independent finite-extension singularity and pencil check for cubic curves over F3."""
import json,itertools
from pathlib import Path
# 6-coefficient basis with entries -YZ^2 chosen to vanish on the four blown-up points.
EXPS=[(0,2,1),(1,0,2),(1,1,1),(1,2,0),(2,0,1),(2,1,0)]
Q=[(0,1,2)] # correction coefficient -1 at Y Z^2 each basis

def ds(c):
 a=[]
 for i in range(6):a.append(c%3);c//=3
 return tuple(a)
def enc(v):return sum(x*3**i for i,x in enumerate(v))
def normalize(v):
 z=next(t for t in v[::-1] if t)
 return tuple((z*t)%3 for t in v)
def fterms(v):
 r={}
 for a,e in zip(v,EXPS):r[e]=a
 r[(0,1,2)]=(-sum(v))%3
 return {e:a for e,a in r.items() if a}
class FiniteField:
 def __init__(self,d,pol):
  self.q=3**d; self.d=d;self.coeffs=[[n//3**i%3 for i in range(d)] for n in range(self.q)]
  self.add=[[sum(((self.coeffs[a][i]+self.coeffs[b][i])%3)*3**i for i in range(d)) for b in range(self.q)] for a in range(self.q)]
  self.mul=[]
  for a in range(self.q):
   row=[]
   for b in range(self.q):
    v=[0]*(2*d-1)
    for i in range(d):
     for j in range(d):v[i+j]=(v[i+j]+self.coeffs[a][i]*self.coeffs[b][j])%3
    for i in range(2*d-2,d-1,-1):
     for j in range(d):v[i-d+j]=(v[i-d+j]-v[i]*pol[j])%3
    row.append(sum(v[i]*3**i for i in range(d)))
   self.mul.append(row)
 def points(self):
  yield from ((1,y,z) for y in range(self.q) for z in range(self.q))
  yield from ((0,1,z) for z in range(self.q))
  yield (0,0,1)
 def evaluation_cache(self):
  allmon=EXPS+[(0,1,2)]
  powers=[[1]+[0]*3 for _ in range(self.q)]
  for x in range(self.q):
   powers[x][1]=x
   for i in range(2,4):powers[x][i]=self.mul[powers[x][i-1]][x]
  result=[]
  for p in self.points():
   one=[]
   for exps in allmon:
    val=[]
    for deriv in [-1,0,1,2]:
     if deriv>=0:
      if exps[deriv]==0:val.append(0);continue
      ee=tuple(z-(i==deriv) for i,z in enumerate(exps))
      factor=exps[deriv]%3
     else:ee=exps;factor=1
     w=self.mul[self.mul[powers[p[0]][ee[0]]][powers[p[1]][ee[1]]]][powers[p[2]][ee[2]]]
     if factor==2:w=self.add[w][w]
     val.append(w)
    one.append(tuple(val))
   result.append(one)
  return result
 def is_singular(self,v,cached):
  cf=list(v)+[(-sum(v))%3]
  add=self.add
  for pt in cached:
   four=[]
   for k in range(4):
    val=0
    for idx,c in enumerate(cf):
     if c==0:continue
     vv=pt[idx][k]
     if c==2:vv=add[vv][vv]
     val=add[val][vv]
    four.append(val)
   if four==[0,0,0,0]:return True
  return False

if __name__=='__main__':
 all_codes=sorted({enc(normalize(ds(c))) for c in range(1,3**6)})
 fields=[FiniteField(1,[0,1]),FiniteField(2,[1,0,1]),FiniteField(3,[1,0,2,1])]
 caches=[f.evaluation_cache() for f in fields]
 smooth=set()
 for code in all_codes:
  v=ds(code)
  if not any(f.is_singular(v,cc) for f,cc in zip(fields,caches)):smooth.add(code)
 print('independent smooth',len(smooth));assert len(smooth)==132
 pencils=set()
 for a,b in itertools.combinations(sorted(smooth),2):
  u,w=ds(a),ds(b)
  c=enc(normalize([(s+t)%3 for s,t in zip(u,w)]))
  d=enc(normalize([(s+2*t)%3 for s,t in zip(u,w)]))
  if c in smooth and d in smooth and len({a,b,c,d})==4:pencils.add(tuple(sorted((a,b,c,d))))
 print('independent pencils',len(pencils));assert len(pencils)==240
 known={tuple(p) for p in json.load(open(Path(__file__).resolve().parent.parent/'data/census.json'))['pencils']}
 assert known==pencils
 print('independent enumerations exactly agree')
