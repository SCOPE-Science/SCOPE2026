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

# Verification record

The finding is proved analytically, not inferred from finite experiments. The following logically exhaustive checks were reconstructed from the definitions:

1. The origin is the unique cut point and each punctured petal is a connected component; all homeomorphisms must fix the origin and permute complete petals.
2. Every nonzero point lies on either an infinite or a finite petal permutation orbit; the first kind is wandering.
3. On a finite orbit, the circle-return map is either orientation preserving, in which case monotone drift away from its fixed-point set is wandering, or orientation reversing, whose square has the same property on its two exchanged arcs.
4. Every point periodic is equivalent to all permutation orbits finite and every return map of order at most two (the order-two case must reverse orientation unless it is the identity).
5. Under that condition the finite invariant union of all cycles meeting finitely many large petals has finite iterate order, and the collapse map from the omitted small petals commutes with all integer iterates. The error is bounded at both ends of a triangle inequality.
6. The entropy-zero case has uniformly bounded separated sets at every scale; the entropy-one lower bound has at least \(N\) separated points for every integer \(N\ge1\); the matching upper bound is the published regular-curve theorem.

No computer program, numerical output, external certificate, or finite computation is required for these universal statements. A full independent audit and complete historical priority determination were not performed. The primary text of the 2026 pointwise-periodic flexibility paper was inaccessible; the source-comparison limitation is recorded in the review.
