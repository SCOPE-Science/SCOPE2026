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

# Reproducibility and verification

The analytic proof constructs every angular block directly from normalized Bergman monomials and normalized disk moments. It verifies the rank-two signed Gram determinant, the trace-class telescoping identity, the two distinct noncritical exponents and the balanced cubic cancellation. The proof, rather than any finite numerical experiment, establishes the infinite-dimensional classification.

Run \(\texttt{python3 checker.py}\) in a Python 3 standard-library environment. The actual package checker passed **83,450** finite assertions involving exact rational disk moments, Gram determinants, finite-block inertia, Hilbert–Schmidt trace telescoping and large-index asymptotic sanity checks. Floating-point asymptotic checks do not certify limiting behavior; the exact algebraic expansions in the proof supply the limiting argument.

This record has not undergone independent mathematical review or externally witnessed software validation. The 2020 dual Toeplitz spectral source could not be examined in full; originality is qualified accordingly.
