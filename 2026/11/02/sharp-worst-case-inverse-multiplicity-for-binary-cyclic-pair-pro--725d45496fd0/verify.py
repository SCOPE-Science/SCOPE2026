"""Standalone integer checks of the stated cyclic binary pair-profile extremum."""
from collections import Counter
from math import comb

def fiber(n, z, t):
    o = n - z
    if not 1 <= t <= min(z, o):
        return 0
    num = n * comb(z-1, t-1) * comb(o-1, t-1)
    assert num % t == 0
    return num // t

def formula(n):
    if n == 1: return 1, {(0,0), (1,0)}
    if n == 2: return 2, {(1,1)}
    if n == 3: return 3, {(1,1), (2,1)}
    if n == 4: return 4, {(1,1), (2,1), (3,1)}
    if n == 5: return 5, {(1,1),(2,1),(3,1),(4,1),(2,2),(3,2)}
    k, r = divmod(n,4)
    if r == 0: zs, ts = [2*k], [k]
    elif r == 1: zs, ts = [2*k, 2*k+1], [k, k+1]
    elif r == 2: zs, ts = [2*k+1], [k+1]
    else: zs, ts = [2*k+1,2*k+2], [k+1]
    return fiber(n, zs[0], ts[0]), {(z,t) for z in zs for t in ts}

def check_parameters():
    for n in range(1, 201):
        options = [(1,0,0),(1,n,0)]
        options.extend((fiber(n,z,t),z,t) for z in range(1,n) for t in range(1,min(z,n-z)+1))
        largest = max(x[0] for x in options)
        maxima = {(z,t) for v,z,t in options if v == largest}
        assert (largest,maxima)==formula(n), (n,largest,maxima,formula(n))
    print('PARAMETER_OPTIMA_OK')

def check_direct():
    for n in range(1,20):
        counts = Counter()
        for word in range(1 << n):
            z = n-word.bit_count()
            changes = sum(((word >> i) & 1) == 0 and ((word >> ((i+1)%n)) & 1) == 1 for i in range(n))
            counts[(z,changes)] += 1
        for (z,t),multiplicity in counts.items():
            assert multiplicity == (1 if t==0 else fiber(n,z,t)), (n,z,t,multiplicity)
        greatest = max(counts.values())
        winners = {k for k,v in counts.items() if v==greatest}
        assert (greatest,winners)==formula(n), (n,greatest,winners,formula(n))
    print('DIRECT_WORD_CENSUS_OK')
if __name__ == '__main__':
    check_parameters()
    check_direct()
    print('VERIFY_OK')
