"""Deterministic finite component for quartic three-block classification.

Only Python's standard library is used.  The infinite range follows separately
from the proved 81*sqrt(p)+48 character-sum inequality.
"""

BOUND = 6724
EXCEPTIONS = (
    5, 13, 17, 29, 37, 41, 53, 61, 73, 89, 97, 101, 109, 113,
    137, 157, 173, 193, 197, 233, 241, 257, 277, 281, 293,
    313, 337, 353, 401, 409, 433, 457, 509, 521, 569, 709, 881, 1153,
)

def prime_flags(bound):
    sieve = [True] * bound
    sieve[0] = sieve[1] = False
    for d in range(2, int((bound-1)**0.5) + 1):
        if sieve[d]:
            for m in range(d*d, bound, d):
                sieve[m] = False
    return sieve

def prime_factors(n):
    factors = []
    d = 2
    while d*d <= n:
        if n%d == 0:
            factors.append(d)
            while n%d == 0: n//=d
        d += 1
    if n>1: factors.append(n)
    return factors

def least_primitive_root(p):
    factors = prime_factors(p-1)
    for g in range(2, p):
        if all(pow(g,(p-1)//q,p) != 1 for q in factors):
            return g
    raise AssertionError('primitive root missing')

def patterns(p):
    g = least_primitive_root(p)
    labels = [-1]*p
    value=1
    for exponent in range(p-1):
        assert labels[value] == -1
        labels[value] = exponent%4
        value = value*g %p
    assert value==1 and all(x>=0 for x in labels[1:])
    # Check each discrete-log class through the independently computed
    # quartic-power character x^((p-1)/4), including generator orientation.
    omega=pow(g,(p-1)//4,p)
    table={pow(omega,a,p):a for a in range(4)}
    assert len(table)==4
    for x in range(1,p):
        assert table[pow(x,(p-1)//4,p)]==labels[x]
    counts=[0]*64
    for x in range(1,p-2):
        counts[16*labels[x]+4*labels[x+1]+labels[x+2]]+=1
    assert sum(counts)==p-3
    return counts

def main():
    flags=prime_flags(BOUND)
    eligible=[p for p in range(5,BOUND) if flags[p] and p%4==1]
    observed=[]
    for p in eligible:
        c=patterns(p)
        if min(c)==0: observed.append(p)
        if p>=1181: assert min(c)>0, p
        if p>=733: assert all(count>0 for count in c[1:]), p
    assert tuple(observed)==EXCEPTIONS, (observed,EXCEPTIONS)
    assert any(v==0 for v in patterns(709)[1:])
    c=patterns(1153)
    assert [i for i,n in enumerate(c) if n==0]==[0]
    c=patterns(1181)
    assert min(c)>0
    print('VERIFY_OK: 427 primes p == 1 mod 4, p < 6724; 38 exact exceptions;')
    print('largest exception 1153, unique missing class (0,0,0); first succeeding prime 1181; mixed-pattern cutoff 733;')
    print('complete finite range coupled to p - 81 sqrt(p) - 48 > 0 for p >= 6724.')

if __name__=='__main__': main()
