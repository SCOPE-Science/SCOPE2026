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
# Verification of exact halved-cube endpoint norms

Run the accompanying standard-library-only checker with:

`python3 check_halved_cube.py`

Observed successful output:

`HALVED_CUBE_ENDPOINT_EXACT_OK dimensions=9 grounded_dimensions=4 full_graph_edges=47102`

For each integer dimension \(3\le n\le11\), the script constructs the full even-weight vertex set and all distance-two edges, evaluates the integral Green-potential with exact fractions, verifies the graph Laplacian equation at **every** vertex, sums **every** absolute electrical edge current, and checks both closed norms and the trace-diagonal identity. The total number of explicitly checked undirected edges across the nine graphs is \(47{,}102\).

For each dimension \(3\le n\le6\), the same code independently solves the grounded graph Laplacian using exact rational Gauss–Jordan elimination and checks every reconstructed potential up to its irrelevant additive constant. All tests use integers and rational numbers; there are no floating-point tolerances or external data files.

The proof for all \(n\ge6\) is the Fourier–Green integral and algebraic binomial-sum evaluation in RESULT.md. Finite verification of dimensions \(3\) through \(11\) does not constitute an exhaustive check of infinitely many dimensions. Independent mathematical auditing has not been performed.
