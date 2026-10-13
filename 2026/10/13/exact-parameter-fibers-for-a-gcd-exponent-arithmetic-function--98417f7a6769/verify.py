from math import gcd, lcm
from itertools import product
from collections import Counter

def divisors(n):
    return [d for d in range(1,n+1) if n%d==0]

def phi(n):
    return sum(1 for k in range(1,n+1) if gcd(k,n)==1)

def sig(exps,a):
    return tuple(gcd(e,a) for e in exps)

cases=pairs=0
# Exhaust all support sizes <=4 and exponents <=5; this keeps L <=60.
for r in range(1,5):
  for exps in product(range(1,6), repeat=r):
    L=1
    for e in exps: L=lcm(L,e)
    ds=divisors(L)
    reps={d:sig(exps,d) for d in ds}
    assert len(set(reps.values()))==len(ds)
    for a in range(1,L+1):
      sa=sig(exps,a)
      assert sa==reps[gcd(a,L)]
      for b in range(1,L+1):
        assert (sa==sig(exps,b))==(gcd(a,L)==gcd(b,L))
        pairs+=1
    counts=Counter(gcd(a,L) for a in range(1,L+1))
    assert counts==Counter({d:phi(L//d) for d in ds})
    periods=[T for T in range(1,L+1) if all(sig(exps,a+T)==sig(exps,a) for a in range(1,L+1))]
    assert periods and periods[0]==L
    cases+=1
print(f'VERIFY_OK exponent_tuples={cases} parameter_pairs={pairs} max_exponent=5 max_support=4')
