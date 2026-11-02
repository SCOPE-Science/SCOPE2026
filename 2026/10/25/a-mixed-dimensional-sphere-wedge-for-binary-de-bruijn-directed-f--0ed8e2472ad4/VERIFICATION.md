---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

The final assertion is for exactly the eight length-three binary-word vertices and fourteen nonloop shift-register arcs, faces being directed acyclic arc sets with indegree at most one at every target. Independently generated all 2^14 masks: precisely 2,186 nonempty faces with f-vector (14,84,280,560,672,448,128), 132 facets (four size 6, 128 size 7). Reconstructed indexed greedy matching: 1,091 pairs and critical faces 0x1 (dimension 0), 0x348a (dimension 5), 0x2cd2 and 0x32cc (dimension 6); independent Kahn traversal visits all 2,186 vertices across all 10,192 oriented Hasse incidences. Direct signed elimination of matched faces gives zero integral 6-to-5 Morse boundary for both critical 6-cells, seven cancellations apiece. Thus CW model has one 0-cell, one 5-cell, two 6-cells, trivial attaching degree in pi_5(S^5)=Z, hence S^5 ∨ S^6 ∨ S^6, not just homology. The fetched verifier gives a separate ordinary boundary rank calculation and exact rational complement action (H6 matrix swaps two top generators, H5 Lefschetz trace -1); checked program algorithm and signed conventions, no nonfinite extrapolation.

## originality

PASS

Best-of-knowledge PASS for the exact binary order-three de Bruijn directed-forest homotopy and bit-complement representation, after statement-level comparisons with directed-tree complexes and published small-complex homotopy results. This strongly cyclic shift-register digraph is not a doubled underlying tree, not a DAG and not the tree-source families in the inspected prior results; none yields the concrete invariants from an applicable theorem. Inaccessible full texts remain risks rather than fabricated noncoverage.

## value

PASS

A canonical binary order-three de Bruijn shift-register network yields a complete integral homotopy and nontrivial automorphism-module invariant for its full natural directed-forest complex. The mixed dimension-5/6 cell structure and sign representation are not determined by f-vector or standard results for acyclic/bidirected tree families. It is one motivated finite graph, not a general classification; finite exact results can have standalone value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
