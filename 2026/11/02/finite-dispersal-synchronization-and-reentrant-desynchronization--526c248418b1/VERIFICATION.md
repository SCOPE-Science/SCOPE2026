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

The supplied standalone `verify.py` requires Python 3 with SymPy, NumPy and SciPy. Invoke `python verify.py` in the directory containing this file. The script independently solves the exact stationary Lyapunov equations for arbitrary symbolic positive local relaxation and forcing parameters and verifies the determinant formula. It then tests the exact stationary covariance and derivative factorizations for the singular common-noise and nonsingular \(99/100\)-correlated-noise cases.

The script verifies the rational stationary covariance identities and computes independent double-precision solutions of the continuous Lyapunov equation for ten coupling values under each of the two forcing regimes. The analytic proof, not those finite numerical comparisons, establishes the global number and location order of extrema using Descartes' rule and exact sign inequalities.

The generic classification asserts existence, not uniqueness, of a post-synchronization minimum. Only the explicit examples receive a global uniqueness claim. The physical meaning is limited to Gaussian linearized fluctuations and stationary Pearson correlation; independent experimental or ecological validation has not been performed.
