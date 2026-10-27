import math

def rank(xs):
  piv={}
  for w in xs:
    while w:
      i=w.bit_length()-1
      if i in piv:w^=piv[i]
      else:piv[i]=w;break
  return len(piv)

def update(x,m,n):
  y=0
  for a in range(m):
    for b in range(n):
      j=a*n+b
      u=((a+1)%m)*n+b
      d=((a-1)%m)*n+b
      l=a*n+(b-1)%n
      r=a*n+(b+1)%n
      if ((x>>u)^(x>>d)^(x>>l)^(x>>r))&1:y|=1<<j
  return y

def test(m,n):
 N=m*n
 k=m&-m;l=n&-n
 g=math.gcd(m//k,n//l)
 z=k*l*(2*g-1)
 T=max(k,l) if g>1 else max(1,k//2,l//2)
 cols=[1<<j for j in range(N)]
 rprev=N
 rs=[]
 for t in range(T+2):
  r=rank(cols);rs.append(r)
  if t>=T and r!=N-z:raise Exception('BAD stable',m,n,t,r,N-z,rs)
  if t==T-1 and T>0 and r==N-z:raise Exception('NOT SHARP',m,n,T,rs)
  cols=[update(v,m,n) for v in cols]
 if g>1 and max(k,l)>1:
  expected_maxblock=2*(g-1)*min(k,l)
  if rs[T-1]-rs[T]!=expected_maxblock:raise Exception('BAD MAXBLOCK',m,n,rs,expected_maxblock)
 return T,z,rs

s=0
for m in range(3,15):
 for n in range(3,15):
  t,z,r=test(m,n);s+=1
  if (m,n) in [(3,3),(3,4),(3,6),(4,4),(6,9),(6,10),(8,12),(12,12),(15,15)]:print(m,n,t,z,r)
print('MATRIX_VERIFIED',s)
# independent direct state iteration for all configurations on small dimensions
for m,n in [(3,3),(3,4),(4,3),(4,4)]:
 N=m*n;t,z,rs=test(m,n)
 pts=set()
 # periodic detection by fixed repeated F^T trajectory, F periodic after a finite order
 for x in range(1<<N):
  v=x
  for _ in range(t):v=update(v,m,n)
  pts.add(v)
 if len(pts)!=(1<<(N-z)):raise AssertionError((m,n,len(pts),z))
 print('STATE_VERIFIED',m,n,1<<N,len(pts),t)
print('VERIFY_OK')
# Exhaustive *depth* census to independently check the sharp maximum-depth fraction.
for m,n in [(3,3),(3,6)]:
 N=m*n
 T,z,_=test(m,n)
 cols=[1<<j for j in range(N)]
 for _ in range(T):cols=[update(c,m,n) for c in cols]
 reachable={0}
 for c in cols:reachable|={u^c for u in tuple(reachable)}
 assert len(reachable)==2**(N-z)
 depths=[0]*(T+1)
 for x in range(1<<N):
  v=x
  for t in range(T+1):
   if v in reachable:
    depths[t]+=1
    break
   v=update(v,m,n)
  else:raise AssertionError('unreached',m,n,x)
 g=math.gcd(m//(m&-m),n//(n&-n))
 k=m&-m;l=n&-n
 predicted=1-2**(-(2*(g-1)*min(k,l) if max(k,l)>1 else 2*g-1))
 assert depths[T]==round((1<<N)*predicted),(m,n,depths,predicted)
 print('DEPTH_DISTRIBUTION',m,n,depths)
print('DEPTH_VERIFY_OK')
