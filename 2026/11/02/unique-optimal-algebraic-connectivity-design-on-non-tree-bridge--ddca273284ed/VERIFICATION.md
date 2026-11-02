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

Run `python verify.py` in the directory containing `verify.py` and `RESULT.md`. It uses only Python 3's standard library and checks 81 pairs of community sizes with exact fractions for the budget and candidate eigenvector. A Jacobi eigensolver checks the full weighted Laplacian eigenvalues to numerical tolerance; 24 outside-threshold pairs are checked against the strict Rayleigh bound. For the five-vertex counterexample it checks the expected spectrum against five explicit rational values.

These checks establish finite reproducibility but do not certify the entire infinite family. The mathematical proof is the centered-Rayleigh equality argument plus the strict/endpoint matrix-inertia calculations described in `RESULT.md`. The eigenvalue multiplicity at the endpoint is allowed; the explicit smallest cyclic example lies in the strict regime and has simple algebraic connectivity.

Independent audit: not performed.
