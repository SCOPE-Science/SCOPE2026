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
# Verification and limits

The proof is self-contained modulo the standard prime number theorem and Chinese remainder theorem. The independent integer calculations in `verify.py` evaluate all endpoint integrality, congruence, exact-sum, distinctness and small-size enumeration assertions for selected witnesses. They do not certify unbounded existence by themselves; the quantified existence follows from the analytic prime supply and the CRT.

No external independent audit has been performed. No lower bound uniform in every cycle size, no optimality assertion, and no numerical conditioning issue are claimed.
