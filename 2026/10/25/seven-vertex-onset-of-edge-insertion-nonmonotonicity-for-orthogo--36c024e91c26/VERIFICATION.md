---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For connected simple unweighted G with oriented incidence B (one row deleted), the Euclidean cycle-space orthogonal projection is C_G=I-B^T(BB^T)^-1 B; all column-sum norms can be computed exactly as integer cofactors divided by the matrix-tree determinant. The inspected C99 verifier enumerates all labeled connected graph masks on n=2,...,6 (connected counts 1,4,38,728,26704), all 189587 missing-edge additions, and compares exact rational norms by cross-multiplication with no cycle-norm decrease. Finite exhaustive enumeration proves the finite bound if the arithmetic algorithm is sound; independently, graph_atlas_g yielded all 142 unlabeled connected isomorphism types through six vertices, and exact SymPy calculations checked all 821 non-isomorphic representatives' missing-edge insertions with no decreases. The explicit 7-vertex edge list and insertion (1,5) independently yield 313/153 to 55/27, difference 4/459. Arbitrary orientation conjugates by diagonal sign and cannot change induced l1/linfty norms. Finite assertion is genuinely exhaustive, not an extrapolation.

## originality

PASS

Dilworth--Kutzarova--Ostrovskii 2023 study minimal/invariant cycle-space projections, including special graph families, but the present object is specifically the Euclidean orthogonal projector and changes its ambient edge space under insertion. Their invariant-projection constructions do not imply all-small-graph monotonicity or this sharp counterexample.

## value

PASS

The sharp onset at graph order seven for a natural canonical projection norm is a meaningful finite classification of how graph edge insertion fails to preserve an operator norm, despite effective-resistance Rayleigh monotonicity. A concrete exact witness and exhaustive lower-order barrier make the cutoff independently useful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
