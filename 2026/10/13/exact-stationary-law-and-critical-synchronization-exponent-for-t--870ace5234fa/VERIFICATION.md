---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

Conditioned on K held coupons, predeletion size grows by Bernoulli((n-K)/n), then binomial thinning with q. Factorial moment recursion m_r[1-(1-r/n)q^r]=(r(n-r+1)/n)q^r m_{r-1} solves the product, and exchangeability yields every inclusion probability and full law. Pair covariance algebra is strictly negative. For q_n=1-c/n, Stirling and improper Riemann sum with bounds j/n<=d_nj<=(1+c)j/n yield I(c); differentiating I(c)-log(1+c) and bounding its integrand proves strict positivity for all c>0, not just numerics. Independent rational full stationary transition kernels for n=2..5 and q=1/3,1/2,3/4 confirmed every inclusion probability and pair covariance.

## originality

PASS

The source same process supplies one-coupon recurrence and critical scaling; Long gives standard stationary entry flux but its large-n theorem holds fixed p. Neither implies n-dependent p=c/n large-deviation exponent or full stationary multi-coupon joint moments. Clumsy collector changes only drawn coupon and is not equivalent. Relevant classical immigration-thinning prior remains an admitted risk.

## value

PASS

A complete stationary dependence structure and strict exponential correction to false independence heuristic for a natural stochastic collector; directly needed for full synchronization rarity and rare event estimates.

The dated certificate retains the supplied scientific assessment, sources and limitations.
