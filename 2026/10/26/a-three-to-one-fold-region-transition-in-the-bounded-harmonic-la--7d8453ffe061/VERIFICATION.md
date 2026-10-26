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

# Verification scope

The proof was checked from the full definitions with strict-superlevel topology. The checker `CHECK.py` uses only the Python standard library. It verifies exact formal polynomial identities for the circle bridge and radial derivative, evaluates the saddle threshold and the source Jacobian independently at test points, and confirms the correct inequality orientation on both sides of the threshold. Its successful output is `CHECK_OK`.

Mathematical validity of the infinite family does **not** follow from the finite numerical tests: it comes from the displayed inequalities, maximum principle, pole boundary analysis, and complete component-exclusion argument in `RESULT.md`. The hosted full text of several nearby mathematical-index records was unavailable; only their published statement descriptions could be compared. Independent audit has not been performed.
