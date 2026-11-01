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

# Verification

Run `python verify.py` using Python 3 and NumPy. Every possible radius-selection vector is generated for each of the four graph sizes. For each nonexceptional selection the program proposes a positive rationally-scaled integer vector numerically, then reconstructs the integer averaging matrix and checks each entry of its strict positive-supervector inequality with arbitrary-precision Python integer arithmetic. Therefore the numerical solve is not itself an acceptance criterion.

Observed result: `CERTIFICATE_OK selections=66420 strict=66401 exceptional=19`. Per-case counts were 79/2, 726/3, 6557/4 and 59039/10 (strict/exceptional). Exact algebraic root identities, all equality cases and strict radius choices are derived in RESULT.md. A finite certificate proves only the finite cases enumerated. Independent audit has not been performed.
