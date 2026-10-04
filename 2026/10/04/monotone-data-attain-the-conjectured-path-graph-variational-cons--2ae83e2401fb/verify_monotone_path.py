from fractions import Fraction
from itertools import combinations_with_replacement

def maximal_path(values):
    n = len(values)
    out = []
    for i in range(n):
        best = Fraction(-1, 1)
        for r in range(n):
            a = max(0, i - r)
            b = min(n - 1, i + r)
            avg = sum(values[a:b+1], Fraction(0, 1)) / (b - a + 1)
            if avg > best:
                best = avg
        out.append(best)
    return out

def variation(values):
    return sum(abs(values[i+1] - values[i]) for i in range(len(values)-1))

checked = 0
for n in range(3, 9):
    for raw in combinations_with_replacement(range(4), n):
        f = [Fraction(x, 1) for x in raw]
        mf = maximal_path(f)
        lhs = variation(mf)
        mean = sum(f, Fraction(0, 1)) / n
        exact = f[-1] - mean
        rhs = Fraction(n - 1, n) * variation(f)

        assert all(mf[i] <= mf[i+1] for i in range(n-1))
        assert lhs == exact
        assert lhs <= rhs

        if variation(f) > 0:
            equality = (lhs == rhs)
            expected = all(f[i] == f[0] for i in range(n-1)) and f[-1] > f[0]
            assert equality == expected

        g = list(reversed(f))
        mg = maximal_path(g)
        lhs_g = variation(mg)
        mean_g = sum(g, Fraction(0, 1)) / n
        exact_g = g[0] - mean_g
        rhs_g = Fraction(n - 1, n) * variation(g)

        assert all(mg[i] >= mg[i+1] for i in range(n-1))
        assert lhs_g == exact_g
        assert lhs_g <= rhs_g

        if variation(g) > 0:
            equality_g = (lhs_g == rhs_g)
            expected_g = g[0] > g[1] and all(g[i] == g[1] for i in range(1, n))
            assert equality_g == expected_g

        checked += 1

print(f"checked_monotone_sequences={checked}")
print("n_range=3..8")
print("value_set={0,1,2,3}")
print("exact_formula=OK")
print("sharp_bound=OK")
print("equality_classification=OK")
print("reflection_case=OK")
print("VERIFY_OK")
