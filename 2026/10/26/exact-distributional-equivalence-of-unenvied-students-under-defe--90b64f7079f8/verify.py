#!/usr/bin/env python3
"""Exact finite checks for unenvied-count equivalence in random school choice."""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, permutations, product
from math import factorial, prod


def rsd_counts(n):
    """Exhaust all fixed-priority RSD preference profiles for n<=4."""
    orders = tuple(permutations(range(n)))
    freq = Counter()
    incidences = Counter()
    total = len(orders) ** n
    for preferences in product(orders, repeat=n):
        available = set(range(n))
        assigned = []
        for pref in preferences:
            obj = next(x for x in pref if x in available)
            assigned.append(obj)
            available.remove(obj)
        unenvied = tuple(i for i in range(n)
                         if all(preferences[j].index(assigned[j]) <
                                preferences[j].index(assigned[i])
                                for j in range(n) if j != i))
        freq[len(unenvied)] += 1
        for size in range(1, n+1):
            for subset in combinations(unenvied, size):
                incidences[subset] += 1
    return {k: Fraction(v, total) for k, v in freq.items()}, incidences, total


def da_counts(n):
    """Exhaust both sides' independent strict preferences for n<=3."""
    orders = tuple(permutations(range(n)))
    freq = Counter()
    total = len(orders) ** (2*n)
    for student_prefs in product(orders, repeat=n):
        for school_priorities in product(orders, repeat=n):
            next_choice = [0]*n
            held = [None]*n
            free = list(range(n))
            while free:
                student = free.pop()
                school = student_prefs[student][next_choice[student]]
                next_choice[student] += 1
                incumbent = held[school]
                if incumbent is None:
                    held[school] = student
                elif school_priorities[school].index(student) < school_priorities[school].index(incumbent):
                    held[school] = student
                    free.append(incumbent)
                else:
                    free.append(student)
            assigned = [None]*n
            for school, student in enumerate(held):
                assigned[student] = school
            unenvied = sum(all(student_prefs[j].index(assigned[j]) <
                               student_prefs[j].index(assigned[i])
                               for j in range(n) if j != i)
                            for i in range(n))
            freq[unenvied] += 1
    return {k: Fraction(v, total) for k, v in freq.items()}, total


@lru_cache(maxsize=None)
def coupon_state(n, seen, singleton):
    """Exact law of singleton count at cover; discard self-loops analytically."""
    if seen == n:
        return {singleton: Fraction(1)}
    out = Counter()
    changing = n-seen+singleton
    new_chance = Fraction(n-seen, changing)
    for val, chance in coupon_state(n, seen+1, singleton+1).items():
        out[val] += new_chance*chance
    if singleton:
        repeated_chance = Fraction(singleton, changing)
        for val, chance in coupon_state(n, seen, singleton-1).items():
            out[val] += repeated_chance*chance
    return dict(out)


def joint_formula(n, selected):
    """Expected probability that all fixed serial positions remain unenvied."""
    r = len(selected)
    return Fraction(factorial(r), prod(n-i+j for j, i in enumerate(selected)))


def product_formula(n, selected):
    acc = Fraction(1)
    for t in range(1, n):
        old = sum(i<t for i in selected)
        acc *= Fraction(n-t, n-t+old)
    return acc


def run():
    checks = 0
    for n in range(1, 9):
        coupon = coupon_state(n, 0, 0)
        assert sum(coupon.values(), Fraction(0)) == 1
        assert sum(k*p for k,p in coupon.items()) == sum((Fraction(1, j) for j in range(1, n+1)), Fraction(0))
        checks += 2
        for r in range(1, n+1):
            for S in combinations(range(n), r):
                assert joint_formula(n, S) == product_formula(n, S)
                checks += 1
    for n in range(1, 5):
        law, inc, total = rsd_counts(n)
        assert law == coupon_state(n, 0, 0)
        checks += 1
        for r in range(1, n+1):
            for S in combinations(range(n), r):
                assert Fraction(inc[S], total) == joint_formula(n, S)
                checks += 1
        print(f'RSD n={n}: profiles={total}, law={law}')
    for n in range(1, 4):
        law, total = da_counts(n)
        assert law == coupon_state(n, 0, 0)
        checks += 1
        print(f'DA n={n}: profiles={total}, law={law}')
    print(f'PASS: {checks} exact identities/probability checks (plus {sum(factorial(n)**n for n in range(1,5))} RSD and {sum(factorial(n)**(2*n) for n in range(1,4))} DA preference profiles)')


if __name__ == '__main__':
    run()
