---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducible verification

The general affine-hull criterion is established analytically in `RESULT.md`. At the negative diagonal radial endpoint, active inequalities force the pinned edge coordinates by switching and character orthogonality. A positive slack neighborhood in the other coordinates provides the matching dimension bound. The triangle with pendant edges gives a direct product check of nonuniqueness.

The original standard-library `verify.py` is unchanged and checks only the edge-transitive numerical specialization and the balanced complete multipartite MaxCut evaluation, not the general criterion. Running `python verify.py` is expected to check 174 edge-transitive labeled graphs, 1,508 automorphism actions, 2,422 cut switches and 60 multipartite parameter pairs with exact arithmetic. These finite checks are not used as a proof.
