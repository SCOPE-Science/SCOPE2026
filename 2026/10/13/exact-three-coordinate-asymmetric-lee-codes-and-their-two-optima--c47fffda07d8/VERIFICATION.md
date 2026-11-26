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

Minimizing forbidden pairs is exactly independent-set search on the complement of the stated compatibility graph. My independent replay /workspace/replay/3.py built the forbidden graph from the symbol costs, then partitioned every candidate set by including or excluding one conflict vertex. A cover by disjoint conflict cliques is an upper bound on extensions, and pruning strictly below (not at) the incumbent preserves every equality case. An edgeless remainder is attained uniquely by taking all remaining vertices. In 2,677 nodes this reproduced 1,752 compatibility edges, optimum 19 and exactly 32 distinct masks. Explicit coordinate permutations and local swaps sent both frozen masks through disjoint orbits of sizes 8 and 24 exhausting the optimum set. The action has order 384, giving stabilizers 48 and 16. Pair histograms for distances 3 through 8 are (24,69,0,24,24,30) and (28,61,4,24,24,30), each accounting for all 171 pairs. The frozen Bron–Kerbosch histogram and greedy-coloring verifier were inspected; the independent search establishes the optimum and equality census without depending on the histogram of smaller maximal cliques.

## originality

PASS

The original ALD and its general bounding framework are prior. Its directly comparable numerical entry is a strict interval containing 19, not an exact optimum. The exact maximum and the two-orbit geometry with enumerated invariants are distinct on the inspected evidence.

## value

PASS

Minimum distance three is a natural low-distance ALD design threshold already singled out in the literature, and length three is an existing comparison cell with a substantial explicit bound gap. Closing 6–30 to 19 gives an exact small benchmark for bounding and construction methods. More importantly, a complete optimizer census shows equal cardinality need not mean equal geometry: there are two inequivalent optimal designs with different numbers of closest pairs. A researcher testing exact optimization, symmetry reduction or robustness criteria based on close pairs could use these precise data.

The dated certificate retains the supplied scientific assessment, sources and limitations.
