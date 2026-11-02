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

# Reproducible verification

Run `python3 verify_abelian_ideal_schubert.py` with Python 3 and no third-party packages. The program constructs every row-reduced-echelon \(\alpha(G)\)-subspace independently of the formula; it directly tests its edge-coordinate brackets and compares the resulting count with the independent-support graph formula.

Every labeled simple graph on \(1\), \(2\), \(3\), or \(4\) vertices is checked over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_4\), giving \(225\) cases. Four more graphs (the five-vertex path, five-cycle, five-clique and six-vertex path) are checked over \(\mathbb F_2\) and \(\mathbb F_3\), giving \(8\) more cases. The two four-vertex witnesses are additionally checked directly over \(\mathbb F_5\), giving \(2\) more cases, for \(235\) independently enumerated cases in total. The arithmetic of \(\mathbb F_4\) uses the irreducible polynomial \(u^2+u+1\). Additional checks confirm the exact witness formulas for four field sizes and their invariance under vertex relabeling.

Expected final output contains `GRAPH_MAXIMAL_ABELIAN_SCHUBERT_OK 235` and the witness count list. All \(235\) cases passed when this package was prepared. These computations are not a proof for arbitrary fields or larger graphs. The proof in `RESULT.md` identifies the equations in every echelon stratum and establishes the unbounded all-fields statement.
