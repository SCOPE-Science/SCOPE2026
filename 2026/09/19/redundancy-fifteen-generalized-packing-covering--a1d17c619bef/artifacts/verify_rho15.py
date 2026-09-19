from math import comb

RHO = 15
EXCEPTIONAL = {(3, 4), (3, 5), (4, 5), (4, 6)}
FIELDS = (2, 3, 4, 5, 7, 8)


def dimension_cap(q, t, r):
    a = RHO - 2 * r + t - 2
    b = RHO - 2 * r - 1
    values = []
    for h in range(a + 1, RHO + 1):
        numerator = (q**h - q ** (h - a)) * h - b * (q**h - 1)
        denominator = q ** (h - a) - 1
        values.append(numerator // denominator)
    return min(values)


def reduced_tuples(q):
    out = []
    for t in range(3, RHO - 4):
        for r in range(t + 1, (RHO + t - 3) // 2 + 1):
            if 3 * r >= 2 * RHO:
                continue
            if (t, r) in EXCEPTIONAL:
                continue
            if q >= r:
                continue
            out.append((t, r))
    return out


unresolved = []
summary = []
for q in FIELDS:
    low_dimension = 0
    binomial = 0
    for t, r in reduced_tuples(q):
        K = dimension_cap(q, t, r)
        if K <= 5 * t - 2:
            low_dimension += 1
            continue
        N = RHO + K
        if comb(N, r) < q ** (t * (RHO - r)):
            binomial += 1
            continue
        unresolved.append((q, t, r, K, N))
    summary.append((q, len(reduced_tuples(q)), low_dimension, binomial))

assert unresolved == [(2, 3, 6, 78, 93)], unresolved

# For the exceptional shortening, every 2-dimensional subspace of F_2^6
# contains at most four generator columns. The pairing proof bounds the
# multiset size for each possible multiplicity z of the zero column.
h = 6
line_cap_bounds = []
for z in range(5):
    c = 4 - z
    if c == 0:
        bound = z
    else:
        candidates = []
        for M in range(1, c + 1):
            trivial = M * (2**h - 1)
            pairing = M + (2 ** (h - 1) - 1) * (c - M)
            candidates.append(z + min(trivial, pairing))
        bound = max(candidates)
    line_cap_bounds.append(bound)
assert max(line_cap_bounds) == 64

# d_4 >= k+2 and N <= 64 give k <= 62, hence n <= 77.
k_max = 62
n_max = RHO + k_max
sphere_volume = sum(comb(n_max, i) * 7**i for i in range(7))
target = 2**45
assert n_max == 77
assert sphere_volume < target

print("rho=15 finite reduction summary (q,total,low-dimension,binomial):")
for row in summary:
    print(row)
print("sole leftover before the line-cap argument:", unresolved[0])
print("line-cap bounds for zero multiplicity z=0..4:", line_cap_bounds)
print("improved exceptional dimension cap: k <=", k_max)
print("V_8(77,6) =", sphere_volume)
print("2^45 =", target)
print("PASS")
