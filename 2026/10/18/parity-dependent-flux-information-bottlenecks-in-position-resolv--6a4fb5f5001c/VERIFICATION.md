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

Run `python verify.py` with the libraries in `requirements.txt`. The direct finite-matrix program reconstructs the uniform magnetic-cycle Hamiltonian and its flux derivative for lengths three through eleven, compares independent spectral and matrix-exponential evolution, verifies normalization, tests differentiation through finite differences, checks the exact quantum Fisher information and its bound on classical position Fisher information, and evaluates the limiting coefficients for nonexceptional fluxes. It also tests all first-order blind fluxes at multiple times, including the distinction between vanishing ordinary scores and vanishing observation probabilities.

Observed execution result:

`VERIFY_OK 784 finite probability, Fisher, symmetry and leading-coefficient checks`

These calculations are finite numerical corroboration only; the all-size result follows from the analytic Bessel winding expansion and shortest-path estimates in `RESULT.md`. They cannot establish publication priority. The nonregular Fisher convention and parameter-dependent gauge limitation are integral to the scope.
