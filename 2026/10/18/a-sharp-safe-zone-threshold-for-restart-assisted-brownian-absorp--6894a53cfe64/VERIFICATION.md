---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification of the Brownian conditional-reset threshold

The calculation uses the standard Brownian generator \(\tfrac12\partial_x^2\), with absorbing endpoints \(\pm L\) and rate-\(r\) alarms. All formulas are derived directly in `RESULT.md` from the Green function and an exact renewal equation. No sampling or finite-dimensional approximation is used as an infinite proof.

An independent discretization of the backward expectation problem solves
\[
-\tfrac12u''(x)+ru(x)-r\mathbf1_{\{|x|<a\}}u(0)=1,
\qquad u(-L)=u(L)=0.
\]
The submitted `verify_threshold.py` discretizes this equation, including its nonlocal reset term, using a sparse 801-point centered finite-difference system. It cross-checks the exact center mean for three cutoff values and four alarm rates, samples the non-improvement inequality on and below the critical geometric parameter, checks the existence of improvement above it, and tests the near-critical optimal-rate and gain coefficients at three small positive excess values.

Execution: `python verify_threshold.py`. Observed result: `PASS 157 independent checks; max finite-difference relative error=0.00154554`. Differences stem from finite spatial mesh resolution, particularly at the state-dependent alarm threshold. The finite tests neither establish all-rate optimality nor replace the coefficient inequality or implicit-function argument. No external or independent audit has been carried out.

The rigorous verification boundaries are the exact physical assumptions in `RESULT.md`; drifted motions, spatially asymmetric cutoffs, non-Poisson clocks, and finite reset traversal times are unproved. A neighboring publication was compared at abstract level because its complete text was inaccessible; this limits priority confidence, not the self-contained mathematical derivation.
