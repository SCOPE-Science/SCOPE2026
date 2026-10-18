#!/usr/bin/env python3
"""Exact interval certificate for the closure of the reciprocal-fourth unitary divisor range.
Uses integer arithmetic and fractions; no numerical evaluation of pi or zeta is assumed.
"""
from fractions import Fraction as Q


def atan_partial(num, den, n):
    x = Q(num, den)
    result = Q(0)
    for j in range(n):
        result += ((-1) ** j) * x ** (2 * j + 1) / (2 * j + 1)
    return result


def pi_interval(n=40):
    # Alternating remainders give atan(1/z) between S_n and S_{n+1} for even n.
    assert n % 2 == 0
    a_lo, a_hi = atan_partial(1, 5, n), atan_partial(1, 5, n + 1)
    b_lo, b_hi = atan_partial(1, 239, n), atan_partial(1, 239, n + 1)
    return 16 * a_lo - 4 * b_hi, 16 * a_hi - 4 * b_lo


def prime_sieve(limit):
    marks = bytearray(b'\x01') * (limit + 1)
    marks[0] = marks[1] = 0
    for k in range(2, int(limit**0.5) + 1):
        if marks[k]:
            for j in range(k * k, limit + 1, k):
                marks[j] = 0
    return [j for j in range(limit + 1) if marks[j]]


def finite_prime_certificate():
    ps = prime_sieve(5000)
    # The last checked prime is p_462=3271, and p_463=3299. Thus
    # the cited prime-gap theorem, valid from index 463, covers all larger p.
    assert ps[461] == 3271 and ps[462] == 3299
    # e < 11/4 gives e^8 < (11/4)^8 < 3275 < 3299.
    assert Q(11, 4)**8 < 3275
    worst = None
    checked = 0
    for i, p in enumerate(ps):
        if not (17 <= p < 3275):
            continue
        ns = ps[i + 1: i + 11]
        assert len(ns) == 10
        lhs = p**4
        rhs = p**4 + 1
        for q in ns:
            lhs *= q**4 + 1
            rhs *= q**4
        assert lhs > rhs, (p, ns)
        checked += 1
    # Two subsequent primes q1 <= 11p/10, q2 <= (11/10)^2 p imply
    # (p/q1)^4+(p/q2)^4 >= (10/11)^4+(10/11)^8 > 1.
    assert Q(10, 11)**4 + Q(10, 11)**8 > 1
    return checked


def make_intervals():
    pi_lo, pi_hi = pi_interval()
    assert Q(3141592653589793, 10**15) < pi_lo
    assert pi_hi < Q(3141592653589794, 10**15)
    small_primes = [2,3,5,7,11,13]
    K = Q(1)
    for p in small_primes:
        K *= 1 + Q(1, p**4)
    t_lo = Q(105,1) / (pi_hi**4 * K)
    t_hi = Q(105,1) / (pi_lo**4 * K)
    assert Q(1) < t_lo < t_hi < Q(10001,10000)
    # An interval pair (a,b) represents [a, T*b], where T in [t_lo,t_hi].
    ivs = [(Q(1),Q(1))]
    cutoffs = {13:2,11:2,7:2,5:2,3:3,2:4}
    stage_counts = []
    for p in reversed(small_primes):
        cutoff = cutoffs[p]
        delta = Q(1, p**(4*cutoff))
        assert 1 + delta <= t_lo
        if cutoff > 1:
            assert 1 + Q(1, p**(4*(cutoff-1))) > t_hi
        cand = []
        for a,b in ivs:
            # Exponents >= cutoff, together with p absent, fill this band.
            cand.append((a, b * (1+delta)))
            for exp in range(1, cutoff):
                fac = 1 + Q(1, p**(4*exp))
                cand.append((a*fac,b*fac))
        cand.sort(key=lambda z:z[0])
        ivs = []
        for a,b in cand:
            if not ivs:
                ivs.append((a,b))
            else:
                lo,hi=ivs[-1]
                if a <= hi*t_lo:
                    assert a <= hi*t_lo
                    ivs[-1]=(lo,max(hi,b))
                else:
                    assert a > hi*t_hi, ('uncertain overlap', p)
                    ivs.append((a,b))
        for (a,b),(c,d) in zip(ivs,ivs[1:]):
            assert b*t_hi < c
        stage_counts.append((p,cutoff,len(cand),len(ivs)))
    assert stage_counts == [(13,2,2,2),(11,2,4,4),(7,2,8,8),
                            (5,2,16,16),(3,3,48,48),(2,4,192,140)]
    assert ivs[0][0] == 1
    total_max = Q(105,1)/(pi_lo**4)
    assert ivs[-1][1]*t_hi <= total_max
    # The sup value is exactly the global Euler product (every prime exponent 1).
    assert ivs[-1][1] == K
    gaps = [ (c-b*t_hi, c-b*t_lo) for (a,b),(c,d) in zip(ivs,ivs[1:])]
    assert all(x>0 for x,y in gaps)
    return ivs,stage_counts,t_lo,t_hi


def main():
    checked=finite_prime_certificate()
    ivs,counts,low,high=make_intervals()
    print('VERIFY_OK')
    print('finite_tail_prime_tests=',checked)
    print('stage_counts=',counts)
    print('components=',len(ivs))
    print('intervals_are_[a,T*b]_and_T=105/(pi^4*prod_(p<=13)(1+p^-4))')
    print('min_gap_lower_bound_gt_0=',str(min(c-b*high for (a,b),(c,d) in zip(ivs,ivs[1:]))>0))
    from pathlib import Path
    expected = 'lower_rational\tupper_coefficient_rational\n' + ''.join(
        str(a)+'\t'+str(b)+'\n' for a,b in ivs)
    assert (Path(__file__).resolve().parent/'INTERVALS.tsv').read_text(encoding='utf8') == expected
    print('interval_endpoint_table=VERIFIED')

if __name__ == '__main__':
    main()
