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

PASS: Expanding source PMF p_x = theta^4 q^x(x+1)(x²+A x+B)/[6(1+theta)^8] gives cubic count polynomial. Differentiating q^(x+1)/(1-q) with q d/dq three times yields exact strict-survival polynomial with corrected omega1=6 theta^7+36 theta^6+108 theta^5+174 theta^4+146 theta^3+45 theta²+6 theta; other coefficients unchanged. Difference from source omega1 is theta^4(5 theta³+30 theta²+90 theta+87). Exact symbolic calculation independently recovered all four polynomial coefficients, and exact rational recurrences S(x-1)-S(x)=p_x held theta=1,2,5,9 and x=1..19. The hazard at theta=5,x=2 is 1814375/1739338>1 printed vs corrected 1814375/2336838<1. The proof applies all theta>0, x nonnegative via analytic rational-generating function, not finite tests.

## originality

PASS

PASS: Original PMF defines the distribution but paper prints a different explicit survival polynomial. Exact corrected theta-polynomial and counterexample hazard>1 are not in inspected source or earlier one-summand Poisson-XLindley literature. The original PMF mathematically entails the tail, but a nontrivial omitted cubic-tail summation is necessary to expose the published coefficient error. Resultary results are about other distributions.

## value

PASS

PASS: The proposed count distribution’s entire survival/CDF/hazard and stress-strength section depends on the coefficient. A one-coefficient polynomial repair enforces all count distribution identities, rules out an impossible conditional hazard greater than one, and changes a concrete reliability prediction by about 0.0236. Central exact law correction remains valuable even without a new general theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
