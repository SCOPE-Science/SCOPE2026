from fractions import Fraction
from itertools import combinations

def sample_variance(xs):
    n = len(xs)
    s = sum(xs)
    q = sum(x*x for x in xs)
    return (Fraction(q) - Fraction(s*s, n)) / (n-1)

def formula(n, r):
    return Fraction(r*(n+1)*((n+2)*r-(n-2)), 12*n*(n-1))

def run(max_M=17):
    subsets = 0
    strata = 0
    assertions = 0
    for M in range(2, max_M+1):
        population = range(M+1)
        for n in range(2, M+2):
            by_range = {}
            for xs in combinations(population, n):
                subsets += 1
                r = xs[-1] - xs[0]
                by_range.setdefault(r, []).append(sample_variance(xs))
            for r, vals in by_range.items():
                strata += 1
                exact = sum(vals, Fraction(0)) / len(vals)
                assert exact == formula(n, r)
                assertions += 1
                assert r >= n-1 and r <= M
                assertions += 1
    print("VERIFY_OK")
    print(f"max_M={max_M}")
    print(f"subsets_enumerated={subsets}")
    print(f"range_strata={strata}")
    print(f"exact_assertions={assertions}")

if __name__ == "__main__":
    run()
