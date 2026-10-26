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

# Reproducibility checks

Run `python verify.py` with Python 3 and SymPy. The program checks four symbolic identities, representative almost-sure rate approximations for four positive, negative, and indefinite spectra, six angular quadrature identities, and twelve exact-rational near-pole witnesses. The script reports 26 checks when successful.

The proof's universal claims are analytic, not statistical estimates: Gaussian inverse moments diverge at every iteration, and the one-dependent log-norm increments satisfy a strong law. Simulation tolerances check implementations, not theorem validity. No independent external verification has occurred.
