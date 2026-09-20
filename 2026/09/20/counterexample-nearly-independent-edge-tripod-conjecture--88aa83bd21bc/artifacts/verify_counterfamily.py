from functools import lru_cache

@lru_cache(None)
def F(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return F(n - 1) + F(n - 2)

def q(t):
    """Number of vertex subsets of P_t inducing exactly one edge."""
    if t <= 1:
        return 0
    return (2 * t * F(t + 1) - (t + 1) * F(t)) // 5

def z_tripod(a, b, c):
    """Z_1([P_a,P_b,P_c]) from the line-graph arm-state decomposition."""
    arm = (a, b, c)
    total = 0
    for i in range(3):
        x = arm[i]
        y = arm[(i + 1) % 3]
        z = arm[(i + 2) % 3]
        total += q(x) * F(y + 1) * F(z + 1)
        total += q(x - 1) * (F(y) * F(z + 1) + F(y + 1) * F(z))
    total += F(a) * F(b) * F(c + 1)
    total += F(a) * F(b + 1) * F(c)
    total += F(a + 1) * F(b) * F(c)
    return total

def tripod_edges(a, b, c):
    edges = []
    nxt = 1
    for length in (a, b, c):
        prev = 0
        for _ in range(length):
            cur = nxt
            nxt += 1
            edges.append((prev, cur))
            prev = cur
    return edges

def brute_z1(a, b, c):
    """Directly enumerate all edge subsets; intended only for the 20-edge checks below."""
    edges = tripod_edges(a, b, c)
    m = len(edges)
    adj = [0] * m
    for i, e in enumerate(edges):
        for j, f in enumerate(edges):
            if i != j and (e[0] in f or e[1] in f):
                adj[i] |= 1 << j
    pair_count = bytearray(1 << m)
    answer = 0
    for mask in range(1, 1 << m):
        bit = mask & -mask
        i = bit.bit_length() - 1
        rest = mask ^ bit
        value = pair_count[rest] + (adj[i] & rest).bit_count()
        pair_count[mask] = 2 if value > 1 else value
        if value == 1:
            answer += 1
    return answer

def predicted_difference(n):
    d = n - 7
    return 2 * (d - 1) * F(d + 1) - 3 * d * F(d)

# Formula and direct-enumeration check at the first counterexample order.
a = z_tripod(2, 2, 16)
c = z_tripod(3, 3, 14)
print("n=21 formula [P2,P2,P16] =", a)
print("n=21 formula [P3,P3,P14] =", c)
print("n=21 formula difference =", a - c)
print("n=21 brute [P2,P2,P16] =", brute_z1(2, 2, 16))
print("n=21 brute [P3,P3,P14] =", brute_z1(3, 3, 14))

# Check the closed difference identity and positivity through a substantial finite range.
closed_ok = True
positive_ok = True
for n in range(21, 201):
    lhs = z_tripod(2, 2, n - 5) - z_tripod(3, 3, n - 7)
    closed_ok &= lhs == predicted_difference(n)
    positive_ok &= lhs > 0
print("closed difference identity n=21..200 =", closed_ok)
print("counterfamily inequality n=21..200 =", positive_ok)

# Exhaust all tripod parameter triples in the range. This is only a finite sanity check,
# not part of the proof of the infinite counterfamily.
tripod_pattern_ok = True
for n in range(12, 201):
    best_value = -1
    best = []
    for x in range(1, n - 2):
        for y in range(x, n - 1 - x):
            z = n - 1 - x - y
            if y > z:
                continue
            value = z_tripod(x, y, z)
            if value > best_value:
                best_value = value
                best = [(x, y, z)]
            elif value == best_value:
                best.append((x, y, z))
    expected = [(3, 3, n - 7)] if n <= 20 else [(2, 2, n - 5)]
    tripod_pattern_ok &= best == expected
print("all-tripod winner pattern n=12..200 =", tripod_pattern_ok)
