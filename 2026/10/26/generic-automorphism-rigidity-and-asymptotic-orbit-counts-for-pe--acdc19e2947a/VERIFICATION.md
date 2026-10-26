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

# Reproducibility and limits

Run `python verify_generic.py` with Python 3. It has no nonstandard package dependencies. The checker generates every matrix in the six prime-field/dimension configurations \((q,n)=(2,2),(2,3),(3,2),(3,3),(5,2),(2,4)\). It independently tests invertibility by Gaussian elimination, compares direct multiplication preservation with the monomial fixed-point equation, computes automorphism-order histograms and Burnside orbit counts, and checks finite-size upper bounds with exact rational arithmetic.

The run on the provided program returned `VERIFY_OK`. The numbers of orbits were respectively \(4,33,7,249,17,908\). These tests cover matrices over prime fields only; the formulas for all prime powers and the asymptotic theorem are justified by the written proof rather than finite enumeration. No independent audit was performed.
