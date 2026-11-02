"""Exact small-modulus checks for prime-square sieve-tail probabilities."""
from fractions import Fraction
from math import prod


def primes_upto(y):
    return [p for p in range(3, y + 1, 2) if all(p % d for d in range(3, int(p ** .5) + 1, 2))]


def exact_tails(y):
    ps = primes_upto(y)
    H = sum((Fraction(1, p) for p in ps), Fraction())
    S = sum((Fraction(1 if p % 4 == 1 else -1, p) for p in ps), Fraction())
    pmf = {0: Fraction(1)}
    for p in ps:
        chi = 1 if p % 4 == 1 else -1
        pmf_new = {}
        for k, pr in pmf.items():
            pmf_new[k] = pmf_new.get(k, Fraction()) + pr * Fraction(p - 1, p)
            pmf_new[k + chi] = pmf_new.get(k + chi, Fraction()) + pr * Fraction(1, p)
        pmf = pmf_new
    tail1 = sum((v for k, v in pmf.items() if k - S >= H / 2), Fraction())
    pmf = {0: Fraction(1)}
    for p in ps:
        if p % 4 != 1:
            continue
        w = Fraction(2, p - 1)
        nd = {}
        for k, pr in pmf.items():
            nd[k] = nd.get(k, Fraction()) + pr * (1 - w)
            nd[k + 1] = nd.get(k + 1, Fraction()) + pr * w
        pmf = nd
    tail2 = sum((v for k, v in pmf.items() if k - S < H / 2), Fraction())
    return ps, H, S, tail1, tail2


def brute(y):
    ps, H, S, e1, e2 = exact_tails(y)
    Q = prod(ps)
    count1 = 0
    for n in range(1, Q+1):
        t = sum((1 if p%4 == 1 else -1) for p in ps if n%p == 0) - S
        count1 += (t >= H/2)
    assert Fraction(count1,Q) == e1, (y,'first',e1,count1,Q)
    units = [u for u in range(1,Q+1) if all(u % p for p in ps)]
    count2=0
    for u in units:
        for v in units:
            t=sum((1 if p%4 == 1 else -1) for p in ps if (u*u+v*v)%p == 0)-S
            count2 += (t < H/2)
    assert Fraction(count2,len(units)**2)==e2,(y,'second',e2,count2,len(units))
    return Q,len(units),count1,count2


if __name__=='__main__':
    for y in [5,7,11]:
        print('CRT_EXACT',y,brute(y))
    for y in [13,17,31,53,101,251]:
        ps,H,S,e1,e2=exact_tails(y)
        assert 0 <= e1 <= 1 and 0 <= e2 <= 1
        print('DISTRIBUTION',y,len(ps),float(H),float(e1),float(e2))
    print('VERIFY_OK prime_set_cutoffs=9 direct_CRT_cutoffs=3')
