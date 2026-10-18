"""Direct group-orbit census on actual functions, without profile compression."""
from itertools import product
from s5_orbit_burnside import partitions,frame,auts,orbits_burnside

def brute_group(src,dst):
 A,B=frame(src),frame(dst);n,m=sum(src),sum(dst)
 bid={v:j for j,b in enumerate(B) for v in b}
 valid=[]
 for f in product(range(m),repeat=n):
  if set(f)!=set(range(m)):continue
  for a in A:
   js={bid[f[v]] for v in a}
   if len(js)!=1 or set(f[v] for v in a)!=set(B[next(iter(js))]):break
  else:valid.append(f)
 source=[t for t,_ in auts(A)]
 target=[t for t,_ in auts(B)]
 canon={}
 for f in valid:
  best=None
  for s in source:
   arr=tuple(f[s[v]] for v in range(n))
   for t in target:
    key=tuple(t[y] for y in arr)
    if best is None or key<best:best=key
  canon[f]=best
 return len(set(canon.values())),len(valid)

if __name__=='__main__':
 c=0;total=0
 for n in range(1,5):
  for src in partitions(n):
   for m in range(1,min(n,3)+1):
    for dst in partitions(m):
     a,k=brute_group(src,dst);b=orbits_burnside(src,dst)
     assert a==b,(src,dst,a,b)
     total+=k;c+=1
 print('ALL PASS',c,'complete source-and-target automorphism-action instances;',total,'surjective bounded maps')
