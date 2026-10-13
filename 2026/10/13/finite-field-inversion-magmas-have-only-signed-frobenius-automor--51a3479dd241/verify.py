import itertools,math

def field(p,k,poly):
 q=p**k
 def digits(x):return [(x//p**i)%p for i in range(k)]
 def enc(xx):return sum((a%p)*(p**i) for i,a in enumerate(xx))
 def add(a,b):return enc([(x+y)%p for x,y in zip(digits(a),digits(b))])
 def neg(a):return enc([-x for x in digits(a)])
 def sub(a,b):return add(a,neg(b))
 def mul(a,b):
  cc=[0]*(2*k-1)
  for i,x in enumerate(digits(a)):
   for j,y in enumerate(digits(b)):cc[i+j]=(cc[i+j]+x*y)%p
  for i in range(2*k-2,k-1,-1):
   t=cc[i]
   for j in range(k):cc[i-k+j]=(cc[i-k+j]-t*poly[j])%p
  return enc(cc[:k])
 def pw(a,n):
  r=1
  while n:
   if n&1:r=mul(r,a)
   a=mul(a,a);n//=2
  return r
 inv=lambda a:pw(a,q-2) if a else 0
 op=lambda x,y:sub(inv(sub(y,x)),inv(neg(x)))
 return q,add,sub,mul,pw,inv,op

for p,k,poly in [(2,1,[1]),(3,1,[1]),(2,2,[1,1]),(5,1,[1]),(7,1,[1]),(2,3,[1,1,0]),(3,2,[1,0]),(2,4,[1,1,0,0])]:
 q,add,sub,mul,pw,inv,op=field(p,k,poly)
 print('checking q=',q)
 assert all(mul(x,inv(x))==1 for x in range(1,q))
 table=[[op(x,y) for y in range(q)] for x in range(q)]
 expected=[]
 for i in range(k):
  frob=lambda x:pw(x,p**i)
  for c in ({1} if p==2 else {1,p-1}):
   fc=lambda x:mul(c,frob(x))
   tup=tuple(fc(x) for x in range(q))
   assert all(tup[table[x][y]]==table[tup[x]][tup[y]] for x in range(q) for y in range(q))
   expected.append(tup)
 assert len(set(expected))==len(expected)==k*(1 if p==2 else 2)
 if q<=9:
  autos=[]
  for tail in itertools.permutations(range(1,q)):
   f=(0,)+tail
   if all(f[table[x][y]]==table[f[x]][f[y]] for x in range(q) for y in range(q)):
    autos.append(f)
  assert set(autos)==set(expected),('auto',q,len(autos),len(expected))
  print(' exhaustive_automorphisms',len(autos))
 s=[u for u in range(q) if all(sub(inv(add(t,u)),inv(t))==inv(u) for t in range(q))]
 if q>=5:assert s==[0],(q,s)
 else:assert len(s)==q
 print(' socle_size',len(s))
 # repair lemma: for each y!=0, good ratios recover pair rule (when root excluded)
 for y in range(1,q):
  for x in range(q):
   ratio=mul(x,inv(y))
   B=mul(ratio,sub(1,ratio))==1
   if not B and x not in (0,y):
    fib={z for z in range(q) if table[z][y]==table[x][y]}
    assert fib=={x,sub(y,x)},('fib',q,y,x,fib)
 if q>=7:
  B={r for r in range(q) if mul(r,sub(1,r))==1}
  for u in range(1,q):
   for v in range(1,q):
    zs=[]
    for z in range(q):
     firsts=[(v,z),(u,sub(v,z)),(add(sub(u,v),z),z)]
     if all(a==0 or mul(b,inv(a)) not in B for a,b in firsts):zs.append(z)
    assert zs,('repair none',q,u,v)
 print(' fiber_and_repair_checks_OK')
print('VERIFY_OK')
