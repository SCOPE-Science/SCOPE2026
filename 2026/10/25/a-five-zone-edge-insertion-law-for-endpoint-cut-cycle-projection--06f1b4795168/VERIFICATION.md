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

# Exact-rational verification and scope

The complete all-integer proof is in `RESULT.md`, equations (1)–(7). The independent numerical reconstruction provided by `check_projection.py` uses the Python standard library `fractions.Fraction`; it does not call the asserted rank-one formula to build its matrix.

It constructs the incidence columns of the graph, forms a grounded Laplacian by deleting one vertex row, inverts that Laplacian by exact Gaussian elimination, and evaluates the cut projector \(Q=B^{\mathsf T}L_{\mathrm{ground}}^{-1}B\) and the complementary cycle projector \(I-Q\). Every absolute column sum is compared against the separately encoded three-orbit formulas. The result is also compared against the global norm formulas and the five-zone sign conditions.

Command: `python check_projection.py`

Observed output:

`GRAPH_PROJECTION_CERTIFICATE_OK cases=58 columns=1858`

The cases consist of all \(2\le m,n\le8\), plus the pairs \((m,5)\) for \(9\le m\le13\), and \((m,6)\) for \(11\le m\le14\). These checks cover the small-size exceptional orbit maxima and both strict onset zones in the two latter slices. They are finite tests and do not certify the inequalities for arbitrarily large parameters; the symbolic proof provides the universal argument.

No external mathematical audit has been performed. There is no claim of verification of arbitrary graph families or minimum-norm nonorthogonal projections.
