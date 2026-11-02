from collections import Counter
from itertools import product

def expected_pal(a,b,k):
 p=a+b
 if k%2: R0=R1=(k-1)//2*p
 else: R0=(k//2-1)*p+b;R1=(k//2-1)*p+a
 left0=('1'*b+'0'*a)*(R0//p+2)
 left1=('0'*a+'1'*b)*(R1//p+2)
 return {''}|{'0'*i for i in range(1,a+1)}|{'1'*i for i in range(1,b+1)}|{left0[:t][::-1]+'0'*a+left0[:t] for t in range(1,R0+1)}|{left1[:t][::-1]+'1'*b+left1[:t] for t in range(1,R1+1)}

def expected_mapw(P):
 return {ch+s+ch for s in P for ch in '01' if ch+s+ch not in P}

def direct_pal(W):
 return {''}|{W[i:j] for i in range(len(W)) for j in range(i+1,len(W)+1) if W[i:j]==W[i:j][::-1]}

def direct_mapw(W):
 fac={''}|{W[i:j] for i in range(len(W)) for j in range(i+1,len(W)+1)}
 cand=set()
 for l in range(2,len(W)+3):
  for s in fac:
   if len(s)==l-2 and s==s[::-1]:
    for ch in '01':
     v=ch+s+ch
     if v not in fac: cand.add(v)
 return cand

cases=0;literal_pals=0;literal_absent=0;checks=0
for a,b,k in product(range(1,8),range(1,8),range(1,9)):
 W=('0'*a+'1'*b)*k
 E=expected_pal(a,b,k);A=expected_mapw(E)
 D=direct_pal(W);B=direct_mapw(W)
 assert D==E,(a,b,k,'pal',D^E)
 assert B==A,(a,b,k,'absent',B^A)
 assert len(A)==len(W)+4,(a,b,k,'total',len(A))
 assert max(map(len,A))==len(W)-min(a,b)+2,(a,b,k,'maximum',max(map(len,A)))
 cases+=1;literal_pals+=len(D);literal_absent+=len(B)
 for l in range(2,len(W)+3):
  p_old=sum(len(v)==l-2 for v in E)
  p_here=sum(len(v)==l for v in E)
  count=sum(len(v)==l for v in A)
  assert count==2*p_old-p_here,(a,b,k,l,'gf')
  checks+=1
print('VERIFY_OK cases=%d distinct_palindromes=%d distinct_MAPW=%d length_checks=%d total_n_plus_four=True longest_n_minus_min_plus_two=True'%(cases,literal_pals,literal_absent,checks))
