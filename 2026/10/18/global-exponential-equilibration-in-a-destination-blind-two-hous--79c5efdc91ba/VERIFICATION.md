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

Use Python 3.10+ and execute `python verify.py` from the directory containing this file. The checker needs no third-party modules. It reconstructs the ordered relocation event table, verifies stationary ODE residual zero exactly using rational fractions, matches 1,458 directed pairwise detailed-balance comparisons across 81 positive parameter grids, checks exact mass/density normalization and strict mixed-state suppression, and checks negative relative-entropy derivative at an explicit compatible non-equilibrium interior distribution.

The exact, infinite-dimensional-in-time claims are established analytically in RESULT.md: coercive strictly convex log-partition, pointwise detailed balance, strict dissipation, uniform boundary avoidance through a finite-state irreducible chain, an entropy-dissipation spectral gap, and a positive covariance Schur complement. The checker does not establish global attraction, optimal exponential rates, or originality. Independent audit and independent validation have not occurred.
