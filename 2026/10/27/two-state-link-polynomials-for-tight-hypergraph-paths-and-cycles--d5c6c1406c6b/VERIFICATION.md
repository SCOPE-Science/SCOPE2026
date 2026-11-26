---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Over an individually named finite base A, an extension point's link specifies the induced one-point extension. Two realizations of the same link are conjugate over A by homogeneity. A link is allowed exactly when it omits at least one of the three pairs of every hyperedge of A: a new tetrahedron must consist of the extension point and three adjacent base vertices. Every allowed link has arbitrarily many distinct realizations by taking copies with no edges involving two new points and using the age extension property. Thus the allowed links give all nonalgebraic types exactly once, and the only algebraic types are the n equality types. The designated bases are admissible: a tetrahedron extending the base triple (i,i+1,i+2) would require its fourth vertex simultaneously to be i−1 and i+3; this cannot occur on the path or modulo n≥5. For n=4 the cycle is forbidden. The constrained pairs are consecutive edges a_i and distinct distance-two chords b_i (including at n=5); each constraint is a_i a_(i+1) b_i=0. Summing over each private b_i gives 1+u except at (a_i,a_(i+1))=(1,1), where it gives 1. The weight u^(a_(i+1)) produces exactly the stated M; a fixed labelled starting edge leads to vM^(n−2)1 for the path and trace M^n for the cycle, without any rotational quotient. Isolated pair variables explain the free exponents. At u=1 the determinant is −2 and trace 3, so eigenvalue powers give all the stated counts and the fraction with decay base (3+√17)/8>7/8. The supporting verifier and recorded output were inspected, not executed. Independent inclusion-exclusion over sets of base triples gives the small totals, including 573, 16328 and 930432, and the n=5 cycle coefficient sequence (1,10,45,115,175,152,65,10); replay /workspace/branches/independent_small_checks.py. The proof, not the finite tests, covers all n.

## originality

PASS

The supported contribution is the explicit all-length, degree-refined type count and resulting probability over these two named-base families, not the Fraïssé framework or a new transfer-matrix method. The auxiliary problem is the weak independence polynomial of a loose hyperpath or hypercycle and was checked in that form too. The strongest inspected general weak-independence recurrences compute the invariant for any hypergraph but do not provide the family-specific two-state simplification or its sharp type-count asymptotic in the passages read. The inspected exact expansion result counts a different kind of independent set.

## value

PASS

The tight path and cycle provide natural overlapping-edge bases in the same homogeneous structure, with respectively open and periodic boundary conditions. The formulas determine every rank of the link spectrum, not just small counts, and quantify the difference from treating consecutive tetrahedron constraints as independent. The exact family-wide reduction to two states gives usable information not supplied by brute force or the base's age alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
