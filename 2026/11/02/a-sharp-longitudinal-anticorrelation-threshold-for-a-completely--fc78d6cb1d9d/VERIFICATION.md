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

For simultaneous Poisson resets to (0,0,0), a stationary law exists by exponential-age regeneration and is unique by coupling at a common reset. If a reset intervenes during the lag, the future coordinate is independent of the centered initial coordinate conditional on the future reset times, so only the no-reset event contributes. Free angular conditional means decay at rate a, and the trapped coordinate convolves that decay with rate k. Multiplication by no-reset survival exp(-rh) gives the two exponentials and their resonant limit. The stationary moment equations, including the reset terms, give the asserted V_x,V_y,H,G and J; translational Brownian noise gives strictly positive variance. Dividing by exp(-(r+k)h) gives V_x+vJ times the convolution factor in the sense of V_x+vJ f(h), where f increases strictly from zero to infinity for k>=a, or to the unattained bound 1/(a-k) for k<a. Thus equality at the weak-trap threshold produces no finite zero. The sign of J is minus the sign of P; P has one positive critical point and one simple positive root past it, and at k=a it factors as (r+2a)(r^2-3ar-a^2). The root gives the onset only for k>=a, with the stated logarithmic or reciprocal divergence of the crossing lag. The transverse bracket is strictly positive. In the weak trap the slow coefficient has positive thermal term 2D/(2k+r) and active leading term -v^2 k/((a-k)r^2). Independent rational evaluation with k=1/2, a=v=1, D=1/200 gives the slow coefficient 101/360, -15457/11157300 and 11218439/1076844213900 at r=1,10,100, respectively, with the single finite crossing at r=10 near 3.592591005228. Replay by substituting those rational parameters in the moment equations of RESULT.md lines 73–84 and forming V_x+2J. This exact example corroborates but does not replace the proof. VERIFICATION.md and check.py were inspected; the uploaded script was not executed.

## originality

PASS

The supported distinct contribution is the connected longitudinal two-time sign classification for complete reset, including the single-zero criterion, the rate threshold and the example of thermal reentrance. The transverse covariance formula, including at resonance, is already covered by a distinct indexed finding and receives no originality credit; one-time variance receives no such credit either. None of the inspected matches supplies or automatically specializes to the longitudinal boundary.

## value

PASS

The result determines when a fixed-heading regenerative process has a negative connected position correlation even though its transverse covariance stays positive. The unique crossing, the different onset divergences at and away from resonance, and exact evidence that thermal noise restores positivity at high reset rates resolve distinct dynamical regimes, not just individual moment calculations. This is an expectation-level classification; it does not guarantee experimental detectability or a unique reentrant interval for all weak traps.

The dated certificate retains the supplied scientific assessment, sources and limitations.
