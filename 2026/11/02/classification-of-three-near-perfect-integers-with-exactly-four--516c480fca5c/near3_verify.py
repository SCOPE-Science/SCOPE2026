"""Exact finite certificate for three-near-perfect numbers with omega=3, Omega=4.

The proof in RESULT.md establishes the global prime bounds; this code
exhausts the resulting finite cases with integer arithmetic only.
"""
from itertools import combinations
from math import isqrt

EXPECTED = (60, 84, 90, 132, 140, 156, 220, 234, 260, 308, 342, 350,
            364, 490, 532, 550, 572, 666, 726, 740, 748, 820, 1148,
            1316, 1484)

def prime(n):
    if n < 2:
        return False
    for d in range(2, isqrt(n) + 1):
        if n % d == 0:
            return False
    return True

def divisors(factors):
    values = [1]
    for p, power in factors:
        current = [p**j for j in range(power + 1)]
        values = [a*b for a in values for b in current]
    return sorted(values)

def shape_factors(shape, p, q):
    if shape == '4pq':
        return [(2, 2), (p, 1), (q, 1)]
    if shape == '2p2q':
        return [(2, 1), (p, 2), (q, 1)]
    if shape == '2pq2':
        return [(2, 1), (p, 1), (q, 2)]
    raise AssertionError(shape)

def cases():
    for p in (3, 5, 7, 11):
        upper = {3:28, 5:42, 7:56, 11:19}[p]
        for q in range(p+2, upper+1, 2):
            if prime(q):
                yield '4pq', p, q
    for p, upper in ((3,39),(5,11)):
        for q in range(p+2, upper+1, 2):
            if prime(q):
                yield '2p2q', p, q
    for p, upper in ((3,11),(5,7)):
        for q in range(p+2, upper+1, 2):
            if prime(q):
                yield '2pq2', p, q

def verify():
    result = []
    count = {'4pq':0, '2p2q':0, '2pq2':0}
    for shape, p, q in cases():
        count[shape] += 1
        factors = shape_factors(shape, p, q)
        D = divisors(factors)
        n = D[-1]
        S = sum(D)
        delta = S - 2*n
        if shape == '4pq':
            assert delta == (7-p)*q + 7*p+7
        elif shape == '2p2q':
            assert delta == (3+3*p-p*p)*q + 3*(p*p+p+1)
        else:
            assert delta == (3-p)*q*q + 3*(p+1)*(q+1)
        assert len(D) == 12
        witness = tuple(c for c in combinations(D[:-1], 3) if sum(c) == delta)
        if witness:
            result.append((shape, p, q, n, delta, witness))
    assert count == {'4pq':32, '2p2q':12, '2pq2':4}, count
    assert len(result) == 25
    assert tuple(sorted(x[3] for x in result)) == EXPECTED
    assert {s:sum(x[0]==s for x in result) for s in count} == {'4pq':17,'2p2q':6,'2pq2':2}
    assert len({x[3] for x in result}) == 25
    assert all(all(len(set(t)) == 3 and sum(t) == d and all(n%v==0 and v<n for v in t) for t in W) for _,_,_,n,d,W in result)
    print('VERIFY_OK cases=48 by_shape=32,12,4 solutions=25 by_shape=17,6,2 witnesses='+str(sum(len(x[-1]) for x in result)))
    for shape,p,q,n,delta,witnesses in sorted(result, key=lambda x:x[3]):
        print(n, shape, p, q, 'delta='+str(delta), 'witnesses='+str(witnesses))
    return result

if __name__ == '__main__':
    verify()
