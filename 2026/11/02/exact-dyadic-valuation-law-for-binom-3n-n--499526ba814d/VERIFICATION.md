---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

Kummer identifies valuations with carries of the overlapping binary strings for n+2n. Merging states (1,0),(0,1) gives exact 3x3 weighted transfer matrix M(z), initial state (1,0,0) and a necessary final zero-input carry column (1,1,z). Independent symbolic inversion reproduced (1+t)(1-tz)/(1-(1+z)t+(z-z^2-1)t^2+(z+z^2)t^3); numerator and denominator are coprime over Q(z). The first carry forces a second, excluding valuation 1; no-carry words are Fibonacci. Dominant eigenvalue derivatives lambda'(1)=1 and lambda''(1)=4/3 give slopes 1/2 and 11/12, with primitive transfer matrix yielding a genuine CLT. Independent direct digit-sum checks r<=14 corroborated exact zero count and absent valuation 1; finite data do not prove the CLT.

## originality

PASS

Best-of-knowledge PASS for the explicit diagonal binomial valuation enumerator, reduced order-three rational function and concrete Gaussian law. Spiegelhofer-Wallner compute distributions along fixed Pascal rows, a different quantifier domain. General digit-function normality tools could imply an asymptotic but not automatically this exact polynomial or constants.

## value

PASS

A complete finite-block distribution of a classical binomial-diagonal valuation; it gives nontrivial forbidden valuation, Fibonacci zero count, moments and asymptotic fluctuations, which are mathematically natural rather than an arbitrary finite slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
