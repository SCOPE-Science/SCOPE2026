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

D(I−tS)⁻¹ is compact even on ℓ∞ since D is a norm limit of its finite sections; triangularity at the first nonzero coordinate identifies the nonzero eigenvalues and gives geometric simplicity. The right-vector equation follows by summing binomial coefficients, and the left-vector equation by the alternating partial-binomial sum after replacing binom(m,n)/(n+1) by binom(m+1,n+1)/(m+1). Their pairing is one, ruling out a Jordan chain and giving the claimed Riesz projection. The rank-one norm product holds at both endpoints too, since the left functional is finitely supported. At t=0 the projections are coordinate projections. For fixed 0<t<1 the normalized right and absolute left arrays are sums of m+1 independent geometric and m independent Bernoulli variables, respectively; the integer laws have span one and the stated variances. The uniform lattice local limit gives a Gaussian central Riemann sum and the peak estimate. For finite r≥1 the scaled r-power tail outside M standard deviations is bounded by a constant times the tail mass, using the uniform bound on standard deviation times maximum atom; Chebyshev then lets M tend to infinity. Multiplying the factors gives (2πmt)⁻¹ᐟ² p⁻¹ᐟ⁽²ᵖ⁾ q⁻¹ᐟ⁽²ᑫ⁾ times ((1+t)/(1−t))^(m+1/p), including the supremum limits. For p<∞ an annihilator is analytic via its coefficient generating series, and its derivatives all vanish at t, proving completeness. The coordinate functionals give minimality and any basis ordering would force uniform boundedness of the one-term projections, contrary to the growth law. No such completeness claim is made on ℓ∞. The script was inspected, not executed; exact finite sections and truncated numerical ratios cannot certify the infinite asymptotic.

## originality

PASS

The published eigenvectors already imply the exact norm product by rank-one duality, and a separate indexed theorem explicitly gives the p=2 asymptotic and no-order conclusion, with refinements in that sector. Credit both overlaps. The supported distinct contribution is the sharp asymptotic across the full range of p, including endpoints and the exact p-dependent multiplier, not the norm product, basic spectral data, or the p=2 case alone. The inspected statements do not establish full coverage.

## value

PASS

The known compact spectrum and complete eigenvectors alone do not quantify spectral conditioning. The exact exponential scale and polynomial prefactor, including their exponent dependence and both norm endpoints, give sharp conditioning estimates for isolated spectral components. The basis obstruction clarifies a consequence of that conditioning but is not the sole justification for value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
