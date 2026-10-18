#!/usr/bin/env python3
"""Exhaustive finite-conductor checker for terminal-gap numerical semigroups.

The enumeration tests ideal closure and the numerical double dual independently
of the binary-word theorem. All tested ideals contain zero and the ambient semigroup.
"""
from math import comb


def no_singleton_zero_words(n):
    return sum(comb(n-k+1, 2*k) for k in range((n+1)//3+1))


def enumerate_ideals(m, terminal_gaps):
    conductor = 2*m
    missing = list(range(1, m)) + list(range(2*m-terminal_gaps, 2*m))
    small_s = set(range(conductor)).difference(missing)
    positive_s = sorted(s for s in small_s if s)

    def in_semigroup(z):
        return z >= conductor or z in small_s

    def valid_ideal(extra):
        # The complement beyond the conductor is empty, so only small sums matter.
        small_ideal = small_s.union(extra)
        return all(x+y >= conductor or x+y in small_ideal
                   for x in extra for y in positive_s)

    def double_dual(extra):
        small_ideal = small_s.union(extra)
        # Any element in S-I must be in S because 0 lies in I.
        colon_small = {x for x in small_s
                       if all(in_semigroup(x+y) for y in small_ideal)}
        # Every x >= conductor lies in S-I, and every y >= conductor
        # is automatically safe when evaluating a nonnegative x.
        dual_small = {x for x in range(conductor)
                      if all(in_semigroup(x+y) for y in colon_small)}
        return dual_small == small_ideal

    total = reflexive = 0
    for mask in range(1 << len(missing)):
        extra = {g for i,g in enumerate(missing) if mask & (1 << i)}
        if valid_ideal(extra):
            total += 1
            if double_dual(extra):
                reflexive += 1
    return total, reflexive


def main():
    for m in range(3, 14):
        total, reflexive = enumerate_ideals(m, 2)
        predicted = (2**(m-1)+5, no_singleton_zero_words(m-1)+1)
        assert (total, reflexive) == predicted, (m, total, reflexive, predicted)
        total1, reflexive1 = enumerate_ideals(m, 1)
        predicted1 = 2**(m-1)+1
        assert (total1,reflexive1) == (predicted1,predicted1), (m,total1,reflexive1)
        print(f"m={m}: 2-gap totals={total}, reflexive={reflexive}; "
              f"1-gap both={total1}")
    print('VERIFY_OK: 22 exhaustive semigroup families; independent ideal and double-dual membership')


if __name__ == '__main__':
    main()
