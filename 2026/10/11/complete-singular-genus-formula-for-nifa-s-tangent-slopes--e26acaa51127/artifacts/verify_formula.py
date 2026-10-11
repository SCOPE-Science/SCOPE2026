from fractions import Fraction


def residue_formula(N, M):
    assert N >= 2 and M >= 1
    a, r = divmod(M, N)
    if r == 0:
        return 1 + (a * (N - 1) + 1) // 2
    A = a * (N - 1) + r - 1
    return 1 + (A + 1) // 2


def compact_exact(N, M):
    e = Fraction(M * (N - 1), N)
    # floor((1+e)/2) exactly
    x = (1 + e) / 2
    return 1 + x.numerator // x.denominator


def ehn_threshold(N, M):
    e = Fraction(M * (N - 1), N)
    g = 1
    while not e < 2 * g - 1:
        g += 1
    return g


cases = 0
for N in range(2, 101):
    for M in range(1, 1001):
        a, r = divmod(M, N)
        f = residue_formula(N, M)
        assert f == compact_exact(N, M)
        assert f == ehn_threshold(N, M)
        if r == 0:
            source = 1 + (a * (N - 1) + 1) // 2
            assert f == source
        else:
            A = a * (N - 1) + r - 1
            eps = A & 1
            # D=M, boundary count a+1, chi=-D-eps.
            num = M + eps - a + 1
            assert num % 2 == 0
            genus = num // 2
            assert genus == 1 + (A + eps) // 2
            assert genus == f
            e = Fraction(M * (N - 1), N)
            delta = Fraction(N - r, N)
            assert e == A + delta
            assert 0 < delta < 1
        cases += 1

# Directly verify the elementary low-degree cycle-factorization fact.
import itertools

def compose(p, q):
    return tuple(p[q[i]] for i in range(len(p)))

def parity(p):
    return sum(p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p))) & 1

def is_full_cycle(p):
    n = len(p)
    seen = set()
    x = 0
    for _ in range(n):
        if x in seen:
            break
        seen.add(x)
        x = p[x]
    return len(seen) == n and x == 0

for D in (2, 3, 4):
    perms = list(itertools.permutations(range(D)))
    cycles = [p for p in perms if is_full_cycle(p)]
    products = {compose(x, y) for x in cycles for y in cycles}
    evens = {p for p in perms if parity(p) == 0}
    assert products == evens

print(f"VERIFY_OK cases={cases} N=2..100 M=1..1000 residue=compact=EHN central=true cover_genus=true low_cycles=true")
