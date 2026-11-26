---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

On z=(u,v,v,v,v) the weighted matrix gives the displayed two rows exactly. The largest eigenvalue of the full positive definite edge Gram matrix is (5+√17)/2 (the complementary eigenvalues to the two-coordinate restriction are 3,1,1). The derivative of the full lift is similar to I+h K_*^{1/2} diag(α,1,1,1,1) diag(cos z) K_*^{1/2}; the stipulated strict bound keeps it invertible for α near one. The torus map is homotopic to the identity and hence its local diffeomorphism has degree one. In w=u−v−π coordinates the exact update is w⁺=w+h[sin v−α sin(v+w)]. At α=1 the map on w=0 is v⁺=v+2h sin v, increasing on [0,π], with tangent multipliers 1+2h and 1−2h and normal multipliers 1−h and 1+h at the two endpoints, respectively. The local manifolds are smooth graphs over v; near each persistent endpoint the parameter derivative of the graph vanishes at the endpoint, and the derivative in v at α=1 is zero. This justifies the decaying boundary condition on the derivative along the moving perturbed half-orbit. Moving v makes no term in the normal derivative. Iterating W_{j+1}=a_jW_j−h sin(v_j) from the past gives a negative unstable contribution and solving backward from the future gives a positive stable contribution; the endpoint multipliers yield geometric tails. Smooth continuation to a transverse section gives a quadratic Taylor remainder with the indicated sign and order of subtraction.

## originality

PASS

The unit-weight connection on this exact tree and its scalar dynamics are known. The supported distinct claim is the signed nonvanishing derivative under central-edge-only detuning, at each fixed interior section. Neither the unit-weight result, the inspected weighted criteria, nor the nearby catalogue results supply that derivative or its sign.

## value

PASS

This is a motivated perturbation of a known nontransverse obstruction, not another example of the same exact arc. A single physical edge-weight change has an explicitly oriented nonzero effect without assuming small step size beyond the original invertibility range. The two-sided series explains why cancellation cannot occur and supplies an actionable prediction at a chosen section.

The dated certificate retains the supplied scientific assessment, sources and limitations.
