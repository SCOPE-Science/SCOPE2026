from itertools import product
from math import isqrt

PRIMES = [2,3,5,7]

def e(m,d):
    return m//d + (m % d)

def value(ms,d):
    v=1
    for p,m in zip(PRIMES,ms):
        v *= p**e(m,d)
    return v

def candidates(ms):
    M=max(ms)
    if M < 2:
        return {2}
    out=set()
    for m in ms:
        q=1
        while q <= m:
            d=m//q
            if d>=2:
                out.add(d)
            q=m//d + 1
    return out

def direct_argmins(ms):
    M=max(2,max(ms))
    vals={d:value(ms,d) for d in range(2,M+1)}
    mv=min(vals.values())
    return {d for d,v in vals.items() if v==mv}, mv

def candidate_argmins(ms):
    cs=candidates(ms)
    vals={d:value(ms,d) for d in cs}
    mv=min(vals.values())
    return {d for d,v in vals.items() if v==mv}, mv

cases=0
for r in range(1,4):
    for ms in product(range(1,26), repeat=r):
        da,dv=direct_argmins(ms)
        ca,cv=candidate_argmins(ms)
        assert dv==cv
        assert da <= candidates(ms)
        M=max(ms)
        if M>=2:
            # Every omitted unit step is a strict descent.
            C=candidates(ms)
            for d in range(2,M):
                if d not in C:
                    assert value(ms,d+1) < value(ms,d)
            # Safe O(sum sqrt(m)) candidate-count bound.
            assert len(C) <= sum(2*isqrt(m) for m in ms)
        cases += 1

rey=(10,1,5)
assert candidates(rey)=={2,3,5,10}
ra,rv=direct_argmins(rey)
assert ra=={5}
print(f"VERIFY_OK exhaustive_vectors={cases} max_exponent=25 reyssat_candidates=2,3,5,10 reyssat_minimizer=5")
