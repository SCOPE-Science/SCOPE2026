---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

Splitting 2-space W must complement TV, uniquely parameterized by 4d-4 coefficients. The source explicit module automorphism with diagonal-unit images sends W to span{e1, P e1+e2}, P uniform t-divisible long-block polynomial. Eliminating Krylov columns leaves r×r Hankel (b_{1+i+j}) for r>=1. Dwivedi–Grinberg Theorem 1.1 gives exactly q^{2r-2} singular out of q^{2r-1}, yielding success fraction 1-1/q and count (q-1)q^{4d-5}. Balanced r=0 follows from module Nakayama. Independently counted nonsingular Hankel matrices for q=2,3 and r<=3 from all coefficient tuples; full d,q theorem relies on algebra and cited Hankel theorem, not finite range.

## originality

PASS

Aggarwal–Ram explicit results for least nonconstant invariant factor degrees d or d-1 cover balanced and r=1; r>=2 has smaller block degree <=d-2, so those formulas do not directly imply this result. Prasad–Ram handles splitting length two, not all d>=3. Dwivedi–Grinberg Hankel rank count is established and explicitly credited; the new step is its exact reduction across all unequal nilpotent two-block profiles.

## value

PASS

A full exact finite-field count for a naturally invariant two-block operator class, with surprising uniformity across every positive imbalance, is useful as a controllability/Krylov benchmark and is not simply a case table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
