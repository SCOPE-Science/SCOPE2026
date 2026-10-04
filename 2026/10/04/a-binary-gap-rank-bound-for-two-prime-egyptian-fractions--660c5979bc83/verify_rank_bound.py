#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations_with_replacement
from math import ceil

TABLE4 = {
    3:3,5:4,7:5,11:6,13:6,17:6,19:7,23:8,29:8,31:9,37:8,41:8,
    43:8,47:10,53:9,59:10,61:10,67:9,71:10,73:9,79:11,83:10,89:10,
    97:9,101:10,103:11,107:10,109:11,113:10,127:13,131:10,137:10,
    139:11,149:11,151:11,157:12,163:11,167:12,173:12,179:12,181:12,
    191:14,193:10,197:11,199:12,211:12,223:13,227:12,229:12,233:12,
    239:12,241:12,251:14,257:10,
}

def floor_log2(n):
    return n.bit_length() - 1

def lower_bound(p):
    return floor_log2(p) + 2

def ceil_fraction(n, d):
    return (n + d - 1) // d

def discrete_rhs(p, r):
    return r + ceil_fraction(p, 1 << r)

def check_gap_small():
    for r in range(0, 9):
        if r == 0:
            assert Fraction(1) >= Fraction(1, 1 << r)
            continue
        for exps in combinations_with_replacement(range(1, 11), r):
            s = sum((Fraction(1, 1 << a) for a in exps), Fraction(0))
            if s < 1:
                assert 1 - s >= Fraction(1, 1 << r), (r, exps, s)

def check_discrete_optimization():
    for p in range(3, 20001, 2):
        k = floor_log2(p)
        for r in range(0, k + 12):
            assert discrete_rhs(p, r) >= k + 2, (p, r)

def check_table4():
    for p, rank in TABLE4.items():
        assert rank >= lower_bound(p), (p, rank, lower_bound(p))

def check_fermat_identity():
    for n, p in enumerate((3, 5, 17, 257, 65537)):
        k = 1 << n
        assert p == (1 << k) + 1
        s = sum((Fraction(1, 1 << j) for j in range(1, k + 1)), Fraction(0))
        s += Fraction(1, p) + Fraction(1, (1 << k) * p)
        assert s == 1
        assert lower_bound(p) == k + 2

if __name__ == '__main__':
    check_gap_small()
    check_discrete_optimization()
    check_table4()
    check_fermat_identity()
    print('VERIFY_OK')
