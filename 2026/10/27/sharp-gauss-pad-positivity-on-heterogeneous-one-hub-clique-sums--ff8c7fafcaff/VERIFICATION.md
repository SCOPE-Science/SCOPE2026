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

The proof is mathematical: orthogonal eigenspace decomposition, three exact off-diagonal formulas and Descartes' unique-positive-root argument. For each petal size \(k\ge2\) the graph has \(n\ge k+2\), making the quartic coefficient of \(h^4\) negative and its lower coefficients positive. Consequently each critical entry has one nonreentrant zero.

Run `python verify.py` in the directory containing `requirements.txt` after installing the listed Python dependency. The verifier independently constructs the adjacency and combinatorial Laplacian matrices; it forms the matrix quotient without using projector formulas, compares rational off-diagonal entries, checks row sums and diagonal signs, and symbolically verifies the critical scalar identities. The tests cover 23 one-hub clique-sum configurations, six rational timestep values each, 2,322 exact off-diagonal entry comparisons and two sharp-boundary examples. The analytic proof, not the finite test census, establishes the universal statement. Software execution does not provide an external proof or independent audit.

The sharp positive root is defined algebraically for arbitrary petal sizes; numerical decimals appearing in examples are illustrations, while exact rational sign substitutions enclose the roots. No claim is made for weighted edges or other graphs. Independent audit is not performed.
