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

Execute `python3 verify.py` with Python 3. The script constructs the given bracket over prime fields directly, checks right Leibniz and derivation identities, and enumerates every input vector to test the pointwise almost-inner condition for the candidate central map. It runs 60 parameter/field/dimension tests using dimensions 4–7 and characteristics 2, 3, and 5, and in eight small cases independently solves all derivation linear equations and tests every resulting derivation. Expected terminal line:

`VERIFY_OK 60 Leibniz/derivation/pointwise tests; 8 full derivation-space exhaustive checks`

The code checks finite examples only. The unrestricted theorem follows from the algebraic classification in RESULT.md. No independent mathematical audit has been performed.
