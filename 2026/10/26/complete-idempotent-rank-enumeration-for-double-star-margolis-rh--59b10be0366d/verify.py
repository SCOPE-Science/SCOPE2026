# Standalone exact exhaustive small-case test for the double-star idempotent rank formula.
# Uses only the Python standard library. Undefined vertices are encoded as -1.
from itertools import product
from math import comb
from collections import Counter

def graph(a,b):
 n=a+b+2
 e={(0,1)}
 e.update((0,i) for i in range(2,a+2))
 e.update((1,i) for i in range(a+2,n))
 return n,e

def continuous(f,edges):
 n=len(f)
 for t in range(n):
  pre=[i for i,x in enumerate(f) if x==t]
  if len(pre)>2:return False
  if len(pre)==2 and tuple(pre) not in edges:return False
 for x,y in edges:
  pre=[i for i,v in enumerate(f) if v==x or v==y]
  if len(pre)>2:return False
  if len(pre)==2 and tuple(pre) not in edges:return False
 return True

def idem(f):
 return all(f[v]==v for v in f if v>=0)

def formula(a,b):
 from math import comb
 from collections import defaultdict
 def plus(X,Y):
  z=Counter(X)
  z.update(Y)
  return z
 def mul(X,Y):
  Z=Counter()
  for i,u in X.items():
   for j,v in Y.items():Z[i+j]+=u*v
  return Z
 def sh(X,k):return {i+k:u for i,u in X.items()}
 F=lambda n:{i:comb(n,i) for i in range(n+1)}
 H=lambda n:{i:comb(n,i)+(n*comb(n-1,i-1) if i else 0) for i in range(n+1)}
 Fa,Fb,Ha,Hb=F(a),F(b),H(a),H(b)
 D={0:1}
 P=mul(Ha,Hb)
 Ua=plus(Fa,{0:a}); Ub=plus(Fb,{0:b})
 P=plus(P,sh(mul(Ua,Hb),1)); P=plus(P,sh(Fb,1));P=plus(P,sh(mul(Ub,Ha),1));P=plus(P,sh(Fa,1));P=plus(P,sh(mul(Fa,Fb),2))
 return P

for a,b in [(1,1),(1,2),(2,2),(1,3),(2,3)]:
 n,E=graph(a,b)
 Ct=Counter(); Ct_all=0
 for f in product(range(-1,n),repeat=n):
  if idem(f) and continuous(f,E):
   Ct[len(set(v for v in f if v>=0))]+=1
 P=formula(a,b)
 print('a,b',a,b,'n',n,'counts',sorted(Ct.items()),'pred',sorted(P.items()),'total',sum(Ct.values()))
 assert Ct==P
print('VERIFY_OK')
