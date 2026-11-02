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

# Reproducibility and scope

Run `python3 check_gq_rips.py` using Python 3 and only its standard library. The program builds the eight-cycle and the duad–syntheme incidence model of the order-(2,2) generalized quadrangle from first principles. It checks all graph distances, the two color-class clique structures, the exact face vectors, and binary boundary ranks of the threshold-three complex. It additionally enumerates the 720 label permutations and compares the induced graph-cycle character with its tensor-square character. The final line is `GQ_RADIUS_THREE_JOIN_AND_720_CHARACTER_EXACT_OK`.

For the eight-cycle the exact mod-two Betti vector is `(1,0,0,1)` at threshold three. For the order-(2,2) quadrangle the nonempty face vector is `(30,315,1380,2475,1350,225)` and mod-two Betti vector `(1,0,0,256,0,0)`. The computed natural S6-fixed tensor-square dimension is one.

These finite checks do not establish the arbitrary-graph theorem on their own: universal validity follows from the forbidden-four/six-cycle common-neighbor lemma, explicit cone attachments and collapses, join Künneth, and the invariant cycle-space tensor in RESULT.md. The checker does not enumerate the full automorphism groups of arbitrary generalized quadrangles or independently certify mathematical novelty.
