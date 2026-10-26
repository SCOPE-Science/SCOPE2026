#!/usr/bin/env python3
"""Exact finite verification of a first change in optimal pollinator protection.

Pure Python standard library. All comparisons are exact integers or fractions.
"""
from collections import Counter
from fractions import Fraction
from itertools import permutations, product
import json

def connected(rows, pollinator_count):
    plant_count = len(rows)
    if any(mask == 0 for mask in rows):
        return False
    if any(not any(mask & (1 << j) for mask in rows)
           for j in range(pollinator_count)):
        return False
    parent = list(range(plant_count + pollinator_count))

    def root(vertex):
        while parent[vertex] != vertex:
            vertex = parent[vertex]
        return vertex

    for i, mask in enumerate(rows):
        for j in range(pollinator_count):
            if mask & (1 << j):
                parent[root(i)] = root(plant_count + j)
    return len({root(x) for x in range(len(parent))}) == 1

def score_coefficients(rows, pollinator_count):
    degrees = [mask.bit_count() for mask in rows]
    return tuple(tuple(sum(bool(mask & (1 << j)) and d == k
                           for mask, d in zip(rows, degrees))
                       for k in range(1, pollinator_count + 1))
                 for j in range(pollinator_count))

def quadratic_nonnegative_on_unit_interval(a, b, c):
    # The quadratic a + b q + c q^2 is checked at 0, 1 and,
    # when applicable, its unique interior minimum vertex.
    if a < 0 or a + b + c < 0:
        return False
    if c > 0 and -2*c < b < 0:
        return 4*a*c >= b*b
    return True

def universal_optima(coefficients):
    count = len(coefficients)
    winners = []
    for i in range(count):
        okay = True
        for j in range(count):
            diffs = [a - b for a, b in zip(coefficients[i], coefficients[j])]
            diffs += [0] * max(0, 3 - len(diffs))
            # In the <=7 census, pollinator_count<=6. For >3 coefficients
            # this quadratic criterion cannot be applied. We only call the
            # polynomial checker where m>=4 and hence pollinator_count<=3,
            # or where there are at most 3 plants (proved analytically).
            if len(coefficients[i]) > 3:
                raise ValueError("unsupported polynomial degree")
            if not quadratic_nonnegative_on_unit_interval(*diffs[:3]):
                okay = False
                break
        if okay:
            winners.append(i)
    return tuple(winners)

def canonical(rows, pollinator_count):
    return min(tuple(sorted(sum(((mask >> old_bit) & 1) << new_bit
                                for new_bit, old_bit in enumerate(perm))
                            for mask in rows))
               for perm in permutations(range(pollinator_count)))

def exact_survival_expectation(rows, protected, failure):
    pollinator_count = max(mask.bit_length() for mask in rows)
    other = [j for j in range(pollinator_count) if j != protected]
    survival = 1 - failure
    total = Fraction()
    for state in product((False, True), repeat=len(other)):
        live_mask = 1 << protected
        prob = Fraction(1)
        for bit, present in zip(other, state):
            if present:
                live_mask |= 1 << bit
                prob *= survival
            else:
                prob *= failure
        total += prob * sum(bool(mask & live_mask) for mask in rows)
    return total

def eval_benefit(coefficients, failure):
    return sum(Fraction(c) * failure ** (i + 1)
               for i, c in enumerate(coefficients))

def main():
    census = []
    exceptional = Counter()
    for order in range(2, 8):
        for plant_count in range(1, order):
            pollinator_count = order - plant_count
            total_connected = 0
            switching = 0
            for rows in product(range(1 << pollinator_count),
                                repeat=plant_count):
                if not connected(rows, pollinator_count):
                    continue
                total_connected += 1
                if plant_count <= 3 or pollinator_count <= 2:
                    # Analytically, all these graphs have a persistent
                    # optimal pollinator; no finite grid is used.
                    continue
                winners = universal_optima(score_coefficients(rows, pollinator_count))
                if not winners:
                    switching += 1
                    exceptional[canonical(rows, pollinator_count)] += 1
            census.append((order, plant_count, pollinator_count,
                           total_connected, switching))
    assert all(rare == 0 for n, p, t, count, rare in census if n <= 6)
    assert sum(rare for n, p, t, count, rare in census if n == 7) == 108
    assert exceptional == Counter({(1,3,6,6):72, (1,6,6,7):36})
    assert next(rec[3] for rec in census if rec[:3] == (7,4,3)) == 1795
    witnesses = []
    for rows in ((1,3,6,6), (1,6,6,7)):
        coeff = score_coefficients(rows,3)
        for fail in (Fraction(1,4), Fraction(3,4)):
            real = tuple(exact_survival_expectation(rows,j,fail)
                         for j in range(3))
            base = sum(1 - fail ** mask.bit_count() for mask in rows)
            derived = tuple(base + eval_benefit(poly, fail) for poly in coeff)
            assert real == derived
            witnesses.append({
                "row_masks": list(rows), "failure_probability":str(fail),
                "expected_surviving_plants": list(map(str,real)),
                "best_pollinator_zero_based": [j for j,x in enumerate(real)
                                               if x == max(real)]})
    assert all(row["best_pollinator_zero_based"] == [0]
               for row in witnesses if row["failure_probability"] == "1/4")
    assert all(row["best_pollinator_zero_based"] == ([1] if row["row_masks"] == [1,3,6,6] else [1,2])
               for row in witnesses if row["failure_probability"] == "3/4")
    report = {
        "status":"PASS", "method":"exact integer quadratic positivity and subset enumeration",
        "labeled_connected_4x3":1795, "switching_labeled_4x3":108,
        "switching_unlabeled_classes":{
            "1,3,6,6":72,"1,6,6,7":36
        },
        "census":[{"order":n,"plants":m,"pollinators":t,
                   "connected_labeled":c,"switching_labeled":s}
                  for n,m,t,c,s in census],
        "independent_witness_checks":witnesses,
    }
    print(json.dumps(report,sort_keys=True,separators=(",",":")))

if __name__=="__main__":
    main()
