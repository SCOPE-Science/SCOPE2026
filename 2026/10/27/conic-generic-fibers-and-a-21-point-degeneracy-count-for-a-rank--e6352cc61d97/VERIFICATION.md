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

Run `python3 verify.py` with a standard Python 3 interpreter. It performs integer truncated-polynomial arithmetic and asserts the two five-degree series, Chern number 21, Segre coefficients 8 and 0, and canonical coefficients 9 and 1.

The exact program checks rational polynomial identities, not generic smoothness, Kleiman transversality, or the projective-bundle pushforward theorem; those are justified geometrically in RESULT.md. The resulting theorem makes no claim of external or independent verification.
