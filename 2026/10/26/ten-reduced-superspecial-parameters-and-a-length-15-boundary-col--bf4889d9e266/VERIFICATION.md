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

The frozen proof falsely calls the v² coefficient of B a nonzero constant and conflates the length of the scheme-theoretic u=2 fiber with the sum of the full local lengths over it. The complete repaired RESULT.md corrects both: the coefficient is 3(u−2), B(2,v)=0, and the fiber cut by u−2 has length 5, whereas the three affine intersection local algebras over u=2 have total length 17. The revised proof uses the determinant of multiplication by B in the rank-five free k[u]-module k[u,v]/(A). Its order at each base point equals the length of its cokernel over the local DVR, hence the sum of the local geometric lengths. Independent coefficient convolution and multiplication-matrix computation gave the stated determinant, eight simple other roots, the two nonzero Jacobians (8), and the three boundary gcds. Independently imposing (u−2)^17 and inverting (v−3)(v−4) gives a quotient with 15 standard monomials, confirming the local length. The relative Cartier entries are the specified even coefficients; this zero scheme on the smooth family, not an absolute semilinear matrix on the boundary, is what is counted. Finite support gives the complete intersection, and the homogeneous forms also rule out infinity.

## originality

PASS

The repair preserves the original outcome but distinguishes the fiber length from the affine local length precisely. The supported distinct contribution is the exact decomposition for this marked plane, in particular the affine length-15 triple collision. Prior work treats the very same normal form, establishes general reducedness in smooth Rosenhain coordinates, and catalogues the two abstract curves; none of the inspected statements accounts for the extended coefficient ideal at the degenerate parameter.

## value

PASS

On a natural normal-form family with a distinguished branch pair, a smooth moduli census does not account for intersections absorbed by degeneration. The exact marked decomposition distinguishes ten simple smooth points from local mass 15 at the unique excluded triple collision and locates all ten smooth parameters. The 5-versus-17 length distinction makes this useful for checking elimination multiplicities and compactification comparisons rather than just reproducing a list of abstract genus-two curves.

The dated certificate retains the supplied scientific assessment, sources and limitations.
