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

# Reproducibility and verification limits

The analytic proof in `RESULT.md` constructs the stationary process, derives the covariance ODE and its coefficients, proves positivity through a positive-convolution decomposition, proves infinitely many negative bands through a nonzero oscillatory spectral component, and bounds the first negative lag to one mechanical period beyond the envelope threshold.

The exact witness uses \(\beta=1/2\), \(\omega_0=1\), \(q=1\), \(a=1\) and lag \(t=2\pi/\sqrt3\); the resulting difference of exponentials is strictly negative. This is an exact sign argument, not a floating-point certificate.

Execute `python3 checker.py` using Python 3 and only its standard library. The checker separately integrates the three-variable second-moment evolution by fourth-order Runge–Kutta, compares it with the explicit stationary autocovariance over many parameters and lags, tests the critical amplitude and sampled sign regimes, and checks near-boundary envelope scaling. The current package reports 2015 passed finite diagnostics. These finite calculations do not establish the universal assertions; the proof does.

No formal proof assistant, independent audit, laboratory measurement, or literature-priority certificate has been supplied. In particular, the claim does not extend to additive thermal white noise, nonlinear trapping, non-exponential propulsion correlations, or nonstationary initial conditions.
