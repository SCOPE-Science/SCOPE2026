---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

For m squarefree, m² has exactly 2^r exponential divisors and reciprocal-sum denominator S_e(m²)=∏(p+1), so the type-2 test is exactly ∏(p+1)|2^r m². The parity/minimum-prime argument proves m>1 forces 6|m. With r≥3, the least q>3 has q+1=2^a3^b, a∈{1,2,3}, b∈{0,1}, hence q∈{5,7,11,23}. For m=6qr, (q+1)(r+1)|48q²r² forces r+1|48q² and r<48q². An independent exact prime sieve over every derived finite range reproduced all nine pairs [(5,7),(5,19),(5,199),(7,13),(7,41),(7,97),(7,293),(11,43),(11,241)], and checked the reduced divisibility; the 15 listed bases include 1,6 and the four 3-prime cases. This uses a proved finite cutoff and does not extrapolate unbounded-support completeness.

## originality

PASS

The claim is an exact support≤4 arithmetic classification plus a support-independent least-additional-prime obstruction; definitions and special cases of type-2 exponential harmonicity are classical. Sándor establishes squarefree n, not this squarefree-square m² classification; OEIS enumerates individual type-2 numbers but lacks the unrestricted least-prime obstruction and complete no-size-bound four-prime theorem. Resultary hits mostly bi-unitary or e-unitary variants, which do not imply the same denominator divisibility. Inaccessible thesis/older number-theory enumeration is a residual priority risk.

## value

PASS

Harmonicity under exponential divisors is a natural divisibility property; a complete prime-support classification with a mathematically forced last-prime cutoff and sharp, attained unrestricted least-prime spectrum is a substantive exact arithmetic result, even without classifying ≥5 primes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
