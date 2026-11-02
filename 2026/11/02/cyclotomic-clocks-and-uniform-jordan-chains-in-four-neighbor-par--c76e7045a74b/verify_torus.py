"""Direct bit-matrix checks of finite-field torus neighbor-sum dynamics.
Reproducibility: Python 3 standard library, python verify_torus.py.
"""
from math import gcd
from itertools import product


def matmul(A,B):
  out=[]
  for row in A:
    z=0
    while row:
      b=row & -row
      z^=B[b.bit_length()-1]
      row-=b
    out.append(z)
  return out

def mpow(A,k):
  n=len(A);out=[1<<i for i in range(n)]
  while k:
    if k&1:out=matmul(out,A)
    k>>=1
    if k:A=matmul(A,A)
  return out

def rank(A):
  piv={}
  for v in A:
    while v:
      i=v.bit_length()-1
      if i in piv:v^=piv[i]
      else:
        piv[i]=v;break
  return len(piv)

def poly_rem(a,b):
  deg=b.bit_length()-1
  while a and a.bit_length()-1>=deg:
    a ^= b << (a.bit_length()-1-deg)
  return a

def poly_gcd(a,b):
  while b:
    a,b=b,poly_rem(a,b)
  return a

def plus1pow(k):
  p=1;j=0
  while k:
    if k&1:p^=p<< (1<<j)
    j+=1;k>>=1
  return p

def rootcount(m,u):
  assert m%2 and u%2
  rootpol=(1<<m)-1
  poly=plus1pow(2*u)^(1<<u)
  return poly_gcd(rootpol,poly).bit_length()-1

def formula(a,b,m,t):
  M=2**a; d=2**b;P=M//2;H=max(P,d)
  C=2*min(M,d);L=max(M,d)//2
  R=2*min(P,d)*min(H,t & -t)*rootcount(m,t//(t&-t))
  return C*min(t,L),R

def torus(M,N):
  A=[]
  for x in range(M):
    for y in range(N):
      row=0
      for u,v in [((x-1)%M,y),((x+1)%M,y),(x,(y-1)%N),(x,(y+1)%N)]:
        row^=1 << (u*N+v)
      A.append(row)
  return A

def test_matrix(a,b,m,times):
  M=2**a;N=m*2**b;A=torus(M,N);n=M*N
  for t in times:
    ak=mpow(A,t)
    null=n-rank(ak)
    R=n-rank([ak[i]^(1<<i) for i in range(n)])
    pn,pr=formula(a,b,m,t)
    assert null==pn,(a,b,m,t,'nil',null,pn)
    assert R==pr,(a,b,m,t,'fix',R,pr)
  return len(times)

def state_step(x,rows):
  y=0
  for i,mask in enumerate(rows):
    if (x&mask).bit_count()&1:y |=1<<i
  return y

def enumerate_states(a,b,m):
  M=2**a;N=m*(2**b);s=M*N
  assert s<=20
  rows=torus(M,N)
  counts={}
  for x in range(1<<s):
    seen={};y=x
    while y not in seen:
      seen[y]=len(seen)
      y=state_step(y,rows)
    pre=seen[y]; period=len(seen)-pre
    counts[pre,period]=counts.get((pre,period),0)+1
  C=2*min(M,2**b);L=max(M,2**b)//2
  periods=set(p for _,p in counts)
  for p in periods:
    def divisors(n):return [d for d in range(1,n+1) if n%d==0]
    def mobius(n):
      i=2;number=0
      while i*i<=n:
        if n%i==0:
          n//=i;number+=1
          if n%i==0:return 0
          while n%i==0:n//=i
        i+=1
      if n>1:number+=1
      return -1 if number%2 else 1
    primitive=sum(mobius(p//d)*(1<<formula(a,b,m,d)[1]) for d in divisors(p))
    for t in range(L+1):
      shell=(1<<C*t)-(1<<C*(t-1)) if t else 1
      assert counts.get((t,p),0)==shell*primitive,(a,b,m,t,p,counts.get((t,p),0),shell*primitive)
  assert sum(counts.values())==1<<s
  return counts

def run():
  # These cases are small enough to verify quickly by exact GF(2) elimination.
  cases=[(2,0,3),(2,0,5),(2,0,7),(2,0,9),(2,0,11),
         (2,1,3),(2,1,5),(2,1,7),(2,2,3),
         (3,0,3),(3,0,5),(3,0,7),(3,1,3),(3,1,5),
         (4,0,3),(4,0,5)]
  tests=0
  for a,b,m in cases:
    M=2**a;N=m*(2**b)
    times=[1,2,3,4,5,6,7,8,9,10,12,14,16,21]
    tests+=test_matrix(a,b,m,times)
    print('matrix',M,N,'checked',len(times),flush=True)
  counts=enumerate_states(2,0,3)
  print('exhaustive_4x3', sorted(counts.items()))
  print('all_good',tests,'matrix rank/fixed checks',sum(counts.values()),'full state trajectories')

if __name__=='__main__':run()
