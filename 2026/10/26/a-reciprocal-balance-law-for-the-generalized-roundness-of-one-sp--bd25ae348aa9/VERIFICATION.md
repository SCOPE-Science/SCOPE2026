---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

For a star whose m ordinary arms have length one and exceptional arm length t, write zero-sum leaf coefficients as equal-arm fluctuations, common sum s and exceptional coefficient b, with hub coefficient −s−b. The p-distance quadratic form has m−1 transverse eigenvalues −2^p and a 2×2 Schur-complement block. Its negativity is equivalent to H_p(t)^2≤2[2−(m−1)2^p/m] for H_p=((1+t)^p−t^p−1)/t^{p/2}. H_p is monotone in p in the required interval and bounded by 2^p−2, yielding a unique threshold p∈(1,p₀), p₀=log₂[2m/(m−1)], and a one-dimensional null direction at equality. The exact invariance H_p(t)=H_p(1/t) proves t↔1/t reciprocity. The balanced minimum at t=1 is log₂[2(m+1)/m]; expansion near t↓0 yields p₀−p∼p₀² t^{2−p₀}/(4 ln 2) when m≥3 and the Lambert-W logarithmic critical law for m=2. Independent high-precision roots and full zero-sum negative-type matrices were checked on both sides of threshold. Infinite monotonicity, global inequality and asymptotics follow the analytic arguments, not these tests.

## originality

PASS

Doust–Weston arXiv:0705.0411 Theorem 5.6 already computes the equal-arm star threshold, exactly the t=1 specialization, which must be credited. Sánchez arXiv:1108.0451 Corollary 2.4 provides a general distance-matrix criterion for any finite metric space, but not this explicit one-unequal-edge threshold profile, reciprocal length law, strict minimum or two distinct singular asymptotic regimes. No Resultary hit covers the same metric and invariant; other weighted-star studies concern Dudley norms or polytope invariants.

## value

PASS

Supremal p-negative type is a natural nonlinear embedding invariant of metric trees; a single arm perturbation is a canonical test of sensitivity to inhomogeneity. The exact reciprocal-length symmetry, balanced extremum, and change from power to Lambert-W behavior at m=2 quantify a motivated natural geometric transition, not a cosmetic reparameterization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
