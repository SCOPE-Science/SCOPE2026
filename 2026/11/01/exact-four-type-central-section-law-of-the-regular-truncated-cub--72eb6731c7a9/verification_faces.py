from itertools import permutations,product
import numpy as np,math
rng=np.random.default_rng(20141)
t=math.sqrt(2)-1
V=[]
for perm in set(permutations([1.,1.,t])):
 for signs in product([-1,1],repeat=3):
  V.append(tuple(s*p for s,p in zip(signs,perm)))
V=sorted(set(V)); assert len(V)==24
faces=[]
for j in range(3):
 for s in [-1,1]:
  vv=[v for v in V if abs(v[j]-s)<1e-9]; assert len(vv)==8
  faces.append(vv)
for s in product([-1,1],repeat=3):
 vv=[v for v in V if abs(sum(v[i]*s[i] for i in range(3))-(2+t))<1e-9]; assert len(vv)==3
 faces.append(vv)
assert len(faces)==14
counts={4:0,6:0,8:0,10:0}; mismatches=[]
for k in range(40000):
 u=rng.normal(size=3); a,b,c=sorted(map(abs,u),reverse=True)
 n=4+2*(a<b+t*c)+2*(t*b+c<a<(b+c)/t)+2*(b>t*a+c)
 actual=sum(min(sum(x*y for x,y in zip(u,v)) for v in face)<0<max(sum(x*y for x,y in zip(u,v)) for v in face) for face in faces)
 if actual!=n: mismatches.append((u,n,actual))
 counts[n]+=1
print('counts',counts,'mismatch',len(mismatches),'first',mismatches[:1])
