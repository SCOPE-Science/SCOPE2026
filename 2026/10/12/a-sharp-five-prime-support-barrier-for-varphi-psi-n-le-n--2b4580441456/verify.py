from fractions import Fraction

LIMIT = 200000

# Exact symbolic-bound checks used in the proof.
even_support = Fraction(3,2)*Fraction(4,3)*Fraction(6,5)*Fraction(8,7)*Fraction(12,11)
odd_no_five = Fraction(4,3)*Fraction(8,7)*Fraction(12,11)*Fraction(14,13)*Fraction(18,17)
odd_with_five = Fraction(4,3)*Fraction(6,5)*Fraction(8,7)*Fraction(12,11)*Fraction(14,13)
assert even_support == Fraction(1152,385) and even_support < 3
assert odd_no_five == Fraction(4608,2431) and odd_no_five < 2
assert odd_with_five == Fraction(1536,715) and odd_with_five < 3

# Smallest-prime-factor sieve for the finite regression scan.
spf = list(range(LIMIT + 1))
for p in range(2, int(LIMIT**0.5) + 1):
    if spf[p] == p:
        for m in range(p*p, LIMIT + 1, p):
            if spf[m] == m:
                spf[m] = p

def support(n):
    out = []
    while n > 1:
        p = spf[n]
        out.append(p)
        while n % p == 0:
            n //= p
    return out

def dedekind_psi(n):
    y = n
    for p in support(n):
        y = (y // p) * (p + 1)
    return y

def euler_phi(n):
    y = n
    t = n
    p = 2
    while p*p <= t:
        if t % p == 0:
            y = (y // p) * (p - 1)
            while t % p == 0:
                t //= p
        p = 3 if p == 2 else p + 2
    if t > 1:
        y = (y // t) * (t - 1)
    return y

psi_39270 = dedekind_psi(39270)
phi_39270 = euler_phi(psi_39270)
assert psi_39270 == 124416
assert phi_39270 == 41472 > 39270
assert len(support(39270)) == 6

violations = []
equalities = []
first_failure = None
checked_safe = 0
for n in range(2, LIMIT + 1):
    w = len(support(n))
    value = euler_phi(dedekind_psi(n))
    if w <= 5:
        checked_safe += 1
        if value > n:
            violations.append((n, w, value))
        if value == n:
            equalities.append(n)
    if first_failure is None and value > n:
        first_failure = (n, w, value)

assert violations == []
assert equalities == [2]
assert first_failure == (39270, 6, 41472)
print(
    "VERIFY_OK "
    f"limit={LIMIT} safe_support_cases={checked_safe} "
    f"equalities={equalities} first_failure={first_failure[0]} "
    f"first_failure_omega={first_failure[1]} first_failure_value={first_failure[2]}"
)
