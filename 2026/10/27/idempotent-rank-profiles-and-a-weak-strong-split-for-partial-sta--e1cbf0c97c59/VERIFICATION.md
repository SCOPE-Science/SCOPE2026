---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

An idempotent is a retraction onto its fixed image, including the empty retraction. If the center is absent and r leaves fixed, the other m−r leaves each have r+1 choices. If the center is fixed, a strict or strong map again has r+1 choices; a weak map has r+2; a strong-weak map allows collapsing leaves to the center only if r=0, since a pair of leaves with images center and fixed leaf would violate reflection of edges. If the center moves to a fixed leaf, the center is not in the image, its edge with that leaf collapses, and all included leaves must map to that same leaf. This gives m·2^(m−1) rank-one maps for both weak types and none for the strict types. The injective cases are partial identities. These partitions prove the six coefficients, equality of strict and strong idempotent sets and both differences, including m=1 where the higher-rank difference is zero. The EGFs follow by summing over the number of fixed leaves and then the other leaves. For a_m=A_m(1), the term r=floor(m/log m) gives log a_m≥m log m−m log log m−O(m), so the rank-one correction is negligible. For R=ceil(m/sqrt(log m)), the r>R contribution to a_m is o(a_m) by the bound (m+1)2^m(m+1)^(m−R). On r≤R the B-to-A term ratio is at least (1+1/(R+1))^(m−R), which diverges. Thus b_m/a_m→∞, giving the two differently paired total-count limits. I independently generated retractions and tested their pair predicates and ranks through m=6, matching all six spectra, including totals (6200,11737,6200,6455,128,128) at m=6. Replay: python3 /workspace/branches/reproduce_frozen.py stars; log /workspace/branches/reproduction-stars.txt. Finite checks only supplement the proof.

## originality

PASS

The known monoid classifications substantially overlap with the ingredients of the explicit coefficients, and the rank-one difference is already known at the level of all maps. Credit is limited to the combined rank-refined idempotent comparison and opposite limiting proportions for the two stated pairs, not to the membership classifications, rank-one mechanism or the standard partial-identity and leaf-only counts. No equivalent prior comparison was established in the inspected sources.

## value

PASS

The rank variable resolves which relaxation matters in a natural class of retracts: allowing collapsed edges while still reflecting adjacency adds only negligible rank-one retracts, whereas dropping reflection creates higher-rank defects and an asymptotically dominant population. The exact degree-by-degree difference and the analysis of the two relative totals make this materially more useful than another count of all maps or a standard single-monoid identity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
