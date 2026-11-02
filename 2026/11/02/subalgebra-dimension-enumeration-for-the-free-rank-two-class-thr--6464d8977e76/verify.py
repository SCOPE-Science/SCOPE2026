"""Independent finite-field exhaustive enumeration for five-dimensional free class-three Lie algebra."""
import itertools,sys,collections

def operations(q):
 if q==4:
  add=lambda a,b:a^b
  def mul(a,b):
   out=0
   while b:
    if b&1:out^=a
    b>>=1; a<<=1
    if a&4:a^=7
   return out
  inv={1:1,2:3,3:2}
 elif q in (2,3,5):
  add=lambda a,b:(a+b)%q
  mul=lambda a,b:a*b%q
  inv={a:pow(a,-1,q) for a in range(1,q)}
 else: raise ValueError(q)
 def sub(a,b):return add(a,b) if q==4 else (a-b)%q
 return add,mul,sub,inv

def spaces(q,n=5):
 for k in range(n+1):
  for pivots in itertools.combinations(range(n),k):
   positions=[(i,j) for i,p in enumerate(pivots) for j in range(p+1,n) if j not in pivots]
   for cs in itertools.product(range(q), repeat=len(positions)):
    rows=[[0]*n for _ in range(k)]
    for i,p in enumerate(pivots):rows[i][p]=1
    for (i,j),v in zip(positions,cs):rows[i][j]=v
    yield k,pivots,rows

def test(q):
 add,mul,sub,_=operations(q)
 def bracket(a,b):
  return [0,0,sub(mul(a[0],b[1]),mul(a[1],b[0])),sub(mul(a[0],b[2]),mul(a[2],b[0])),sub(mul(a[1],b[2]),mul(a[2],b[1]))]
 def member(vec,pivots,rows):
  vec=vec[:]
  for p,row in zip(pivots,rows):
   scale=vec[p]
   if scale:
    for j in range(p,5):vec[j]=sub(vec[j],mul(scale,row[j]))
  return not any(vec)
 counts=collections.Counter(); abel=collections.Counter(); subspaces=collections.Counter();
 for k,pivots,rows in spaces(q):
  subspaces[k]+=1
  ok=True; a=True
  for i in range(k):
   for j in range(i):
    b=bracket(rows[j],rows[i]);
    if any(b):a=False
    if not member(b,pivots,rows):ok=False;break
   if not ok:break
  if ok:
   counts[k]+=1
   if a:abel[k]+=1
 predicted={0:1,1:q**4+q**3+q**2+q+1,2:1+q*(q+1)*(q*q+q+1),3:(q*q+q+1)+q*q*(q+1),4:q+1,5:1}
 print('q',q,'counts',dict(sorted(counts.items())),'abel',dict(sorted(abel.items())),'ambient',dict(sorted(subspaces.items())), 'pred',predicted,flush=True)
 assert dict(counts)==predicted,(q,counts,predicted)
 assert abel[3]==q*q+q+1 and counts[3]-abel[3]==q*q*(q+1)

if __name__=='__main__':
 for q in [2,3,4]:test(q)
 print('VERIFY_OK')
