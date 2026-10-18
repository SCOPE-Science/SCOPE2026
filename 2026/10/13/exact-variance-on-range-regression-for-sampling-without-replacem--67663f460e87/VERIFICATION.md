---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Conditioning on both extreme observations, the k=n-2 internal draws are a uniform k-subset of {1,...,r-1}, independent of location a and ambient population M. Their exact first and second power sums and finite-population variance yield E T=nr/2, E T^2=n^2r^2/4+(n-2)r(r-n+1)/12 and E Q=r^2+(n-2)r(2r-1)/6. E[(Q-T^2/n)/(n-1)] is exactly r(n+1)((n+2)r-(n-2))/(12n(n-1)) for all n-1<=r<=M, 2<=n<=M+1; n=2 reduces r^2/2 and the full-interior-sampling boundary remains valid. An arithmetic progression multiplies by its lattice spacing squared. Independent rational exhaustive range strata over all populations M=2..13 confirmed 454 strata from 32,646 subsets; not used as an infinite proof.

## originality

PASS

Best-of-knowledge exact finite-sample conditional unbiased-variance regression on a uniform consecutive lattice; the continuous uniform conditional range regression and general finite-population order-statistic bounds do not immediately imply its nonzero finite-lattice correction. The highly relevant 2003 general sample-range paper could not be read in full, so priority uncertainty remains. No false uniqueness claim.

## value

PASS

Conditioning on a realized sample range is a canonical statistical dependence problem. The exact M-independent quadratic-plus-linear regression with a strictly lattice-specific correction quantifies a nontrivial effect relevant to finite-population sampling; not a tiny unmotivated parameter slice. Future exact finite-sample calibration can use the precise coefficient.

The dated certificate retains the supplied scientific assessment, sources and limitations.
