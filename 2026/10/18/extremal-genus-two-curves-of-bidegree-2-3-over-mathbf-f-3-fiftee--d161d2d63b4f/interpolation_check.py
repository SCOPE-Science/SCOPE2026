"""Independently enumerate maximal-point bidegree-(2,3) models via fiber interpolation."""
import itertools,collections
p=3
# Binary cubic basis S^3,S^2 T,S T^2,T^3 evaluated at rational base P1 points.
base=[(1,0),(0,1),(1,1),(2,1)]
E=[[pow(s,3-j,3)*pow(t,j,3)%3 for j in range(4)] for s,t in base]

def inverse(M):
 a=[row[:]+[int(i==j) for j in range(len(M))] for i,row in enumerate(M)]
 n=len(M)
 for j in range(n):
  k=next(k for k in range(j,n) if a[k][j]%3)
  a[k],a[j]=a[j],a[k]
  a[j]=[v*pow(a[j][j],-1,3)%3 for v in a[j]]
  for k in range(n):
   if k!=j:
    f=a[k][j];a[k]=[(u-f*v)%3 for u,v in zip(a[k],a[j])]
 return [row[n:] for row in a]
Einverse=inverse(E)

def split_quadratics():
 pts=[(1,0),(0,1),(1,1),(2,1)];L=[(b,-a%3) for a,b in pts]
 out=[]
 for i,j in itertools.combinations(range(4),2):
  a,b=L[i];c,d=L[j];q=((a*c)%3,(a*d+b*c)%3,(b*d)%3)
  out.extend((q,tuple(2*x%3 for x in q)))
 return out
split=split_quadratics(); assert len(set(split))==12
half=split[::2]

def disc(v):
 out=[0]*7
 for i in range(4):
  for j in range(4):out[6-i-j]=(out[6-i-j]+v[4+i]*v[4+j]-v[i]*v[8+j])%3
 return out

def trim(a):
 while a and a[-1]==0:a.pop()
 return a

def remainder(a,b):
 a=trim(a[:]);b=trim(b[:]);db=len(b)-1
 if db<0:raise ZeroDivisionError
 while len(a)-1>=db:
  f=a[-1]*pow(b[-1],-1,3)%3;k=len(a)-len(b)
  for j in range(len(b)):a[k+j]=(a[k+j]-f*b[j])%3
  a=trim(a)
 return a

def gcd(a,b):
 a=trim(a[:]);b=trim(b[:])
 while b:a,b=b,remainder(a,b)
 return a

def smooth(d):
 if d[6]==d[5]==0:return False
 deriv=[i*d[i]%3 for i in range(1,7)]
 return len(gcd(d,deriv))==1

def power_x_mod(n,f):
 t=[0,1];r=[1]
 while n:
  if n&1:r=remainder(poly_mul(r,t),f)
  t=remainder(poly_mul(t,t),f);n//=2
 return r

def poly_mul(a,b):
 c=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]=(c[i+j]+x*y)%3
 return trim(c)

def factor_type(d):
 # d[j] is coefficient S^j T^(6-j)
 f=trim(d[:]); assert len(f)==7 and f[-1]!=0
 a=power_x_mod(9,f);a[0]=(a[0]-0)%3
 if len(a)<=1:a+=[0]
 a[1]=(a[1]-1)%3
 e2=len(gcd(f,a))-1
 if e2==6:return '2+2+2'
 if e2==2:return '2+4'
 a=power_x_mod(27,f)
 if len(a)<=1:a+=[0]
 a[1]=(a[1]-1)%3
 e3=len(gcd(f,a))-1
 if e3==6:return '3+3'
 assert e2==0 and e3==0
 return '6'

stats=collections.Counter();survivors=[];candidates=0
for qs in itertools.product(split,repeat=3):
 for q0 in half:
  quadvals=[q0,*qs]
  coeff=[]
  for k in range(3):
   w=[quadvals[j][k] for j in range(4)]
   coeff += [sum(Einverse[i][j]*w[j] for j in range(4))%3 for i in range(4)]
  d=disc(coeff);candidates+=1
  if smooth(d):
   ty=factor_type(d);stats[ty]+=1;survivors.append(tuple(coeff))
print('fiber_candidates',candidates)
print('smooth',len(survivors))
print('branch_factor_types',dict(sorted(stats.items())))
assert candidates==10368 and len(survivors)==6096
assert dict(stats)=={'2+2+2':336,'2+4':1872,'6':3888}
