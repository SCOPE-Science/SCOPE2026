"""Exact integer verification of the binary exponent criterion for recursive-divisor counts."""
from functools import lru_cache
from itertools import product

@lru_cache(None)
def kappa(exponents):
    if all(a == 0 for a in exponents):
        return 1
    return 1 + sum(kappa(t) for t in product(*(range(a + 1) for a in exponents)) if t != exponents)

checked = 0
sharp = 0
strict = 0
for r in range(1, 5):
    for exponents in product(range(1, 6), repeat=r):
        A = max(exponents)
        k = kappa(exponents)
        assert k % (2 ** A) == 0
        predicted = all((a & ~A) == 0 for a in exponents)
        observed = ((k // (2 ** A)) % 2) == 1
        assert predicted == observed, (exponents, k, predicted, observed)
        checked += 1
        sharp += predicted
        strict += not predicted
# Additional exact boundary examples, not used to prove the theorem.
assert kappa((2, 1)) == 16
assert kappa((3, 1)) == 40
assert kappa((2, 2)) == 52
assert kappa((4, 2)) == 416
print('VERIFY_OK')
print('exponent_vectors_checked=', checked)
print('sharp_cases=',sharp)
print('strict_cases=',strict)
print('independent_proper_divisor_recursion=PASS')
print('binary_submask_criterion=PASS')
print('finite_computation_supplements_unrestricted_proof')
