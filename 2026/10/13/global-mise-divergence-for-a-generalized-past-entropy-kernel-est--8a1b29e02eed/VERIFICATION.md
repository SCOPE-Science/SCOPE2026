---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

PASS: For Exp(1), beta=1/2 the true past entropy tends to log4. For every fixed sample of Gaussian kernels, both A_n=int_0^infty f_n and B_n=int_0^infty sqrt(f_n) are finite positive, and estimated entropy converges to L_n=2log B_n-log A_n. On equal-location samples at c, A_n=Phi(c/b_n), B_n=b_n^(1/2)*2^(3/4)*pi^(1/4)*Phi(c/(sqrt2*b_n)), so L_n(c)->log sqrt(8*pi/n) as c->infty, never log4 for any integer n (equality demands n=pi/2). Local dominated convergence yields a positive-probability open neighborhood of samples with nonzero limiting error. On it the nonnegative global squared-error Lebesgue integral diverges, hence its expected value is infinite for EACH n. This is an analytic infinite-tail argument, not a finite simulation. Independently verified Gaussian normalization and exceptional integer n arithmetic.

## originality

PASS

PASS best-of-knowledge: exposes a theorem-3.3 global MISE failure for the exact published generalized-past-entropy estimator. The prior source states the false convergence, not this positive-probability Gaussian-tail counterexample; no exact earlier correction surfaced in the inspected sources.

## value

PASS

PASS: Corrects a concrete published global-integrated risk theorem at a genuine domain boundary; nondecaying Gaussian mixture tails cause infinite expected integrated loss for every sample size, a substantive mathematical obstruction to an advertised asymptotic assertion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
