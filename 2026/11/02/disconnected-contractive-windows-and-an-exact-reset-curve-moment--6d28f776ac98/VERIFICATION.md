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

# Reproduction

Use Python 3.9 or later with standard-library support. Run `python verify.py` in the directory containing this document. The expected terminal line begins `VERIFY_OK assertions= 15397`. It checks independent symbolic/numeric consequences of the stated formulas and uses a deterministic random seed for its Monte Carlo diagnostic. It requires no downloaded datasets, compiler, specialist library, or external service.

## What was checked

The verifier checks phase intervals at several sampled curvature ratios, exact reset coefficients \(0,-8\), exact rational run-length conditional variances for thirty-five values of \(K\), transformed recurrence equality for 10,000 independent draws, closed stationary variance at the finite-moment settings, and 180,000 sequential draws (with a burn-in) against that variance. The expected variance is about \(1.19047619\) at \(\lambda=1,q=0.8,h=0.4\). A diagnostic sample produced approximately \(1.19052220\).

## What was proved, rather than numerically checked

The complete open-interval contractivity classification, existence and uniqueness of the contractive stationary law, strict second-moment threshold, and the all-real-exponents moment dichotomy follow from the displayed analytic proof in RESULT.md. Finite grids cannot prove interval completeness; finite Monte Carlo cannot establish infinite-variance or heavy-tail claims. The tests do not assess sampling quality outside the scalar model. No independent audit or external certification was performed.
