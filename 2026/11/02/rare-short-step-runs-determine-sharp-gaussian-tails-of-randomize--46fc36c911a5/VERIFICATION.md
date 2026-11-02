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

# Reproduction notes

Run `python verify.py` with a standard Python 3 interpreter. No external packages are needed. The checker uses deterministic exact rational arithmetic for both specified random-step laws and for thousands of randomly chosen positive rational parameters, plus elementary floating-point checks only for positivity of the logarithmic exponent. It also examines a finite family of backward deficit strings against the exact endpoint-contraction bounds. The recorded output for the checked package is 50,315 passed assertions.

The general tail law is a mathematical deduction from the geometric-run sandwich, a Gaussian scale-mixture representation and the uniform Mills estimates, not an empirical extrapolation. Finite diagnostic enumeration does not establish the infinite theorem. No independent audit has been performed.
