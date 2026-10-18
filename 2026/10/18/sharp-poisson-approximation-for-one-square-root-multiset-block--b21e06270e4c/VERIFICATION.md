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

# Mathematical verification

`verification/check.py` is a self-contained Python 3 standard-library checker. Run `python verification/check.py` from the package root. It constructs exact rational distributions through all mixed factorial moments, compares small instances with brute-force uniform multiset arrangements, and checks normalization, nonnegativity, the exact expectation, and the independently derived second factorial cumulant. For successively larger square sizes it reports the product of sample-size square root and total variation from the exact-mean Poisson law, for comparison with \(5e^{-2}/3\).

The infinite signed expansion follows from an analytic proof: the exact factorial transform (4), the uniform ratio expansion (7) with a degree-four error, factorial domination outside low indices, and the complex Cauchy coefficient bound. These steps, including high-index control, are essential; finite enumeration and printed values are not an infinite certificate.

Poisson tails beyond the support of \(W_n\) are included in numerical total-variation calculations. No numerical equality is claimed for finite \(n\); the displayed constant is asymptotic. The matching Poisson mean is \(\lambda_n\), not the limiting mean two.
