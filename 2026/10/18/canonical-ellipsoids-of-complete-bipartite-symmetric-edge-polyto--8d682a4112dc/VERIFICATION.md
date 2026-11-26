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

For the standard metric on the zero-sum space H, the tight edge roots span H exactly when their graph is connected. Feasibility forces each positive tight edge to run from a maximum in the first part to a minimum in the second part; negative tight edges run between the opposite extremes. If both parts vary, these graphs have disjoint vertex sets, so a polar vertex must have a constant part. Conversely the listed centered sign normals have every edge tight. The two lists intersect only at the two constant-part contrast normals. Thus all primal facets have support 1 for the candidate shape L/(ab). For the inner optimality certificate, the projected balanced signs have trace a−u_a²/a on the first zero-sum block (respectively b−u_b²/b on the second), and contrast variance bu_a²/(aN) (respectively au_b²/(bN)); permutation invariance eliminates cross terms. Substitution gives the three eigenvalues of the mixed covariance as a/d, b/d and ab/(Nd), with positive weights summing to one even in the smallest and odd-size cases. The whitened polar contacts are isotropic, giving polar Löwner optimality and hence primal John optimality. Each edge root is exposed (all have the same Euclidean norm), the uniform signed roots have covariance L/(ab), and transitivity plus the trace identity makes every whitened outer norm one. Their isotropy proves outer optimality. Symmetry and uniqueness place the centers at zero. The eigenvalues give the stated radii, determinant N/(a^a b^b) and volume ratio d^(d/2).

## originality

PASS

The full two-parameter John shape and positive polar contact certificate, simultaneous exact homothety, and all-facet contact survive the checked comparisons. Neither the published facet rule, the general ellipsoid criterion, the standard symmetric containment bound, nor the indexed same-body results supply the complete claim. The outer shape on its own follows from symmetry and the general contact criterion, and the indexed cactus result already gives the exceptional cube case. This is a bounded statement-level priority assessment, not a priority guarantee.

## value

PASS

An exact intrinsic inscribed ellipsoid for a natural two-parameter graph-polytope family is useful beyond counting its facets. The explicit balanced-sign contact measure exposes why both canonical ellipsoids have the same shape up to scale and why both contact sets are exhaustive, including for dense noncactus graphs. This is not just the known cube case or a re-expression of the standard outer symmetry calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
