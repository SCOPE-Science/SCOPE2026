from fractions import Fraction
from itertools import product


def H(x):
    x = Fraction(x)
    if x > Fraction(1, 2):
        return H(1 - x)
    if x <= Fraction(1, 3):
        return x - Fraction(3, 2) * x * x
    y = 1 - x
    return y / 2 - Fraction(3, 8) * y * y


def Phi(m, a):
    if m == 0:
        return Fraction(0)
    return m * m * H(Fraction(a, m))


def h_table(M):
    h = [[0]]
    if M >= 1:
        h.append([0, 0])
    for m in range(2, M + 1):
        prev = h[m - 2]
        row = []
        for a in range(m + 1):
            vals = []
            if a <= m - 2:
                vals.append(prev[a] + a)
            if 0 <= a - 1 <= m - 2:
                vals.append(prev[a - 1] + max(a, m - a))
            if 0 <= a - 2 <= m - 2:
                vals.append(prev[a - 2] + (m - a))
            row.append(max(vals))
        h.append(row)
    return h


def direct_cut(m, bits):
    total = 0
    for i in range(1, m + 1):
        for j in range(i + 1, m + 1):
            if i + j <= m + 1 and bits[i - 1] != bits[j - 1]:
                total += 1
    return total


def brute_fixed_size(m, a):
    best = -1
    for bits in product((0, 1), repeat=m):
        if sum(bits) == a:
            best = max(best, direct_cut(m, bits))
    return best


def bellman_phi(m, a):
    vals = []
    if a <= m - 2:
        vals.append(Phi(m - 2, a) + a)
    if 0 <= a - 1 <= m - 2:
        vals.append(Phi(m - 2, a - 1) + max(a, m - a))
    if 0 <= a - 2 <= m - 2:
        vals.append(Phi(m - 2, a - 2) + (m - a))
    return max(vals)


MAX_M = 1000
h = h_table(MAX_M)

# Directly validate the threshold-graph recurrence on small instances.
for m in range(1, 13):
    for a in range(m + 1):
        assert h[m][a] == brute_fixed_size(m, a)

# The exact low-density branch used as a check on the closed form.
for m in range(1, 301):
    for a in range(m + 1):
        if 3 * a <= m:
            target = Fraction(a * m) - Fraction(3 * a * a - a, 2)
            assert h[m][a] == target

# Check the Bellman comparison residual for a wide finite range.
max_residual = Fraction(0)
for m in range(2, MAX_M + 1):
    for a in range(m + 1):
        r = abs(Phi(m, a) - bellman_phi(m, a))
        max_residual = max(max_residual, r)
assert max_residual <= Fraction(1, 2)

# Check the O(m) comparison induced by the residual bound.
for m in range(MAX_M + 1):
    bound = Fraction((m // 2), 2)
    for a in range(m + 1):
        assert abs(Fraction(h[m][a]) - Phi(m, a)) <= bound

# Compute the weighted maximum that equals half the rainbow count for n=2m.
print("max Bellman residual through m=1000:", max_residual)
print("target limiting constant:", float(Fraction(9, 22)))
for m in (100, 200, 500, 1000):
    M = max(a * (m - a) + h[m][a] for a in range(m + 1))
    arg = [a for a in range(m + 1) if a * (m - a) + h[m][a] == M]
    print(m, M, float(Fraction(M, m * m)), arg[:8])

print("verification passed")
