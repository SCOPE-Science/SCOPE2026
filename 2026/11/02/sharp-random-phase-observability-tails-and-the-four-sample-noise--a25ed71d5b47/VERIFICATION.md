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

The smaller eigenvalue is (m−|Σ exp(2iΘ_j)|)/2 and vanishes only on the projective diagonal. The minimum over a direction of Σ sin²(Θ_j−φ) places the entire ε-sublevel set within O(√ε) of that diagonal. In wrapped differences from Θ_1 the Jacobian is one and the quadratic term is I−11ᵀ/m on m−1 coordinates, with determinant 1/m. Rescaling the differences gives a bounded domain, an ellipsoid boundary of measure zero, and joint density tending uniformly to w(φ)^m, including where w vanishes. This proves the stated coefficient and the inverse-moment boundary by integration. For the noise tail, t^(m−1)P(σ|Z|/√λ_->t | Z) is bounded by a constant times |Z|^(m−1), using the sublevel bound extended to all positive arguments. Dominated convergence gives the stated Gaussian moment factor. The larger-eigenvalue coordinate is bounded by σ√(2/m)|Z'| and a fixed fractional-threshold sandwich followed by taking the fraction to zero preserves the coefficient. Tail integration gives the exact error moment cutoff, and strict Jensen gives uniqueness of the continuous constant density. Minor scope wording: for actual oscillator times a reduction modulo π can also introduce a separate ± sign on each row, in addition to a fixed reflection; it does not change the Gram eigenvalues, or the conditional Gaussian error law for independent acquisition noise. The finding itself is stated for V and independent Gaussian noise and does not rely on that wording. The packaged checks were inspected, not rerun; the asymptotics are proved analytically.

## originality

PASS

The distinct supported contribution is the sharp coefficient for arbitrary continuous projective densities and the resulting exact Gaussian least-squares norm tail and leading-constant optimization over those densities. The uniform Gram law and inverse-moment threshold, including the four-sample threshold as a consequence, are not independent novelty claims: a distinct same-day indexed circular-sketch result has exact uniform spectral overlap up to a factor of two, with no demonstrated publication ordering. The strongest material read did not establish coverage of the surviving general-density statement.

## value

PASS

Almost-sure rank is a poor predictor of reconstruction risk: two or three observations suffice for rank but can have infinite unconditional MSE. The density-sensitive exact coefficient distinguishes observation designs even when they share the same moment cutoff, identifies uniform sampling as the unique asymptotic minimizer, and quantifies the heavy-tail tradeoff. This is not a statement about all finite thresholds or other estimators.

The dated certificate retains the supplied scientific assessment, sources and limitations.
