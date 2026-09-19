from itertools import product


def enumerate_ranges(a, b, lazy):
    # Root A[0] at zero. Diameter bounds the needed candidate heights.
    a_values = range(-2, 3)
    b_values = range(-1, 2)
    counts = {}
    for tail in product(a_values, repeat=a - 1):
        A = (0,) + tail
        for B in product(b_values, repeat=b):
            good = True
            for x in A:
                for y in B:
                    gap = abs(x - y)
                    if (gap > 1) if lazy else (gap != 1):
                        good = False
                        break
                if not good:
                    break
            if good:
                values = A + B
                r = max(values) - min(values)
                counts[r] = counts.get(r, 0) + 1
    return counts


def standard_formula(a, b):
    total = 2**a + 2**b - 2
    ans = {1: 2, 2: total - 2}
    return {r: c for r, c in ans.items() if c}


def lazy_formula(a, b):
    n = a + b
    total = 3**a + 3**b + 2**n - 2**(a + 1) - 2**(b + 1) + 1
    ans = {0: 1, 1: 2**n - 2, 2: total - 2**n + 1}
    return {r: c for r, c in ans.items() if c}


checked = 0
for a in range(1, 5):
    for b in range(1, 5):
        s = enumerate_ranges(a, b, False)
        l = enumerate_ranges(a, b, True)
        assert s == standard_formula(a, b), (a, b, s, standard_formula(a, b))
        assert l == lazy_formula(a, b), (a, b, l, lazy_formula(a, b))
        checked += 1

print(f"verified {checked} pairs with 1 <= a,b <= 4")
print("all standard and lazy range coefficients match")
print("K_2,3 standard:", standard_formula(2, 3))
print("K_2,3 lazy:", lazy_formula(2, 3))
