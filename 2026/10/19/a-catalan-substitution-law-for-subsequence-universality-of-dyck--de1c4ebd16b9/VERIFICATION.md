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

The formal proof is in RESULT.md. The attached `verify.py` makes two independent finite checks: direct subsequence inclusion on all Dyck words through semilength eight, and height/arch-state recurrence coefficients through semilength 27. It also checks the first seventeen Catalan finite differences and the top two index layers through semilength 27. These finite checks do not establish the all-length result, which follows from the weighted Dyck first-return matrix equation and exact elimination.
