---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

The two-state Feynman-Kac generator yields f_s''+f_s'+s f_s=0, f_s(0)=1,f_s'(0)=0, with F_N=f_s(kt)^N. Gaussian covariance integration yields g_s(tau)=exp[-s(tau-1+exp(-tau))]. For s<=1/4 the positive causal Green kernel applied to (D^2+D+s)g=s^2(1-exp(-tau))^2 g gives f<g. For 1/4<s<=1/2, logarithmic derivatives prove f<g before the first zero, and the postzero cosine envelope H(tau) has a strictly decreasing bound whose value at first zero is below one. Above 1/2, the cosine peaks have log(|f|/g) diverging to +infinity and infinitely many zeros. Fourth derivatives give the stated short-time correction. Boundary s=1/2 and finite N are covered analytically. Independently sampled 271 checks are corroborative.

## originality

PASS

The two-state relaxation, independent-spin product rule, and OU Gaussian comparison formulas are known. The claim is a sharp all-positive-time envelope ordering with distinct breakpoints s=1/4 (oscillation onset) and s=1/2 (global comparator failure). Inspected primary treatments gave forward formulas, spectral examples or revival measures, not this exact inequality theorem. O=PASS with Kubo-Anderson envelope-comparison priority risk.

## value

PASS

A covariance-matched Gaussian replacement need not be a conservative dephasing envelope; this theorem gives the exact count of microscopic independent sources needed for a uniform bound and identifies arbitrarily late failure above it. This is a naturally motivated infinite-time classification, not a single moment comparison.

The dated certificate retains the supplied scientific assessment, sources and limitations.
