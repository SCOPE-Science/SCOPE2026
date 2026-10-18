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

# Reproducibility
Execute `python3 verify_inverse.py` with Python 3.10 or later; no third-party dependencies are required. It must print `VERIFY_OK`. The script independently checks the antipodal circular coefficient minimum, integer monomial exponent-matrix cancellation, and parity recurrence in the stated finite ranges. It does not attempt to prove a universal statement by extrapolating these tests.

The general proof uses elementary cyclic convolution, an explicit circular arc-overlap identity, the root-of-unity filter, and the elementary trigonometric factorization of \(P_s\). The mathematics is field-independent, even though complex roots of unity are used as an auxiliary proof device.
