---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

Every bracket coefficient on edge (v,w) equals det((a_v,b_v),(a_w,b_w)), including characteristic two with alternating bracket. Nonzero-root tree extension realizes arbitrary incident edge data with nonzero descendant vectors. On the unique cycle, zero/two/at-least-three nonzero edge coefficients admit nonzero vectors throughout via explicit base triangle and subdivision; exactly one nonzero edge forces a zero at a cycle vertex off the active edge. If an unbranched vertex exists there, zero can be located without blocking attached-edge data; otherwise prescribing a nonzero attached coefficient at every branched vertex gives contradiction. Deleting one cycle edge leaves a spanning tree and a second bracket supplies its residual. Thus width 1 iff each edge e has U\V(e) nonempty; else exactly 2 for all fields. Independent F2 brute force verified triangle, triangle-with-leaf, square-with-leaf, square-with-adjacent-leaves bracket images and two-bracket sums; this is corroboration, not the infinite proof.

## originality

PASS

The precise arbitrary-field unicyclic cycle/attachment criterion is not the standard derived-algebra span assertion and is not implied by prior results restricted to low-dimensional derived algebras; the graph-Lie construction itself is credited. Complete priority outside indexed terminology is not claimed.

## value

PASS

A natural infinite family of 2-step graphical Lie algebras has a sharp, constructive exact word-width classification; branching positions on the cycle determine when a single bracket covers the full derived algebra. Witnesses separate width-one from width-two even at fixed cycle length. This is a structural theorem, not a tiny numerical gain.

The dated certificate retains the supplied scientific assessment, sources and limitations.
