---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For centered equal-variance Gaussian eps_j, Var(eps2-2eps1+eps0)=0 forces eps1=(eps0+eps2)/2 and equal variances then all three common, with nonzero deterministic denominator. Otherwise D has smooth positive density at zero. Conditional Gaussian second moment E[X^2|D=0]=s^2+(mX-c*mD/vD)^2 cannot vanish: if it did, X=(mX/mD)D almost surely, implying eps2=(1+r)eps1-r eps0; equal variances force Cov(eps0,eps1)=sigma^2, hence common noise, contradiction. Gaussian conditional integrability yields t-tail f_D(0) E[X^2|D=0] symmetrically for X^2/D, while Gaussian Z0 is light-tailed. Exact tail integration proves the p<1 threshold and 4K capped loss; covariance calculation yields the equicorrelation coefficient. Independent 300 PSD Gaussian covariance designs gave positive K; continuous-law proof does not rely on numerical sampling.

## originality

PASS

PASS with explicit generic ratio-tail predecessor credit: noisy ratios and near-zero denominators are known to generate inverse-linear tails, and regularized nonlinear acceleration has prior stability theory. What survives is the all-equal-marginal, even singular arbitrary-covariance necessity-and-sufficiency result for pole cancellation, exact positive coefficient and equicorrelation boundary. Broader unregularized correlated-Aitken literature remains a priority risk.

## value

PASS

PASS: this sharp classification identifies when a widely used nonlinear extrapolator ceases to possess even a first moment, including exactly which noise covariance geometry avoids it; quantitative tail and capped-risk laws are useful for robust extrapolation design.

The dated certificate retains the supplied scientific assessment, sources and limitations.
