#!/usr/bin/env python3
from fractions import Fraction
from math import isqrt


def primes_upto(n):
    out=[]
    for x in range(2,n+1):
        ok=True
        for p in out:
            if p*p>x: break
            if x%p==0:
                ok=False; break
        if ok: out.append(x)
    return out


def pp_sum(p,a,q,b,sign):
    # sign=+1 pseudoperfect, sign=-1 Giuga
    n=(p**a)*(q**b)
    s=sum(Fraction(1,p**i) for i in range(1,a+1))
    s+=sum(Fraction(1,q**j) for j in range(1,b+1))
    s+=sign*Fraction(1,n)
    return s


def pred_plus(p,a,q,b):
    return p==2 and q==(1<<a)+1


def pred_minus(p,a,q,b):
    return p==2 and b==1 and q==(1<<a)-1

P=primes_upto(200)
plus=[]; minus=[]; mis=[]
for ii,p in enumerate(P):
  for q in P[ii+1:]:
    for a in range(1,7):
      for b in range(1,7):
        sp=pp_sum(p,a,q,b,+1)
        sm=pp_sum(p,a,q,b,-1)
        ap=(sp==1)
        # Machacek definition is a positive integer; in the two-prime range any hit must equal 1.
        am=(sm.denominator==1 and sm.numerator>=1)
        if ap: plus.append((p,a,q,b,p**a*q**b))
        if am: minus.append((p,a,q,b,p**a*q**b,sm.numerator))
        if ap!=pred_plus(p,a,q,b):
            mis.append(('plus',p,a,q,b,sp,pred_plus(p,a,q,b)))
        if am!=pred_minus(p,a,q,b):
            mis.append(('minus',p,a,q,b,sm,pred_minus(p,a,q,b)))

print('prime_bound=200 exponents=1..6')
print('tuples_checked=',sum(1 for ii,p in enumerate(P) for q in P[ii+1:] for a in range(1,7) for b in range(1,7)))
print('pseudoperfect_hits=',len(plus))
print('giuga_hits=',len(minus))
print('mismatches=',len(mis))
print('first_plus=',plus[:20])
print('first_minus=',minus[:20])
if mis:
    print('first_mismatches=',mis[:20])
    raise SystemExit(1)
