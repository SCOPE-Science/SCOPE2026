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
The algebraic proof determines all rational fibers. `artifacts/verify.py` uses exact integer polynomial arithmetic to check the homogeneous factor identities and direct finite-field enumeration to check the complete rational fiber census for representative prime fields in both congruence classes modulo 3. The enumerations are regression witnesses only; the proof in RESULT.md establishes the theorem for arbitrary admitted prime powers.
