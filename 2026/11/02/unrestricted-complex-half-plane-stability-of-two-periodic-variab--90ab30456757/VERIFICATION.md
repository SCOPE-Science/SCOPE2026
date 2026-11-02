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

Run `python verify.py` with Python 3, SymPy and NumPy. The script independently constructs the period matrix, checks exact rational identities for trace/determinant, verifies the complete symbolic Schur–Cohn factorization, checks the singular multiplier limits, and compares direct matrix products with the characteristic equation on seeded samples. The infinite-dimensional parameter assertions rest on the written positivity proof, not a finite floating-point sweep.

The scientific scope is fixed-coefficient scalar dynamics under **exactly two-periodic** positive step lengths. For any finite ratio, the closed right half-plane is strictly damped except the simple neutral zero-frequency solution. The infinite-ratio limit does not preserve uniform damping on the imaginary axis. No general nonperiodic-mesh, nonlinear energy, or implementation-level numerical stability certification is attempted.
