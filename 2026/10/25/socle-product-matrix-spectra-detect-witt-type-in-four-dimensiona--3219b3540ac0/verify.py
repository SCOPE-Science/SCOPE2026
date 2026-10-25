import numpy as np

def fops(q):
 if q==4:
  def add(a,b):return a^b
  def mul(a,b):
   x=0
   for j in range(2):
    if (b>>j)&1:x^=a<<j
   for j in (3,2):
    if (x>>j)&1:x^=7<<(j-2)
   return x
 else:
  add=lambda a,b:(a+b)%q
  mul=lambda a,b:(a*b)%q
 return add,mul

def test(q,H,run_full=False):
 add,mul=fops(q)
 vs=[(a,b) for a in range(q) for b in range(q) if a or b]
 def B(v,w):
  s=0
  for i in range(2):
   for j in range(2):s=add(s,mul(mul(v[i],H[i][j]),w[j]))
  return s
 c=1;t= sum(B(v,v)==0 for v in vs)//(q-1)
 C=np.array([[int(B(v,w)==c) for w in vs] for v in vs],dtype=float)
 expected={round(q,7):1,round(1.,7):(q+1-t)//2,round(-1.,7):(q-1+t)//2,round(np.sqrt(q),7):(q+1)*(q-2)//2,round(-np.sqrt(q),7):(q+1)*(q-2)//2}
 got={}
 for z in np.linalg.eigvalsh(C):
  key=round(z,7);got[key]=got.get(key,0)+1
 ex={a:b for a,b in expected.items() if b}
 assert got==ex,(q,H,t,got,ex)
 if run_full:
  R=[(a,v,b) for a in range(q) for v in [(x,y) for x in range(q) for y in range(q)] for b in range(q)]
  def prod(x,y):
   a,v,b=x;d,w,e=y
   return (mul(a,d), (add(mul(a,w[0]),mul(d,v[0])),add(mul(a,w[1]),mul(d,v[1]))),add(add(mul(a,e),mul(d,b)),B(v,w)))
  N=len(R)
  mat=np.array([[int(prod(x,y)==(0,(0,0),1)) for y in R] for x in R], dtype=float)
  got2={}
  for z in np.linalg.eigvalsh(mat):
   key=round(z,6);got2[key]=got2.get(key,0)+1
  k=(q-1)+(q+1)*(q-2)//2
  ex2={round(q*q,6):1,round(float(q),6):(q+1-t)//2,round(-float(q),6):(q-1+t)//2,round(q**1.5,6):k,round(-q**1.5,6):k,0:q**4-q*q-2*q+3}
  ex2={a:b for a,b in ex2.items() if b}
  assert got2==ex2,(q,H,t,got2,ex2)
 print('OK',q,H,'isotropic lines',t,'full' if run_full else 'C only', 'eigs',got)
for q,HH,full in [
(2,((0,1),(1,0)),True),(2,((1,0),(0,1)),True),
(3,((0,1),(1,0)),True),(3,((1,0),(0,1)),True),
(4,((0,1),(1,0)),True),(4,((1,0),(0,1)),True),
(5,((0,1),(1,0)),False),(5,((1,0),(0,2)),False)]:
 test(q,HH,full)
