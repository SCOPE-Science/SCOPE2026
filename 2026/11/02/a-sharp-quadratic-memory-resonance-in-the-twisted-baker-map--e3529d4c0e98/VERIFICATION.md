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

# Verification of exact quadratic-memory formulas

The included `verification/check_energy.py` reconstructs the two-branch transfer operator in centered square coordinates with exact SymPy arithmetic. Its direct checks cover the invariant constant, quadratic-spectrum factorization, centered energy, eigenfunction identity, 25 exact time correlations, 29 exact finite-time variance formulas, and the bounded martingale-coboundary equation. It integrates the squared martingale difference over both half-squares to obtain \(104/135\).

The infinite correlation formula follows analytically by invariant polynomial subspaces. The Gaussian limit relies on the established Bernoulli property of the map and the classical bounded stationary reverse-martingale central limit theorem. Finite symbolic verification does not independently certify those general theorems or publication priority.

To run: `python verification/check_energy.py`. Python 3 and SymPy are required.
