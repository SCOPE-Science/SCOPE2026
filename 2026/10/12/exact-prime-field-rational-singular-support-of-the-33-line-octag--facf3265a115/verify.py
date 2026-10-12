from collections import Counter,defaultdict
from itertools import combinations
from functools import reduce
from math import gcd
# encoding a+b*r, r^2=2
R=lambda a=0,b=0:(a,b)
def add(x,y):return x[0]+y[0],x[1]+y[1]
def neg(x):return -x[0],-x[1]
def sub(x,y):return add(x,neg(y))
def mul(x,y):return x[0]*y[0]+2*x[1]*y[1],x[0]*y[1]+x[1]*y[0]
def norm(x):return x[0]**2-2*x[1]**2
def det3(x,y,z):return sub(add(mul(x[0],sub(mul(y[1],z[2]),mul(y[2],z[1]))),mul(x[1],sub(mul(y[2],z[0]),mul(y[0],z[2])))),mul(x[2],sub(mul(y[1],z[0]),mul(y[0],z[1]))))
def xyz(*a):return tuple(R(*v) if isinstance(v,tuple) else R(v) for v in a)
# triples (x,y,z) as ints or (a,b); all according to paper
L=[
xyz(1,(1,-1),-1), #1
xyz(1,(1,1),(-3,-2)), #2
xyz(1,1,0), #3
xyz(1,(-1,-1),0), #4
xyz(1,(1,-1),0), #5
xyz(1,(-1,1),(1,1)), #6
xyz(0,1,0), #7
xyz(1,(1,-1),(-1,-1)), #8
xyz(1,(-1,1),(-1,1)), #9
xyz(1,(1,1),-1), #10
xyz(1,(1,1),1), #11
xyz(1,(1,1),(-1,-1)), #12
xyz(1,(-1,1),-1), #13
xyz(1,(-1,-1),(-1,-1)), #14
xyz(1,(1,1),(3,2)), #15
xyz(1,(-1,1),(-1,-1)), #16
xyz(1,(-1,-1),(-3,-2)), #17
xyz(1,(-1,-1),1), #18
xyz(1,(1,-1),(-1,1)), #19
xyz(1,(-1,-1),(1,1)), #20
xyz(1,(-1,1),1), #21
xyz(1,(1,-1),1), #22
xyz(1,0,0), #23
xyz(1,(1,1),(1,1)), #24
xyz(1,(-1,1),0), #25
xyz(1,(1,1),0), #26
xyz(1,(1,-1),(1,-1)), #27
xyz(1,(-1,-1),-1), #28
xyz(1,-1,0), #29
xyz(1,(-1,1),(1,-1)), #30
xyz(0,0,1), #31
xyz(1,(1,-1),(1,1)), #32
xyz(1,(-1,-1),(3,2))] #33
assert len(L)==33

def factor(n):
 n=abs(n);d=2;out=[]
 while d*d<=n:
  if n%d==0:
   out.append(d)
   while n%d==0:n//=d
  d+=1
 if n>1:out.append(n)
 return out
