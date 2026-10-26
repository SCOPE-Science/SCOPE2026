from pathlib import Path
BASE = Path(__file__).resolve().parent
import numpy as np,itertools,collections,math,time,json
MON=[(i,j,4-i-j) for i in range(5) for j in range(5-i)]
MI={e:i for i,e in enumerate(MON)}
vecs={tuple(map(int,line.strip().split(','))) for line in open(str(BASE/'smooth_vectors.csv')) if line.strip()}
assert len(vecs)==234

def mul(a,b):
 c=collections.defaultdict(int)
 for e,v in a.items():
  for f,w in b.items():
   g=tuple(e[i]+f[i] for i in range(3));c[g]=(c[g]+v*w)%3
 return {k:v for k,v in c.items() if v}
def power(a,n):
 b={(0,0,0):1}
 for _ in range(n):b=mul(b,a)
 return b

def action_matrix(M):
 pol=[{(int(i==0),int(i==1),int(i==2)):int(M[j,i]) for i in range(3) if M[j,i]} for j in range(3)]
 Pows=[[power(p,k) for k in range(5)] for p in pol]
 T=np.zeros((15,15),dtype=np.int16)
 for i,exps in enumerate(MON):
  d=mul(mul(Pows[0][exps[0]],Pows[1][exps[1]]),Pows[2][exps[2]])
  for e,v in d.items():T[MI[e],i]=v
 return T

def norm(v):
 k=next(t for t in v if t)
 return tuple(int(x*(1 if k==1 else 2)%3) for x in v)

def rank2(A):return (A[0,0]*A[1,1]-A[0,1]*A[1,0])%3 !=0
Ms=[]
for a,b,c,d,e,f in itertools.product(range(3),range(3),range(3),range(3),range(3),range(3)):
 L=np.array([[c,d],[e,f]],dtype=np.int16)
 if not rank2(L):continue
 Ms.append(np.array([[1,a,b],[0,c,d],[0,e,f]],dtype=np.int16))
assert len(Ms)==432
T=[action_matrix(M) for M in Ms]
st=time.time();seen=set();orbs=[]
for v in sorted(vecs):
 if v in seen:continue
 orbit={norm((t@np.array(v,dtype=np.int16))%3) for t in T}
 assert orbit<=vecs, ('not stable',len(orbit-vecs),list(orbit-vecs)[:1])
 seen.update(orbit)
 orbs.append((v,orbit))
print('orbits',len(orbs),'sizes',collections.Counter(len(o) for _,o in orbs),'time',round(time.time()-st,2))
print('global',len(vecs)*13)
print('representatives')
for k,(v,o) in enumerate(orbs):
 print(k+1,'fixed-center orbit',len(o),'global',13*len(o),'stabilizer',432//len(o),v)
with open(str(BASE/'orbits.json'),'w') as fp:
 json.dump({'center_fixed_count':len(vecs),'global_count':len(vecs)*13,'orbits':[{'representative':v,'center_fixed_orbit_size':len(o),'global_orbit_size':13*len(o),'stabilizer_order':432//len(o),'members':[list(u) for u in sorted(o)]} for v,o in orbs]},fp,indent=2)
