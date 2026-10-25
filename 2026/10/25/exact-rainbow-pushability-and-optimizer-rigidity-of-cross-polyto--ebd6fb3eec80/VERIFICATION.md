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

The accompanying standalone `verify_crosspolytope.py` was executed with standard Python. It produced `PASS: 21 exact balanced constructions, plus one strict nonoptimizer`. It enumerated possible signed-axis outcomes with rational probabilities for dimensions two through five and varying sample sizes. It checked collective balance, exact equality for attaining constructions, and strict inequality for a nonattaining balanced family.

The unrestricted-dimensional formula and the necessity of the optimizer conditions follow from the analytic proof in `RESULT.md`. Finite enumeration is **not** claimed as an infinite-dimensional proof. No independent audit has been performed.
