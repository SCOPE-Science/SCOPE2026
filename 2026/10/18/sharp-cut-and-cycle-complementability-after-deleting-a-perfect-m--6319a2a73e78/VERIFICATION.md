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

# Verification notes

`crown_verify.py` is a Python-standard-library program using `fractions.Fraction`; it was executed successfully on \(n=3,\ldots,9\). It checks every edge-column's exact cut and flow conditions, self-adjointness, equality on a spanning family of cut vectors, both endpoint column norms, and the strict matching-deletion and cut-cycle crossover comparisons.

`crown_pinv_check.py` uses NumPy and independently constructs the vertex-edge incidence matrix and the Moore–Penrose pseudoinverse of its graph Laplacian. It was executed successfully for \(n=3,\ldots,10\), with maximum absolute discrepancy less than \(9\times10^{-15}\).

These checks are finite validations. The proof for arbitrary \(n\ge3\) is the equivariance-plus-spectral calculation in `RESULT.md`. No external, independent scientific audit has been performed. No claim of exhaustive literature coverage is made.
