"""Independent exhaustive and formal-series verification for paired domination of rook graphs.
Python 3 standard library only. The two computations use different descriptions.
"""
from math import factorial, comb
from fractions import Fraction
from functools import lru_cache

# A small polynomial is a map exponent -> rational coefficient.
def add(a,b,scale=1):
 c=a.copy()
 for d,v in b.items():
  c[d]=c.get(d,0)+scale*v
 return {d:v for d,v in c.items() if v}
def mul(a,b):
 c={}
 for i,x in a.items():
  for j,y in b.items():c[i+j]=c.get(i+j,0)+x*y
 return {d:v for d,v in c.items() if v}
def conv(A,B,m,n):
 return addmany(mul(A.get((i,j),{}), B.get((m-i,n-j),{}))
                for i in range(m+1) for j in range(n+1))
def addmany(items):
 c={}
 for p in items:c=add(c,p)
 return c

def egf_coefficients(M,N):
 plus={};minus={}
 for i in range(M+1):
  for j in range(N+1):
   den=factorial(i)*factorial(j)
   plus[i,j]={k:Fraction(comb(i*j,k),den) for k in range(i*j+1)}
   minus[i,j]={k:Fraction((-1)**k*comb(i*j,k),den) for k in range(i*j+1)}
 F={(i,j):conv(plus,minus,i,j) for i in range(M+1) for j in range(N+1)}
 B={(0,0):{0:Fraction(1)}}
 for d in range(1,M+N+1):
  for i in range(M+1):
   j=d-i
   if j<0 or j>N:continue
   other=addmany(mul(B[a,b],B[i-a,j-b])
      for a in range(i+1) for b in range(j+1)
      if (a,b)!=(0,0) and (a,b)!=(i,j))
   B[i,j]={k:v/2 for k,v in add(F[i,j],other,-1).items()}
 out={}
 for m in range(1,M+1):
  for n in range(1,N+1):
   p=B[m,n].copy()
   for a in range(1,m+1):
    for b in range(1,n+1):
     p=add(p,B[m-a,n-b],-Fraction((-1)**(a+b),factorial(a)*factorial(b)))
   p={k:int(v*factorial(m)*factorial(n)) for k,v in p.items() if v}
   for k,v in p.items():
    assert v>=0 and v==int(v)
   out[m,n]=p
 return out

def brute(m,n):
 V=[(i,j) for i in range(m) for j in range(n)];N=len(V)
 adj=[sum(1<<b for b,(k,l) in enumerate(V) if a!=b and (i==k or j==l))
     for a,(i,j) in enumerate(V)]
 @lru_cache(None)
 def pm(S):
  if S==0:return True
  if S.bit_count()%2:return False
  v=(S&-S).bit_length()-1
  rest=S^(1<<v)
  nei=adj[v]&rest
  while nei:
   one=nei&-nei;nei-=one
   if pm(rest^one):return True
  return False
 counts={}
 for S in range(1<<N):
  size=S.bit_count()
  if size%2 or size==0:continue
  # A vertex selected is dominated for closed domination; only nonselected need a neighbor.
  if any(not (S>>v&1) and not (adj[v]&S) for v in range(N)):continue
  if pm(S):counts[size]=counts.get(size,0)+1
 return counts

def main():
 M=N=4
 e=egf_coefficients(M,N)
 total=0
 for m in range(1,M+1):
  for n in range(1,N+1):
   b=brute(m,n);f=e[m,n]
   if b!=f:raise AssertionError((m,n,b,f))
   total+=sum(b.values())
   expected=2*((min(m,n)+1)//2) if max(m,n)>1 else None
   assert min(b) == expected if expected is not None else not b
   print(f'{m}x{n}: {f}')
 print(f'VERIFY_OK 16 boards 2^16-largest exhaustive subset search; {total} paired dominating sets checked against formal coefficient identity')
if __name__=='__main__':main()
