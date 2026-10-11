---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The exponential-spacing proof is sound. The spacings are independent with \(D_k\sim\mathrm{Exp}((n-k+1)\lambda)\); therefore the minimum \(D_1\) is independent of all later spacings, while both range and translation-invariant sample variance depend only on those later spacings, proving joint independence. Writing the later spacings as independent coordinates \(Z_i\) gives \(S^2=Z^\top A Z\) with \(A_{ij}=\min(i,j)(n-\max(i,j))/(n(n-1))\). For independent coordinates, centered expansion yields \(\operatorname{Cov}(\sum Z_i,Z^\top AZ)=2\sum_i v_i(A\mu)_i+\sum_iA_{ii}\tau_i\). Substituting exponential moments reduces the sum to \(2((n-1)\lambda^3)^{-1}\sum_{1\le r\le k\le n-1}(rk)^{-1}\), hence the stated \((H_{n-1}^2+H_{n-1}^{(2)})/((n-1)\lambda^3)\). Independent exact-rational reconstruction for \(2\le n\le20\) reproduced the unsimplified quadratic-form covariance and closed harmonic formula. Combining the standard range variance and unbiased-sample-variance variance yields the stated correlation and its asymptotic.

## originality

PASS

The primary spacing paper confirms the independent-exponential representation underlying the proof but does not study range jointly with sample variance. Lam's highly plausible 1980 source was first sought through open web routes; only its abstract was available there, so the authorized institutional copy was then read in full. It derives exact marginal sample-variance densities for \(n=2,3,4\), discusses moments, and does not present a range--variance covariance or joint law. Royen's gamma-sample work concerns the marginal sample-variance distribution. Fresh Resultary and web searches for range/sample-variance covariance, correlation, harmonic numbers and exponential sampling returned no equivalent formula. The audited covariance is thus a new joint-statistic calculation to best current knowledge.

## value

PASS

Range and sample variance are standard dispersion statistics, and the exponential law is the canonical memoryless lifetime model. The exact positive covariance, closed correlation, and vanishing \((\log n)^2/\sqrt n\) correlation scale give a clean joint-statistic description not supplied by the known marginal laws. The minimum's joint independence from the pair is a useful structural companion fact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
