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

The three-move game preserves the correspondence within each level under truncation at three: at a move requiring a fresh element, at most two choices have already been used. For an independent type census I encoded a pair of anchors in different levels by its order direction and five availability bits for the third move: before both, fresh at the lower anchor's level, between, fresh at the upper anchor's level, and after both. Both exact anchor equalities are always available. For coincident anchors and distinct anchors in a common level, only the before, after and fresh-in-level bits are needed, with fresh thresholds two and three respectively. This describes exactly all atomic extensions; taking sets once over second moves and once over first moves checks both sides of the EF game. The replay gives 3279 distinct types over all heights 1–7 and 6417 at height eight. Its complete list of nonsingleton eight-level fibers equals the prescribed 144 pairs, with 6273 singletons. The all-three vector is unique in each tested family's relevant class, so the respective upper bounds 21 and 24 from truncation are attained. The two strata are not combined to assert a cross-height theorem.

## originality

PASS

The supported contribution is the exact recovery range and the complete exceptional relation at fixed height eight for rank three in the pure order language. The closest same-family catalogue result characterizes unrestricted-depth finite-variable logic and does not bound the rank of distinguishing sentences; in fact at width three it distinguishes each of the swapped pairs that rank three merges. The primary coloured-linear-order character results use named predicates and do not furnish the required recovery or merger rule for unlabelled ties. The bounded searches and statement comparisons support distinctness, not a definitive priority claim.

## value

PASS

The exact boundary is motivated by a natural expressibility question for finite rankings with ties: when does rank-three first-order logic cease to recover the sequence of tie sizes that it can in principle count? The first failure is not just an example; the controlled central swap and the required four surrounding nonsingleton levels explain every failure within height eight. This gives exact classification and sharp in-family compression at the boundary, independently useful without an arbitrary-height theorem. The 3279 and 6417 totals are consequences, not the sole source of value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
