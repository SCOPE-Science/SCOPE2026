from functools import lru_cache
@lru_cache(None)
def noncrossing(seq):
 if not seq:return ((),)
 out=[];a=seq[0]
 for j in range(1,len(seq),2):
  b=seq[j]
  for L in noncrossing(seq[1:j]):
   for R in noncrossing(seq[j+1:]):out.append(tuple(sorted(((a,b),)+L+R)))
 return tuple(out)
def multiply(n,X,Y):
 p=list(range(3*n))
 def root(a):
  while a!=p[a]:p[a]=p[p[a]];a=p[a]
  return a
 def join(a,b):p[root(a)]=root(b)
 def loc(a,j):return (a if a<n else n+(2*n-1-a)) if j==0 else (n+a if a<n else 2*n+(2*n-1-a))
 for a,b in X:join(loc(a,0),loc(b,0))
 for a,b in Y:join(loc(a,1),loc(b,1))
 c={}
 for a in [*range(n),*range(2*n,3*n)]:c.setdefault(root(a),[]).append(a)
 assert all(len(v)==2 for v in c.values())
 def encode(a):return a if a<n else 2*n-1-(a-2*n)
 return tuple(sorted(tuple(sorted(map(encode,v))) for v in c.values()))
def rank(n,p):return sum(a<n<=b for a,b in p)
def Xij(n,i,j,k=1):
 a=set(range(1,n+1));b=set(range(1,n+1));z=[]
 direction=1 if j>=i else -1
 for h in range(k):
  aa=i+2*h*direction;bb=j-2*h*direction
  assert aa>=1 and aa<n and bb>=1 and bb<n
  assert aa in a and aa+1 in a and bb in b and bb+1 in b
  a.remove(aa);a.remove(aa+1);b.remove(bb);b.remove(bb+1)
  z.append((aa-1,aa));z.append((2*n-(bb+1),2*n-bb))
 for t,s in zip(sorted(a),sorted(b)):
  z.append((t-1,2*n-s))
 return tuple(sorted(tuple(sorted(e)) for e in z))
if __name__=='__main__':
 total=0
 for n in range(2,10):
  ms=noncrossing(tuple(range(2*n)));hist={};maxes=[]
  for X in ms:
   y=X; k=1
   while True:
    z=multiply(n,y,X)
    if z==y:break
    y=z;k+=1
    assert k<=max(1,n//2)
   hist[k]=hist.get(k,0)+1
   if k==n//2:maxes.append(X)
  if n>=3:
   for i in range(1,n):
    for j in range(1,n):
     K=1+abs(i-j)//2;X=Xij(n,i,j)
     assert X in ms
     Y=X
     for k in range(1,K+1):
      assert Y==Xij(n,i,j,k),(n,i,j,k,Y,Xij(n,i,j,k))
      assert rank(n,Y)==n-2*k
      Y=multiply(n,Y,X)
     assert Y==Xij(n,i,j,K),(n,i,j,K,'not stationary')
  print(n,len(ms),hist,'maxcount',len(maxes))
  total+=len(ms)
 print('PASS',total)
