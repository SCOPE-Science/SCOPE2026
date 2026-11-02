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
# Verification

The exact quadratic-form identity is derived in RESULT.md. The crucial estimate (1) compares a weighted lattice edge midpoint sum to the continuum exponential potential with uniform quadratic-in-spacing form error. The sharp constant follows by the positive Dirichlet Bessel resonance and a ground-state transform. The spectral limit is justified using compactness of interpolated negative-energy vectors; ordinary finite truncation is never used as a proof of the infinite claim.

Run `python check.py` with numpy and scipy to reproduce positive-weight Jacobi threshold-root computations at four mesh sizes and the finite-section spectral comparisons at two couplings. The recurrence computation truncates only after the coefficients have decayed exponentially, and numerical root accuracy does not certify an infinite-dimensional threshold. The Bessel order is found by a numerical root finder. For \(\lambda\) exactly at the limiting threshold no yes/no assertion is made for each fixed small mesh.
