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

# Verification details

The theorem is analytical; a finite checker cannot certify an infinite limit. In `checker.py`, exact integer identities test the Hamiltonian cancellation and the transformed second derivative, while a direct physical-time quadrature for the solvable `a=0, kappa=1` subfamily checks the direction of convergence. Run with `python3 checker.py` using Python 3 with no third-party dependencies. `CHECK_OK` is a smoke-test result, not independent verification or publication priority. The general proof relies on Gaussian-tail estimates and compact-uniform convergence of the scaled equations; neither is delegated to a numerical check.
