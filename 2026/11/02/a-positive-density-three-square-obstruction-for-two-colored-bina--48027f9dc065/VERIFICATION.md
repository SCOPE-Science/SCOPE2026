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

The exact symbolic certificate and an independent initial coefficient check are implemented in `verify.py`. Run `python3 verify.py`; it must finish with `VERIFY_OK degree 1538 certified_residues [36, 62] independent_coefficients 8192`. The polynomial has degree 1538; the residue test is exhaustive at modulus 128, while the 8192 coefficients are supplementary finite checks. External or independent assessment has not been performed.
