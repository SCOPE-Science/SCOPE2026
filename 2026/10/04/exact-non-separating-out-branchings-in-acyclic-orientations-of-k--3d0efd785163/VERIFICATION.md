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
# Verification

The proof has two logically separate parts. The four negative block codes are certified by forced-edge arguments: a specific vertex has every incident edge in every out-branching, so its deletion complement is disconnected. The positive part is constructive and gives one parent for each non-source vertex in four cases; the unused edges exhibited in the proof form a connected spanning subgraph.

`verify_k3n.py` implements the canonical block-word model directly. For \(4\le n\le30\), it instantiates every positive block word and checks that the stated parent construction uses only forward arcs, has exactly \(|V|-1\) edges, forms a spanning tree, and leaves a connected complement. For \(4\le n\le7\), it separately enumerates every possible parent choice for every non-source vertex and checks whether any resulting out-branching has connected complement. This exhaustive computation covers both positive and negative orientations in that finite range.

Replay output:

```
ALL CHECKS PASSED; constructed_cases=9792; exhaustive_cases=295; exhaustive_n=4..7; construction_n=4..30
```

Limits: exhaustive search is finite, and the construction replay through \(n=30\) is also finite. Neither is used to infer the theorem for all \(n\); the general proof in `RESULT.md` supplies the infinite quantifier. The computation does not count all valid non-separating out-branchings and makes no claim about \(K_{m,n}\) with \(m\ge4\).
