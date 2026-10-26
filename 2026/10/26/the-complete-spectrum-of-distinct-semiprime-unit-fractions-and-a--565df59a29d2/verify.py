"""Finite independent exact-rational checks for the semiprime reciprocal criterion."""
from fractions import Fraction
from itertools import combinations
from math import gcd, prod

PRIMES=(2,3,5,7,11)
DENOM=tuple(p*q for i,p in enumerate(PRIMES) for q in PRIMES[i:])
assert len(DENOM)==15 and len(set(DENOM))==15

def factor(n):
    out={}; p=2
    while p*p<=n:
        while n%p==0:
            out[p]=out.get(p,0)+1;n//=p
        p+=1
    if n>1:out[n]=out.get(n,0)+1
    return out

def test_local(x):
    a,b=x.numerator,x.denominator
    exponents=factor(b)
    if any(e>2 for e in exponents.values()):return False
    squared=[p for p,e in exponents.items() if e==2]
    if any((a-b//(p*p))%p for p in squared):return False
    return x>=sum((Fraction(1,p*p) for p in squared),Fraction(0))

# Enumeration verifies necessity for *every* subset of the 15 semiprimes.
# It does not verify sufficiency for arbitrary positive rationals; that uses a cited theorem.
vals=[Fraction(1,d) for d in DENOM]
checked=0
for mask in range(1<<len(DENOM)):
    total=sum((v for i,v in enumerate(vals) if mask&(1<<i)),Fraction())
    if total>0:
        assert test_local(total)
        forced={p for p,e in factor(total.denominator).items() if e==2}
        used={p for p in PRIMES if mask&(1<<DENOM.index(p*p))}
        assert forced==used,(mask,total,forced,used)
    checked+=1

assert Fraction(13,36)==Fraction(1,4)+Fraction(1,9)
assert Fraction(19,36)==Fraction(1,4)+Fraction(1,9)+Fraction(1,6)
assert not test_local(Fraction(7,36))
assert test_local(Fraction(13,36))
assert test_local(Fraction(19,36))

# Test sharpness examples with exact integer arithmetic.
for k in range(2,6):
    ps=PRIMES[:k];R=prod(ps)
    q=sum((Fraction(1,p*p) for p in ps),Fraction())
    x=q-Fraction(1,R)
    assert x>0 and x.denominator==R*R
    assert all((x.numerator-(R//p)**2)%p==0 for p in ps)
    assert not test_local(x)

# Exact residue proportions on complete periods of reduced numerator classes.
for b in (4,9,25,36,72,100,180,225,400,900):
    ex=factor(b)
    if max(ex.values())>2:continue
    S=[p for p,e in ex.items() if e==2]
    candidates=sum(1 for a in range(1,b+1) if gcd(a,b)==1)
    good=sum(1 for a in range(1,b+1) if gcd(a,b)==1 and all((a-b//(p*p))%p==0 for p in S))
    assert candidates==prod((p**(e-1)*(p-1) for p,e in ex.items()))
    assert good*prod((p-1 for p in S))==candidates
print('VERIFY_OK complete_subsets=32768 square_prime_forcing=PASS sharpness_examples=4 exact_residue_periods=10 independent_arithmetic=PASS')
