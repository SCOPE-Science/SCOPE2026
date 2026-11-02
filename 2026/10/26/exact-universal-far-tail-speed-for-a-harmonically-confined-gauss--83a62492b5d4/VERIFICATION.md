---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

The stationary Poisson stochastic convolution has an all-real mgf: Dt²/(2k)+r/(2k)*integral_0^(sigma² t²/2)(e^v-1)dv/v. Choosing t=sqrt(2)(1-epsilon)sqrt(log x)/sigma makes mgf subleading relative to t*x, giving Chernoff liminf >=sqrt(2)/sigma. A burst of about (1+epsilon)x/(sigma sqrt(2log x)) kicks during last 1/log x, with each Gaussian mark near sigma sqrt(2 log x), costs n*(2 log x+o(log x)); independent older bath is nonnegative with probability at least half. This gives matching limsup and symmetry handles other tails. Independently confirmed exact second and fourth stationary cumulant coefficients and sampled large-log event costs; finite diagnostics do not establish limit.

## originality

PASS

Di Bello et al. 2023 derive the exact Gaussian shot-noise bath stationary law, Fourier transform and moments, but the examined model paper does not give the sharp log tail x sqrt(log x) coefficient. Gilbert–Pollak 1960 gives general shot-noise distribution/transform equations including exponential kernels, a serious potential implicit-coverage source; their inspected examples do not state the Gaussian mark coefficient. A general transform-to-tail Tauberian or large-deviation theorem could imply this by combining past results, a remaining mathematical priority risk.

## value

PASS

The exact coefficient and independence from confinement, kick rate and thermal diffusivity determine the far rare-event scale for an established non-Gaussian active-bath model. This is a quantitative sharp asymptotic not explained by the prior low-order moments or qualitative leptokurtosis.

The dated certificate retains the supplied scientific assessment, sources and limitations.
