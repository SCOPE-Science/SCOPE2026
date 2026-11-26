---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

At fixed digit length the translation distinguishes the bit string, and the slope distinguishes digit lengths. Occurrences of 01 are disjoint; choosing which are single tokens gives exactly binomial(M,L−n) parsings at generator time n. The two-state occurrence series is 1/(1−2u+u²(1−v)), and summing the interval L−M through L gives the claimed series, including n=0. Partial fractions give A_n=F_(2n+3)−2^n (F_0=0, F_1=1), hence the stated growth. For fixed output at time n the token counts are fixed, so the conditional parses are equiprobable. The entropy loss is the expected log binomial; the strong law for single tokens and adjacent pairs and the uniform log-binomial estimate give the stated limit. The digit gap law p_0=b, p_k=(ab+c)a^(k−1) has mean block length (1+c)/(1−a) and (1−a)H(p)=h. Its relative entropy from the fair-bit gap law is strictly positive, since equality forces c=0. The established dimension identity applies with contraction exponent −(1+c)log 2; both binary branches have positive weight, giving full support, and the strict dimension drop gives singularity. Equal weights give the stated dimension. The supplied script was inspected as text only; the analytic reconstruction, not its finite output, establishes the scope of the claim.

## originality

PASS

Credit the published same-token ambiguity, special input probabilities and general entropy–dimension theorems. The supported distinct content is the exact generator-time enumeration and the collision-corrected product entropy for all positive weights, with the explicit dimension as an application. No inspected prior statement covers these calculations in full. This is a best-of-knowledge assessment, not a priority guarantee.

## value

PASS

This is a published ambiguous code and a natural small exact-overlap example, not an arbitrary parameter slice. The exact growth separates generator time from digit length, and the entropy correction quantifies precisely the information lost by merging parses, including the published law whose unmerged entropy exceeds the binary per-digit ceiling. The dimension application illustrates the difference between full support and absolute continuity; it is not a new general dimension theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
