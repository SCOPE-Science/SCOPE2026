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

# Reproducibility and limits

The standalone `verify_categorical.py` requires Python 3 with SymPy. Execute `python verify_categorical.py` in a directory containing the script. The expected final line is:

`CATEGORICAL_COMPLETE_GRAPH_EXACT_OK configurations=100 edge_current_checks=162450 grounded_projection_columns=126 symbolic_identities=PASS`

The script reconstructs the graph from its coordinate adjacency rule; computes exact-rational source potentials for 100 parameter pairs; directly checks graph-Laplacian residuals, absolute edge-current sums and the complementary projection diagonal formula; independently inverts three grounded Laplacians and evaluates all their edge projection columns; and simplifies the analytic coarea and sharp upper-bound identities with symbolic algebra.

The analytic proof uses the tensor decomposition of the graph Laplacian, the exact order of nine potential heights for both coordinate-size orderings, and graph coarea. The finite checks do not claim to enumerate all integer sizes or replace these infinite-family arguments. Self-review has passed; independent audit has not been performed.
