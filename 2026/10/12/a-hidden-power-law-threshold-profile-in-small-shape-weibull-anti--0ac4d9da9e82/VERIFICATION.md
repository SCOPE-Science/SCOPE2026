---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Unit-rate reduction removes lambda. For r=1/alpha the true m=Gamma(r+1), q=Gamma(2r+1), and s=sqrt(q-m^2) satisfy m^2/q~sqrt(pi*r)4^-r, hence the lower standardized endpoint is negative uniformly for y in a fixed compact positive interval. Therefore T=exp[-(m+y*s)^(1/r)] exactly there. Logarithmic Stirling gives (m+ys)^(1/r)=2r/e+log(4pi*r)/(2e)+2log(y)/e+o(1), so exponentiation yields the full multiplicative equivalent rather than only a logarithmic rate. Independent mpmath loggamma computation for alpha=0.00625 gives additive exponent errors 0.00346, 0.00844, 0.01566 at y=0.5,1,2; these are checks, not a proof.

## originality

PASS

Hu–Song–Tan prove qualitative zero standardized anti-concentration, and the closest published Resultary paper obtains only the leading Weibull logarithmic rate 2/e. Neither proves this sharper multiplicative prefactor, nonconstant y^-2/e profile, or tail ratio. Standard Stirling is a known premise, not a published identical probability result.

## value

PASS

After the familiar standardized anti-concentration infimum collapses to zero, its leading essential-exponential rate is independent of y. The exact remaining y^-2/e power-law profile and ratio law answer the natural question of how two fixed standardized thresholds still differ. This is a motivated refinement beyond a generic Stirling exercise, although it uses classical special-function methods.

The dated certificate retains the supplied scientific assessment, sources and limitations.
