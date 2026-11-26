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

In normalized variables with s=u+v−1, the two-step linearization at ε=0 on the neutral segment is [[1,−u],[0,uv]], v=1−u. To check forcing, write D_1=v²+3u² and D_2=u²+3v². The first updated coordinate is u−εD_1 at s=0 to first order. The second is v+ε(vD_1−D_2), because the intermediate coordinate changes the second denominator. Thus the ε forcing in (u,s) is (−D_1,−uD_1−D_2). The left eigenvector normalized on the tangent is (1,−u/(1−uv)); its projected forcing is (uD_2−vD_1)/(1−uv)=(u−v)^3/(1−uv). At u=3/4 this is 2/13, whereas the uncorrected first component is −7/4. On a slightly larger compact interior segment, the transverse recurrence keeps s=O(ε); subtracting εH_s/(1−uv) leaves a residual bounded by C(εq^j+ε²), q<1, using O(ε) changes of u. Its absolute sum up to T/ε is O(ε), so perturbed Euler and an interior stopping argument give uniform convergence, also for the v coordinate. This includes u_0=1/2 as the constant limiting solution. On either strict outward branch, dD/dt=8D³/(3+D²), and direct integration gives the stated clock. Strict outward motion and uniform convergence on both sides of the threshold exclude earlier crossings and ensure crossing soon after the limiting time. Since u_j=y_{2j−1}, the original iteration count is 2J_ε up to O(1). The frozen script and notes were inspected, not executed; the analytic estimates, not finite residuals, establish the limit.

## originality

PASS

The same recurrence and critical surface, its nonhyperbolic multipliers, boundary-cycle attractors and basin separation are established in earlier work. Supported distinct content is the projected slow vector field along the entire fixed-interior limiting neutral line and the exact first-crossing constant on the a/b scale. No claim of novelty is made for the competitive-map setting, invariant-curve techniques or critical multiplier. The closest distinct indexed slow-selection problem has a different map and perturbation.

## value

PASS

The critical surface of this known rational recurrence ends at a full neutral family of two-cycles. Knowing the ultimate attractors does not explain how long small a/b orbits retain a phase. The quantitative selection law gives a nontrivial signed cubic after eliminating a transverse displacement of the same order; the explicit two-sided threshold clock measures that effect for an entire range of initial states rather than just the equilibrium.

The dated certificate retains the supplied scientific assessment, sources and limitations.
