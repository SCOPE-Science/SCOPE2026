---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

Source RESULT.md steps 1–5 explicitly construct all 3m+1 vertices in affine chart; give positive contact weights w and covariance with eigenvalues g=3w-8mw², B=3w, w; verify all orbit quadratic norms Q_axis=Q_pair=2m, Q_origin=2m for m<=4 and 8 for m>=4. For any competing ellipsoid, averaging contact inequalities gives trace(S^-1 C)<=1 and determinant AM-GM yields det S>=d^d det C with equality only at center c, S=dC; this is global uniqueness, not symmetry-only. Intrinsic metric multiplies constant modes by m+1 and has chart-volume Jacobian m+1. Independent exact symbolic checks of both branches and finite rational construction (source verification/check_pq_star.py) support algebra.

## originality

PASS

No prior located that mathematically covers the exact star PQ Löwner ellipsoid/contact transition. The balanced PQ all-contact result is a different family; classical John/Löwner covariance criterion is credited. Full relevant earlier PQ geometry paper studies normalized lattice volume not intrinsic metric. Best-of-knowledge rather than proof of absolute priority.

## value

PASS

Smallest complete bipartite star family inside a natural PQ graph-polytope construction; gives exact unique enclosing ellipsoid, intrinsic axes/volume and a sharp finite-to-infinite contact orbit threshold m=4. This benchmark has independent relevance to convex approximation and optimal design, not a generic algebraic substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
