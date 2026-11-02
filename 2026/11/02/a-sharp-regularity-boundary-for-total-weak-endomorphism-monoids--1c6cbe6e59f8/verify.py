from itertools import product

def weak(f,lab):
 n=len(f)
 return all(lab[f[i]]!=lab[f[j]] or f[i]==f[j] for i in range(n) for j in range(i+1,n) if lab[i]!=lab[j])

def split_certificate(f,a,b):
 I=set(f)
 if len(I)==1:return True
 for xside in (set(range(a)),set(range(a,a+b))):
  yside=set(range(a+b))-xside
  if all(any(i in xside and f[i]==t for i in range(a+b)) for t in I if t<a) and all(any(i in yside and f[i]==t for i in range(a+b)) for t in I if t>=a):return True
 return False

def direct_regular(f,lab,weak_maps):
 I=set(f)
 return any(all(f[g[z]]==z for z in I) for g in weak_maps)

for a,b in [(1,1),(1,2),(1,3),(1,4),(2,2),(2,3),(2,4),(3,3)]:
 n=a+b; lab=[0]*a+[1]*b
 F=[f for f in product(range(n),repeat=n) if weak(f,lab)]
 bad=[f for f in F if not split_certificate(f,a,b)]
 print('BIPARTITE',a,b,'weak_size',len(F),'no_split_certificate',len(bad),flush=True)
 assert not bad

for P in ([1,1,1],[1,1,2],[1,2,2],[2,2,2]):
 n=sum(P);lab=sum(([i]*k for i,k in enumerate(P)),[])
 F=[f for f in product(range(n),repeat=n) if weak(f,lab)]
 if n<=5:
  bad=[f for f in F if not direct_regular(f,lab,F)]
  print('MULTIPARTITE',P,'weak_size',len(F),'nonregular',len(bad),'witness',bad[0] if bad else None,flush=True)
  assert (len(bad)>0)==(max(P)>=2 and len(P)>=3)
 else:
  # explicit obstruction (part0/1/2, third part has >=2):
  i0=0;i1=P[0];j0=P[0]+P[1];j1=j0+1
  f=[i0]*n; f[j0]=i1;f[j1]=j0
  assert weak(f,lab)
  assert not any(lab[x]!=lab[y] or x==y for x in [j0] for y in [j1])
  print('MULTIPARTITE',P,'weak_size',len(F),'obstruction_works',True,flush=True)
print('VERIFY_OK')
