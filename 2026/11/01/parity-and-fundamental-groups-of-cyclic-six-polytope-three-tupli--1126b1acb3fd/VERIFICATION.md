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

Run `python3 verify.py` with the Python standard library from this directory. The checker independently enumerates cycle facets both by disjoint edge matchings and Gale's original evenness condition for ten parameters; independently checks both necessary small connectedness bases; and confirms the graph counts, components, and rank formulas for sixteen cyclic parameters. It also verifies the path-extension covering step for twenty-one finite lengths.

The core infinite proof is a finite base plus mathematical induction: any new terminal triple extends to a union of three disjoint path edges, where the other two edges are chosen using a perfect or near-perfect matching of a residual path. The checker is not claimed to replace this quantifier argument. No independent mathematical audit has been performed.
