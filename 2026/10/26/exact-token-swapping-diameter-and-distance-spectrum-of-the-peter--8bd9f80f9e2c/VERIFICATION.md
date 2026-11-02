---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

Breadth-first search over a bijective factorial encoding of S_10, with exactly 15 edge-transposition generators on GP(5,2), computes true shortest distances because FIFO discovers vertices at minimal depth. Left translation makes the Cayley graph vertex transitive, so identity eccentricity equals its diameter. A new, separately written C++ implementation used the Kneser KG(5,2) graph and all 3,628,800 states; its complete distances reproduce exactly 14 shells (largest nonempty index 13), 11,616 distance-13 placements partitioned among seven stated cycle types, and deficit counts (431532,1509516,1382012,299060,6680) for gaps 0..4. Each swap moves two tokens at most one base-graph edge, proving transport lower bound L=ceil(sum distances/2). This is an EXHAUSTIVE FINITE proof for Petersen, not an infinite-family argument.

## originality

PASS

Best-of-knowledge novel exact Petersen token-swapping metric census, not new BFS algorithm or general token-swapping definition. Independent comparisons include alternative graph labels and Cayley-word conventions, general algorithms, transposition-tree theorems, Resultary numeric records and a plausible survey. No inspected statement supplies the exact histogram; unindexed older numeric enumeration remains possible.

## value

PASS

Petersen is a canonical small, highly symmetric cubic graph with non-tree edges. The complete 10!-state distance spectrum, 11,616 farthest states, cycle-type classification and sharp four-swap gap from transport bound are natural benchmark invariants reusable in sorting algorithm validation; not an arbitrary slice or a general-family claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
