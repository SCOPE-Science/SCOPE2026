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

# Verification and reproducibility

Run `python3 verify_two_level_star.py` with Python 3 and the standard library. The executable rebuilds the weighted-star distance matrices from the graph and their edge lengths rather than importing the theoretical two-by-two formula as the input data. It carries out 168 exact rational comparisons of the quadratic form with its symmetry decomposition, including a direct exact \(p=1\) edge-cut identity; then it checks 20 parameter profiles by an independent Jacobi eigensolver immediately below, at, and above the analytically defined critical exponent. It also checks the uniform-length reduction, sample monotonicity with contrast, and length-ratio exchange symmetry.

Expected completion line: `ALL_TWO_LEVEL_STAR_CHECKS_OK`.

The proof in `RESULT.md`, not these finite computations, establishes uniqueness, strictness for all real exponents, the hyperbolic-concavity inequality, and limiting behavior. The numeric eigensolver is subject to floating-point precision, so only the exact rational checks are exact computational identities. No external proof assistant, independent audit, or exhaustive literature certification is asserted.
