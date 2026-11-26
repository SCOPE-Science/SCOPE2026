---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

Run `python3 verification.py` for bounded checks using only the Python standard library. The direct ellipse calculation divides the imaginary semiaxis by \(2|1-2/p|\) and compares the resulting coordinates with the hyperbolic axes at representative exponents and their conjugates. Additional checks test selected cone threshold normals, limiting support maximizers, the vertical half-width, and the second-order vertical excess at the limiting height maximizer.

All universal, infinite-dimensional, and asymptotic conclusions follow from the explicit analytical proof in `RESULT.md` and the prior essential-range identity cited there. Numerical sampling cannot establish uniqueness for all parameters or the quadratic Hausdorff bound.
