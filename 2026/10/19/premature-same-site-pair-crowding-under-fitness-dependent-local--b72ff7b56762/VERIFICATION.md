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

Run `python checks/checker.py` using the versions specified in `requirements.txt` (or compatible versions). The self-contained checker solves three finite one-site generator equations by linear algebra, integrates the exact continuum stationary mean and pair formulas for four representative reset exponents, and tests the beta-integral amplitude. Its completed execution reported **32 passing numerical consistency assertions**.

For the independent finite-state checks, generator truncation to occupation counts at most 240 was used. The continuum quadratures used mpmath 40-digit precision; the critical approach is slow near the logarithmic exponent. The checker intentionally tolerates finite-cutoff and finite-distance errors and does not assert an infinite-size numerical proof.

The mathematically decisive verification is the generator proof of the two factorial moments; the explicit normalized integral in the stationary mean-field limit; boundedness of the established first-moment closure; and the three regular-variation cases near maximal fitness, with a convergent Euler beta integral for the strict supercritical case. The limiting order and the distinction between within-site pairs and total-particle fluctuations are essential. No independent audit or external validation has been performed.
