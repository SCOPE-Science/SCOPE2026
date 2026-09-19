from itertools import product
from math import sqrt


def gf2_rank(rows):
    rows = [int(x) for x in rows if x]
    rank = 0
    bit = max((x.bit_length() for x in rows), default=0) - 1
    while bit >= 0:
        pivot = next((j for j in range(rank, len(rows)) if (rows[j] >> bit) & 1), None)
        if pivot is not None:
            rows[rank], rows[pivot] = rows[pivot], rows[rank]
            for j in range(len(rows)):
                if j != rank and ((rows[j] >> bit) & 1):
                    rows[j] ^= rows[rank]
            rank += 1
        bit -= 1
    return rank


def complete_basis_rank(r):
    # Bit r records the class of -1; lower bits record p_1,...,p_r.
    rows = [(1 << r) | mask for mask in range(1 << r)]
    return gf2_rank(rows)


def bound(Q, D):
    return (D * Q / (D - 2)) ** (-(D - 2) / 4)


print("complete multiquadratic basis ranks and separation exponents")
for r in range(1, 6):
    K = 1 << r
    s = complete_basis_rank(r)
    D = 1 << s
    new_exponent = D // 2 - 1
    old_exponent = (1 << (K - 1)) - 1
    print(f"r={r} K={K} rank={s} D={D} new_M_exponent={new_exponent} AFT_M_exponent={old_exponent}")

# Exact norm check for beta=-5+sqrt(2)-5sqrt(3)+5sqrt(6).
a, b, c, d = -5, 1, -5, 5
A = a*a + 2*b*b - 3*(c*c + 2*d*d)
B = 2*a*b - 6*c*d
norm_real = A*A - 2*B*B
norm_imaginary_field = norm_real * norm_real
beta = a + b*sqrt(2) + c*sqrt(3) + d*sqrt(6)
Q = a*a + 2*b*b + 3*c*c + 6*d*d
D = 8
new_bound = bound(Q, D)
old_bound = (Q / (1 - 2 ** (1 - 4))) ** (-(2 ** (4 - 1) - 1) / 2)
print("\nexample a={1,2,3,6}, m=(-5,1,-5,5)")
print(f"Q={Q}")
print(f"real_biquadratic_norm={norm_real}")
print(f"imaginary_multiquadratic_norm={norm_imaginary_field}")
print(f"abs_linear_form={abs(beta):.15g}")
print(f"degree_sensitive_bound={new_bound:.15g}")
print(f"AFT_exact_bound={old_bound:.15g}")

# Finite sanity check for the complete basis {1,2,3,6}, coefficients in [-3,3].
rad = [1, 2, 3, 6]
worst_ratio = float("inf")
checked = 0
for coeffs in product(range(-3, 4), repeat=4):
    if not any(coeffs):
        continue
    val = abs(sum(m * sqrt(x) for m, x in zip(coeffs, rad)))
    q = sum(m*m*x for m, x in zip(coeffs, rad))
    bnd = bound(q, 8)
    worst_ratio = min(worst_ratio, val / bnd)
    if val + 1e-14 < bnd:
        raise AssertionError((coeffs, val, bnd))
    checked += 1
print(f"finite_sanity_vectors={checked}")
print(f"minimum_observed_value_over_bound={worst_ratio:.12g}")
print("status=PASS")
