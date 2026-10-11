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

After unit-distance normalization, \(\mathcal F(M)\) is the zero-sum hyperplane with norm \(\|\mu\|=\frac12\sum|\mu_i|\), and its unit ball is the convex hull of the molecules \(u_{ij}=e_i-e_j\). For any norm-one operator, finite norm attainment gives a molecule whose image has positive and negative mass one; the four sign configurations of its two selected coordinates yield an indicator functional norming the molecule and evaluating the image with modulus at least one half. Thus every norm-one operator has numerical radius at least one half. The explicit three-coordinate cyclic operator in the package has norm one and numerical radius at most one half; for a general norming pair, convex decomposition forces every positive-weight molecule to be normed by the same functional, extending the molecule estimate. The two-point boundary is one-dimensional.

## originality

PASS

The full Cobollo-Guirao-Montesinos paper was inspected: Corollary 5.3 gives the equilateral triangle value \(1/2\), but the paper is explicitly about two-dimensional free spaces and contains no all-cardinality equilateral theorem. The polyhedral numerical-index paper supplies a generic finite method and an unrelated three-dimensional example; the extreme-point paper characterizes molecules under strict metric segments but does not compute this numerical index. Searches using the isometric aliases zero-sum \(\ell_1\) hyperplane, root polytope and complete/equilateral metric found no stronger theorem. Resultary likewise returned only the audited all-cardinality result.

## value

PASS

Finite equilateral metrics form the canonical homogeneous family, and the numerical index is a natural operator-geometric invariant. The theorem gives an exact dimension-independent value in every dimension above one, with a sharp two-point threshold and an explicit extremal operator. This is a reusable family theorem rather than a tiny-instance computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
