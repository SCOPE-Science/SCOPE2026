---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Independently reconstructed both labeled graphs and tested every common-neighbor count and degree, hence their shared strongly regular parameters and spectrum. For diameter two, unselected vertices are distinguished exactly by their selected-neighbor subsets; selected vertices are distinguished by their own zero distances. Enumerated all subsets through size four and matched the explicit rook cross families and all three disjoint Shrikhande translation families. Formed every pairwise basis overlap. In the rook case the one-exchange adjacency agrees with equality of the central row/column and variation of exactly one excluded coordinate; all 288 moves slide. Shrikhande has no overlap of size three. For exact two exchanges both graphs are connected, with 1872 and 240 edges, degrees 26 and 10, and eccentricity three at every basis. At capacity five consecutive size-four states along any path are identical or share three landmarks, so different one-exchange components cannot join. At six, each exact-two step uses the union of the two bases and costs four add/delete moves; the diameter-three paths therefore give the claimed twelve-step upper bound, not optimality of twelve.

## originality

PASS

Pass for the ordinary four-landmark mobility contrast and the exact two-replacement restoration and capacity threshold, not for the metric dimensions, rook basis count or its underlying shape. Neither the confirmed prior static characterization nor the close indexed reconfiguration comparisons supplies the Shrikhande ordinary-basis obstruction and paired two-exchange connectivity and distances. Thesis coverage remains an access risk, not evidence of overlap.

## value

PASS

The graph pair is a canonical test of what strong regularity and shared metric dimension do not determine. The ordinary basis spaces genuinely differ in local mobility, and the exact two-exchange calculation gives a sharp, comparable resolution-preserving capacity boundary rather than a bare census. These are usable finite benchmarks for landmark reconfiguration; no general bound for strongly regular graphs is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
