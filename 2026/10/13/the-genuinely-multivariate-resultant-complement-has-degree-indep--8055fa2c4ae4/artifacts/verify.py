from itertools import product
from math import factorial

def monomials(n, d):
    out = []
    def rec(pos, remaining, prefix):
        if pos == n - 1:
            out.append(tuple(prefix + [remaining]))
            return
        for a in range(remaining + 1):
            rec(pos + 1, remaining - a, prefix + [a])
    rec(0, d, [])
    return out

def has_common_projective_zero(monomial_tuple):
    n = len(monomial_tuple)
    supports = [
        {j for j, exponent in enumerate(m) if exponent > 0}
        for m in monomial_tuple
    ]
    for mask in range(1, 1 << n):
        point_support = {j for j in range(n) if (mask >> j) & 1}
        # A monomial is nonzero at a point with this exact support
        # iff all variables in its support lie in point_support.
        if all(not support.issubset(point_support) for support in supports):
            return True
    return False

formats = 0
fixed_systems = 0
nonresultant_fixed_systems = 0
weight_checks = 0

for n, max_degree in [(3, 3), (4, 2)]:
    for degrees in product(range(1, max_degree + 1), repeat=n):
        formats += 1
        monomial_lists = [monomials(n, d) for d in degrees]
        base = max(degrees) + 1

        for mons in monomial_lists:
            weights = []
            for exponents in mons:
                weight = sum(exponents[j] * (base ** j) for j in range(n))
                weights.append(weight)
                weight_checks += 1
            assert len(weights) == len(set(weights))

        local_nonresultant = 0
        for monomial_tuple in product(*monomial_lists):
            fixed_systems += 1
            if not has_common_projective_zero(monomial_tuple):
                local_nonresultant += 1
                nonresultant_fixed_systems += 1

        assert local_nonresultant == factorial(n)

assert formats == 43
assert fixed_systems == 45275
assert nonresultant_fixed_systems == 546
assert weight_checks == 961

print('VERIFY_OK', formats, fixed_systems, nonresultant_fixed_systems, weight_checks)
