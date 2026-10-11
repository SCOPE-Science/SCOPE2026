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

The all-parameter proof is symbolic. The executable check is supplementary and does not replace the proof.

`verify.py` constructs each test graph from an explicit edge list or generator, builds the full ordinary neighborhood complex, and applies the same local elementary-collapse order used in the proof. Before deleting a pair it verifies that the proposed free face has exactly one remaining strict coface. It then verifies that the terminal complex is one-dimensional, has exactly \(2m-n\) edges, has the component count dictated by bipartiteness, and has the cycle ranks stated in the theorem.

The six replay cases are \(C_5\), \(C_6\), the Petersen graph, the Heawood graph, two cycles of lengths \(5\) and \(6\) joined by a bridge, and two cycles of lengths \(6\) and \(8\) joined by a bridge. The last two are irregular and stress that regularity is not assumed.

Limits: the executable cases are finite corroboration only. They do not certify every graph satisfying the hypotheses; the universal claim rests on the explicit collapse proof in `RESULT.md`.
