---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

Read RESULT.md blob 67b12fc260f3d5e31539f28df1f8a6b2d91b6bcc and verify.py blob 19630e47eac9623dd1f5677c4e2823a511664946. Explicit dyadic low/high attracting sets cover zero-only words via longest gap, one-1 factors via dominating neighboring gaps, and multi-1 factors via alternating consecutive-1 pairs. The trailing-zero projection lemma maps any suffix-block attractor to one for W_m. Lower-bound certificates comprise factors U_i=10^{2^i-1}1 with unique occurrences in disjoint intervals, additional unique V_m and F_m, and in even high blocks a zero-only factor restricted to the suffix. This matches each upper formula, including m=2 edge cases. Independent direct factor-mask coverage checked 76 values through n≈184 and seven larger dyadic thresholds, with brute optimality for n≤12. No extrapolation from bounded tests is used.

## originality

PASS

Best-of-knowledge priority based on comparison of actual statements and implication directions: The equality of objects/upper formulas was checked; the present lower certificate establishes new optimality rather than renaming the known upper bound. General decidability or asymptotic classification is not a numerical sharp profile; the unique-interval lower-bound construction is mathematically additional. Residual overlap risk retained; search absence alone is not evidence of novelty.

## value

PASS

Exact all-prefix minimum cardinality and sharp jump positions settle a genuine lower-bound gap for a natural sparse automatic word; it turns an explicit established upper construction into a complete structural profile without claiming uniqueness or unrelated words.

The dated certificate retains the supplied scientific assessment, sources and limitations.
