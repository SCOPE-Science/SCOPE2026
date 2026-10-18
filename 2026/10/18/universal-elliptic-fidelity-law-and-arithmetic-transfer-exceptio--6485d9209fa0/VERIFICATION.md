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

The analytical proof gives infinite-chain Hamiltonian reduction, uniquely ergodic torus flow, independence of arcsine factors, elliptic multiplicative convolution, and parity-based rational exceptions. The numerical companion `verify.py` checks those identities on independently constructed finite matrices and quadrature paths.

Reproduction: `python verify.py` with Python 3, NumPy and SciPy installed. Expected status: `PASS checks=71`; numerical comparison tolerances are defined in the program. The demonstrated matrix residual was less than \(7\times10^{-15}\). Numeric sampling does not establish irrational equidistribution, nor does finite calculation prove the theorem at all real fluxes. It also does not assert independent external validation.
