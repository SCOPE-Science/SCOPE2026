from math import comb

def add(a,b):
 if len(a)<len(b):a,b=b,a
 c=a.copy()
 for i,v in enumerate(b):c[i]+=v
 while c and not c[-1]:c.pop()
 return c

def mul(a,d,e):
 if not a:return []
 z=[0]*(len(a)+d*e)
 for j in range(e+1):
  m=comb(e,j)
  for i,v in enumerate(a):
   if v:z[i+d*j]+=v*m
 while z and not z[-1]:z.pop()
 return z

def div(a,d):
 if not a:return []
 z=[0]*len(a)
 for i,v in enumerate(a):z[i]=v-(z[i-d] if i>=d else 0)
 while z and not z[-1]:z.pop()
 assert len(z)==len(a)-d
 return z

def binary_num(n):
 prev=[[1]]+[[] for _ in range(n)]
 ds=[];i=1
 while i<=n:ds.append(i);i*=2
 for d in reversed(ds):
  row=[]; e=n//d
  for r in range(n+1):
   c=mul(prev[r],d,e)
   if r>=d:c=add(c,div(row[r-d],d))
   row.append(c)
  prev=row
 return prev[n]


def mul2(a,b):
 c=0
 while a:
  j=(a&-a).bit_length()-1
  c^=b<<j
  a&=a-1
 return c

def ypower(e):
 q=1;p=3
 while e:
  if e&1:q=mul2(q,p)
  p=mul2(p,p);e>>=1
 return q

def B(n):
 a=[0]*(n+1);a[0]=1
 d=1
 while d<=n:
  for j in range(d,n+1):a[j]+=a[j-d]
  d*=2
 return a[n]

def check():
 for n in range(2,101):
  e=n-(n%2);t=0;v=e
  while not v%2:t+=1;v//=2
  d=sum((1<<k)*(n//(1<<k)) for k in range(1,n.bit_length()+1))
  c=(B(e)//2)&1
  q=c*ypower(1<<t)
  for j in range(t):q^=mul2(1<<(1<<j),ypower((1<<t)-(1<<(j+1))))
  expected=mul2(ypower(d-(1<<t)),q)
  coeffs=binary_num(n)
  assert all(v%2==0 for v in coeffs),n
  observed=sum(1<<j for j,v in enumerate(coeffs) if (v//2)%2)
  assert expected==observed,n
  assert (q.bit_count()&1)==1,n
  assert coeffs[1]%4==2,n
 print('PASS: all coefficients and exact modular-root multiplicity, n=2..100')

if __name__=='__main__':check()
