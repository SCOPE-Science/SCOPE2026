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

The incidence-level checker `verify.py` was executed using Python 3. It enumerates all input subsets at the stated small parameters, compares independent double-Galois closure against the analytic box formula, measures minimal direct premises, and simulates the explicit iterative Horn rules. For larger \((q,d)=(3,3)\), the test uses a seeded finite sample rather than an exhaustive census. These calculations do not prove the all-parameter theorem or verify the automorphism classification independently; the general arguments appear in RESULT.md.
