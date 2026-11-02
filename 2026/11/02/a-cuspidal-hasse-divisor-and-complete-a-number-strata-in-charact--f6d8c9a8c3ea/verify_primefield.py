#!/usr/bin/env python3
"""Independent finite-field replay: f^3 coefficients, exact rank, gcd(f,f') over F7."""
import itertools
P=7

def trim(v):
 while len(v)>1 and v[-1]%P==0:v.pop()
 return v

def mul(u,v):
 w=[0]*(len(u)+len(v)-1)
 for i,a in enumerate(u):
  for j,b in enumerate(v):w[i+j]=(w[i+j]+a*b)%P
 return trim(w)

def rem(u,v):
 u=trim(u[:]);v=trim(v[:]); assert v[-1]
 while len(u)>=len(v) and any(u):
  z=u[-1]*pow(v[-1],-1,P)%P;off=len(u)-len(v)
  for j,coef in enumerate(v):u[off+j]=(u[off+j]-z*coef)%P
  trim(u)
 return u

def gcd(u,v):
 while any(v):u,v=v,rem(u,v)
 return trim(u)

def rank(M):
 M=[row[:] for row in M];n=len(M);r=0
 for j in range(n):
  pivot=next((i for i in range(r,n) if M[i][j]%P),None)
  if pivot is None:continue
  M[r],M[pivot]=M[pivot],M[r]
  u=pow(M[r][j],-1,P);M[r]=[(x*u)%P for x in M[r]]
  for k in range(n):
   if k!=r:
    z=M[k][j];M[k]=[(x-z*y)%P for x,y in zip(M[k],M[r])]
  r+=1
 return r

counts={'ordinary':0,'a1':0,'a2':0,'singular':0}
representatives={}
for a,b,c in itertools.product(range(P),repeat=3):
 f=[0]*12; f[1]=b;f[3]=c;f[6]=a;f[11]=1
 df=[(i*coef)%P for i,coef in enumerate(f)][1:]
 if len(gcd(f,df))>1:
  counts['singular']+=1
  continue
 f2=mul(f,f);f3=mul(f2,f)
 H=[[f3[7*(i+1)-(j+1)] if 7*(i+1)-(j+1)<len(f3) else 0 for j in range(5)] for i in range(5)]
 actual=5-rank(H)
 F=(2*pow(c,5,P)+b*(a*a-b)*(a*a+b)**2)%P
 predicted=2 if c==0 and (a*a+b)%P==0 else (1 if a==0 or F==0 else 0)
 assert actual==predicted,(a,b,c,actual,predicted,F,H)
 key='ordinary' if actual==0 else 'a'+str(actual)
 counts[key]+=1
 representatives.setdefault(key,(a,b,c))
assert counts['a2']>0 and counts['a1']>0 and counts['ordinary']>0
print('GF7_EXHAUSTIVE_343_CUSP_STRATA_OK',counts,representatives)
