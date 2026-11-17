---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-08.md",
      "INDEPENDENT_AUDIT_2026-11-08.json"
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

The edge set is the 20 off-diagonal squares of a 5×5 board. Derangements are exactly 44 perfect-matching facets and their subset closure has 734 nonempty faces with f=(20,130,320,220,44). Independently regenerated all facets and Morse vertex-order pairing: 350 disjoint pairs, one 0-cell and 33 2-cells, with all 2320 Hasse incidences verified acyclic. Discrete Morse gives integral wedge of 33 S^2. The frozen verifier additionally specifies independent 2^20 membership tests, boundary ranks (19,111,176,44), all 240 orientation-signed Lefschetz traces, seven cycle-type pairs and Murnaghan–Nakayama inner products; the trace algorithm and character decomposition were inspected in source but not independently reexecuted in full. The identity trace 33, transpose trace 9, ± dimensions 21 and 12 and absence of full invariants follow from the documented complete certificate plus Lefschetz theorem. Pure dimension four, non-top degree homology rules out shellability.

## originality

PASS

A perfect-matching-extendible subcomplex is different from the ordinary matching complex of the same five-crown graph, whose known homology is concentrated in degrees two and three with ranks 1 and 13, respectively. The existing full S5×C2 character calculation is for that larger different complex. Honeycomb graph results and generalized full chessboard capacity complexes do not imply this restricted derangement-facet complex. The new exact homotopy wedge together with rational symmetry splitting is not an identified consequence of those statements; no exhaustive priority guarantee.

## value

PASS

Five-crown is a canonical dense bipartite graph obtained from K5,5 by removing a 1-factor. Its perfect-matching complex tests the topological effect of extendibility beyond ordinary matching complexes, and the nontrivial 240-element symmetry representation is a natural invariant, not merely a count of derangements. The 33-sphere wedge and two distinct central involution eigenspaces are meaningful complete facts for the first four-regular crown case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
