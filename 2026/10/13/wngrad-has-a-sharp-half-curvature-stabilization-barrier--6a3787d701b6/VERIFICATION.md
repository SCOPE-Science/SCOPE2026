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

For r_k>0 the objective ratio is (1-1/z_k)^2, so the exact sign boundary is z_k=1/2. The additive accumulator increments are respectively r_k^2/z_k and r_{k+1}^2/z_k. Both are nonnegative; prior to the first entry into z≥1/2 with r_0>0, the radius grows and each increment exceeds 2r_0^2. This yields the stated ceiling bound and rules out later increases. For z≥1, r_k^2-r_{k+1}^2 is at least the scale increment in both conventions: for pre-step the ratio, when defined, is 2-1/z ≥1; for post-step it is z(2z-1)/(z-1)^2 ≥1 at z>1, and at z=1 the next radius is zero. Thus the scale is bounded by telescoping from first entry into z≥1, or by 1 if there is no such entry. The increments go to zero and 0<z_0≤z_k≤z_infinity forces the radii to zero. A nonterminating trajectory at z=1/2 makes a strictly positive next scale increment, so its limiting scale is strictly above the boundary and its limiting radius ratio is the stated number in [0,1). The zero-radius initialization already terminates and is not subject to the finite-escape bound. The proof handles both exact-arithmetic recurrences, including the equality cases; verify.py was inspected, not executed.

## originality

PASS

The one-step boundary is the classical quadratic constant-stepsize condition, and is not credited as new by itself. The supported distinct result is the quantitative finite unstable prefix for WNGrad, from arbitrary positive initial scales, together with scale control and the resulting contraction for both source conventions. The strongest related scalar transient theorem found uses AdaGrad-Norm, not either WNGrad map.

## value

PASS

The relevant question for learning a stepsize from gradient norms is whether an arbitrarily aggressive starting scale can cause recurrent instability. On the basic quadratic this result proves that all objective increases occur in a single finite prefix with an explicit bound, and that the eventual scale and contraction are controlled in both versions of the algorithm. This explains a transient behavior not settled by the classical one-step boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
