import itertools,math
from mpmath import iv
iv.dps=28

def pattern(w):
 d={}
 for mask in range(16):
  k=mask.bit_count();x=sum(w[i] for i in range(4) if mask>>i&1)
  d.setdefault(x,[0]*5)[k]+=1
 return tuple(sorted(tuple(t) for t in d.values()))
reps={}
for w in itertools.combinations_with_replacement(range(1,9),4):reps.setdefault(pattern(w),w)
assert len(reps)==23

def polys(c):
 z=[0]*5
 for k,x in enumerate(c):
  for j in range(5-k):z[k+j]+=x*(-1)**j*math.comb(4-k,j)
 yield tuple(z)
 for d in range(1,3):
  z=[i*z[i] for i in range(1,len(z))]; yield tuple(z)

def evalpoly(c,p):
 r=iv.mpf(0)
 for x in reversed(c):r=r*p+x
 return r

def all_uppers(pattern,a,b):
 p=iv.mpf([str(a),str(b)])
 h=iv.mpf(0)
 for c in pattern:
  # q in Bernstein to keep positive
  q=iv.mpf(0)
  for k,x in enumerate(c):
   if x:q+=x*p**k*(1-p)**(4-k)
  _,der1,der2=tuple(polys(c))
  qp=evalpoly(der1,p);qpp=evalpoly(der2,p)
  if q.a<=0:return False
  h-=qpp*iv.log(q)+qp*qp/q
 return h.b<0
N=0;depth=0
for pat,w in reps.items():
 stack=[(0.0001,0.5,0)]
 cnt=0;dmax=0
 while stack:
  a,b,d=stack.pop()
  N+=1;cnt+=1;dmax=max(dmax,d)
  if not all_uppers(pat,a,b):
   if d>38:raise RuntimeError((w,a,b))
   m=(a+b)/2
   stack.extend([(a,m,d+1),(m,b,d+1)])
 print('PASS',w,'nodes',cnt,'depth',dmax,flush=True)
print('GLOBAL PASS:',len(reps),'patterns',N,'subinterval nodes')
