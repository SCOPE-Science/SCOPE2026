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

Every rank-at-most-d correlation matrix is represented by unit normals in \(\mathbb R^d\), and for fixed normals the event at threshold \(t\) is the dilation \(tK\). Gaussian density convergence at the origin gives the fixed-configuration asymptotic. The nontrivial uniform lower bound is handled by truncating \(K\) in a ball: compactness of the normal configuration space and boundary-null continuity give minima \(a_R\), and monotone exhaustion forces \(a_R\uparrow V_{d,n}\); otherwise a convergent sequence of minimizers would produce a limiting polyhedron of full volume below \(V_{d,n}\). This controls even \(t\)-dependent near-minimizers. In three dimensions with five facets, the minimum-volume unit-inradius circumscribed polyhedron is the right equilateral triangular prism; its cross-section has side \(2\sqrt3\), area \(3\sqrt3\), and height two, hence volume \(6\sqrt3\).

## originality

PASS

Mulgund's current primary paper explicitly poses the fixed-threshold rank-constrained problem for \(d\ge3,n\ge d+2\) and states that outside a few special cases the optimal configurations are unknown. The triangular-prism tangent-volume fact itself is classical, so it is not counted as new. The surviving contribution is the general small-threshold reduction, including the uniformity over varying covariance configurations, and its consequence that the first open \((d,n)=(3,5)\) case has a rigorous leading constant.

## value

PASS

The theorem gives a structural reduction of a current Gaussian extremal problem to a natural Euclidean tangent-polyhedron invariant. It also resolves the leading-order behavior of the first three-dimensional five-direction case left open at fixed threshold, with an exact constant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