def crossk(a,b):return (sub(mul(a[1],b[2]),mul(a[2],b[1])),sub(mul(a[2],b[0]),mul(a[0],b[2])),sub(mul(a[0],b[1]),mul(a[1],b[0])))
def dotk(a,b):return add(add(mul(a[0],b[0]),mul(a[1],b[1])),mul(a[2],b[2]))
def sg(a):return a[0],-a[1]
def ff(p):
 rt=next((r for r in range(p) if r*r%p==2%p),None)
 if rt is not None:
  def m(a,b):return a*b%p
  def c(q):return (q[0]+q[1]*rt)%p
  z=0;o=1
  def negg(a):return -a%p
  def addg(a,b):return (a+b)%p
  def invg(a):return pow(a,p-2,p)
  def fmt(a):return a
 else:
  def m(a,b):return ((a[0]*b[0]+2*a[1]*b[1])%p,(a[0]*b[1]+a[1]*b[0])%p)
  def c(q):return (q[0]%p,q[1]%p)
  z=(0,0);o=(1,0)
  def negg(a):return ((-a[0])%p,(-a[1])%p)
  def addg(a,b):return ((a[0]+b[0])%p,(a[1]+b[1])%p)
  def invg(a):
   t=pow((a[0]*a[0]-2*a[1]*a[1])%p,p-2,p)
   return ((a[0]*t)%p,(-a[1]*t)%p)
  def fmt(a):return a
 def subg(a,b):return addg(a,negg(b))
 def cross(a,b):return (subg(m(a[1],b[2]),m(a[2],b[1])),subg(m(a[2],b[0]),m(a[0],b[2])),subg(m(a[0],b[1]),m(a[1],b[0])))
 def normp(v):
  for x in v:
   if x!=z:
    inv=invg(x);return tuple(m(t,inv) for t in v)
  return None
 lines=[normp(tuple(c(t) for t in a)) for a in L]
 linecounts=Counter(lines)
 points=defaultdict(set)
 for i,j in combinations(range(len(lines)),2):
  if lines[i]!=lines[j]:
   P=normp(cross(lines[i],lines[j]));points[P].add(i);points[P].add(j)
 return rt, lines, linecounts,points

# All computations in Z[sqrt(2)] or in the indicated finite field.
def verify():
    assert len(L)==33
    pair_support=set()
    for i,j in combinations(range(33),2):
        vec=crossk(L[i],L[j])
        n=reduce(gcd,(abs(norm(u)) for u in vec))
        assert n!=0
        pair_support.update(factor(n))
    assert pair_support=={2}

    triple_support=set()
    triples_zero=0
    for i,j,k in combinations(range(33),3):
        a=det3(L[i],L[j],L[k]);n=norm(a)
        if n==0:
            assert a==(0,0)
            triples_zero+=1
        else:triple_support.update(factor(n))
    assert triples_zero==480 and triple_support=={2,3,7}

    points={}
    for i,j in combinations(range(33),2):
        v=crossk(L[i],L[j]); ids=tuple(k for k in range(33) if dotk(L[k],v)==(0,0))
        points.setdefault(ids,v)
    assert len(points)==169
    assert Counter(map(len,points))=={2:108,3:40,5:16,8:5}

    rational={}
    exceptional_support=set()
    for ids,v in points.items():
        w=tuple(sg(x) for x in v)
        c=crossk(v,w)
        if all(x==(0,0) for x in c):rational[ids]=v
        else:
            n=reduce(gcd,(abs(norm(x)) for x in c))
            assert n!=0
            exceptional_support.update(factor(n))
    assert len(rational)==9 and exceptional_support=={2,3}
    standard=[(1,0,0),(0,1,0),(0,0,1),(1,1,0),(1,-1,0),
              (1,0,1),(1,0,-1),(0,1,1),(0,1,-1)]
    for v in rational.values():
        assert any(all(t==(0,0) for t in crossk(v,tuple(R(x) for x in z))) for z in standard)

    for p,expected in [(2,(5,6,6)),(3,(33,89,13)),(7,(33,57,57)),
                       (5,(33,169,9)),(11,(33,169,9)),(17,(33,169,169)),
                       (23,(33,169,169))]:
        root,lines,linecount,pts=ff(p)
        rational_count=sum(root is not None or all(c[1]==0 for c in point) for point in pts)
        assert (len(linecount),len(pts),rational_count)==expected,(p,len(linecount),len(pts),rational_count)
        if p==3:assert Counter(map(len,pts.values()))=={2:12,3:40,4:16,5:16,8:5}
        if p==7:assert Counter(map(len,pts.values()))=={2:4,4:24,5:24,8:5}
    print('VERIFY_OK: 33 source lines; pair and triple norm primes; 169 geometric points; nine rational over Q; all exceptional and sampled finite-field counts')

if __name__=='__main__':verify()
