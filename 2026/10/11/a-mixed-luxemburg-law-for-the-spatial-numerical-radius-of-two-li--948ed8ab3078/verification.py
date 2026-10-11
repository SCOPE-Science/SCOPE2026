import math,random

def radius(a,b,p):
 q=p/(p-1); k=(p-1)**(1/q)/p
 if a==0 and b==0:return 0.
 lo=0.; hi=max(a,b)*10+1
 for _ in range(220):
  mid=(lo+hi)/2
  h=(k*a/mid)**p+(k*b/mid)**q
  if h>1:lo=mid
  else: hi=mid
 return (lo+hi)/2

def witness(a,b,p):
 W=radius(a,b,p)
 if not a or not b:return None
 u=(p-1)*a/(p*W);v=(b/(p*W))**(1/(p-1))
 den=(1+u**p+v**p)**(1/p)
 x,y,z=u/den,1/den,v/den
 return x,y,z

rng=random.Random(24017); count=0
for p in [1.1,1.2,1.3333333333333,1.5,1.75,2.,2.5,3.,4.,6.,8.,15.]:
 for a,b in [(1.,1.),(0.1,1.),(1.,0.1),(2.,1.),(1.,2.),(0.2,0.6),(3.,4.)]:
  W=radius(a,b,p); x,y,z=witness(a,b,p)
  achieved=a*x**(p-1)*y+b*y**(p-1)*z
  assert abs(achieved-W)<1e-10*(1+W),(p,a,b,achieved,W)
  count+=1
  q=p/(p-1)
  assert abs(W-radius(b,a,q))<1e-10*(1+W)
  count+=1
  for _ in range(30):
   vals=[rng.random()+1e-9 for i in range(3)]
   norm=sum(t**p for t in vals)**(1/p)
   xx,yy,zz=[t/norm for t in vals]
   candidate=a*xx**(p-1)*yy+b*yy**(p-1)*zz
   assert candidate < W+1e-9
   count+=1
for a,b in [(2.,1.),(3.,1.),(4.,3.),(1.01,1.),(10.,1.),(100.,1.)]:
 assert radius(a,b,4.)>radius(b,a,4.)+1e-12
 count+=1
print('successful checks',count)
print('p4 W(2,1)',radius(2,1,4),'W(1,2)',radius(1,2,4))
