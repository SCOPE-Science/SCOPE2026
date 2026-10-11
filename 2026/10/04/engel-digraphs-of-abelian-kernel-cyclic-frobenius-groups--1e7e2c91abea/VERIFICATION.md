---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

The proof reconstructs every arc. Fixed-point-freeness gives trivial center and hypercenter. For an outside target \(y\), the map \(a\mapsto[a,y]\) is an endomorphism of the finite abelian kernel with trivial kernel \(C_K(y)\), hence an automorphism; therefore a kernel-origin Engel commutator cannot die. For an outside source and kernel target, the first commutator is a nontrivial kernel element and the second vanishes because the kernel is abelian, giving exact depth two. Since the quotient is cyclic, outside-outside commutators lie in the kernel and can vanish under iteration exactly when the elements already commute; the outside centralizer is the unique cyclic conjugate complement containing the target. These facts prove the component partition and all formulas. The packaged finite replay was inspected as corroboration only, not as the universal proof.

## originality

PASS

The closest general source proves only that Frobenius groups obstruct strong connectivity and, specifically, that no nontrivial kernel element has an Engel arc to an outside element. The later co-Engel paper computes dihedral and prime-by-prime special families. Neither inspected source classifies every directed arc for arbitrary finite abelian Frobenius kernels with cyclic complement, nor gives the full strong-component star or the uniform equality with the 2-Engel graph. The fresh Resultary search returned the assigned finding itself as the exact match and only non-covering neighboring group-graph results.

## value

PASS

Frobenius groups are singled out by the foundational connectivity theorem as the principal soluble obstruction to strong connectivity. Replacing that qualitative obstruction by the complete directed graph, exact Engel depth, condensation, degrees, and arc count on a broad natural family is a substantive structural refinement rather than an isolated computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
