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

# Verification record

The proof uses the complete finite-field multiplication table implicit in the matrix-unit basis and works uniformly in every characteristic. The key checkable steps are equation (1) for the inner commutator; the graph-incidence matrix rank on edges of equal endpoint labels; the fact that a unicyclic graph has a single possible cycle dependence; the two transfer-matrix eigenvalues; and the exceptional all-monochromatic, all-nonzero cycle correction.

Execute the packaged standalone program with `python3 check_rank.py`. It forms the product of basis units directly, enumerates every element for the stated small prime fields, constructs its full adjoint matrix and performs exact modular Gaussian elimination. It separately expands the symbolic claimed polynomial by integer arithmetic and checks the commuting-pair count and rank-one coefficient. The checked configurations are a four-cycle over \(\mathbf F_2\) and \(\mathbf F_3\), that cycle with one pendant edge over both fields, a four-cycle with two pendant edges over \(\mathbf F_2\), and a six-cycle over \(\mathbf F_2\). All six exhaustive checks passed.

The symbolic proof extends beyond these finite tests. The executable checks do not address possible publication overlap or independent mathematical validation. Neither of those is asserted.
