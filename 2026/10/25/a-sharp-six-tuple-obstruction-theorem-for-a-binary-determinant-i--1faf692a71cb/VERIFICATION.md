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

Run `python3 checker.py` with a standard Python 3 interpreter. The expected terminal marker is `ALL_CHECKS_OK 11856`. The program exhaustively considers all team supports in the seven finite domains indicated in RESULT.md, compares direct red/blue partition semantics with the normal-form solver for the first three domain sizes, and enumerates all inclusion-minimal failures by deletion tests. It checks both counting formulas and the allowed sizes four and six.

The checker does not prove the infinite family of assertions; that follows from the register characterization and structural case split in RESULT.md. No formal prover, independent external audit, or probabilistic certificate is claimed.
