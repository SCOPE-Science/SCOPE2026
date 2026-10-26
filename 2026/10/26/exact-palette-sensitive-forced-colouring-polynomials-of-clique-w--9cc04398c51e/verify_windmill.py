#!/usr/bin/env python3
"""Independent exhaustive validation of forcing-domain counts on clique bouquets.
Run: python verify_windmill.py
"""
from itertools import product
from math import comb, factorial


def polynomial(r, m, q):
    """Predicted ordinary generating polynomial, coefficient by seed count."""
    n = 1 + m * (r - 1)
    out = [0] * (n + 1)
    if q < r:
        return out
    pf = 1
    for j in range(r - 1):
        pf *= q - 1 - j
    total = q * pf ** m
    if q == r:
        scale = r * factorial(r - 1) ** m
        # Expand (1+z)*((r-1) z^(r-2) + z^(r-1))^m
        for a in range(m + 1):
            coeff = comb(m, a) * (r - 1) ** (m - a)
            exponent = m * (r - 2) + a
            out[exponent] += scale * coeff
            out[exponent + 1] += scale * coeff
        out[m * (r - 2)] -= scale * (r - 1)
    else:
        out[n] = total
        surjective = 0
        for j in range(q):
            t = q - 1 - j
            ff = 1
            for k in range(r - 1):
                ff *= t - k
            surjective += ((-1) ** j) * comb(q - 1, j) * ff ** m
        out[n - 1] += q * surjective
    return out


def brute(r, m, q):
    n = 1 + m * (r - 1)
    neighbors = [set() for _ in range(n)]
    for i in range(1, n):
        neighbors[0].add(i)
        neighbors[i].add(0)
    for p in range(m):
        block = list(range(1 + p * (r - 1), 1 + (p + 1) * (r - 1)))
        for u in block:
            for v in block:
                if u != v:
                    neighbors[u].add(v)
    neighbors = [tuple(sorted(x)) for x in neighbors]
    out = [0] * (n + 1)
    trials = 0
    good = 0
    for assignment in product(range(-1, q), repeat=n):
        trials += 1
        if any(assignment[v] == assignment[u] != -1 for v in range(n) for u in neighbors[v] if u < v):
            continue
        labels = list(assignment)
        while -1 in labels:
            changed = False
            for v in range(n):
                if labels[v] != -1:
                    continue
                used = {labels[u] for u in neighbors[v] if labels[u] != -1}
                if len(used) == q - 1:
                    labels[v] = next(color for color in range(q) if color not in used)
                    changed = True
                    break
            if not changed:
                break
        if -1 not in labels and all(labels[v] != labels[u] for v in range(n) for u in neighbors[v] if u < v):
            out[n - assignment.count(-1)] += 1
            good += 1
    return out, trials, good


def main():
    cases = [(3,1,3),(3,2,3),(3,2,4),(3,2,5),(3,2,6),
             (4,2,4),(4,2,5),(3,3,3),(3,3,4),
             (5,1,5),(2,3,2),(2,3,3)]
    total = 0
    for r,m,q in cases:
        model = polynomial(r,m,q)
        observed, trials, good = brute(r,m,q)
        assert model == observed, (r,m,q,model,observed)
        total += trials
        print(f'CASE r={r} m={m} q={q} trials={trials} accepted={good} coefficients={observed}')
    print(f'VERIFY_OK cases={len(cases)} complete_assignments={total}')

if __name__ == '__main__':
    main()
