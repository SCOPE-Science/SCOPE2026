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

The standalone `verify.py` enumerates admissible simplices directly from graph edges and constructs every signed simplicial boundary (dimensions two and three). It performs rank elimination over the prime fields of characteristics 2 and 3, checks the exact face counts, first and second homology vanishing, and the predicted top rank. It exhaustively treats all connected bipartite graphs for labeled bipartitions (1,1), (2,2), (2,3), and (3,3), plus selected longer even cycles, bicliques, the cube, a Fano-plane incidence graph, and linked squares: 240 connected cases. It also exhaustively checks projected relative boundary surjectivity for all 639 missing cross-edges over connected labeled (3,3) bipartite graphs, in both characteristics.

Replay: `python3 verify.py`
Expected final line: `VERIFY_OK 240 connected graphs and 639 edge insertions; mod 2/3 exact ranks`

This is a finite numerical check, not an integral homotopy proof. The exact integral rank and all-graph homotopy arguments are in RESULT.md. The finite checks have no external audit status.
