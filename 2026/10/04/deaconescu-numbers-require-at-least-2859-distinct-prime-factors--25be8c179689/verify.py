#!/usr/bin/env python3
from math import isqrt, log, exp

LIMIT = 100000

def primes_upto(n):
    mark = bytearray(b"\x01") * (n + 1)
    mark[0:2] = b"\x00\x00"
    for p in range(2, isqrt(n) + 1):
        if mark[p]:
            start = p * p
            mark[start:n+1:p] = b"\x00" * (((n - start) // p) + 1)
    return [i for i, flag in enumerate(mark) if flag]

def product_pair(primes):
    num = 1
    den = 1
    for p in primes:
        num *= p - 1
        den *= p - 2
    return num, den

def log_ratio(primes):
    return sum(log(p - 1) - log(p - 2) for p in primes)

def main():
    ps = primes_upto(LIMIT)
    q = [p for p in ps if p >= 7 and p % 3 == 1]
    s = [p for p in ps if p >= 5 and p % 3 == 2]
    assert len(q) >= 2858 and len(s) >= 2859

    qa_num, qa_den = product_pair(q[:2857])
    qb_num, qb_den = product_pair(q[:2858])
    sc_num, sc_den = product_pair(s[:2858])
    sn_num, sn_den = product_pair(s[:2859])

    assert 2 * qa_num < 5 * qa_den
    assert qb_num < 5 * qb_den
    assert sc_num < 3 * sc_den
    assert sn_num > 3 * sn_den

    assert q[2856] == 56569
    assert q[2857] == 56599
    assert s[2857] == 56081
    assert s[2858] == 56087

    print("VERIFY_OK")
    print("q_2857=56569")
    print("q_2858=56599")
    print("s_2858=56081")
    print("s_2859=56087")
    print("A_2858~", 2.0 * exp(log_ratio(q[:2857])))
    print("B_2858~", exp(log_ratio(q[:2858])))
    print("C_2858~", exp(log_ratio(s[:2858])))
    print("C_2859~", exp(log_ratio(s[:2859])))

if __name__ == "__main__":
    main()
