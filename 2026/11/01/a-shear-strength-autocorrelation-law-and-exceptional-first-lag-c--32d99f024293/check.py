from fractions import Fraction as F
from itertools import product
from math import factorial
from collections import Counter
from time import time

sq=[(F(0),F(0)),(F(1),F(0)),(F(1),F(1)),(F(0),F(1))]

def clip(poly,A,B,C): # keep A*x+B*y+C >= 0
 if not poly:return []
 out=[]
 for i,v in enumerate(poly):
  u=poly[i-1]
  fu=A*u[0]+B*u[1]+C; fv=A*v[0]+B*v[1]+C
  if (fu<0 and fv>0) or (fu>0 and fv<0):
   q=fu/(fu-fv);out.append((u[0]+q*(v[0]-u[0]),u[1]+q*(v[1]-u[1])))
  elif fu*fv==0 and ((fu<0 and fv==0) or (fu==0 and fv<0)):
   pass
  if fv>=0:out.append(v)
 # compact duplicate
 ans=[]
 for x in out:
  if not ans or x!=ans[-1]:ans.append(x)
 if len(ans)>1 and ans[0]==ans[-1]:ans.pop()
 return ans

def cellpoly(a,b,c,i,j):
 poly=sq
 for A,B,C in [(a,b,-i),(-a,-b,i+1),(b,c,-j),(-b,-c,j+1)]:
  poly=clip(poly,A,B,C)
  if len(poly)<3:return []
 return poly

parts=[]
for words in product(range(3),repeat=4):
 cnt=Counter(words)
 parts.append((words,factorial(cnt[0])*factorial(cnt[1])*factorial(cnt[2])))

def tr_eval(tr,a,b,c,i,j):
 v0,v1,v2=tr
 d=abs((v1[0]-v0[0])*(v2[1]-v0[1])-(v1[1]-v0[1])*(v2[0]-v0[0]))
 if not d:return F(0)
 vals=[[v[0]-F(1,2),v[1]-F(1,2),a*v[0]+b*v[1]-i-F(1,2),b*v[0]+c*v[1]-j-F(1,2)] for v in tr]
 res=F(0)
 for inds,f in parts:
  z=f
  for k,ind in enumerate(inds):z*=vals[ind][k]
  res+=z
 return d*res/F(720)

def compute(a,b,c):
 t=time();result=F(0);N=0
 for i in range(a+b):
  for j in range(b+c):
   poly=cellpoly(a,b,c,i,j)
   if not poly:continue
   for v in range(1,len(poly)-1):
    result+=tr_eval((poly[0],poly[v],poly[v+1]),a,b,c,i,j);N+=1
 print((a,b,c),'cells',N,'time',round(time()-t,3),'exact',result,'float',float(result), flush=True)

if __name__=='__main__':
    for k in range(1,15):
        a,b,c=k*k+1,k,1
        z=F(0)
        for i in range(a+b):
            for j in range(b+c):
                poly=cellpoly(a,b,c,i,j)
                if len(poly)>2:
                    for v in range(1,len(poly)-1):
                        z+=tr_eval((poly[0],poly[v],poly[v+1]),a,b,c,i,j)
        expected=-F((k*k-1)*(5*k*k+4),720*k*k*(k*k+1)**2)
        assert z==expected,(k,z,expected)
    a,b,c=5,3,2
    z=F(0); groups={}
    for i in range(a+b):
        for j in range(b+c):
            poly=cellpoly(a,b,c,i,j)
            if len(poly)>2:
                v=F(0)
                for h in range(1,len(poly)-1):
                    v+=tr_eval((poly[0],poly[h],poly[h+1]),a,b,c,i,j)
                if v:groups[(i,j)]=v
                z+=v
    assert z==-F(121,81000),(z,groups)
    assert sorted(Counter(groups.values()).values())==[4,4,4], groups
    print('PASS: 14 exact shear-strength integrals, two-lag exact integral, and 12 polygon-cell contributions')
