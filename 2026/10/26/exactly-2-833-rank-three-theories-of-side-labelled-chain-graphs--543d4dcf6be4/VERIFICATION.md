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

Every finite bipartite chain graph with named sides A,B is representable as a creation word, 0 inserting an isolated A vertex, 1 inserting a B vertex joined to all preceding A; nested B neighborhoods give the word order, including empty structures. The rank-three Hintikka/Ehrenfeucht–Fraïssé invariant H(G) is built from realized atomic triple types and their extension sets. It is a COMPLETE invariant of rank≤3 sentences (not just a heuristic colour refinement): one-round tuple-type recursion induces exact 3-type of the empty tuple. Appending either creation letter preserves 3-equivalence by an EF strategy matching new vertices and using the winning old strategy. Thus closure of quotient word states is an infinite completeness certificate. Independently RECOMPUTED H for every one of the actual 2833 source certificate words, checked all signatures unique, all 5666 claimed successors exactly, BFS reachability of all 2833 states and distances equal claimed shortest word lengths. The maximum is 21 with exactly two words at that distance: 001100110011011001100, 110011001001100110011. This is exhaustive for all creation words because the fully verified transition table is closed, not a bounded word-sample extrapolation.

## originality

PASS

Best-of-knowledge PASS for the precise complete 2833 rank-three theory census and sharp 21-vertex minimal kernel for named-side chain graphs. Pikhurko–Verbitsky provide EF foundations, Boyacı–Ekim–Shalom exploit chain structure for MaxCut, and Alecu–Atminas–Lozin–Malyshev study quasi-chain structural decomposition. None of the inspected mathematical results states this numerical first-order classification. Published rank-q results for other graph/word classes differ in signature and domain.

## value

PASS

The 2833 precise theory count and optimal 21-vertex kernel give a natural complete low-rank model-theoretic classification of all finite bipartite chain graphs with named sides. The sharp two extremal witness classes and verified finite syntactic quotient are independently useful for testing bounded-depth logical properties; this is a complete canonical finite classification rather than an arbitrary numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
