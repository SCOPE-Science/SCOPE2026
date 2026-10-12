#!/usr/bin/env python3
"""Finite principal-filter verification of a product-modal correspondence."""
from itertools import product


def product_validity(n, m, rows_x, rows_y):
    # Each row bitmask is the generator of a (possibly improper) finite filter.
    full = (1 << (n * m)) - 1
    for x in range(n):
        for y in range(m):
            hx = sum(1 << (u * m + y) for u in range(n) if rows_x[x] & (1 << u))
            vy = sum(1 << (x * m + v) for v in range(m) if rows_y[y] & (1 << v))
            xy = sum(1 << (u * m + v) for u in range(n) for v in range(m)
                     if (rows_x[x] & (1 << u)) and (rows_y[y] & (1 << v)))
            for val in range(full + 1):
                if val & xy == xy and ((val & hx) != hx or (val & vy) != vy):
                    return False, (x, y, val)
    return True, None


def classification(n, m, a, b):
    all_improper = all(row == 0 for row in a) and all(row == 0 for row in b)
    all_T = all((row & (1 << x)) != 0 for x, row in enumerate(a)) and all(
        (row & (1 << y)) != 0 for y, row in enumerate(b))
    return all_improper or all_T


def run(n, m):
    total, yes, all_t, all_improper = 0, 0, 0, 0
    for a in product(range(1 << n), repeat=n):
        for b in product(range(1 << m), repeat=m):
            observed, _ = product_validity(n, m, a, b)
            predicted = classification(n, m, a, b)
            assert observed == predicted, (n, m, a, b, observed, predicted)
            total += 1
            yes += observed
            all_t += all(row & (1 << x) for x,row in enumerate(a)) and all(row & (1 << y) for y,row in enumerate(b))
            all_improper += all(row == 0 for row in a) and all(row == 0 for row in b)
    assert yes == all_t + all_improper
    return total, yes, all_t, all_improper


def main():
    for n,m in ((1,1),(1,2),(2,2),(2,3)):
        total,yes,t,imp=run(n,m)
        print(f'{n}x{m}: {total} ordered pairs of finite normal frames; sub valid {yes}; T-pairs {t}; both-improper {imp}')
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
