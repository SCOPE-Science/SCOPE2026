from itertools import product
from math import isqrt

S = (-5,-3,3,5)
expected = {3:{5,6,7,9,10}, 5:{6,9,10,11,14,15}, 7:{8,9,10,12,13,15,16,19,20}}
prime_expected = {(3,5),(3,7),(5,11),(7,13),(7,19)}

def isprime(n):
    if n < 2: return False
    if n % 2 == 0: return n == 2
    d=3
    while d*d <= n:
        if n % d == 0: return False
        d += 2
    return True

def signed_candidates(p):
    out=set()
    zeros=[]
    for u,v,w in product(S, repeat=3):
        den=p+u
        num=-(v*p+w)
        if den==0:
            if num==0:
                zeros.append((u,v,w))
            continue
        if num % den == 0:
            q=num//den
            if q>p:
                out.add(q)
    return out, zeros

def direct_half(p,q):
    ds=[1,4,p,q,4*p,4*q,p*q]
    total=sum(ds)
    if total % 2: return False
    target=total//2
    for mask in range(1, (1 << len(ds)) - 1):
        s=sum(ds[i] for i in range(len(ds)) if mask>>i & 1)
        if s==target:
            return True
    return False

for p in (3,5,7):
    got, zeros=signed_candidates(p)
    assert not zeros, (p,zeros)
    assert got==expected[p], (p,got,expected[p])

for p,q in prime_expected:
    assert direct_half(p,q)

# Exhaustive regression scan well beyond the finite symbolic boundary.
checked=0
hits=[]
primes=[n for n in range(3,1001,2) if isprime(n)]
for i,p in enumerate(primes):
    for q in primes[i+1:]:
        checked += 1
        got=direct_half(p,q)
        want=(p,q) in prime_expected
        assert got==want, (p,q,got,want)
        if got: hits.append((p,q))

# Symbolic bound used in the proof: for p>=11,
# q <= 5(p+1)/(p-5) < p because p^2-10p-5>0.
assert 11*11-10*11-5 > 0
assert all(p*p-10*p-5 > 0 for p in range(11,1000))
print('VERIFY_OK')
print('candidate_tables=', {p:sorted(expected[p]) for p in expected})
print('prime_pairs=', sorted(prime_expected))
print('regression_prime_pairs_checked=', checked)
print('regression_bound_q=', 1000)
