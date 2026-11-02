"""Finite exact-arithmetic cross-checks for the two-agent EF1 Nash-welfare bound.

Run: python3 verify.py
Enumeration is finite evidence; the universal theorem uses the analytic proof.
"""
from fractions import Fraction
from itertools import product


def ef1(values, bits):
    a = sum(v for v, b in zip(values, bits) if not b)
    b = sum(values) - a
    amax = max((v for v, t in zip(values, bits) if not t), default=0)
    bmax = max((v for v, t in zip(values, bits) if t), default=0)
    return a >= b - bmax and b >= a - amax


def check_instance(values):
    m = len(values)
    v = sum(values)
    heavy = max(values)
    delta = Fraction(heavy, v)
    prods = []
    for bits in product((0, 1), repeat=m):
        a = sum(w for w, t in zip(values, bits) if not t)
        prods.append((bits, a * (v - a)))
    opt = max(prod for _, prod in prods)
    assert opt > 0
    universal = 0
    heavy_checks = 0
    prefix_checks = 0
    for bits, prod in prods:
        if ef1(values, bits):
            universal += 1
            assert 2 * prod >= opt, (values, bits, prod, opt)
            if delta >= Fraction(1, 2):
                # 4h P >= (V+h) OPT  iff P/OPT >= (1+delta)/(4delta)
                assert 4 * heavy * prod >= (v + heavy) * opt, (values, bits, prod, opt)
                heavy_checks += 1
            if all(ef1(values[:t], bits[:t]) for t in range(1, m + 1)):
                prefix_checks += 1
    assert universal
    # Online least-load rule is prefix-EF1 without future knowledge.
    a = b = 0
    greedy = []
    for w in values:
        recipient = 0 if a <= b else 1
        greedy.append(recipient)
        if recipient == 0:
            a += w
        else:
            b += w
        assert ef1(values[:len(greedy)], tuple(greedy))
    assert 2 * a * b >= opt
    return universal, heavy_checks, prefix_checks


def main():
    instances = finals = heavy = temporal = 0
    for m in range(2, 8):
        for values in product((1, 2, 3, 4), repeat=m):
            e, h, p = check_instance(values)
            instances += 1
            finals += e
            heavy += h
            temporal += p
    # At every fixed delta >= 1/2, this three-good family attains equality.
    for t in range(2, 201):
        values = (1, 1, t)
        v = sum(values)
        heavy_value = max(values)
        allocation = (0, 1, 1)
        a = values[0]
        b = values[1] + values[2]
        assert all(ef1(values[:i], allocation[:i]) for i in range(1, 4))
        opt = 2 * t if t >= 2 else max(a * b, 2 * t)
        assert 4 * heavy_value * a * b == (v + heavy_value) * opt
    print(f"PASS instances={instances}, final_EF1_allocations={finals}, heavy_branch_checks={heavy}, prefix_EF1_allocations={temporal}, sharp_three_item_examples=199")

if __name__ == '__main__':
    main()
