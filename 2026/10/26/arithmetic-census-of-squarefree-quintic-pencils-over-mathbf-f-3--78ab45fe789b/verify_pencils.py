import itertools,collections,json,math
p=3; d=5
# represent coeffs low to high i in x^i z^(d-i)
def encode(a):return sum(t*3**i for i,t in enumerate(a))
def dec(q):return tuple((q//3**i)%3 for i in range(d+1))
def norm(v):
 if not any(v):return None
 a=next(t for t in v if t);z=pow(a,-1,3)
 return encode(tuple(t*z%3 for t in v))
def add(a,b,k=1):return tuple((a[i]+k*b[i])%3 for i in range(d+1))
def trim(f):
 f=list(f)
 while f and not f[-1]:f.pop()
 return f
def rem(a,b):
 a=trim(a);b=trim(b)
 if not b:raise ZeroDivisionError
 while len(a)>=len(b):
  t=a[-1]*pow(b[-1],-1,3)%3; j=len(a)-len(b)
  for i,x in enumerate(b):a[j+i]=(a[j+i]-t*x)%3
  a=trim(a)
 return a
def gcd(a,b):
 a,b=trim(a),trim(b)
 while b:a,b=b,rem(a,b)
 return [] if not a else [(t*pow(a[-1],-1,3))%3 for t in a]
def sf(v):
 f=trim(v)
 return len(f)>=5 and len(gcd(f,[(i*f[i])%3 for i in range(1,len(f))]))==1
projective=sorted(set(norm(v) for v in itertools.product(range(3),repeat=6) if any(v)))
smooth=[q for q in projective if sf(dec(q))]
print('forms',len(projective),'squarefree',len(smooth),flush=True)
S=set(smooth); qset=set();pairs=0
for ix,a in enumerate(smooth):
 v=dec(a)
 for b in smooth[ix+1:]:
  w=dec(b)
  n1=norm(add(v,w,1));n2=norm(add(v,w,2))
  if n1 in S and n2 in S:
   qset.add(tuple(sorted((a,b,n1,n2))));pairs+=1
Q=sorted(qset)
assert 6*len(Q)==pairs,(pairs,len(Q))
print('pencils',len(Q),'all pencils',11011,flush=True)
base=collections.Counter();profile=collections.Counter();rational=collections.Counter()
for g in Q:
 v,w=dec(g[0]),dec(g[1]);h=gcd(v,w)
 deg= (len(h)-1)+int(v[-1]==0 and w[-1]==0)
 base[deg]+=1
 pts=[0,1,2]
 rt=sum(all(sum(dec(f)[i]*pow(t,i,3) for i in range(6))%3==0 for f in g) for t in pts)+int(all(dec(f)[5]==0 for f in g))
 rational[rt]+=1
 # factor-degree partitions later
print('base divisor degree',sorted(base.items()),'rational base',sorted(rational.items()),flush=True)
# PGL2(3) transforms
def poly_mul(A,B):
 C=[0]*(len(A)+len(B)-1)
 for i,a in enumerate(A):
  for j,b in enumerate(B):C[i+j]=(C[i+j]+a*b)%3
 return C
def pow_poly(A,k):
 R=[1]
 for i in range(k):R=poly_mul(R,A)
 return R
def make_map(a,b,c,e):
 mono=[]
 for i in range(6):
  m=poly_mul(pow_poly([b,a],i),pow_poly([e,c],5-i))
  assert len(m)==6
  mono.append(m)
 mp={}
 for q in projective:
  v=dec(q);new=tuple(sum(v[i]*mono[i][j] for i in range(6))%3 for j in range(6))
  mp[q]=norm(new)
 return mp
GL=[];seenmap=set()
for a,b,c,e in itertools.product(range(3),repeat=4):
 if (a*e-b*c)%3:
  mp=make_map(a,b,c,e)
  key=tuple(mp[q] for q in projective)
  if key not in seenmap:seenmap.add(key);GL.append(mp)
assert len(GL)==24
print('GL count',len(GL),flush=True)
Qset=set(Q);seen=set();orbitinfo=[]
for g in Q:
 if g in seen:continue
 O={tuple(sorted(mp[q] for q in g)) for mp in GL}
 assert O<=Qset,(len(O),len(Qset-O))
 assert not O&seen
 seen.update(O)
 rep=min(O)
 vv,ww=dec(rep[0]),dec(rep[1]);h=gcd(vv,ww)
 deg=(len(h)-1)+int(vv[-1]==0 and ww[-1]==0)
 orbitinfo.append([len(O),deg,rep])
assert len(seen)==len(Q)
print('orbits',len(orbitinfo),'sizes',sorted(collections.Counter(o[0] for o in orbitinfo).items()),'base by orbit',sorted(collections.Counter((o[0],o[1]) for o in orbitinfo).items()),flush=True)

assert len(smooth)==216
assert len(Q)==1098 and base=={0:1029,2:24,3:24,4:21}
assert len(orbitinfo)==54 and collections.Counter(t[0] for t in orbitinfo)=={3:2,6:2,12:10,24:40}
from pathlib import Path
folder=Path(__file__).resolve().parent
expected={tuple(map(int,line.split())) for line in (folder/'pencils.txt').read_text().splitlines()}
assert expected==set(Q)
import csv
rows=[]
for row in csv.DictReader((folder/'orbit_representatives.csv').open()):
    rows.append((int(row['orbit_size']),int(row['base_divisor_degree']),tuple(map(int,row['representative_four_normalized_coeff_ints'].split(':')))))
assert sorted((size,deg,tuple(rep)) for size,deg,rep in orbitinfo)==sorted(rows)
print('EXACT PENCILS AND SOURCE ORBITS VERIFIED')
