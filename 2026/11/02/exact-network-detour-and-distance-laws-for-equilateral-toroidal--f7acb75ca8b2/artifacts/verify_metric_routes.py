from fractions import Fraction as F
from collections import Counter
from itertools import product

def circ(x,y,n):
    d=abs(x-y)%n
    return min(d,n-d)

def pairs(m,n):
    out=[]
    for i,j in product(range(m),range(n)):
      out.append(('h',i,j, ((i,j),((i+1)%m,j))))
      out.append(('v',i,j, ((i,j),(i,(j+1)%n))))
    return out

def path_dist(e,f,s,t,m,n):
    a,b=e[3];c,d=f[3]
    dist=lambda a,b: circ(a[0],b[0],m)+circ(a[1],b[1],n)
    path=min(s+t+dist(a,c),s+1-t+dist(a,d),1-s+t+dist(b,c),2-s-t+dist(b,d))
    if e==f:
      path=min(path,abs(s-t))
    return path

def predicted(e,f,s,t,m,n):
    typ,i,j,_=e;typ2,k,l,_=f
    if typ!=typ2:
      if typ=='h':
        return circ(F(i)+s,F(k),m)+circ(F(j),F(l)+t,n)
      return circ(F(i),F(k)+t,m)+circ(F(j)+s,F(l),n)
    if typ=='h':
      if i==k and j!=l:
        return circ(j,l,n)+min(s+t,2-s-t)
      return circ(F(i)+s,F(k)+t,m)+circ(j,l,n)
    if j==l and i!=k:
      return circ(i,k,m)+min(s+t,2-s-t)
    return circ(i,k,m)+circ(F(j)+s,F(l)+t,n)

total=0
for m,n in product(range(3,7),repeat=2):
  ed=pairs(m,n)
  fractions=[F(1,7),F(1,3),F(2,5)]
  exceptional_pairs=sum(1 for e,f in product(ed,repeat=2) if e[0]==f[0] and ((e[0]=='h' and e[1]==f[1] and e[2]!=f[2]) or (e[0]=='v' and e[2]==f[2] and e[1]!=f[1])))
  assert F(exceptional_pairs,len(ed)**2)==F(m+n-2,4*m*n)
  for e,f,s,t in product(ed,ed,fractions,fractions):
    pred=predicted(e,f,s,t,m,n)
    tru=path_dist(e,f,s,t,m,n)
    assert pred==tru,(m,n,e[:3],f[:3],s,t,pred,tru)
    def point(edge,u):
      typ,i,j,_=edge
      return (F(i)+u,F(j)) if typ=='h' else (F(i),F(j)+u)
    ex=point(e,s);ey=point(f,t)
    ambient=circ(ex[0],ey[0],m)+circ(ex[1],ey[1],n)
    exceptional=e[0]==f[0] and ((e[0]=='h' and e[1]==f[1] and e[2]!=f[2]) or (e[0]=='v' and e[2]==f[2] and e[1]!=f[1]))
    detour=2*min(min(s,t),1-max(s,t)) if exceptional else F(0)
    assert tru-ambient==detour,(m,n,e[:3],f[:3],s,t,tru,ambient,detour)
    total+=1
print('PASS exact point distances',total)

def avg(m,n):
  sm=(m+n)*F(1,4)
  corr=F(m+n-2,12*m*n)
  if m%2: corr-=F(1,16*m)
  if n%2: corr-=F(1,16*n)
  return sm+corr
for m,n in product(range(3,21),repeat=2):
  shift=avg(m,n)-F(m+n,4)
  if shift<=0:print('nonpositive shift',m,n,shift)
