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

# Verification scope

Execute `python verify_flux_reset.py` from this package, with NumPy and SymPy installed. The checker tests the flux-reversal difference of exact finite-time moments through order \(N+1\) for cycle sizes \(3\le N\le9\), constructs and diagonalizes Hermitian cycle Hamiltonians for seven sizes and three fluxes, evaluates the Poisson-reset stationary density independently, and compares selected strong-reset total-variation asymptotics. The reproducibility program tests a finite collection and does not certify all \(N\). The analytic argument in RESULT.md proves the general statement.

Independent audit status: not performed.
