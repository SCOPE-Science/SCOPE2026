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

Run `python verify.py` with any Python 3 interpreter supporting `pow(value, -1, 3)`.

The verifier performs exact arithmetic modulo three, reconstructs every structure table, derives the annihilator of each ternary quadratic net, exhausts the 364 projective quadrics and 19,683 multiplication tables, and enumerates the unit-preserving basis-change group of order 432. It independently checks the rank-six criterion, associativity and the two orbit representatives. Expected completion text begins `VERIFY_OK:`.

No random sampling, floating-point tolerance, unprovided data, network access or other files are required. The certificate proves a finite classification only. It does not substitute for an independent mathematical audit, and no result for larger fields is claimed.
