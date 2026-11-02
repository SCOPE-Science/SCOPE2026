---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

RESULT.md blob 9431142f3bc3d5091e18597a8642e00a44655e44: a coherent orientation of the 2^d sign-choice facets gives the exact full-dimensional signed volume d!vol(P)=|det C| for C=[p_i^+-p_i^-], independent of central symmetry or origin position. Expanding 2d squared vertex deviations yields D=4d-2 max_R tr(R^T C)=4d-2 sum_i s_i by orthogonal Procrustes. Applying AM-GM to the positive singular values produces the sharp global envelope and equal-singular-value characterization. To prove actual polytope realizability, p_i^±=±r e_i+t e_{i+1} with t=sqrt(1-r²), 2t<r; every sign-choice facet is strictly exposed by the unique solution of u_i=1-(t/r) eps_{i+1}u_{i+1}, and each opposite point lies strictly inside the supporting halfspace; positive barycentric weights place origin inside. Thus equality continuum r in (2/sqrt5,1], D=4d(1-r), yields the exact local coefficient 2^d/(4d!). Independent exact rational verification checked all supporting sign facets for d=2..5 and r=12/13,t=5/13, including cyclic d=2; does not substitute for uniform contraction proof.

## originality

PASS

Best-knowledge statement-level novelty survives comparison with relevant primary literature and published records, with the exact theorem and aliases checked. This gives an explicit global distance-conditioned and dimension-uniform stability envelope for the classical regular cross-polytope volume maximizer, classifies equality, and verifies a positive interval of genuinely achievable sharp deficits by noncentrally symmetric inscribed configurations. Priority residuals are explicitly retained; a failed search is not a novelty certificate.

## value

PASS

This gives an explicit global distance-conditioned and dimension-uniform stability envelope for the classical regular cross-polytope volume maximizer, classifies equality, and verifies a positive interval of genuinely achievable sharp deficits by noncentrally symmetric inscribed configurations. While determinant/Procrustes/AM-GM themselves are standard, the geometric parameterized attainability and exact optimal local coefficient address a natural shape-stability invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
