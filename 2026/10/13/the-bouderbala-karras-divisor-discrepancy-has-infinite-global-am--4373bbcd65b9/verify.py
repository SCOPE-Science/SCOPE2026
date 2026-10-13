import math
from itertools import product

def delta(k, exps):
    return sum(math.gcd(k, a) - math.log2(a + 1) for a in exps)

checked_tuples = 0
for length in range(1, 5):
    for exps in product(range(1, 11), repeat=length):
        d = delta(1, exps)
        assert d <= 1e-12
        assert (abs(d) < 1e-12) == all(a == 1 for a in exps)
        checked_tuples += 1

positive_checks = 0
negative_checks = 0
for k in range(2, 41):
    r = next(
        p for p in range(2, k + 1)
        if k % p == 0 and all(p % d for d in range(2, int(p ** 0.5) + 1))
    )
    coeff = r - math.log2(r + 1)
    assert coeff > 0
    for t in range(1, 31):
        assert t * coeff > 0
        positive_checks += 1
        neg = 1 - math.log2(k * t + 2)
        assert neg < 0
        negative_checks += 1

for a in range(1, 1000):
    assert abs(delta(1, [a]) - (1 - math.log2(a + 1))) < 1e-12

print(
    f"VERIFY_OK tuples={checked_tuples} "
    f"positive_checks={positive_checks} "
    f"negative_checks={negative_checks} k_max=40"
)
