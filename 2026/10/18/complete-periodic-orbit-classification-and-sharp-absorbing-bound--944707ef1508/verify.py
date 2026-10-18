"""Independent exact checks for the shifted-totient map F(n)=phi(n)+3.

The general theorem is proved symbolically in RESULT.md; finite checks are
regression tests and do not certify the infinite descent argument.
"""
from math import isqrt

CYCLES = {(9,), (11, 13, 15), (23, 25)}
EXPECTED_TABLE = (
    4, 4, 5, 5, 7, 5, 9, 7, 9, 7, 13, 7, 15, 9, 11, 11, 19,
    9, 21, 11, 15, 13, 25, 11, 23,
)


def phi_by_factors(n):
    result, m, p = n, n, 2
    while p*p <= m:
        if m % p == 0:
            result -= result // p
            while m % p == 0:
                m //= p
        p += 1
    if m > 1:
        result -= result // m
    return result


def sieve_phi(N):
    v = list(range(N+1))
    for p in range(2,N+1):
        if v[p] == p:
            for k in range(p,N+1,p):
                v[k] -= v[k]//p
    return v


def canonical_cycle(xs):
    j = xs.index(min(xs))
    return tuple(xs[j:] + xs[:j])


def main():
    assert tuple(phi_by_factors(n)+3 for n in range(1,26)) == EXPECTED_TABLE
    assert max(EXPECTED_TABLE) == 25
    for n in range(26,5000):
        p = phi_by_factors(n)
        prime = p == n - 1
        if prime:
            assert n >= 29
            q = n + 2
            qprime = phi_by_factors(q) == q-1
            if qprime:
                assert (n+4)%3 == 0
                assert phi_by_factors(n+4) + 3 < n
            else:
                assert phi_by_factors(q) + 3 < n
        else:
            assert p + 3 < n
    N=1000000
    sv=sieve_phi(N+5)
    for n in range(1,N+1):
        if n <= 2500 or n % 37 == 0:
            assert sv[n] == phi_by_factors(n)
    attr = {}; count={c:0 for c in CYCLES}; max_preperiod=0
    for n in range(1,N+1):
        if n in attr:
            continue
        seen={}; path=[]; x=n
        while x not in attr and x not in seen:
            seen[x]=len(path); path.append(x)
            assert x < len(sv), (n,x)
            x=sv[x]+3
        if x in seen:
            c=canonical_cycle(path[seen[x]:])
            assert c in CYCLES, (n,c)
            for y in path[seen[x]:]:attr[y]=(c,0)
            path=path[:seen[x]]
        for y in reversed(path):
            nxt=sv[y]+3
            attr[y]=(attr[nxt][0],attr[nxt][1]+1)
    for n in range(1,N+1):
        c,depth=attr[n]
        count[c]+=1
        max_preperiod=max(max_preperiod,depth)
    assert set(count) == CYCLES
    assert sum(count.values())==N
    print('Finite table verified for 1..25:', EXPECTED_TABLE)
    print('Symbolic descent branch checks for inputs 26..4999: passed')
    print('Totient sieve cross-checked against factorization:', len(range(1,2501))+len(range(2501,N+1,37)), 'inputs (possibly overlapping rounded)')
    print('Initial values checked:',N)
    print('Observed cycles:', sorted(CYCLES))
    print('Basins among first million initial values:',count)
    print('Maximum preperiod length:',max_preperiod)
    print('Sharpness: 25 is recurrent and every integer 1..25 maps into 1..25')

if __name__ == '__main__':
    main()
