---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

The top boundary-incidence Gram matrix has the exact oriented form L=nI−ss^T. For even n, the affinely centred columns split as the orthogonal free sum of two regular (m−1)-simplices: the product of their polars gives r=n/sqrt(2m(m−1)), while vertex barycenter averaging gives unique enclosing radius sqrt(n(n−2)). For odd n, the simplex barycentric functionals λ_i(x)=x_i/n+s_i(1−1·x/n) have two intrinsic facet gradient norms sqrt(n−1)/n and sqrt(n+3)/n; the sum of normalized slacks yields the unique optimal incenter and r, and the p-positive-vertex barycenter gives the uniquely minimal enclosing ball and strict q-negative-vertex deficit. All centres lie in the affine hull. Both parity asymptotics and almost-equal edge-length contrast follow from exact formulas.

## originality

PASS

Best-of-knowledge original metric parity classification of the canonical boundary-simplex top-Laplacian polytope; its combinatorial and lattice structure is prior art and explicitly credited.

## value

PASS

The original-column Euclidean inradius and minimum enclosing radius are canonical shape-quality invariants of a widely studied simplicial Laplacian polytope. The sharp order-parity gap r_even→sqrt2 versus sqrt(n)r_odd→1, despite edge lengths becoming almost equal, reveals a nontrivial high-dimensional geometric instability with exact contact sets; this is not a mere normalization check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
