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

Run `python3 verify_subdivision_mmd.py` for the direct all-pairs distance and mutually-maximally-distant checks for orders four, five and six. Run `python3 verify_subdivision_resolving.py` for an independent direct geodesic-inequality evaluation of **all** candidate resolving sets at orders four and five. Both scripts use only the Python standard library, with recorded exact stdout in corresponding `.out` files. Neither checker is a proof for general order; the general proof appears in RESULT.md. Independent external audit has not been performed.
