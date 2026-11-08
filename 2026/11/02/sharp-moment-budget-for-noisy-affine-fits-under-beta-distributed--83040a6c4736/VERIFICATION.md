---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

Conditioning on nodes, the slope error is N(0,sigma²/S_m) with S_m=sum_i(X_i-Xbar)²; hence q-moment finiteness reduces to E S_m^{-q/2}. For range R, R²/2<=S_m<=mR²/4, so their small-ball exponents govern the same moment threshold. Exact minimum-order-statistic integral m int_0^1 f(x)[F(min(1,x+r))-F(x)]^{m-1}dx splits into two endpoint layers and interior. Endpoint pieces give r^{m alpha}, r^{m beta}, interior r^{m-1} and a log only at endpoint-integrability ties, proving gamma and boundary divergence by layer cake. Four arcsine nodes yield 48/pi^4 via x=r*sinh²(t) and 2 int exp(-3t) cosh(t) dt=3/4, while uniform range formula is 4r³-3r⁴. Independent small-radius quadrature approaches 48/pi^4 and exact m alpha threshold identities corroborate. No claim to higher-degree or weighted/conditioned regression.

## originality

PASS

Critical strongest predecessor now identified and actually inspected: Royen (2008), Theorem 3, proves the general-n pure-power one-endpoint small-variance exponent and critical logarithm, plus a range identity. This important mechanism is prior and must not be portrayed as new. Published Resultary three-Beta-sample paper explicitly limits itself to m=3 and credits Royen. The present m>=4, two-endpoint Beta competition, noisy OLS moment interpretation and sharp four-versus-five arcsine MSE boundary are not stated in those inspected results; transfer from Royen and beta endpoint asymptotics is a substantive but fairly close extension. A broader Royen theorem or probabilistic negative-moment criterion may imply the general beta formula; retain material risk.

## value

PASS

The exact unconditional moment budget is a natural stability threshold for unweighted noisy interpolation, notably contrasting apparently benign uniform and Chebyshev/arcsine four-node designs. It gives sharp sample-count boundaries for every beta parameter and all error moments q, not just another finite table. Mathematical value does not require a new concentration theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
