---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproduction and limits

Run `python3 verify.py` in the extracted directory using Python's standard library. This independently reconstructs the source-defined inexact dual update with exact integer/Fraction arithmetic, the nine equiprobable two-step paths, the weighted \(p=24\) expectation, both path-probability bounds for every real \(p\ge24\), the \(\lambda=0\) projection case, and 343 exact-rational consistency checks of the two-row defect identity. The identity's algebraic proof, not the finite consistency checks, covers all real unit-row inner products, errors, and ambient dimensions.

The proof and computation concern exactly two iterates, not longer-run average performance. Calculations do not independently determine the earliest sign-change exponent. Positive regularization is covered by the explicit three-row construction only; the two-row impossibility theorem applies exclusively to ordinary orthogonal projections. The reproduced data neither asserts publication priority nor substitutes for independent mathematical audit.
