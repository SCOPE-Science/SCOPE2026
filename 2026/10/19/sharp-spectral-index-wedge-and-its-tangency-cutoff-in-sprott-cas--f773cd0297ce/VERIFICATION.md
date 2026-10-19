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

The accompanying standalone `sprott_h_checker.py` reproduces the polynomial and derivative identities from the defining ODE using SymPy and checks seven supplementary numerical spectra. The global result follows from the Routh sign-count proof and one-variable monotonicity argument in RESULT.md; the finite samples alone are not an exhaustive proof. No independent mathematical review has been performed.
