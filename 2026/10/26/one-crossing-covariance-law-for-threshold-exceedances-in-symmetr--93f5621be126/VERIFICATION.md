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

Run `python3 verify.py` with Python 3 and no external dependencies. The checker performs exact rational integration and finite covariance/threshold tests for integer concentrations and finite n, checks the gamma density expansion symbolically via rationals, and validates the uniform-spacing limiting curve. Successful output ends with `VERIFY_OK`. No finite sample tests constitute an infinite proof. The proof in RESULT.md covers all real concentrations, n>=3, and all allowed threshold pairs. Independent validation was not performed.
