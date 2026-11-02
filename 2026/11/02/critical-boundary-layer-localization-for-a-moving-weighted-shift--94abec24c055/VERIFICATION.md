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

## Analytical and computational checks

The critical spectral condition and normalized eigenvector are derived from the half-line three-term Jacobi recurrence with a single modified edge. The threshold includes its equality case; the limiting asymptotic holds for fixed positive supercritical parameter only. Full strong \(L^2\) convergence follows from the exact geometric tail and dominated convergence. The mass ratio follows from explicit integration.

Run `python check_boundary_layer.py` in the same directory with SciPy available. Successful diagnostic run: 2723 root, finite-spectrum, recurrence, scaling, and mass checks. A finite-section eigenvalue may be marginally below the infinite Jacobi outlier, and the checker allows for this truncation error. Finite experiments alone do not imply any infinite theorem.

Independent mathematical audit: not performed.
