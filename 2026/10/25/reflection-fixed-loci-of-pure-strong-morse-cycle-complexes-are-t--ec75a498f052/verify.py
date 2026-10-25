from itertools import combinations

def facets(n):
 out=[]
 for gap in range(n):
  path=[(gap+1+t)%n for t in range(n-1)]
  for root in range(n-1):
   f=0
   for k in range(1,n-1):
    v=2*path[k-1]+(0 if k<=root else 1)
    f|=1<<v
   out.append(f)
 return out

def eq(n,a):
 P=[2*((a-i-1)%n)+(1-b) for i in range(n) for b in (0,1)]
 seen=set(); os=[]
 for v in range(2*n):
  if v in seen:continue
  orbit=[v,P[v]]
  assert P[P[v]]==v and P[v]!=v
  seen.update(orbit);os.append(sum(1<<x for x in orbit))
 return os

def claim(n,a):
 m=n//2
 if a==0:
  A=range(1,m);B=range(0,m-1)
 else:
  assert n%2==0
  A=range(2,m); B=range(1,m-1)
 return [sum((1<<(2*i))+(1<<(2*((a-i-1)%n)+1)) for i in A),sum((1<<(2*i+1))+(1<<(2*((a-i-1)%n))) for i in B)]

def run(n,a):
 fs=facets(n);os=eq(n,a)
 actual=set()
 for f in fs:
  U=sum(1<<k for k,o in enumerate(os) if o&f==o)
  actual.add(U)
 maximal=[]
 for U in sorted(actual,key=int.bit_count,reverse=True):
  if not any(U&V==U for V in maximal):maximal.append(U)
 maskpairs=claim(n,a)
 want=[sum(1<<k for k,o in enumerate(os) if o & f==o) for f in maskpairs]
 assert sorted(maximal)==sorted(want),(n,a,maximal,want)
 assert (want[0]&want[1])==0
 assert all(int.bit_count(v)==(n//2-1 if a==0 else n//2-2) for v in want)
 # independently confirm that every orbit union selected by a facet is contained in exactly one of the expected maximal faces
 assert all(any(U&v==U for v in want) for U in actual)
 # both maximal are achieved
 assert all(v in actual for v in want)
 return len(fs),len(os),len(actual),[x.bit_count() for x in maximal]
if __name__=='__main__':
 for n in range(6,41):
  for a in ([0,1] if n%2==0 else [0]):
   x=run(n,a)
   print(f'n={n} a={a} facets={x[0]} orbits={x[1]} submasks={x[2]} sizes={x[3]}')
 print('PASS: all reflection invariant orbit-face complexes equal two disjoint prescribed simplices for 6<=n<=40')
