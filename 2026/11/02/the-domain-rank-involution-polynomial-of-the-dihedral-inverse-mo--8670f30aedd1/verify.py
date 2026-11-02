from collections import Counter
from math import comb

def enumerate_involutions(n):
 perms=[]
 for s in (1,-1):
  for a in range(n):perms.append(tuple((s*x+a)%n for x in range(n)))
 allmaps=set()
 for p in perms:
  for mask in range(1<<n):
   v=tuple(p[i] if mask>>i&1 else -1 for i in range(n));allmaps.add(v)
 byrank=Counter()
 for v in allmaps:
  dom={i for i,x in enumerate(v) if x>=0}
  if all(v[x]==i for i,x in enumerate(v) if x>=0):
   byrank[len(dom)]+=1
 return [byrank[i] for i in range(n+1)],len(allmaps)

def poly(n):
 out=[comb(n,k) for k in range(n+1)]
 if n%2:
  for j in range(1,(n-1)//2+1):
   out[2*j]+=n*comb((n-1)//2,j)
   out[2*j+1]+=n*comb((n-1)//2,j)
 else:
  h=n//2
  for j in range(1,h):
   for d in (0,1,2):
    out[2*j+d]+=h*comb(h-1,j)*comb(2,d)
  for j in range(1,h+1):out[2*j]+=(h+1)*comb(h,j)
  out[2]-=h
 return out
if __name__=='__main__':
 for n in range(3,11):
  a,sz=enumerate_involutions(n);b=poly(n)
  print('n',n,'match',a==b,'involutions',sum(a),'monoid',sz,'rankcounts',a)
  assert a==b
 print('VERIFY_OK')
