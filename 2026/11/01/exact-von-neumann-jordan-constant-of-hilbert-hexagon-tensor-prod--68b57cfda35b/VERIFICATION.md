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
# Mathematical verification

The proof in `RESULT.md` is the primary evidence for the infinite-dimensional claim. It proves the injective norm identity directly from dual-ball vertices, uses a positive definite quadratic form with an exact \(2\times2\) inverse, verifies the two possible maximizing-coordinate patterns, and constructs an attaining orthonormal pair. It proves the projective statement through standard duality and an independent Hadamard-transform explanation of \(C_{\mathrm{NJ}}(X)=C_{\mathrm{NJ}}(X^*)\).

Run `python3 check.py` with the standard Python library. The script checks the critical coefficient identities over \(\mathbb Q(\sqrt3)\), the exact equality witness, and 9,000 seeded, finite-dimensional norm-inequality instances in three dimensions. The finite instances are reproducibility and regression checks only. They do not establish the universal estimate, nor does the script constitute independent peer review.

The proof does not establish any formula for arbitrary polygons, complex tensor factors, or general Banach ranges. Priority comparisons rely on the inspected public manuscript and bounded relevant searches; a claim of global literature exhaustiveness is not made.
