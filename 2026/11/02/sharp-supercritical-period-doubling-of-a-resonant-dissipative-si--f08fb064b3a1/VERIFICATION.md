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

The half-turn two-cycle is exact, and its return matrix has trace 1+λ²−t² and determinant λ². The strict Schur conditions give precisely 0<t<t_c and at equality the simple roots −1,−λ². For local uniqueness without assuming symmetry of an arbitrary candidate, use the odd return G=F² in a chart around the first phase. For any small G-two-cycle with points m±h its midpoint satisfies G(m+h)+G(m−h)−2m=0. The derivative in m at the critical origin is 2(DG−I), invertible; oddness gives m=0 as the unique local solution, so every such cycle satisfies G(p)=−p. The two one-step angular increments then force the displayed momenta and the two sine equations. Their Jacobian has complementary eigenvalue 2t_c and null vector w=(b,t_c+a). Eliminating the complementary coordinate and dividing the odd scalar equation by s reduces it to a smooth equation in s² with nonzero derivative −t_c k²(w_1^4+w_2^4)/6. Its root is s²=6μ/[k²(t_c²+a²)(t_c+a)]+O(μ²). The two signs correspond to one geometric prime four-cycle, and the negative side has no real nonzero root. In the trace of the two-step derivative at that branch, the change from the old cycle's trace is k²[t_c²(u²+v²)+a t_c(v²−u²)]/2+O(μ²)=6t_c μ+O(μ²); the net change from critical is 4t_c μ. The second two-step derivative is identical by oddness. Squaring the two eigenvalues gives 1−8t_c μ/(1−λ²)+O(μ²) and λ⁴+O(μ), both inside the unit disk for small μ>0. Independent scalar bisection and multiplication of four one-step Jacobians corroborated the amplitude and slope in nine cases.

## originality

PASS

The supported distinct content is the flip of the specified half-turn branch in the torqued dissipative standard map, including its local orbit equations, amplitude and multiplier slope. Generic flip theory is background, not an originality claim. No inspected theorem gives these coefficients for this branch.

## value

PASS

The exact resonant orbit is singled out by the half-turn drift and the sine zeros, rather than by an arbitrary numerical slice. Its stability boundary and the explicit supercritical branch give a local benchmark for the torqued dissipative standard map, including the dependence of the rate of attraction on damping. The full-space multiplier law and local uniqueness add more than merely identifying a generic flip.

The dated certificate retains the supplied scientific assessment, sources and limitations.
