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

# Verification and limitations

The full proof appears in RESULT.md. The exact Dirichlet coefficient conjugation is equation (1), logarithmic Volterra compression equation (2), boundedness witness equation (3), analytic Schatten decomposition equations (4), and trace-class necessity/sufficiency equations (5)–(7).

Run `python CHECKER.py` with NumPy installed. The finite checker verifies the matrix coefficients against direct polynomial action and the triangular integration singular-value identity for finite sizes; it does not certify any infinite-dimensional assertion.

The main June 2026 weighted Hardy preprint could not be inspected in full. Scientific priority remains subject to source-access limitations; no independent audit has been performed.
