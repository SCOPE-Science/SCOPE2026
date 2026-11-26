---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Uniform divisors correspond bijectively to the product of the integer intervals 0 through a_i. Their independent coordinates have means a_i/2 and variances a_i(a_i+2)/12; summing the second moment of log D gives the displayed factorization. Put b_i=a_i/(a_i+2), x_i=(a_i+2)log p_i and B=sum b_i. Then the excess of sum b_i x_i^2 over (sum b_i x_i)^2/B is sum_{i<j} b_i b_j (x_i-x_j)^2/B. Equality for two distinct primes would identify two positive prime powers, which is impossible. For fixed exponents choose disjoint intervals [exp((T+c_i)/(a_i+2)), 2 exp((T+c_i)/(a_i+2))] by separating equal-exponent offsets and using eventual separation for unequal exponents. Bertrand's postulate applied at the integer part of each large lower endpoint gives distinct primes with x_i=T+O(1). The normalized excess is O(T^-2); no equality is attained for r>=2. Substitution gives both specializations. Independent replay: python3 -I -B /workspace/audit_replays/frozen_math.py 2, with 2025 exact formal second-moment coefficient checks from trial divisors for 2<=n<=600.

## originality

PASS

The supported distinction is the sharp exponent-pattern envelope, including the strict distinct-prime obstruction and limiting attainment, for the established P3 product. Neither the product, its interpretation as a second logarithmic divisor moment, nor the standard finite Dirichlet-polynomial moment machinery is credited as new in isolation. The strongest inspected same-product statement is Sándor's uniform inequality, not the fixed-exponent extremum.

## value

PASS

This determines the best coefficient in an existing named inequality on each natural prime-exponent layer, and says which layers attain it. It separates the uniform 1/4 bound from substantially stronger exact coefficients, for example 3/8 as the unattained two-prime squarefree infimum. The explicit gap pinpoints the prime-scale configurations that nearly minimize it. This is useful refinement of the established divisor product, not value attributed to an elementary variance computation alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
