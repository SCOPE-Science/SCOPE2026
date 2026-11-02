#!/usr/bin/env python3
"""Exact arithmetic certificate for cyclic Rule 30 collision-weight series."""
from collections import Counter

def poly_mul(a,b):
 d={}
 for (i,j),v in a.items():
  for (k,l),w in b.items():
   key=(i+k,j+l)
   d[key]=d.get(key,0)+v*w
 return {p:v for p,v in d.items() if v}

F=[{(0,0):1,(1,1):-1},
   {(0,0):1,(1,0):-1,(3,2):-1,(3,3):-1},
   {(0,0):1,(1,1):1,(1,0):-1,(2,2):1,(2,1):-1}]
R={(0,0):1}
for f in F:R=poly_mul(R,f)
assert R.get((0,0))==1

def conv(a,b):
 d=Counter()
 for i,v in a.items():
  for j,w in b.items():d[i+j]+=v*w
 return d

def expected(N):
 # C=-z R'/R, coefficient polynomial in output weight
 rb=[Counter() for _ in range(max(N+1, max(i for i,j in R)+1))]
 for (n,k),a in R.items():rb[n][k]+=a
 out=[Counter() for _ in range(N+1)]
 for n in range(1,N+1):
  curr=Counter({k:-n*v for k,v in rb[n].items()}) if n<len(rb) else Counter()
  for i in range(1,min(n,len(rb)-1)+1):
   for k,v in conv(rb[i],out[n-i]).items():curr[k]-=v
  out[n]={k:v for k,v in curr.items() if v}
 return out

def matrices(t):
 B=[[0]*4 for _ in range(4)];M=[[0]*16 for _ in range(16)]
 for u in range(4):
  a,b=divmod(u,2)
  for c in (0,1):
   v=2*b+c;r=(30>>(4*a+2*b+c))&1
   B[u][v]+=t**r
 for p in range(16):
  u,v=divmod(p,4);a,b=divmod(u,2);aa,bb=divmod(v,2)
  for c in (0,1):
   for d in (0,1):
    r=(30>>(4*a+2*b+c))&1
    rr=(30>>(4*aa+2*bb+d))&1
    if r==rr:M[p][4*(2*b+c)+(2*bb+d)]+=t**r
 return B,M

def det_izA(A):
 m=len(A);V=[[int(i==j) for j in range(m)] for i in range(m)]
 coeff=[1]
 for k in range(1,m+1):
  W=[[sum(A[i][u]*V[u][j] for u in range(m)) for j in range(m)] for i in range(m)]
  tr=sum(W[i][i] for i in range(m))
  assert tr%k==0,(k,tr)
  ck=-tr//k
  coeff.append(ck)
  for i in range(m):W[i][i]+=ck
  V=W
 return coeff

def evaluate(f,t):
 zmax=max(i for i,j in f)
 out=[0]*(zmax+1)
 for (i,j),c in f.items():out[i]+=c*t**j
 return out

def poly_1d(a,b):
 out=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):out[i+j]+=x*y
 return out

def image(x,n):
 y=0
 for i in range(n):
  tri=((x>>((i-1)%n)&1)<<2)|((x>>i&1)<<1)|(x>>((i+1)%n)&1)
  y|=((30>>tri)&1)<<i
 return y

def collision_graph():
 vertices=tuple((u,v) for u in range(4) for v in range(4) if u!=v)
 edges={v:[] for v in vertices}
 for u,v in vertices:
  a,b=divmod(u,2); aa,bb=divmod(v,2)
  for c in (0,1):
   for d in (0,1):
    r=(30>>(4*a+2*b+c))&1
    s=(30>>(4*aa+2*bb+d))&1
    if r==s:
     to=(2*b+c,2*bb+d)
     if to in edges:edges[(u,v)].append((to,r))
 assert len(vertices)==12 and sum(map(len,edges.values()))==20
 return vertices,edges

def enumerate_simple_cycles(vertices,edges):
 cycles=[]
 for start in vertices:
  def walk(path,used,weight):
   for to,y in edges[path[-1]]:
    if to==start:
     cycles.append((len(path),weight+y,tuple(path)))
    elif to not in used and to>start:
     walk(path+[to],used|{to},weight+y)
  walk([start],{start},0)
 return cycles

def minimum_collision_lengths(max_k=45,max_n=55):
 vertices,edges=collision_graph()
 first={}
 for start in vertices:
  dp={(start,0):1}
  for n in range(1,max_n+1):
   nxt={}
   for (v,k),count in dp.items():
    for to,y in edges[v]:
     if k+y>max_k:continue
     idx=(to,k+y)
     nxt[idx]=nxt.get(idx,0)+count
   dp=nxt
   for k in range(max_k+1):
    if dp.get((start,k),0):first[k]=min(first.get(k,n),n)
 return first

def run():
 # All t monomials in det(I-zA) have t degree at most matrix order (16).
 # 17 specializations establish the polynomial identity for each coefficient.
 for t in range(17):
  B,M=matrices(t)
  dB=det_izA(B);dM=det_izA(M)
  b=poly_1d([1,-t-1],[1,t-1,t*t-t])
  r=evaluate(R,t)
  m=poly_1d(b,r)
  assert dB==b+[0]*(len(dB)-len(b)),('B',t,dB,b)
  assert dM==m+[0]*(len(dM)-len(m)),('M',t,dM,m)
 print('CERTIFIED_DETERMINANTS_17_SPECIALIZATIONS')
 Cs=expected(70)
 for n in range(1,15):
  mult=Counter(image(x,n) for x in range(1<<n))
  observed=Counter()
  for y,k in mult.items():observed[y.bit_count()]+=k*(k-1)
  observed={k:v for k,v in observed.items() if v}
  assert observed==Cs[n],(n,observed,Cs[n])
 print('BRUTE_FORCE_WEIGHTED_COLLISIONS_N1_TO14_OK')
 vertices,edges=collision_graph()
 cycles=enumerate_simple_cycles(vertices,edges)
 spectrum=Counter((n,w) for n,w,_ in cycles)
 assert spectrum==Counter({(1,0):2,(3,3):2,(4,3):2,(6,4):1,(7,4):2,(8,4):1}),spectrum
 # The weight-three length-three cycle and weight-four length-six cycle
 # share (0,1), so concatenation gives the sharp constructive bounds.
 assert any(n==3 and w==3 and (0,1) in route for n,w,route in cycles)
 assert any(n==6 and w==4 and (0,1) in route for n,w,route in cycles)
 first=minimum_collision_lengths()
 for k in range(46):
  predicted=(1 if k==0 else None if k in (1,2,5) else k+2*(k%3))
  assert first.get(k)==predicted,(k,first.get(k),predicted)
 print('TEN_SIMPLE_CYCLES_AND_SHARP_MINIMUM_RING_LENGTHS_OK')
 print('Selected C_n polynomials (dict weight:ordered pair count):')
 for n in (1,2,3,6,9,12,14):print(n,dict(sorted(Cs[n].items())))
 forbidden=[k for k in range(71) if not any(k in Cs[n] for n in range(1,71))]
 print('ABSENT_WEIGHTS_THROUGH_N70',forbidden)
 print('VERIFY_OK')

if __name__=='__main__':run()
