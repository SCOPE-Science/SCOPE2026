from math import gcd, isqrt


def factor(n):
    out = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            e = 0
            while n % d == 0:
                n //= d
                e += 1
            out.append((d, e))
        d = 3 if d == 2 else d + 2
    if n > 1:
        out.append((n, 1))
    return out


def phi(n):
    if n == 1:
        return 1
    v = n
    for p, _ in factor(n):
        v = v // p * (p - 1)
    return v


def cyclic(n):
    return gcd(n, phi(n)) == 1


def sg_cyclic(n):
    return cyclic(n) and cyclic(2 * n + 1)


initial = [n for n in range(1, 22) if sg_cyclic(n)]
initial_counts = [sum(x <= m for x in initial) for m in range(1, 22)]
assert initial == [1, 2, 3, 5, 7, 11, 15, 17]

allowed = {1, 3, 5, 7, 11, 15, 17}
max_window = []
for m in range(1, 22):
    best = max(
        sum(((start + j) % 18) in allowed for j in range(1, m + 1))
        for start in range(18)
    )
    max_window.append(best)

assert max_window[:20] == [
    1, 1, 2, 2, 3, 3, 4, 4, 5, 5,
    6, 6, 6, 6, 7, 7, 7, 7, 8, 8,
]
assert all(max_window[m - 1] <= initial_counts[m - 1] for m in range(1, 21))
assert max_window[20] == 9

left, right = 87088, 87109
witnesses = [n for n in range(left + 1, right + 1) if sg_cyclic(n)]
assert witnesses == [87089, 87091, 87095, 87099, 87101, 87103, 87105, 87107, 87109]
assert len(witnesses) == 9 > initial_counts[20] == 8

print("Sophie Germain cyclic integers in [1,21]:", initial)
print("C_sigma(1..21):", initial_counts)
print("Allowed residues mod 18 for every Sophie Germain cyclic a>2:", sorted(allowed))
print("Maximum allowed-residue counts in windows of lengths 1..21:", max_window)
print("Witness window (87088,87109]:", witnesses)
print("Window count:", len(witnesses), "; C_sigma(21):", initial_counts[20])
print()
print("Factorization and gcd certificates:")
for n in witnesses:
    q = 2 * n + 1
    print(
        f"{n}: factors={factor(n)}, phi={phi(n)}, gcd={gcd(n, phi(n))}; "
        f"{q}: factors={factor(q)}, phi={phi(q)}, gcd={gcd(q, phi(q))}"
    )
print()
print("VERIFIED: finite counts, residue-window maxima, and the (21,87088) witness used in the proof.")
