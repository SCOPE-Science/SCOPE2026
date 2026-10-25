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
# Reproducibility

Execute `python3 checker.py` in a directory containing this file and the standalone checker. It needs only the Python standard library and produces `PASS: 20235 exact-rational assertions; k=2..10 and six rational heat parameters each.`

The verifier constructs the adjacency-defined unnormalized Laplacian; independently builds spectral idempotents as products of shifted Laplacian matrices, checks eigenvalues and their sum, and checks every entry class, every absolute row sum and a sharp sign-valued input. For exact arithmetic it substitutes six rational numbers for \(z=e^{-t}\), which makes all generator-multiplier coefficients rational.

Numerical or finite rational checks cannot establish the all-integer and all-real-time theorem. The full proof, including unique root ordering and asymptotic estimates, appears in `RESULT.md`. No independent mathematical or bibliographic audit has been performed.
