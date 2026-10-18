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

# Verification record
The reproducible standalone `check.py` uses integer Laurent-polynomial convolution, without floating-point approximation, to obtain exact Fourier constant terms of \(\prod_{j<n}X(D^j\theta)\) and \(\prod_{j<n}X(D^j\theta)^2\) for \(1\le n\le9\). It compares these to the exact recurrence \(u_{n+2}=2u_{n+1}+16u_n\), \(u_0=1,u_1=6\), and first moments \(2^n\). Nine rational-covariance coefficient identities are checked as well.

Run: `python3 check.py`. Actual result: `PASS: 9 exact Fourier-constant-term first/second moment cases and 9 log-covariance identities`.

An additional independent high-resolution trigonometric grid integration for \(1\le n\le8\) matched the integer ordinary and second moments to the displayed numerical precision. Neither the finite verification nor the quadrature proves the general moment recurrence or the central limit theorem; those require the analytic transfer calculation and Kac/reverse-martingale reasoning in `RESULT.md`.

No independently performed scientific audit is claimed.
