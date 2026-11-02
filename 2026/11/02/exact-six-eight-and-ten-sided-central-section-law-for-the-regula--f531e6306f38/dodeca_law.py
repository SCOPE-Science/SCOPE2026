import numpy as np,itertools,collections, math
from scipy.spatial import ConvexHull
phi=(1+5**.5)/2
vs=list(itertools.product([-1.,1.],repeat=3))
for s,t in itertools.product([-1.,1.],repeat=2):
 for coords in [(0,s/phi,t*phi),(s/phi,t*phi,0),(t*phi,0,s/phi)]: vs.append(coords)
vs=np.array(vs); hull=ConvexHull(vs)
fac=[]
for eq in hull.equations:
 inds=tuple(sorted(np.where(abs(vs@eq[:3]+eq[3])<1e-7)[0].tolist()))
 if inds not in fac: fac.append(inds)
planes=[]
for v in vs:
 v=v/np.linalg.norm(v)
 if not any(np.linalg.norm(v-w)<1e-10 or np.linalg.norm(v+w)<1e-10 for w in planes): planes.append(v/np.linalg.norm(v))
planes=np.array(planes);print('planes',len(planes),'facets',len(fac))
N=len(planes)
patterns=set()
for i,j in itertools.combinations(range(N),2):
 vv=np.cross(planes[i],planes[j]);l=np.linalg.norm(vv)
 if l<1e-9: continue
 vv/=l
 a=planes[i];b=np.cross(vv,a)
 for s,t in itertools.product([-1,1],repeat=2):
  for sign in [-1,1]:
   w=sign*vv+1e-5*(s*a+t*b);patterns.add(tuple(np.sign(planes@w).astype(int)))
print('patterns',len(patterns))
areas=collections.defaultdict(float);counts=collections.Counter();area_examples=collections.defaultdict(list);K=0; shapes=collections.defaultdict(collections.Counter);sample=collections.defaultdict(list)
for pattern in patterns:
 S=np.array(pattern);A=S[:,None]*planes
 pts=[]
 for i,j in itertools.combinations(range(N),2):
  u=np.cross(A[i],A[j]);l=np.linalg.norm(u)
  if l<1e-9:continue
  u/=l
  for s in [-1,1]:
   p=s*u
   if np.min(A@p)>=-2e-9 and not any(np.linalg.norm(p-q)<2e-7 for q in pts):pts.append(p)
 if len(pts)<3: print('bad',pattern,len(pts));continue
 cp=np.sum(pts,axis=0);cp/=np.linalg.norm(cp)
 b=pts[0]-np.dot(cp,pts[0])*cp;b/=np.linalg.norm(b);c=np.cross(cp,b)
 pts.sort(key=lambda p:np.arctan2(np.dot(c,p),np.dot(b,p)))
 aa=0
 for k in range(1,len(pts)-1):
  x,y,z=pts[0],pts[k],pts[k+1]
  aa+=2*math.atan2(abs(np.dot(x,np.cross(y,z))),1+np.dot(x,y)+np.dot(y,z)+np.dot(z,x))
 u=cp; scores=vs@u
 nsides=sum((scores[list(f)].min()<0) and (scores[list(f)].max()>0) for f in fac)
 areas[nsides]+=aa;counts[nsides]+=1; area_examples[nsides].append(round(aa,9));shapes[nsides][len(pts)]+=1
 if len(sample[nsides])<1: sample[nsides]=[(pattern,pts)]
 K+=1
print('valid cells',K,'total area',sum(areas.values()),'4pi',4*math.pi)
print('count',counts)
print('laws',{n:(v/(4*math.pi),v) for n,v in areas.items()})
for k in areas:
 print('type',k,'distinct areas',collections.Counter(area_examples[k]))

print("SHAPES",shapes)
for k,vals in sample.items():
 print("SAMPLE",k,vals[0][0]); print(np.array(vals[0][1]))
for k,vals in sample.items():
 pts=vals[0][1];angs=[];dotgroup=[]
 for i in range(len(pts)):
  p=pts[i];q=pts[i-1];r=pts[(i+1)%len(pts)]
  x=q-(q@p)*p;y=r-(r@p)*p
  cos=(x@y)/(np.linalg.norm(x)*np.linalg.norm(y)); ang=np.arccos(np.clip(cos,-1,1)); angs.append(ang);dotgroup.append(np.cos(ang))
 print('INTERIOR',k,len(pts),'angles radians',np.round(angs,11),'cosines',np.round(dotgroup,11),'area via GB',sum(angs)-(len(pts)-2)*np.pi)
