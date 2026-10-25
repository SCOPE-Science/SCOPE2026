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
The displayed infinite-family result follows from the proof in `RESULT.md`. `CHECK.py` is a deterministic exact-rational finite regression and may be executed with `python CHECK.py`.

Observed output: `PASS: 140414 exact checks; central defect, cut profiles, convex energies, equality witnesses`.

The tests independently enumerate all nontrivial cuts of representative path weights, confirm the two centered-defect profiles across both phase thresholds, and check the inequality for all ternary data up to six vertices under five representative convex edge functions. They also reconstruct two-level equality witnesses. They do not prove the theorem for arbitrarily many vertices, all positive weights, or all convex functions; those quantifiers are discharged analytically.

No independent scientific audit is claimed.
