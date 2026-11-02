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

# Verification protocol

Run \`python verify.py\` with the packages specified in \`requirements.txt\`. The program evaluates three stationary moments in two independent ways: (i) generator equations in closed form, (ii) numerical integration of finite-age conditional Brownian moments with respect to the exact exponential reset-age distribution. It also checks covariance positive semidefiniteness, complex conjugation under chirality reversal, the explicit eigenvalue gap and cancellation at \(r=2D_r\). The provided version reports 84 checks passed across twelve distinct rate/noise regimes.

The mathematical proof in \`RESULT.md\`, not numerical quadrature, supplies the infinite-parameter statements. The verification does not establish full-density isotropy, statistical estimation properties, physical realization of ideal instantaneous resets or independent literature priority.
