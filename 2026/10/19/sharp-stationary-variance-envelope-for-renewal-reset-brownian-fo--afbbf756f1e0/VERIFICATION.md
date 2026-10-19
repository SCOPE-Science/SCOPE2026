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
# Reproducibility and limits

Run `python verify.py` with Python 3 and no third-party dependencies. The program uses a fixed pseudorandom seed and performs 310 algebraic, quadrature, and inequality assertions on families of two-point renewal laws, including strict endpoint approximations. It cross-compares the renewal-force covariance convolution with the exact moment–Laplace identity, tests the exponential renewal reduction, and compares a uniformly phase-sampled deterministic cycle with independently integrated within-cycle moments derived from the known reset-epoch result.

The proof in `RESULT.md` establishes the assertions for all admissible waiting-time laws and parameters; finite program checks do not certify universal quantifiers, priority, or an external audit. The displayed open endpoints are nonattainable for any positive nonconstant waiting-time law with exactly fixed first and second moments. Full stationary probability laws, dependence under non-iid intervals, waiting laws without finite second moment, and finite-time relaxation are not analyzed here.
