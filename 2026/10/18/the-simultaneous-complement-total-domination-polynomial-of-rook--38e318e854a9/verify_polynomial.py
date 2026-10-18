"""Independent enumeration of all SDCTD sets and the claimed polynomial on rook boards."""
from itertools import product
from math import comb


def mul(p,q):
 r=[0]*(len(p)+len(q)-1)
 for i,a in enumerate(p):
  for j,b in enumerate(q):r[i+j]+=a*b
 return r

def powp(p,n):
 r=[1]
 for _ in range(n):r=mul(r,p)
 return r

def add(p,q,factor=1):
 r=[0]*max(len(p),len(q))
 for i,a in enumerate(p):r[i]+=a
 for i,b in enumerate(q):r[i]+=factor*b
 return r

def xp(p,k): return [0]*k+p

def row(a,b):
 a0=[0]+[comb(b,k) for k in range(1,b+1)]
 if a==2:
  a0[1]=0
  return powp(a0,2)
 out=powp(a0,a)
 out=add(out,[0]*a+[b],-1)
 special=a0[:]
 special[1]-=1
 return add(out,[v*a*b for v in xp(special,a-1)],-1)

def formula(m,n):
 if m==n==2:return [0,0,0,0,1]
 # both-cover polynomial by inclusion exclusion
 E=[0]*(m*n+1)
 for i in range(m+1):
  for j in range(n+1):
   c=(-1)**(i+j)*comb(m,i)*comb(n,j)
   for k in range((m-i)*(n-j)+1): E[k]+=c*comb((m-i)*(n-j),k)
 return add(add(add(row(m,n),row(n,m)),E,-1),[0]*(m+n-2)+[m*n,m*n])

def brute(m,n):
 N=m*n
 closed=[sum(1<<(a*n+b) for a in range(m) for b in range(n) if a==i or b==j) for i in range(m) for j in range(n)]
 complement=[sum(1<<(a*n+b) for a in range(m) for b in range(n) if a!=i and b!=j) for i in range(m) for j in range(n)]
 counts=[0]*(N+1)
 for S in range(1<<N):
  if all(S&c for c in closed) and all(S&c for c in complement): counts[S.bit_count()]+=1
 return counts

def main():
 pairs=[(2,n) for n in range(2,8)]+[(3,n) for n in range(3,7)]+[(4,n) for n in range(4,6)]
 for m,n in pairs:
  f=formula(m,n);b=brute(m,n)
  f=f+[0]*(m*n+1-len(f))
  assert f==b,(m,n,f,b)
  print('Polynomial PASS',m,n,'all sets',sum(b),'degree',max((i for i,x in enumerate(b) if x),default=None))
 print('ALL PASS',len(pairs),'instances; all',sum(2**(m*n) for m,n in pairs),'vertex subsets classified.')

if __name__=='__main__':main()
