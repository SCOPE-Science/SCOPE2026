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

An independent scientific audit has not been performed. The available checks are symbolic identity checks, numerical spot checks, and a transparent mathematical proof.

Run `python verify.py` with the packages in `requirements.txt`. The program verifies the exact substitution from the published joint-state equations, the fluxes at all three faces of the physical simplex, the weighted-Lyapunov cancellation, and both exact quotient differential equations. Fifteen numerical integrations using five values of the recovery-rate ratio and three initial states each yield positive solutions approaching the two predicted scaled constants at dimensionless time \(s=100000\).

The actual infinite-time proof is the comparison/variation-of-constants analysis of \(v/Z\) and \(v/Z^2\), combined with the exact derivative of \(Z^{-2}\) and LaSalle's theorem. Neither finite numerical convergence nor a symbolic software output substitutes for that argument. The result supplies no uniform finite-time errors over arbitrary recovery-rate ratios and no stochastic finite-population bound.
