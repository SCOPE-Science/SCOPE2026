from itertools import combinations
from collections import Counter

def rank(rows):
 p={}
 for v in rows:
  while v:
   k=v.bit_length()-1
   if k in p:v^=p[k]
   else:p[k]=v;break
 return len(p)

def tables(d):
 pairs=list(combinations(range(d),2));trs=list(combinations(range(d),3));qds=list(combinations(range(d),4));
 wt=[];wq=[]
 for pair in pairs:
  b=(1<<pair[0])|(1<<pair[1]); wt0=[];wq0=[]
  for i in range(d):
   s=b|(1<<i)
   wt0.append((1<<trs.index(tuple(k for k in range(d) if (s>>k)&1))) if s.bit_count()==3 else 0)
  for i,j in pairs:
   s=b|(1<<i)|(1<<j)
   wq0.append((1<<qds.index(tuple(k for k in range(d) if (s>>k)&1))) if s.bit_count()==4 else 0)
  wt.append(wt0);wq.append(wq0)
 T=[];Q=[]
 for x in range(1<<len(pairs)):
  ti=[0]*d;qi=[0]*len(pairs)
  for k in range(len(pairs)):
   if x>>k&1:
    for i in range(d):ti[i]^=wt[k][i]
    for i in range(len(pairs)):qi[i]^=wq[k][i]
  T.append(ti);Q.append(qi)
 return T,Q


def gaussian(n,r,q):
 if r<0 or r>n:return 0
 num=1;den=1
 for j in range(1,r+1):num*=q**(n-j+1)-1;den*=q**j-1
 return num//den

def predicted(q):
 C3=gaussian(5,3,q)*gaussian(3,2,q)
 C4=gaussian(5,4,q)*(gaussian(6,2,q)-gaussian(4,3,q)*gaussian(3,2,q))
 C51=gaussian(5,2,q)*(gaussian(9,1,q)-gaussian(3,1,q)*gaussian(5,1,q)+q*gaussian(3,1,q)*gaussian(2,1,q))
 C50=gaussian(10,2,q)-C3-C4-C51
 assert C50==q*(q-1)*C51
 return C3,C4,C51,C50

def run_binary_census():
 d=5;n=10;T,Q=tables(d);pairs=list(combinations(range(d),2))
 Ar=[];supp=[]
 for x in range(1<<n):
  rows=[0]*d
  for j,(a,b) in enumerate(pairs):
   if x>>j&1:rows[a]^=1<<b;rows[b]^=1<<a
  Ar.append(rank(rows));supp.append(rows)
 H=Counter()
 for i in range(n):
  for j in range(i+1,n):
   f1=[k for k in range(i+1,n) if k!=j];f2=list(range(j+1,n))
   for a in range(1<<len(f1)):
    x=(1<<i)|sum(1<<k for z,k in enumerate(f1) if a>>z&1)
    for b in range(1<<len(f2)):
     y=(1<<j)|sum(1<<k for z,k in enumerate(f2) if b>>z&1)
     profile=(10-rank(T[x]+T[y]),5-rank(Q[x]+Q[y]))
     s=rank(supp[x]+supp[y]);n2=sum(Ar[z]==2 for z in (x,y,x^y))
     expected={(5,1):(3,3),(4,0):(4,n2),(2,0):(5,1),(1,0):(5,0)}
     assert (s,n2)==expected[profile],(profile,s,n2)
     H[profile]+=1
 actual=tuple(H[z] for z in ((5,1),(4,0),(2,0),(1,0)))
 expected=predicted(2)
 assert actual==expected,(actual,expected)
 assert sum(actual)==174251
 print('EXHAUSTIVE_BINARY_PASS',actual)

if __name__=='__main__':
 for q in (2,3,4,5,7):
  print('q',q,'C3 C4 C51 C50',predicted(q))
 run_binary_census()
