---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Independently reconstructed RESULT.md:36–100. Differentiation of the stated first integral cancels the velocity-squared force, and its even coercive potential, increasing for x>0, and strictly positive kinetic weight give one compact regular oval per A>0. Integrating dt=dx/y on the positive quarter of the oval and multiplying by four gives the minimal period in physical time. The substitution x=Au gives the factor 2√2, the weight exp(λu⁴/4) with λ=αA⁴, and the denominator √(I₅+εI₁) with ε=(βA⁴)⁻¹. The log-integrand derivative is (u⁴−E[v⁴])/4<0; compact λ-ranges admit a locally uniform (1−u)⁻¹ᐟ² majorant. For the uniform enclosure, the tilted mean I₁/I₅ of v⁻⁴ decreases with λ by its opposite-monotonicity covariance with v⁴; it is integrable at u=0 and bounded by its λ=0 value 3/(1+u²+u⁴). The profile at zero follows by s=u⁶. For the large endpoint the change t=λ(1−u) yields the stated kernel. Its numerator is bounded by e^(−t/4); restricting w to [0,min(t,1)] bounds the normalized denominator integral below by e⁻² min(t,1)/32 for λ≥2. The resulting majorant on (0,∞) is integrable, and the limiting integral is 4∫₀¹(1−s²)⁻¹ᐟ² ds=2π. The multiplicative enclosure then gives finite-profile and divergent-profile matching without exchanging the A and λ limits. The analytic estimates also cover α=0 and every β>0; they do not use a β=0 normalization. The supporting script was inspected, not executed. Its symbolic check and finite quadratures are ancillary, and the moment comparisons there are numerical rather than exact certificates.

## originality

PASS

The supported increment over the earlier indexed period theorem is the finite-amplitude relative-error enclosure uniform on the entire α≥0 half-line, together with the single crossover matching both endpoint regimes. Neither the period quadrature nor the two fixed-parameter constants are new. There is material exact coverage in a distinct later indexed record, d8280613f6f7; this review does not claim uniqueness across the index. No inspected evidence places that exact coverage before the frozen result.

## value

PASS

The two fixed-parameter scalings leave a genuine singular regime near α=0. The all-amplitude multiplicative estimate controls that regime even along parameter sequences with divergent crossover argument, and quantifies when the linear restoring term is negligible without restricting α. This is useful quantitative information beyond rederiving the endpoint constants or the known period monotonicity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
