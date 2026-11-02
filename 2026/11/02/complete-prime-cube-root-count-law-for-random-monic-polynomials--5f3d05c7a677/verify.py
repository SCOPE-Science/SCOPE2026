from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb

def predicted(p):
 n0=p*(p-1)**2//2+p-1
 n1=2*p*(p-1)
 n2=p*(p-1)**2//2
 # local probability via common denom p^6
 weights=Counter({0:0,1:0,p:0,2*p:0,p*p:0})
 weights[1]+=(p-1)*p**4 # (p−1)/p²
 weights[p]+=n1
 weights[2*p]+=n2
 weights[p*p]+=1
 weights[0]=p**6 - sum(weights.values())
 # 0-singular n0 merged into zero via 1−..: indeed weights 0 catches n0
 assert sum(weights.values())==p**6
 ans=Counter({0:1})
 for i in range(p):
  new=Counter()
  for x,a in ans.items():
   for y,b in weights.items(): new[x+y]+=a*b
  ans=new
 return ans, p**(6*p),weights
p=2;d=6;q=p**3
expected,denom,w=predicted(p)
obs=Counter()
for cs in product(range(q),repeat=d):
 rootcount=0
 for t in range(q):
  v=1
  for c in reversed(cs): v=(v*t+c)%q
  if v==0:rootcount+=1
 obs[rootcount]+=1
assert sum(obs.values())==q**d
for k in set(obs)|set(expected):
 assert Fraction(obs[k],q**d)==Fraction(expected[k],denom),(k,obs[k],expected[k],denom)
print('EXHAUSTIVE_OK',p,d,len(obs),dict(sorted(obs.items())))
for p in (3,5,7):
 ans,den,w=predicted(p)
 from random import Random
 rng=Random(1234+p);d=3*p;q=p**3
 for z in range(100):
  cs=[rng.randrange(q) for i in range(d)]
  cnt=0
  for t in range(q):
   v=1
   for c in reversed(cs): v=(v*t+c)%q
   cnt+=(v==0)
  assert cnt in ans
 print('SAMPLE_OK',p,d,'local_weights',sorted((k,v) for k,v in w.items() if v))

# Independent finite-field quadratic census at each tested characteristic.
for pp in (2, 3, 5, 7, 11):
    observed=Counter(sum((A+B*x+C*x*x)%pp==0 for x in range(pp))
        for A in range(pp) for B in range(pp) for C in range(pp))
    theoretical=Counter()
    theoretical[0]+=pp*(pp-1)**2//2+pp-1
    theoretical[1]+=2*pp*(pp-1)
    theoretical[2]+=pp*(pp-1)**2//2
    theoretical[pp]+=1
    assert observed==theoretical,(pp,observed,theoretical)
print('QUADRATIC_CENSUS_OK primes=2,3,5,7,11')
