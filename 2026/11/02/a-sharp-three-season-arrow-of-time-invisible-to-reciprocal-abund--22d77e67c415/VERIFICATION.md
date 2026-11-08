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

For a>1 and any positive periodic beta, y=1/x obeys the positive-intercept contraction a*y_(t+1)-y_t=beta_t. Its Fourier transfer Y_k=B_k/(a exp(2pi ik/n)-1) preserves squared magnitudes when real beta is reversed, proving all n and all cyclic lags. The explicit three-season inverse numerators share e1,e2 and have product difference -a(a-1)^3(a+1)(b-c)(b-d)(c-d). Replacing each numerator L_i by L_i+q(a^3-1) preserves e1,e2 differences and product difference; subtracting their positive-denominator saturated means proves the claimed sign for all finite q>=0. For n<=2 the reversal is a cyclic rotation. Independently reconstructed the polynomial factor with SymPy and rational a=2,b=1,c=2,d=3 cycles.

## originality

PASS

Best-of-knowledge originality for the precise final theorem only, with known component results explicitly excluded from novelty and named inaccessible-source risks; relevant indexed findings and primary literature were compared by implication.

## value

PASS

The smallest order-sensitive seasonal arrangement is a natural finite cutoff: all second-order inverse-population cyclic measurements hide orientation for every n, while a realistic saturating census proxy detects the orientation of three distinct seasons with a parameter-universal exact sign. This is an interpretable structural identification limit, not mere numerical resampling of a known mean.

The dated certificate retains the supplied scientific assessment, sources and limitations.
