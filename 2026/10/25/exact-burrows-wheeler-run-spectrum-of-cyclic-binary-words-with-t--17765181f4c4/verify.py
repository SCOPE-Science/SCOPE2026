from itertools import combinations
from collections import Counter

def w_from_g(g):
 return ''.join('1'+'0'*i for i in g)

def canon_g(g):
 return min(g[i:]+g[:i] for i in range(3))

def all_classes(m):
 return {canon_g((a,b,m-a-b)) for a in range(m+1) for b in range(m-a+1)}

def bwt_runs(w):
 n=len(w);rot=[w[i:]+w[:i] for i in range(n)];rot.sort()
 last=[r[-1] for r in rot]
 return 1+sum(last[i]!=last[i-1] for i in range(1,n))

def is_cyc(g,h):
 return any(g==h[i:]+h[:i] for i in range(3))

def pred(g):
 lo,mi,hi=sorted(g)
 if hi-lo<=1:return 2
 if lo==mi or mi==hi:return 4
 if mi==lo+1 and is_cyc(g,(mi,lo,hi)):return 4
 if hi==mi+1 and is_cyc(g,(mi,hi,lo)):return 4
 return 6

for n in range(4,54):
 C=all_classes(n-3)
 actual=Counter(); predicted=Counter()
 for g in C:
  r=bwt_runs(w_from_g(g));p=pred(g)
  if r!=p: raise AssertionError((n,g,r,p))
  actual[r]+=1;predicted[p]+=1
 expected4=n-4+(n%3==0)
 exp_total=(((n-1)*(n-2)//2)+(2 if n%3==0 else 0))//3
 assert actual[2]==1 and actual[4]==expected4 and sum(actual.values())==exp_total,(n,actual)
 if n<=25 or n%5==0:print(n,len(C),dict(sorted(actual.items())),flush=True)
print('PASS all necklaces n=4..53')
