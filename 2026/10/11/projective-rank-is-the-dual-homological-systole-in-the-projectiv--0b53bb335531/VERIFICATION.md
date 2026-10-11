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

The claim is proved without numerical extrapolation. The verification replay checks the following exact implications.

1. For a cellular embedding, an edge-deleted subgraph is local exactly when the nonzero ambient class in \(H^1(\mathbb{RP}^2;\mathbb F_2)\) restricts trivially.
2. Triviality on the surviving graph is equivalent to the existence of a vertex cochain \(f\) for which \(u+\delta f\) is supported only on deleted edges. Minimizing deleted edges therefore equals minimizing the negative-edge support over all vertex switchings, the frustration index.
3. Cellular Poincare duality takes the support of \(u+\delta f\) to the same-numbered set of dual edges and takes its nonzero cohomology class to the nonzero class in \(H_1(\mathbb{RP}^2;\mathbb F_2)\). This proves equality with the dual homological systole.
4. A dual closed walk is homologically nontrivial exactly when a lift starts at \(\tilde v\) and ends at \(\tau\tilde v\); minimizing over starting vertices gives the double-cover distance formula.
5. Substitution into the cited alternating-link theorem gives the two Jones-piece breadth formulas.

The scope is limited to cellular embeddings for the duality and lift formulas. No finite computation, timeout, or experimental enumeration is used to assert a general theorem.
