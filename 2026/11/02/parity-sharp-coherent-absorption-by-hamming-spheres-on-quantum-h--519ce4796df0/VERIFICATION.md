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

The standard-library Python checker `artifacts/verify.py` was executed from the assembled scientific package. It returned:

`VERIFY_OK krylov=30 parity=8 spectral=284 two_shell=24`

The checker constructs all signed Walsh restriction matrices in dimensions 1 through 8 and compares their ranks with the harmonic formula (284 cases). Independently, it builds the site-basis hypercube adjacency matrix and the physical observability matrix for Hamming-sphere traps in dimensions through 6, including the adjacent-layer full-capture cases (30 tests). Analytic parity formulas and central-layer paired rank conditions supply 32 additional tests.

All finite ranks are evaluated over the prime field of characteristic 1,000,003. Agreement of finite modular calculations is corroboration, not a proof of the characteristic-zero, all-dimension theorem. The infinite family is established by the incidence/harmonic calculation in `RESULT.md`. No independent audit has been performed.
