# Copyright-free standalone reproducibility test. No external dependencies.
from itertools import product
from decimal import Decimal, getcontext, ROUND_FLOOR
getcontext().prec = 70
alpha = Decimal(2).sqrt()-1
def floor(x):
 return int(x.to_integral_value(rounding=ROUND_FLOOR))
MAX=10
seq=[1+floor((i+1)*alpha)-floor(i*alpha) for i in range(-300,301)]
factors={n: {tuple(seq[i:i+n]) for i in range(len(seq)-n+1)} for n in range(MAX+1)}
assert all(len(factors[n])==n+1 for n in range(MAX+1)), [len(factors[n]) for n in range(MAX+1)]

def predicted(S,N):
 f=[0]*(N+1)
 for n in range(1,N+1):f[n]=n if n-1 in S else 0
 g=[0]*(N+1);g[0]=1
 for n in range(1,N+1):g[n]=sum(f[k]*g[n-k] for k in range(1,n+1))
 return [sum(k*f[k]*g[n-k] for k in range(1,n+1)) for n in range(1,N+1)]

def admissible(cyc,S):
 m=len(cyc);markers=[i for i,s in enumerate(cyc) if s==0]
 if not markers:return False # Sturmian zero-free part is aperiodic
 for j,i in enumerate(markers):
  end=markers[(j+1)%len(markers)]
  gap=(end-i-1)%m if len(markers)>1 else m-1
  if gap not in S:return False
  w=tuple(cyc[(i+1+k)%m] for k in range(gap))
  if w not in factors[gap]:return False
 return True

for title,S,N in [
 ('all gaps',set(range(MAX+1)),10),
 ('even gaps',set(range(0,MAX+1,2)),10),
 ('powers of two plus zero', {0,1,2,4,8},10),
 ('sparse initial support', {1,3,7},10),
]:
 pred=predicted(S,N)
 obs=[sum(admissible(w,S) for w in product((0,1,2),repeat=n)) for n in range(1,N+1)]
 assert pred==obs,(title,pred,obs)
 print(title, 'fixed counts n=1..10',pred)
print('ALL_40_COUNTS_EXACT')
