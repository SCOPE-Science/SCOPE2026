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

The admissible covariance interval is exactly [-1/3,1] by the eigenvalues 1-rho (triple) and 1+3rho. Independently recomputed Wick pairings for (4,4,4,4) yield E product X_i^4 = 81 + 3888rho^2 + 20736rho^3 + 110160rho^4 + 290304rho^5 + 570240rho^6 + 663552rho^7 + 368064rho^8. For rho=-t, dividing by rho^2 gives 1296q(t), q=284t^6-512t^5+440t^4-224t^3+85t^2-16t+3. Exact degree-4 Bernstein coefficients of q''(u/3) are (170,58,394/9,878/27,934/27), all positive, and q'(0)=-16<0<178/27=q'(1/3); hence unique interior minimizer tau approximately 0.1655387555 with coefficient C*=2510.5126513. For positive rho the ratio >=3888, so the negative minimizer is globally sharp. At rho=0 equality is trivial; singular endpoints follow by polynomial continuity. These are symbolic identities and a convexity argument, not a finite-grid extrapolation.

## originality

PASS

Best-of-knowledge PASS for the sharp *positive* coefficient and unique negative minimizer. Existing strong/general and equicorrelated Gaussian product inequalities supply qualitative nonnegativity, not the global optimal 2510.5126513 remainder; generic Wick formulae permit but do not tabulate/optimize this specific polynomial. Hirose full text is inaccessible and could contain a concealed quantitative comparison.

## value

PASS

The Gaussian product deficit is a natural and already studied dependence functional. Its best positive quadratic margin for a concrete four-coordinate quartic family supplies a calibrated stability invariant; the worst correlation being interior and negative is informative and not an arbitrary table entry. Scope is deliberately one covariance parameter and fourth powers, not arbitrary covariance/exponents.

The dated certificate retains the supplied scientific assessment, sources and limitations.
