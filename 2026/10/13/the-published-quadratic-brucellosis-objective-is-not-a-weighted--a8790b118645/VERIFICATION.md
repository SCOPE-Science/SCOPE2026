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

The publisher PDF, pp. 552–553, explicitly calls Eq. (16) a weighted-sum transformation of the vector problem and confirms both transcriptions. A fixed weighted sum of the four integrals is the integral of the weighted sum of the original linear rates. Eq. (16) instead squares individual rates, separately within both J2 and J4. Even a single nonnegative cost stream can change order: integrals 1/2<3/5 give squared-rate integrals 1/2>9/25 in the frozen example. This is an unconstrained functional example, not an attainable trajectory claim. The printed state equations are affine in the three controls; differentiating the linear-cost Hamiltonian at fixed state and adjoint gives the three stated switching coefficients. Their nonzero signs select lower or upper endpoints by pointwise minimization over the box; a zero at a switching time alone does not establish a singular arc. For the quadratic cost the added derivative for each control is twice its coefficient times the control (e.g. 2ω3 B0² S² θ), so with positive control-cost coefficients the stationary roots, projected to the box, match all three formulas in Eq. (19), p. 555. Zero weight or zero state factor requires pointwise affine/degenerate minimization rather than division. The finding identifies the objective behind the displayed necessary conditions and, conditionally, the numerical setup; it does not establish global sufficiency of those conditions or verify the numerics. Figure 9's linear-loss caption describes an outcome measure, not evidence the linear sum was optimized. Supplied symbolic checker inspected, not executed; checks above are algebraic.

## originality

PASS

The general definition of weighted-sum scalarization, and the affine-versus-quadratic Hamiltonian distinction, are established and are not novel. The supported distinct claim is the source-level cost mismatch and attribution of the reported control equations to the changed objective in this particular article. Statement-level comparison found no distinct indexed finding or accessible paper identifying that mismatch there.

## value

PASS

A reproduction based on the stated linear objectives and one using the displayed quadratic objective optimize different criteria and use different pointwise control rules. Making that distinction is consequential for interpreting the weights and replicating the published calculation. The simple algebra is not offered as a new control theorem, and the conclusion does not require alleging that the reported trajectories are numerically wrong.

The dated certificate retains the supplied scientific assessment, sources and limitations.
