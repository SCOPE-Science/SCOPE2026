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

# Reproducibility and scope

The full mathematical proof is in `RESULT.md`. It uses the explicit hydrodynamic scale of Mesquita et al., a last-reset renewal-age decomposition, equilibrium renewal theory, the monotone density Tauberian theorem, and elementary beta integrals.

For numerical algebra/integral cross-checks run `python verify.py` after installing packages from `requirements.txt`. On this package's checked computation, the script printed `PASS 43 finite checks: constants, density shape, normalized age, Thomas--Fermi expansion`. It compares the exact inverse expansion law with its derivative, the beta law's normalization, the normalized central/edge asymptotic constants at multiple heavy-tail exponents, and several stationary large-distance coefficients. Numerical quadrature tolerances and tested parameter values are visible in the script.

Finite numerical comparisons are not a proof of convergence, stationary existence, exact sharp constants or original priority. The analytical proof contains the quantified conditions and identifies which renewal and complete Bernstein function theorems it uses. Self-review is the only performed review channel; independent audit has not been performed.
