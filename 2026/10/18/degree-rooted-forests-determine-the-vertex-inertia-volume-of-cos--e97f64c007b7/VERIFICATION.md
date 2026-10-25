---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

Verified the canonical 3m cosmological polytope vertices x_u+x_v-y_e, x_u-x_v+y_e, -x_u+x_v+y_e in R^(n+m), equal vertex masses and all coordinate sums=1. Summing exact outer products gives block moment M=[[3D-A,-B],[-B^T,3I]] with unsigned incidence BB^T=D+A. Schur complement gives det M=3^m(4/3)^n det(2D-A). Since h=1 and h^T M h=3m, rank-one centering identity det*Sigma=(n+m)det M/(3m)^(n+m) yields (n+m)/m^(n+m)(4/9)^n det(2D-A); 2D-A is SPD for connected nontrivial graph. Cauchy–Binet expansion of [oriented incidence | diag(sqrt degree)] yields acyclic edge sets and one degree-weighted root per component. Exact star Schur-complement det=3(n-1)2^(n-2), path tridiagonal recurrence q_n=4q_(n-1)-q_(n-2), eigenroots 2±sqrt3, exponential pseudodeterminant separation and half-rate ellipsoid volume ratio. Independently computed path det n2..8 (3,12,45,168,627,2340,8733) and inspected exact integer-principal-minor and forest enumeration in CHECKER.py, including given six-vertex degree twins 492 and 483. The known tree normalized-volume equality is credited, not proven new.

## originality

PASS

Published cosmological polytope papers establish canonical vertex coordinates, faces, volume and triangulations. The particular invariant is the centered covariance of uniform vertex measure and its graph-rooted-forest pseudodeterminant, not the polytope Euclidean volume or circumradius. The Resultary SCOPE closest cosmological result gives a graph-independent outer enclosing sphere, which does not imply equal-vertex covariance at vertex barycenter. Matrix-forest theorem is general established machinery, while this graph-polytope covariance specialization and asymptotic path/star separation are not located as prior direct claims.

## value

PASS

The canonical equal-vertex-weight inertia ellipsoid is a natural Euclidean shape invariant of cosmological polytopes. The graph forest determinant identity gives a tractable combinatorial formula, and the exponential path/star separation despite identical tree-polytope volumes and vertex sphere is a motivated structural distinction. Degree-sequence twin trees further show nontrivial dependence on adjacency rather than only degrees; not an arbitrary isolated computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
