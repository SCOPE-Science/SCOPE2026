---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Write m=dk² with d>1 squarefree. The two conjugate values of r² are q−k√d and q+k√d; the former is strictly positive because q is rational and r is real and nonzero. Their b-th powers remain unequal. Thus r^(2b) is irrational and belongs to both quadratic fields, forcing equality and n=de² with positive integer e. For odd b, division of r^b by (r²)^((b−1)/2) puts r=x+y√d in this field with 2xy=−k. If k is odd, u=v₂(x), v=v₂(y) satisfy u+v=−1 and δ=v₂(d)∈{0,1}. In the coefficient of √d of r^b the stripped valuation of the j-th odd term (before its binomial multiplier) progresses in steps of 2(v−u)+δ. If u≥0 the step is strictly negative and the j=b term, whose binomial multiplier is 1, has uniquely least valuation bv+(b−1)δ/2<0. If u≤−1 the step is strictly positive and the j=1 term, whose multiplier b is odd, has uniquely least valuation (b−2)u−1<0 for b≥3. Hence there is no cancellation at that valuation and the coefficient cannot be the integer −e. Conversely r=1/2−k√d works at b=1; for b=2j choose integer q>√m and expand (q−k√d)^j; for odd b≥3 with even k expand (1−(k/2)√d)^b. In both latter constructions all terms in the irrational coefficient have negative sign and the coefficient is a negative integer, giving a valid nonsquare n. Because δ≤1, k is even exactly when 4 divides m. This covers all allowed cases and avoids drawing an all-exponent conclusion from the recorded finite sweep.

## originality

PASS

The fixed-shift predecessor is materially different. The claim supported here is the full variable-second-shift classification, including the odd-exponent congruence and quadratic-field locking, not the cases with a prescribed common shift. Focused catalogue and primary comparisons did not identify coverage of that surviving claim.

## value

PASS

Letting the radical change is a natural relaxation of a named exponent-compatibility problem. The result completely identifies which obstructions survive: equality of fields persists, while odd exponents beyond one are possible precisely at the sharp divisibility-by-four threshold. The explicit witnesses and the valuation obstruction together settle all m and exponents; isolated examples or the same-shift theorem cannot give that separation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
