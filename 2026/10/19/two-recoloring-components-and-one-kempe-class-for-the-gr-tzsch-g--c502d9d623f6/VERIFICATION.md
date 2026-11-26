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

Independent executable reproduction: python /workspace/review-evidence/5/replay.py. The graph is generated from the 20 prescribed edges. Restricted-growth words exhaust unlabeled proper partitions; all 520 require four colors, so expanding by every palette permutation gives 12,480 named states uniquely. Common one-coordinate deletion fibers give exactly the single-vertex edges; two-color bit-mask closures give exactly the Kempe switches, including singletons. The reproduction finds 45,240 and 87,120 undirected edges; the first graph splits into two 6,240-state components with minimum degree 5, the second is connected, and 37,440 edges cross the first graph's split. It tests the parity rule on all 299,520 state–permutation pairs. Shortest-path computations from one representative in each palette orbit (without using pentagon symmetries) determine the full census because a palette permutation preserves both move graphs and the within-component distances. Each recoloring component has 1,080, 5,100 and 60 states of eccentricity 15, 16 and 17 respectively; all 12,480 Kempe states have eccentricity 7. The displayed crossing witness is also a legal switch of the stated two-color component and has endpoints in different recoloring components. The supplied verifier and recorded output were inspected, not executed. No inference is drawn for other palettes or graphs.

## originality

PASS

Best-of-knowledge pass for the exact joint reconfiguration classification, especially the Kempe eccentricity, edge census and cross-component count. The known static count is not new. Kempe connectivity in isolation is also not novel: the Las Vergnas–Meyniel degeneracy lemma applies, even though the main regular-graph result cited in the frozen text does not. Two distinct later-dated Resultary records explicitly reproduce the frozen single-vertex component metrics and parity results between them; this is real overlap, not a title match or independent proof of release priority. Neither inspected record supplies the frozen Kempe census, distance profile or cross-component count, and the theorem establishing the contrast with disconnected single-vertex dynamics is not a direct corollary of the degeneracy lemma. The pass does not claim priority over every version of the overlapping recoloring-only evidence.

## value

PASS

The Grötzsch graph is a canonical small triangle-free four-chromatic graph, and four colors is its critical palette. The comparison isolates a reachability obstruction despite every state admitting at least five local moves, classifies the symmetry of that obstruction, and quantifies exactly how Kempe moves bridge it and shorten distances. This is usable finite benchmark data for two natural reconfiguration rules, not merely a repeat of the static count or qualitative Kempe connectivity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
