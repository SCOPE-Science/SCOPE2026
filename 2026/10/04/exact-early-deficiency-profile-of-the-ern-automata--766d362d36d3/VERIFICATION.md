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

The theorem is proved symbolically in `RESULT.md`. The standalone script `artifacts/verify_cerny_deficiency.py` checks the finite cases \(3\le n\le12\) by exact breadth-first search on image subsets. It also checks the explicit word \(b(a^2b)^{s-1}\) and the claimed missing-state set after each admissible deficiency step.

The finite computation does not certify the infinite theorem by itself. Its role is to replay definitions, detect boundary errors, and confirm the proof's formula on 40 parameter pairs.
