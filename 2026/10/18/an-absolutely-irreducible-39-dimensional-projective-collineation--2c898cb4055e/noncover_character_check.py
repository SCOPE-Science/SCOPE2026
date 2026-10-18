import itertools,collections,math,time
q=3
xyz=list(itertools.product(range(q),repeat=3))
def canon(v):
 for x in v:
  if x%3:
   t=x%3
   return tuple((z*t)%3 for z in v)
 return None
pts=sorted({canon(p) for p in xyz}-{None});idx={p:i for i,p in enumerate(pts)}; n=len(pts)
lines=[frozenset(i for i,p in enumerate(pts) if sum(x*y for x,y in zip(l,p))%3==0) for l in pts]
L=set(lines); faces={0}
for l in L:
 ys=[i for i in range(n) if i not in l]
 for k in range(1,len(ys)+1):
  for tup in itertools.combinations(ys,k): faces.add(sum(1<<j for j in tup))
assert len(faces)==3862

def cycle_orbits(p):
 out=[];unseen=set(range(n))
 while unseen:
  x=min(unseen); c=[]
  while x in unseen:
   unseen.remove(x);c.append(x);x=p[x]
  out.append(tuple(c))
 return out

def char(p):
 cyc=cycle_orbits(p)
 part=[(sum(1<<i for i in c),len(c)) for c in cyc]
 # signed reduced Lefschetz, plus trivial H5 action -> H4=L+1
 L=-1 # reduced: subtract empty vertex
 for bs in range(1,1<<len(cyc)):
  mask=0;length=0;nc=0
  for j,(partmask,csize) in enumerate(part):
   if bs>>j &1:
    mask|=partmask;length+=csize;nc+=1
  if mask in faces:
   sign=(-1)**(length-nc)
   L+=(-1)**(length-1)*sign
 return L+1

def determinant(a):
 a,b,c,d,e,f,g,h,i=a
 return (a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g))%3
C=collections.Counter(); occ=collections.Counter(); st=time.monotonic();chars=[];seen=set()
for a in itertools.product(range(3),repeat=9):
 if not determinant(a):continue
 if canon(a)!=a:continue
 p=tuple(idx[canon(tuple(sum(a[i*3+j]*v[j] for j in range(3))%3 for i in range(3)))] for v in pts)
 assert p not in seen;seen.add(p)
 ch=char(p);chars.append(ch)
 typ=tuple(sorted((len(c) for c in cycle_orbits(p)),reverse=True))
 occ[(typ,ch)]+=1
assert len(chars)==5616
assert sum(chars)==0 and sum(t*t for t in chars)==5616
assert occ=={((1,)*13,39):1,((2,)*4+(1,)*5,-1):117,((3,)*3+(1,)*4,3):104,((3,)*4+(1,),0):624,((4,)*2+(2,)*2+(1,),-1):702,((6,)+(3,)+(2,)+(1,)*2,-1):936,((8,4,1),1):1404,((13,),0):1728}
print('size',len(chars),'values',collections.Counter(chars))
print('group invariants',sum(chars)//len(chars),'character norm',sum(t*t for t in chars)/len(chars))
for (typ,ch),cnt in sorted(occ.items(),key=lambda z:(-sum(z[0][0]),z[0][0],z[0][1])):
 print('cycle',typ,'H4trace',ch,'number',cnt)
