"""Exact finite-index and A5 automorphism checks for cyclic group cellular automata."""
from itertools import permutations
from math import gcd

E=tuple(range(5))
def mul(a,b): return tuple(a[b[i]] for i in range(5))
def inv(a): return tuple(a.index(i) for i in range(5))
def powp(a,k):
 r=E
 for _ in range(k): r=mul(r,a)
 return r

def sgn(p):
 return (-1)**sum(p[i]>p[j] for i in range(5) for j in range(i+1,5))
A5=[p for p in permutations(range(5)) if sgn(p)==1]
assert len(A5)==60

def central(q):return sum(mul(q,a)==mul(a,q) for a in A5)

def cycles(pi):
 seen=set(); out=[]
 for i in range(len(pi)):
  if i in seen:continue
  c=[];j=i
  while j not in seen:
   seen.add(j);c.append(j);j=pi[j]
  assert j==i
  out.append(c)
 return out

def actual(N,pi,v,q,t):
 m=len(pi);pred=[0]*m
 for j,k in enumerate(pi):pred[k]=j
 def P(z):
  site,j=z;h=pred[j]
  return ((site+v[h])%N,h)
 def Pt(z):
  for _ in range(t):z=P(z)
  return z
 out=1;seen=set()
 for j in range(m):
  for n in range(N):
   z=(n,j)
   if z in seen:continue
   here=z; Q=E
   while here not in seen:
    seen.add(here)
    cur=here
    for _ in range(t):
     Q=mul(Q,q[pred[cur[1]]]);cur=P(cur)
    here=cur
   assert here==z
   out*=central(Q)
 return out

def predicted(N,pi,v,q,t):
 ans=1
 for cyc in cycles(pi):
  L=len(cyc); V=sum(v[j] for j in cyc)
  g=gcd(N,V); orbit_len=L*N//g;d=gcd(t,orbit_len)
  p={pi[j]:j for j in range(len(pi))}
  j=cyc[0]; Q=E
  for _ in range(L):
   h=p[j];Q=mul(Q,q[h]);j=h
  assert j==cyc[0]
  ans*=central(powp(Q,(N//g)*(t//d)))**(g*d)
 return ans

Q0=E
Q1=(1,0,2,3,4)    # An outer involution on A5.
Q2=(1,2,0,3,4)    # An inner automorphism of order 3.
Q3=(1,2,3,4,0)    # An inner automorphism of order 5.
Q4=(1,0,3,2,4)    # An inner involution.
Q=[Q0,Q1,Q2,Q3,Q4]
assert [central(x) for x in Q]==[60,6,3,5,4]
passed=0
for m in range(1,6):
 for k in range(3):
  pi=list(range(m))
  if k==0: pi=list(range(1,m))+[0] # single cycle
  elif k==1: pi=list(range(m))  # independent cycles
  else:
   pi=[(j+1)%m for j in range(m)]
   if m>=3:
    pi[0]=1;pi[1]=0
    for j in range(2,m-1):pi[j]=j+1
    pi[m-1]=2
  assert sorted(pi)==list(range(m))
  v=[((2*j+3*k+m)%5)-2 for j in range(m)]
  q=[Q[(j+2*k)%len(Q)] for j in range(m)]
  for N in range(1,9):
   for t in range(1,12):
    a=actual(N,pi,v,q,t);b=predicted(N,pi,v,q,t)
    assert a==b,(N,pi,v,q,t,a,b)
    passed+=1
for N in range(1,12):
 pi=[0];v=[1];q=[Q1]
 assert actual(N,pi,v,q,1)==(6 if N%2 else 60)
 assert actual(N,pi,v,q,2)==60**gcd(N,2)
print('A5_EXACT_RING_FIXED_POINT_FORMULA_PASS',passed)
print('A5_ODD_EVEN_TWISTED_SHIFT_PASS',11)
print('INFINITE_TOPOLOGICAL_CONJUGACY_AND_ARBITRARY_AUTOMORPHISMS_REQUIRE_PROOF')
