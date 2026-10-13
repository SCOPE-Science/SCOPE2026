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

# Verification and reproducibility

Run `python3 check_eo_boundary.py` in a directory containing the standalone checker. The expected terminal line is `EO_FIRST_TWO_CONTACT_LAYERS_EXACT_OK`.

The checker implements the permutation \(\pi_\delta\), its cycle decomposition, bad-cycle orientations, directed arrows, and reachability as defined in Muller, arXiv:2609.15024v2, Definitions 1.3–1.5. It exhaustively tests all \(2^g\) increment vectors at every genus \(3\leq g\leq14\), verifying the two boundary layers, the contained low-dimensional strata, and published total supersingular-meeting counts. These counts are cross-checked against Muller's Table 1 and Shimada's Table 1.

The universal theorem is proved separately: dimension weights identify every potentially noncontained stratum in the first two layers, the permutations for \(e_h\) and \(e_{h-1}\) have unreachable bad cycles, and the permutation for \(e_h+e_g\) has only good cycles. The finite enumeration supplies no infinite-dimensional conclusion on its own. The geometric nonemptiness implication in odd characteristic is the published theorem of Muller; the containment implication is the published result recalled by Görtz–Yu.

Independent audit has not been performed. The absence of an independently located equivalent first-two-layer formula is a bibliographic limitation rather than a proof of priority.
