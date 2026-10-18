#!/usr/bin/env python3
"""Exact integer certificates for ternary squared-digit happiness densities.

All calculations use integer arithmetic, including the comparisons with
rational endpoints. The only external mathematical input to the theorem is
Gilmer's density-transfer theorem (arXiv:1110.3836, Theorem 4.1).
"""

def digit_square_sum_3(n):
    s = 0
    while n:
        n, a = divmod(n, 3)
        s += a*a
    return s


def happy_table(limit):
    """Compute whether each 0<=n<=limit reaches 1 (0 is not happy)."""
    T = [-1] * (limit + 1)
    T[0], T[1] = 0, 1
    for n in range(2, limit + 1):
        v, path, seen = n, [], set()
        while v != 1 and v not in seen and T[v] < 0:
            seen.add(v)
            path.append(v)
            v = digit_square_sum_3(v)
            assert v <= limit
        answer = int(v == 1) if v == 1 else (0 if v in seen else T[v])
        for x in path:
            T[x] = answer
    return T


def verify_cycle_reduction():
    """The maximum digit sum decreases n>=27; check finite 1..26."""
    T = happy_table(26)
    expected = [1, 3, 9, 13, 17, 23, 25]
    assert [n for n in range(1, 27) if T[n]] == expected
    assert all(digit_square_sum_3(n) <= 12 for n in range(1, 27))
    for n in range(1, 27):
        assert T[n] == (1 if n == 1 else T[digit_square_sum_3(n)])
    return expected


def interval_count(n):
    """Exact count of happy integers in [3**(n-1),3**n-1]."""
    assert n >= 2
    T = happy_table(4*n + 1)
    # C_{m,t} = [z**t](1+z+z**4)**m.
    C = [1]
    for m in range(n-1):
        nxt = [0] * (len(C)+4)
        for i, v in enumerate(C):
            nxt[i] += v
            nxt[i+1] += v
            nxt[i+4] += v
        C = nxt
        assert sum(C) == 3**(m+1)
    H = sum(c*(T[t+1]+T[t+4]) for t,c in enumerate(C))
    D = 2*3**(n-1)
    assert 0 <= H <= D
    return H,D


def independently_count_small():
    for n in range(2,8):
        lo,hi = 3**(n-1), 3**n
        T = happy_table(hi)
        brute = sum(T[i] for i in range(lo,hi))
        assert interval_count(n) == (brute, hi-lo), n


def verify_bounds():
    verify_cycle_reduction()
    independently_count_small()
    hi_n, lo_n = 136,224
    Hh,Dh = interval_count(hi_n)
    Hl,Dl = interval_count(lo_n)
    # Ratios are STRICT; cross-multiplication proves them exactly.
    assert 100000*Hh > 37188*Dh  # d_136>0.37188
    assert 1000000*Hl < 110033*Dl # d_224<0.110033
    # Direct exact upper certificates for Gilmer's hypotheses (B1)-(B3).
    # Here mu=5/3<2, sigma=sqrt(26)/3<2, sqrt(2)*sigma<3,
    # 2*sigma/sqrt(mu)<3, sqrt(3*mu*3*sigma)<6.
    for n in (hi_n, lo_n):
        assert n % 8 == 0
        assert 28+12*3**(5*n//8) < 3**(n-1)  # B1
        assert 6 < 3**(3*n//8)  # B2
        assert 8*(7+3**(3*n//4)+3*3**(5*n//8)) < 3**(n-1)  # B3
        assert (2*3**(n-1)) % 3**(3*n//4) == 0  # n-strict shell partition
    # Theorem 4.1 error: sigma/sqrt(mu)=sqrt(26/15)<3/2.
    # Hence -delta(n)<2/(3^(n/4)-1)+6/(3^(n/8)-1).
    for n in (hi_n,lo_n):
        den1,den2 = 3**(n//4)-1, 3**(n//8)-1
        assert 1000000*(2*den2+6*den1) < den1*den2
    # Exact consequence: exp(delta)>1-1/1e6.
    # dbar > (37188/100000)*(999999/1e6)>3718/10000.
    assert 37188*999999*10000>3718*100000*1000000
    # dunder < 1 - (1-110033/1e6)*(1-1/1e6)<11004/1e5.
    assert 100000*(1000000**2 - (1000000-110033)*999999) < 11004*(1000000**2)
    print('cycle_basins_1_to_26=', verify_cycle_reduction())
    print('n=136 happy_count=',Hh,'denominator=',Dh,'ratio=',round(Hh/Dh,12))
    print('n=224 happy_count=',Hl,'denominator=',Dl,'ratio=',round(Hl/Dl,12))
    print('CERTIFIED: limsup > 0.3718; liminf < 0.11004')

if __name__=='__main__': verify_bounds()
