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

Run `python verify.py` under Python 3.9+. The script uses the standard library and reports `VERIFY_OK 6956` after checking exact fractional first-step residual identities, eigenvalue-sign invariance, threshold polynomial equivalences, orthogonality and nondegenerate two-step residual sketches. It also compares deterministic numerical angular quadrature with the exact mean-square and growing-step probability formulas at stated parameters. Numerical quadrature, finite rational samples, and logs do not prove the universal theorem; the general proof uses an explicit diagonal reduction, a differentiated angular log integral, exact quadratic roots, and the spanning argument for residual-history sketches.

The assumptions are a real symmetric invertible planar matrix, an initial residual uniformly oriented on the circle for the probabilistic statements, Euclidean weighting, and exact projected solves. The result does not characterize roundoff effects, other sketch selections, or higher dimensions.
