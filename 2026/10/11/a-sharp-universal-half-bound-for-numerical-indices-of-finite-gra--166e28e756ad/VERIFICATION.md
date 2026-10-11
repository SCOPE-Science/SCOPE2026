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
# Verification of the graph numerical-index half bound

The operator estimate is proved analytically. Its critical steps are the edge-molecule convex-hull reduction, integrality of extreme normalized graph-Lipschitz potentials, and the two-function decomposition from a directed nonnegative shortest-path problem. For each arc \(s\to t\), the edge cost is \(1+\min\{0,h(t)-h(s)\}\). Directed distances from a neutral-edge endpoint define the first Lipschitz summand; subtracting it from \(h\) defines the second. The proof checks both directed inequalities, not only experimental samples.

To reproduce finite validation using only the Python standard library, from the extracted package root execute `python3 artifacts/verify.py`. The exact output is:

`VERIFY_OK connected_labeled_graphs= 771 integer_potentials= 41463 equal_edge_decompositions= 88156 n=2..5`

The script exhausts connected labeled simple graphs of orders \(2\) to \(5\), with the base vertex fixed as \(0\). Every normalized integer \(1\)-Lipschitz potential lies in \(\{-(n-1),\ldots,n-1\}\) coordinatewise, so the checker covers that finite set exactly. The script tests both decomposition Lipschitz inequalities at each equal-valued edge. These checks do not certify infinitely many graph orders, all real potentials, or all operators; the symbolic argument supplies those cases. The equal-value decomposition is proved for every integer potential, while only extreme dual potentials need be integral for the numerical-radius argument.

The sharpness input is the exact three-point equilateral computation (Cobollo, Guirao and Montesinos, arXiv:2304.13183v1, Corollary 5.3), not an empirical upper bound. No independent audit has been performed.
