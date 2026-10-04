#!/usr/bin/env python3
from itertools import product
from math import factorial

def check_axioms(op, n):
    top = n - 1
    def f(a, b):
        return op[a][b]

    # P1, P2, P3, P4, P5.
    for a in range(n):
        if f(top, a) > a:
            return False
    for a in range(n):
        for b in range(n):
            if min(a, b) > f(a, b):
                return False
            if f(a, b) > f(a, min(a, b)):
                return False
            for c in range(n):
                if f(a, min(b, c)) > f(a, b):
                    return False
                if f(a, f(min(a, b), c)) > f(min(a, b), c):
                    return False

    # T conditions.
    for a in range(n):
        if f(a, a) != top:
            return False
        if min(a, f(a, 0)) != 0:
            return False

    # F condition.
    for a in range(n):
        neg = f(a, 0)
        negneg = f(neg, 0)
        if a > negneg:
            return False

    return True

def from_births(n, births):
    top = n - 1
    op = [[None] * n for _ in range(n)]

    for a in range(n):
        if a == 0:
            fixed = [top]
        elif a == top:
            fixed = list(range(n))
        else:
            fixed = [0]
            fixed += [
                j for j in range(1, a)
                if births[j] <= a
            ]
            fixed.append(top)
            fixed = sorted(set(fixed))

        for b in range(n):
            op[a][b] = min(x for x in fixed if x >= b)

    return tuple(tuple(row) for row in op)

def all_birth_ops(n):
    if n == 2:
        return {from_births(n, {})}
    js = list(range(1, n - 1))
    choices = [list(range(j + 1, n)) for j in js]
    out = set()
    for vals in product(*choices):
        births = dict(zip(js, vals))
        out.add(from_births(n, births))
    return out

def heyting(n):
    top = n - 1
    return tuple(
        tuple(top if a <= b else b for b in range(n))
        for a in range(n)
    )

# Constructive side through n=9.
for n in range(2, 10):
    ops = all_birth_ops(n)
    assert len(ops) == factorial(n - 2), (n, len(ops))
    assert all(check_axioms(op, n) for op in ops)

    H = heyting(n)
    assert H in ops
    assert sum(op == H for op in ops) == 1

    # All induce the same chain negation.
    for op in ops:
        neg = [op[a][0] for a in range(n)]
        assert neg[0] == n - 1
        assert neg[1:] == [0] * (n - 1)

# Independent brute force through n=6.
for n in range(2, 7):
    top = n - 1
    variable = []
    fixed = {}

    for a in range(n):
        for b in range(n):
            if a == 0:
                fixed[a, b] = top
            elif a == top:
                fixed[a, b] = b
            elif b >= a:
                fixed[a, b] = top
            elif b == 0:
                fixed[a, b] = 0
            else:
                variable.append((a, b))

    ranges = [range(b, n) for a, b in variable]
    brute = set()

    for vals in product(*ranges):
        table = [[None] * n for _ in range(n)]
        for (a, b), v in fixed.items():
            table[a][b] = v
        for (a, b), v in zip(variable, vals):
            table[a][b] = v
        op = tuple(tuple(row) for row in table)
        if check_axioms(op, n):
            brute.add(op)

    constructed = all_birth_ops(n)
    assert brute == constructed, (n, len(brute), len(constructed))
    assert len(brute) == factorial(n - 2)

assert len(all_birth_ops(4)) == 2
assert len(all_birth_ops(3)) == 1

print("VERIFY_OK")
