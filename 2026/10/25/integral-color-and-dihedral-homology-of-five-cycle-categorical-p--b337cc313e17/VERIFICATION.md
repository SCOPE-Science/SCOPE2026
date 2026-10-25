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

# Reproduction checks

Use Python 3 standard library: `python3 verify.py`.

The implementation independently reconstructs the categorical graph product and independence faces at \(n=2,3,4,5\), proves that the ten-cycle independence complex collapses by 48 verified elementary moves onto the induced three-edge matching's octahedral two-sphere, checks every color-collapse map in 36,888 face/map instances, and calculates signed Lefschetz traces of all 1,520 group elements at these sizes by a vertex-orbit conflict-graph recurrence. It computes the mod-two reduced Betti vector from simplicial boundary matrices by exact binary elimination. All checks passed, with completion marker `C5_PRODUCT_INTEGRAL_MODULE_CHECKS_OK`.

The elementary-collapse check verifies that each removed lower simplex has exactly one remaining immediate coface and that all retained faces are precisely those in the target; this is a finite exact certificate of the base generator. The general integral theorem uses a published homotopy-rank theorem and universal color-merging maps, not extrapolation from finite tests. This verification is not an independent external audit and does not certify novelty across all possible literature.
