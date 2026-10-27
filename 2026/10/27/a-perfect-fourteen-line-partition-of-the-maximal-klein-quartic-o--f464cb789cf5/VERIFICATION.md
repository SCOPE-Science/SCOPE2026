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

# Reproducible verification

The finite-field implementation in `CHECK.py` was executed successfully; it emitted `MAXIMAL_QUARTIC_COVER_OK`. It uses a 25-element field encoded by residues modulo five, loops over all 651 normalized projective triples twice (once for points and once for dual lines), and checks 56 rational curve points, the exact intersection-size spectrum, and 14 pairwise disjoint four-point sections. Both incidence identities are tested.

The independent mathematical ingredients are the elementary gradient criterion for smoothness, the plane-quartic genus formula, Bézout's degree-four intersection bound, and the Hasse--Weil bound for genus three. Finite exhaustive checks establish the finite counts; they do not establish claims for unspecified fields or arbitrary curves. The explicitly displayed 14 lines supply an independently inspectable finite certificate. No independent audit has been performed.
