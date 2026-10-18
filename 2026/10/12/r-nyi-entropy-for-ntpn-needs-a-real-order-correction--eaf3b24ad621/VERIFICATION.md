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

From f=C^-1 (2pi)^-1/2 e^{-(x^2+lambda^2)/2}q(x) cosh(lambda x), power gamma and complete Gaussian normalization yield the displayed E[q(Z_gamma)^gamma cosh(lambda Z_gamma)^gamma] times C^-gamma(2pi)^-gamma/2 exp(-gamma lambda²/2) sqrt(2pi/gamma). Bound q(x)^gamma by C(1+|x|)^{2gamma}, cosh(lambda x)^gamma by exp(gamma lambda |x|), giving integrability for every gamma>0. Finite multinomial and binomial expansions are valid only at integer exponents; positive noninteger gamma require generalized infinite series. Independent gamma=1/2 standard-normal integration gives H=1.612085713764618. This does not assert integer coefficients are all correct or address gamma->1.

## originality

PASS

The primary 2026 theorem asserts all gamma>0 except one but derives a finite expansion requiring positive integer powers. The corrected general expectation follows by direct change of Gaussian measure and is not a formula already stated as the needed corrigendum; other skew-family Rényi formulas do not specifically correct NTPN.

## value

PASS

A genuine all-real-order domain error in a published entropy theorem undermines use at noninteger sensitivity parameters. The correction identifies precisely which claimed formula is invalid and supplies a mathematically sound evaluable replacement, while preserving the integer-order plotted example. Simple algebra is substantively motivated here by fixing a faulty published mathematical assertion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
