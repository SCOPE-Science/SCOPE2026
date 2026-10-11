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

# Verification of the Petersen symmetric edge polytope metric theorem

Run `python verify.py` alongside this document with a standard Python installation; no third-party packages, external papers, network access, or precomputed certificate files are needed. The verifier independently constructs all ten vertices of \(KG(5,2)\), its fifteen edges, and one graph spanning tree. Every integer potential satisfying the facet criterion has a representative among the \(3^9\) tree-edge sign assignments; feasibility is tested on all fifteen edges, and each feasible potential is checked for connected tight-edge subgraph.

The exact enumeration gives \(2613\) feasible potentials modulo constants and \(1410\) polar vertices. The maximum of \(10\sum_U p_U^2-(\sum_U p_U)^2\) is \(56\), attained exactly thirty times, so the largest centered polar squared norm is \(56/10=28/5\). An independent explicit construction of the thirty candidate contact vectors agrees with all thirty maximizers. Each has coordinate numerator values \(6,-4,1\) over denominator five, and exact Gram entries, tested directly from all fifteen vectors, show that they span the full nine-dimensional zero-sum hyperplane. A rational elimination confirms rank nine. The squared inradius is consequently \(5/28\).

This computation exhaustively verifies the finite graph, not an infinite family or an inference from a software timeout. The combinatorial cross-intersection argument and the positive-definite Gram formula in `RESULT.md` provide the direct mathematical proof; the enumeration is a separate exact check. The independent-audit channel has not been performed.
