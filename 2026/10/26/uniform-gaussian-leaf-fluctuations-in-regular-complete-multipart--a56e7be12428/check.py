from fractions import Fraction
from itertools import combinations
from math import comb, exp

def formula(n,k):
 assert n % k==0 and n>=4 and 1<=k<=n//2
 r=n//k; d=n-k
 p=Fraction(n-1,n)**(r-2)*Fraction(d-1,d)**((r-1)*(k-1))
 s=Fraction(n-2,n)**(r-2)*Fraction(d-2,d)**((r-1)*(k-1))
 z=Fraction(n-2,n)**(r-2)*Fraction(d-1,d)**(2*(k-1))*Fraction(d-2,d)**((r-2)*(k-1))
 v=n*p*(1-p)+n*(k-1)*(s-p*p)+n*(n-k)*(z-p*p)
 return p,s,z,v

def enum(n,k):
 edges=[(u,v) for u in range(n) for v in range(u+1,n) if u//k!=v//k]
 nr=0;sl=sl2=0
 for subset in combinations(edges,n-1):
  par=list(range(n)); rank=[0]*n; degree=[0]*n
  def root(x):
   while par[x]!=x:x=par[x]
   return x
  good=True
  for x,y in subset:
   a,b=root(x),root(y)
   if a==b:good=False;break
   par[b]=a;degree[x]+=1;degree[y]+=1
  if not good:continue
  nr+=1;leaves=sum(d==1 for d in degree)
  sl+=leaves;sl2+=leaves*leaves
 p,s,z,v=formula(n,k)
 assert Fraction(sl,nr)==n*p,(n,k,'mean',Fraction(sl,nr),n*p)
 assert Fraction(sl2,nr)-Fraction(sl,nr)**2 ==v,(n,k,'var',Fraction(sl2,nr)-Fraction(sl,nr)**2,v)
 return nr,v
if __name__=='__main__':
 for n,k in [(4,1),(4,2),(5,1),(6,1),(6,2),(6,3),(7,1)]:
  print('verified',n,k,enum(n,k))
 target=exp(-1)-2*exp(-2)
 for n in [100,200,400,800]:
  for k in [1,2,n//2]:
   _,_,_,v=formula(n,k)
   print('asymptotic',n,k,round(float(v/n),10),'target',round(target,10))
 print('CHECK PASSED')
