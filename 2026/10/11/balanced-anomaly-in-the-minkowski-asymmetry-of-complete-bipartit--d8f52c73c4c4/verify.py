"""Independent exact-fraction checks for the complete-bipartite spanning-tree asymmetry formula.

Usage: python verify.py
Requires Python 3 standard library only. Finite checks corroborate, not replace, the proof.
"""
from fractions import Fraction
from itertools import combinations


def predicted(p, q):
    num = (p - 1) * (q - 1) * (p + q - 1)
    den = p * p - 2 * p + q * q - 2 * q + 1
    return max(Fraction(p - 1), Fraction(q - 1), Fraction(num, den))


def trees(p, q):
    edges = [(i, p + j) for i in range(p) for j in range(q)]
    for comb in combinations(range(len(edges)), p + q - 1):
        roots = list(range(p + q))
        def find(u):
            while roots[u] != u:
                u = roots[u]
            return u
        valid = True
        for e in comb:
            u, v = edges[e]
            u, v = find(u), find(v)
            if u == v:
                valid = False
                break
            roots[u] = v
        if valid:
            mask = sum(1 << e for e in comb)
            yield mask


def verify(p, q):
    tr = list(trees(p, q))
    assert tr, (p, q)
    t = Fraction(p + q - 1, p * q)
    edges = [(i, p + j) for i in range(p) for j in range(q)]
    ratios = [Fraction(1, t) - 1]  # each nonnegativity inequality -x_e<=0
    checks = 0
    for size in range(2, p + q):
        for S in combinations(range(p + q), size):
            cut = sum((1 << e) for e, (u, v) in enumerate(edges) if u in S and v in S)
            if not cut:
                continue
            vals = [(T & cut).bit_count() for T in tr]
            low, high = min(vals), max(vals)
            assert high == min(len(S) - 1, cut.bit_count()), (p, q, S, high)
            mean = t * cut.bit_count()
            if high > mean:
                r = (mean - low) / (high - mean)
                ratios.append(r)
            checks += len(tr)
    # All inequalities' feasible reflected factors obtained by exhausting original vertices.
    assert max(ratios) == predicted(p, q), (p, q, max(ratios), predicted(p, q))
    # Check phase law separately.
    if p == q:
        assert max(ratios) > p - 1
    else:
        assert max(ratios) == max(p, q) - 1
    return len(tr), checks, max(ratios)


def main():
    total_trees = total_checks = 0
    profiles = [(p, q) for p in range(2, 5) for q in range(p, 5)]
    profiles += [(2, 5), (3, 5)]
    for p, q in profiles:
        ntrees, checks, asym = verify(p, q)
        total_trees += ntrees
        total_checks += checks
        print(f'K_{{{p},{q}}}: spanning_trees={ntrees}, asymmetry={asym}')
    print(f'PASS profiles={len(profiles)} trees={total_trees} vertex-subset-comparisons={total_checks}')


if __name__ == '__main__':
    main()
