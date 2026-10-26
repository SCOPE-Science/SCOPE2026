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

The local blow-up chart calculation was written out in RESULT.md. The included script `artifacts/verify_corner_blowups.py` was executed and returned `CHECK_OK: all 16 corner subsets over Q, F2, F3 and F5`. The script checks the exact six-variable constraint ranks; it does not by itself establish the geometric correspondence between those constraints and global sections. That correspondence is proved in RESULT.md. The proof uses only local coordinates, the global vector fields on \(\mathbb P^1\times\mathbb P^1\), and linear equations, so it applies over every algebraically closed field of the stated characteristic. No external or independent verification channel is claimed.
