#!/usr/bin/env python3
"""Independent finite exact-arithmetic checks of truncated Jacobian Koszul ranks."""
import itertools
import math

PRIME = 32003

def monomials_below(degree):
    result = []
    for total in range(degree):
        for positions in itertools.combinations_with_replacement(range(3), total):
            mon = [0, 0, 0]
            for pos in positions:
                mon[pos] += 1
            result.append(tuple(mon))
    return result

def derivative(poly, axis):
    out = {}
    for mon, coefficient in poly.items():
        if mon[axis]:
            nxt = list(mon)
            nxt[axis] -= 1
            nxt = tuple(nxt)
            out[nxt] = (out.get(nxt, 0) + coefficient * mon[axis]) % PRIME
    return {mon: value for mon, value in out.items() if value}

def syzygy_rank(a, b, perturbed):
    k = b - 1
    basis = monomials_below(k)
    lookup = {mon: pos for pos, mon in enumerate(basis)}
    width = len(basis)
    poly = {(a, 0, 0): 1, (0, b, 0): 1, (0, 0, b): 1}
    if perturbed:
        poly[(1, 0, b - 2)] = 1
    gradients = [derivative(poly, axis) for axis in range(3)]
    pivots = {}
    for i, j in ((0, 1), (0, 2), (1, 2)):
        for shift in basis:
            row = {}
            for axis, sign, derivative_poly in ((i, 1, gradients[j]), (j, -1, gradients[i])):
                for mon, coefficient in derivative_poly.items():
                    target = tuple(mon[t] + shift[t] for t in range(3))
                    if target in lookup:
                        col = axis * width + lookup[target]
                        row[col] = (row.get(col, 0) + sign * coefficient) % PRIME
            row = {col: value for col, value in row.items() if value}
            while row:
                lead = min(row)
                if lead not in pivots:
                    inv = pow(row[lead], -1, PRIME)
                    pivots[lead] = {col: value * inv % PRIME for col, value in row.items()}
                    break
                factor = row[lead]
                for col, value in pivots[lead].items():
                    reduced = (row.get(col, 0) - factor * value) % PRIME
                    if reduced:
                        row[col] = reduced
                    else:
                        row.pop(col, None)
    return len(pivots)

def higher_milnor(a, b, perturbed):
    k = b - 1
    ordinary = (a - 1) * (b - 1) ** 2
    return ordinary + 3 * math.comb(k + 2, 3) - syzygy_rank(a, b, perturbed)

def main():
    for a, b in ((3, 7), (3, 8), (4, 9), (4, 10), (5, 11)):
        exact = ((a - 1) * (b - 1) ** 2
                 + 3 * math.comb(b + 1, 3)
                 - 2 * math.comb(b - a + 2, 3))
        original = higher_milnor(a, b, False)
        perturbed = higher_milnor(a, b, True)
        assert original == exact and perturbed == exact - 1, (a, b, original, perturbed)
        print(f"a={a}, b={b}: principal={original}, perturbation={perturbed}")
    print("VERIFY_OK")

if __name__ == "__main__":
    main()
