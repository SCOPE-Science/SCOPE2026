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

`checker.py` computes the exact number of linear extensions using a subset dynamic program. For each forward-oriented relation subset on up to five labeled elements, the checker constructs the duplicated poset with vertical comparison edges and evaluates the ratio from integer extension counts. It checks the universal lower and upper bounds and both equality conditions by the extension count, then independently matches seven star cases against the closed factorial expression. Actual successful execution: `VERIFY_OK poset_instances= 1099 star_formula_cases= 7`. These are finite corroboration only; analytic proofs in `RESULT.md` establish the theorem for arbitrary finite posets. Independent audit has not been performed.
