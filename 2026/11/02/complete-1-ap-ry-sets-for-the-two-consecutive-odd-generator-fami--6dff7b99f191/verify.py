"""Exact independent finite tests for consecutive-odd first-double-representation Apéry formulas."""
from functools import lru_cache


def predicted(a, kind):
    b = 2*a+1
    if kind == "plus":
        return [4*b+2*s if s < 2 else 2*b+2*s for s in range(b)]
    if kind == "minus":
        return [5*b+2*s if s < 2 else (2*b+2*s if s <= b-3 else 3*b+2*s)
                for s in range(b)]
    raise ValueError(kind)


def expected_uniques(a, kind):
    b = 2*a+1
    if kind == "plus":
        return {b+2*i for i in range(a+2)} | {2*b, 2*b+2, 3*b, 3*b+2}
    return {b+2*i for i in range(a+1)} | {
        2*b, 2*b+2, 3*b, 3*b+2, 4*b-4, 4*b-2, 4*b, 4*b+2}


def dp_counts(coins, bound):
    # Count distinct multiplicity vectors, truncating at 3.
    counts = [0]*(bound+1)
    counts[0] = 1
    for c in coins:
        for n in range(c, bound+1):
            counts[n] = min(3, counts[n] + counts[n-c])
    return counts


def brute_counts(coins, bound):
    # Independent top-down enumeration by the multiplicity of the next coin.
    @lru_cache(None)
    def f(index, remainder):
        if index == len(coins):
            return int(remainder == 0)
        coin = coins[index]
        total = 0
        for k in range(remainder // coin + 1):
            total += f(index+1, remainder - k*coin)
            if total >= 3:
                return 3
        return total
    return [f(0, n) for n in range(bound+1)]


def run():
    cases = residues = singleton_checks = brute_cases = 0
    for a in range(1, 151):
        b = 2*a+1
        for kind in ("plus", "minus"):
            if kind == "minus" and a == 1:
                continue
            coins = [b+2*i for i in range(a+2 if kind == "plus" else a+1)]
            predicted_w = predicted(a, kind)
            upper = max(predicted_w)+b
            counts = dp_counts(coins, upper)
            if a <= 10:
                assert brute_counts(coins, upper) == counts
                brute_cases += 1
            calculated = []
            for s in range(b):
                w = 2*s
                while counts[w] <= 1:
                    w += b
                calculated.append(w)
            assert calculated == predicted_w, (a, kind, calculated, predicted_w)
            genus = sum((w-(2*s % b))//b for s, w in enumerate(calculated))
            assert genus == (5*a+6 if kind == "plus" else 5*a+10)
            first_double = {n for n in range(upper+1) if counts[n] >= 2}
            assert all((n+b) in first_double for n in first_double if n+b <= upper)
            unique = {n for n in range(1, upper+1) if counts[n] == 1}
            assert unique == expected_uniques(a,kind), (a,kind,unique ^ expected_uniques(a,kind))
            assert max(n for n in range(upper+1) if counts[n] <= 1) == (
                3*b+2 if kind=="plus" else 4*b+2)
            cases += 1
            residues += b
            singleton_checks += upper + 1
    print("VERIFY_OK cases=%d residue_classes=%d checked_integers=%d independent_recursive_cases=%d exact_integer=yes" % (
        cases,residues,singleton_checks,brute_cases))

if __name__ == "__main__":
    run()
