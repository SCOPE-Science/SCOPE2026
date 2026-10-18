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

The proof establishes the infinite-dimensional statement algebraically by reduction to rank at most two. The included `checks/verify.py` uses only the Python standard library and constructs complex two-by-two rank-one pairs, computes singular-value moments through two exact Gram invariants, tests a grid of admissible amplitudes and overlaps, and checks attaining projection configurations and small-overlap slopes. These are finite arithmetic diagnostics only, not an exhaustive theorem proof. No independent audit has been performed.
