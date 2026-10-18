---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

The frozen facet set comprises 17 triangles on 8 vertices and 24 edges; every edge has triangle degree 2 (21 cases) or 3 (3 cases), so the full complex admits no initial free-edge collapse. Independently read all 17 entries in the actual 70,599-byte collapse_certificate.json (Git blob 840ce18d4f180c91ca5213259010406f400640de). Reimplemented a fresh exact replay: for each omitted facet, delete that triangle only, retain all proper faces; every 2-to-1 step removes an edge in exactly one remaining triangle, every 1-to-0 step removes a leaf and its unique edge, no omissions or duplicate omitted facets; all 17 end in a connected 2-regular graph. Twelve terminal cycles have 3 vertices, five have 4, for THIS recorded choice of collapse path. Each elementary collapse preserves simple homotopy, so each puncture collapses to S1. No extrapolation to other triangulations or collapse orders.

## originality

PASS

Compared exact claim and logical implication against primary published literature and relevant Resultary entries. Every facet puncture of the minimal eight-vertex dunce hat collapses to a circle survives on best current evidence, with named full-text/access limits and residual risks. Exact nontrivial class/support/collapse/convolution data are not established by identified older stronger or generic statements.

## value

PASS

A global sensitivity/critical-facet property of the canonical eight-vertex dunce hat: although the full noncollapsible 2-complex lacks free edges, EVERY facet puncture (not just some) has a direct collapse route to a cycle. The 17 explicit finite certificates and simple-homotopy conclusion are natural for discrete Morse theory and deletion robustness; the exact property is neither a generic homology deduction nor a restatement of noncollapsibility.

The dated certificate retains the supplied scientific assessment, sources and limitations.
