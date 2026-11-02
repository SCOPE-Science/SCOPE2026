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

# Verification and limits

Run \(\texttt{python verify.py}\) from the extracted file directory; the program uses the Python standard library and deterministically reconstructs the relevant graphs, without downloading anything. In the reviewed run its output was:

```text
VERIFY_OK graph_instances=8 graph_subsets=104272 balanced_factor_checks=6 rectangular_checks=18
```

The tested graph sizes are \((m,n)\in\{(2,2),(2,3),(2,4),(2,5),(3,3),(3,4),(3,5),(4,4)\}\). Every one of the corresponding 104272 vertex subsets is examined. The program checks bipartiteness by direct graph two-coloring, maximality by all one-vertex extensions, and equality against independently calculated proposed coefficients. It also checks that bipartiteness agrees with all row/column degrees at most two, evaluates the balanced coefficient recurrence through degree seven, and checks 18 further rectangular coefficients for positivity.

No finite computation is used to establish a statement for all board sizes; the exhaustive classification and labeled cycle decomposition in the proof establish the exact polynomial. The asymptotic probability and first-order bias use the stated analytic singularity argument, not numerical extrapolation. This is a self-review with no independent external audit.
