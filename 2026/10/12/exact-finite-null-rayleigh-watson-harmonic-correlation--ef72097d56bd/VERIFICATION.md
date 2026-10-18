---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Independently reconstructed the four-frequency moment sum over sample indices: E|sum exp(ikTheta)|^4=2n^2-n, and for distinct positive k,l, E[A_k A_l]=n^2, even when one frequency is a multiple of the other. Uniformity eliminates every nonzero net frequency. Parseval for the mean-centered circular empirical process gives U_n^2=(2*pi^2)^-1 sum_{k>=1} Z_{n,k}/k^2. Square summability ensures L2 convergence; zeta(2), zeta(4) yield E U_n^2=1/12, Var U_n^2=(n-1)/(360n), and the exact cross-correlation. This proves finite uncorrelatedness, NOT independence.

## originality

PASS

Best-of-knowledge finite-sample refinement. Full-text modern Sobolev tests give Fourier weights, Rayleigh/Watson specializations and asymptotic harmonic independence but do not state the all-n squared-harmonic covariance and 3*sqrt(10)/pi^2 correlation. Exact-formula/alias and published-result searches yielded no equivalent claim. Older Watson primary full text is a concrete priority risk.

## value

PASS

The all-n exact null redundancy of two standard and complementary circular goodness-of-fit tests is a useful natural second-moment invariant: Corr squared is 90/pi^4, about 0.924; the decomposition also gives precisely the residual higher-harmonic null variance. Not merely a renaming of the Watson Fourier definition.

The dated certificate retains the supplied scientific assessment, sources and limitations.
