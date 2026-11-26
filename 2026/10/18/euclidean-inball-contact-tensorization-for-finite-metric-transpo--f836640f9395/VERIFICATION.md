---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The edge-root directions span the zero-sum hyperplane, and central symmetry gives an interior origin. Its polar inequalities are exactly the centered Lipschitz constraints. Polar vertices give support-value-one facets, and the longest polar vectors are vertices by strict convexity. Central symmetry allows centering an arbitrary feasible ball at zero without loss of radius. Under the uniform independent coordinates the conditional variance sum weights each orthogonal Hoeffding term on A by |A| rather than 1. Equality forces all |A|>=2 terms to vanish. Centered additive terms are individually feasible and reconstruct a feasible sum for the sum metric; sharpness forces every term to be a factor maximizer. Uniqueness of centered factors gives the product contact count. Antipodal active inequalities force each optimal center to annihilate the contacting normals, and the gaps to finitely many remaining facets give a relative neighborhood in that annihilator. Sign differences isolate every lifted factor span, and distinct lifts are orthogonal; the codimension is therefore the sum of the q_i. For paths, the pairwise squared-distance variance bound is saturated only by the signed centered ramps, since the two endpoints must achieve their full distance. These prove the arbitrary finite metric and grid claims without extrapolation.

## originality

PASS

The scalar radius is covered by Bobkov–Houdré's maximal-variance tensorization and standard polarity; the Boolean-cube and path contact calculations also overlap exactly in their domains. The supported distinct claim is the full contacting-normal product classification and the affine rank law for all optimal centers for arbitrary finite factor metrics, and hence grid contacts beyond Boolean cubes. None of the inspected comparisons supplies that equality-case and geometric classification throughout this domain. Establishing it requires recovering all additive optimizers and proving the antipodal tight-normal span and local sufficiency; multiplying the scalar variance or using a total facet count does not do that.

## value

PASS

This is a complete classification of the origin contacts and a structural rank law for the translation freedom of all largest balls, not a scalar variance estimate or a recomputation of face numbers. It applies to arbitrary finite metrics and explains why path-product grids can have many facets yet relatively few contacts and a large affine incenter locus. It does not claim a complete description of the boundary of that locus.

The dated certificate retains the supplied scientific assessment, sources and limitations.
