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

The proof was reconstructed from the primary definitions rather than inferred from search snippets.

For the column case, a grid state selects one matrix entry in each row and column. The source's bound \(A'(x)\le\mathcal C\) is equality exactly when every selected entry is a column minimum. Hence column-perfect states are exactly perfect matchings of the bipartite graph of column-minimal entries. The row case is identical. When \(\mathcal C\le\mathcal R\), perfect means column-perfect; when \(\mathcal R<\mathcal C\), perfect means row-perfect.

If two perfect matchings exist, their symmetric difference is a nonempty union of alternating even cycles. Conversely, toggling an alternating cycle in one perfect matching creates another. It follows that a perfect state is unique exactly when there is no alternating cycle in the appropriate minimizer graph. Comparing the source's Definition 2.1 with this cycle shows that its matrix loops are the same alternating cycles for column-perfect states.

The bundled script `artifacts/verify_matching_trichotomy.py` exhaustively checks every binary matrix of sizes \(1\) through \(4\). It compares direct enumeration of all grid-state permutations against enumeration of perfect matchings in the selected minimizer graph and verifies the zero/one/multiple classification.

The finite replay is not used as a proof of the universal statement. The independent-audit channel has not been performed.
