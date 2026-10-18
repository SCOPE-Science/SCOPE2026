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

# Exact verification of integral geometric torus lattices

The standalone `verify_k333.py` reconstructs the full nine-vertex graph and its cubical unordered deleted product with 36 zero-, 189 one-, and 216 two-cells, verifying \(\partial_1\partial_2=0\). It enumerates all 6705 simple undirected graph cycles canonically and all 2160 vertex-disjoint pairs, checks the integral boundaries of each product torus, and checks the six length-specific counts.

The exact rank argument uses a rank-135 calculation over \(\mathbb F_3\) as a **lower bound only**, paired with an 81-column integral cycle certificate whose 81-coordinate coefficient determinant is \(+1\). Together these prove exact boundary rank and integral basis saturation. Selected indices are in `basis_indices.json`, with no other external data. Integral Hermite and Smith normal forms then verify the complete quotient invariants, including the free rank and saturation of the rank-deficient case. The key detected nonunit Smith factor for length \((3,6)\) is \(4\), so the corresponding quotient is cyclic.

Run `python verify_k333.py` in a directory containing `basis_indices.json`, using Python 3.11 or newer and `sympy==1.14.0`. The expected success marker is `VERIFY_OK_K333_INTEGRAL_LENGTH_RESTRICTED_TORUS_LATTICES`.

These are exhaustive exact computations for one fixed graph, not a claim about arbitrary larger complete tripartite graphs or about an unbounded family. A separate external scientific audit has not occurred.
