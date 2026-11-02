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
Run `python3 verify.py`. The script implements exact arithmetic in the finite field \(\mathbb F_5[\theta]/(\theta^2-2)\), enumerates all 651 projective base points, checks the 28 explicit bitangents and the 44 branch contacts, and verifies all 826 surface points, including the 778 covered and 48 uncovered. It checks the 24-point coordinate description and one-orbit assertion. No randomized sampling or external dependencies occur. The classical 28-bitangent theorem is a stated geometric input rather than claimed as proved by enumeration.

The run prints `VERIFY_OK` on success. The statements do not assert counts for other fields or independently verified publication priority.
