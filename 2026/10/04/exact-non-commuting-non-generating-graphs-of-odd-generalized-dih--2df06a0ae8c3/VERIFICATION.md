---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

Odd order makes inversion fix only the identity, so the center is trivial and distinct reflections never commute. Rotations commute with one another. For a nonidentity rotation x and reflection r_a, the generated subgroup is Dih(<x>), so adjacency occurs exactly when <x> is proper. For two reflections, their product is ab⁻¹ and the generated subgroup is Dih(<ab⁻¹>), giving the stated Cayley adjacency. Degree and edge formulas follow by counting. If A is noncyclic, every nonidentity element is a non-generator, producing the complete join; if A is cyclic, generators are precisely the unit differences. Fresh independent group enumeration for C3, C9, C15, C3×C3, C3×C5 and C5×C5 reproduced centers, every pair adjacency, degrees and the formula 2|E|=3|A|b(A).

## originality

PASS

Freedman's complete primary paper studies exactly the non-commuting, non-generating graph, proving broad component and diameter alternatives and discussing Frobenius/dihedral phenomena. The inspected full text does not state the all-odd-abelian-kernel generalized-dihedral edge decomposition, degrees, edge count, noncyclic join form, or cyclic unitary-Cayley complement. The nilpotent theorem is inapplicable to nontrivial odd generalized dihedral groups. Resultary returned the assigned theorem as the exact match; neighboring generalized-dihedral records concern different graph invariants.

## value

PASS

The source literature emphasizes component structure and diameter of this graph. Giving the entire graph for a standard infinite nonnilpotent family—down to isolated vertices, degrees, edge count, an order-only join collapse for noncyclic kernels and a classical Cayley-graph identification for cyclic kernels—is a natural complete structural classification with reusable consequences.

The dated certificate retains the supplied scientific assessment, sources and limitations.
