from itertools import product
from collections import Counter
from math import comb
import sympy as s

def rec_burn(c):
 n=len(c); d=[2 if i in (0,n-1) else 3 for i in range(n)]
 if n==2:d=[2,2]
 h=[x+1 for x in c] # firing hub sends 1 to each rim vertex
 done=set()
 while True:
  newly=next((i for i in range(n) if i not in done and h[i]>=d[i]),None)
  if newly is None:break
  i=newly;done.add(i);h[i]-=d[i]
  if i>0:h[i-1]+=1
  if i<n-1:h[i+1]+=1
 return len(done)==n

def stab(c,k):
 n=len(c);d=[2 if i in (0,n-1) else 3 for i in range(n)]
 h=list(c);h[k]+=1;tops=0
 for it in range(10*n):
  i=next((i for i in range(n) if h[i]>=d[i]),None)
  if i is None:break
  h[i]-=d[i];tops+=1
  if i>0:h[i-1]+=1
  if i<n-1:h[i+1]+=1
 else:raise AssertionError('not terminated')
 return tops

def direct(n):
 d=[2]+[3]*(n-2)+[2]
 C=Counter();N=0;check=0
 for c in product(*(range(x) for x in d)):
  yes=rec_burn(c)
  typ=(not any(c[i]==c[j]==0 and all(c[k]!=2 for k in range(i+1,j)) for i in range(n) for j in range(i+1,n)))
  assert yes==typ,(n,c)
  if yes:
   N+=1
   for k in range(n): C[stab(c,k)]+=1
 return N,C

z,t=s.symbols('z t')
B=1/(1-z)**2;L=B-1
R=s.factor(B-1-2*z+L**2*z/(1-z*B))
N=s.factor(-t*z**2*(t*z**2-3*t*z+t+1)*(t*z**3-3*t*z**2+t*z-2*z**2+5*z-2)/((t*z-1)**2*(z*z-3*z+1)**2))
A=s.factor(z*s.diff(R,z)-N.subs(t,1)+N)
for n in range(2,10):
 nr,ca=direct(n)
 pol=s.Poly(s.expand(s.series(A,z,0,n+1).removeO()).coeff(z,n),t)
 cb={e[0]:int(co) for e,co in pol.terms()}
 print(n,nr,dict(sorted(ca.items())),cb)
 assert cb==dict(ca)
print('DIRECT_BURNING_STABILIZATION_PASS')
