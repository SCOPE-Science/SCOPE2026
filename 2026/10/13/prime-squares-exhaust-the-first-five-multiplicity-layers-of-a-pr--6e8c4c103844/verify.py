#!/usr/bin/env python3
LIMIT = 2_000_000

def spf_table(n):
    spf = list(range(n + 1))
    spf[0] = 0
    spf[1] = 1
    for p in range(2, int(n ** 0.5) + 1):
        if spf[p] == p:
            for m in range(p * p, n + 1, p):
                if spf[m] == m:
                    spf[m] = p
    return spf

def factors(n, spf):
    out = []
    while n > 1:
        p = spf[n]
        a = 0
        while n % p == 0:
            n //= p
            a += 1
        out.append((p, a))
    return out

def is_prime_square(fac):
    return len(fac) == 1 and fac[0][1] == 2

spf = spf_table(LIMIT)
solution_count = 0
low_layer_solutions = []
non_square = []

for n in range(2, LIMIT + 1):
    fac = factors(n, spf)
    beta = sum(p for p, _ in fac)
    B = sum(p ** a for p, a in fac)
    Omega = sum(a for _, a in fac)
    if B == beta * beta:
        solution_count += 1
        if Omega <= 5:
            assert is_prime_square(fac), (n, fac, B, beta, Omega)
            low_layer_solutions.append(n)
        if not is_prime_square(fac):
            non_square.append((Omega, n, fac))

assert non_square, 'expected non-prime-square solutions in replay range'
min_omega = min(O for O, _, _ in non_square)
first_at_min = min(n for O, n, _ in non_square if O == min_omega)
assert min_omega == 6
assert first_at_min == 144

fac144 = factors(144, spf)
assert fac144 == [(2, 4), (3, 2)]
assert sum(p ** a for p, a in fac144) == 25
assert sum(p for p, _ in fac144) ** 2 == 25
assert sum(a for _, a in fac144) == 6

print(
    'VERIFY_OK',
    f'limit={LIMIT}',
    f'solutions={solution_count}',
    f'low_layer_solutions={len(low_layer_solutions)}',
    f'min_non_square_Omega={min_omega}',
    f'first_min_non_square={first_at_min}',
    f'first_non_square={[n for _, n, _ in sorted(non_square)[:8]]}',
)
