from functools import lru_cache
from itertools import combinations
import math


def closed_neighborhoods(n):
    out = []
    for i in range(n):
        mask = 1 << i
        for j in range(n):
            if i != j:
                mask |= 1 << (n + j)
        out.append(mask)
    for i in range(n):
        mask = 1 << (n + i)
        for j in range(n):
            if i != j:
                mask |= 1 << j
        out.append(mask)
    return out


def predicted_set(n, mask):
    A = {i for i in range(n) if (mask >> i) & 1}
    B = {i for i in range(n) if (mask >> (n + i)) & 1}
    p, q = len(A), len(B)
    if (p, q) in ((n, 0), (0, n)):
        return True
    if (p, q) == (n - 1, 1):
        return next(iter(B)) in A
    if (p, q) == (1, n - 1):
        return next(iter(A)) in B
    if (p, q) in ((n - 2, 2), (2, n - 2)):
        return len(A & B) <= 1
    return False


def predicted_order_count(n, mask):
    A = {i for i in range(n) if (mask >> i) & 1}
    B = {i for i in range(n) if (mask >> (n + i)) & 1}
    p, q = len(A), len(B)
    if (p, q) in ((n, 0), (0, n)):
        return math.factorial(n)
    if (p, q) in ((n - 1, 1), (1, n - 1)) and len(A & B) == 1:
        return math.factorial(n - 1) + math.factorial(n - 2)
    if (p, q) in ((n - 2, 2), (2, n - 2)):
        if len(A & B) == 1:
            return math.factorial(n - 2)
        if len(A & B) == 0:
            return 2 * math.factorial(n - 2)
    return 0


def exact_order_count(n, mask, neighborhoods):
    vertices = [v for v in range(2 * n) if (mask >> v) & 1]
    full = (1 << (2 * n)) - 1

    @lru_cache(None)
    def dp(used_local, covered):
        if used_local == (1 << len(vertices)) - 1:
            return int(covered == full)
        total = 0
        for local, v in enumerate(vertices):
            if (used_local >> local) & 1:
                continue
            if neighborhoods[v] & ~covered:
                total += dp(used_local | (1 << local), covered | neighborhoods[v])
        return total

    return dp(0, 0)


def global_maximum_length(n, neighborhoods):
    full = (1 << (2 * n)) - 1

    @lru_cache(None)
    def best(used, covered):
        if covered == full:
            return 0
        ans = -10**9
        for v in range(2 * n):
            if (used >> v) & 1:
                continue
            if neighborhoods[v] & ~covered:
                ans = max(ans, 1 + best(used | (1 << v), covered | neighborhoods[v]))
        return ans

    return best(0, 0)


total_sets = 0
total_sequences = 0
for n in range(5, 8):
    neighborhoods = closed_neighborhoods(n)
    assert global_maximum_length(n, neighborhoods) == n
    sets_n = 0
    seq_n = 0
    for chosen in combinations(range(2 * n), n):
        mask = sum(1 << v for v in chosen)
        exact = exact_order_count(n, mask, neighborhoods)
        expected = predicted_order_count(n, mask)
        assert exact == expected
        assert (exact > 0) == predicted_set(n, mask)
        if exact:
            sets_n += 1
            seq_n += exact
    assert sets_n == 2 + n * (n - 1) * (2 * n - 1)
    assert seq_n == 4 * n * math.factorial(n)
    total_sets += sets_n
    total_sequences += seq_n

print(f"VERIFY_OK n_range=5..7 maximum_sets={total_sets} maximum_sequences={total_sequences} max_order=14")
