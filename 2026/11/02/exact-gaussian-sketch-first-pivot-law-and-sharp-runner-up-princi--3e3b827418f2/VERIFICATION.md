---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For fixed n>=2 mutually orthogonal nonzero columns with unique largest squared norm alpha_1, the same iid standard Gaussian sketch gives independent column sketch squared norms alpha_j*chi_k², by multivariate Gaussian orthogonality. Conditioning on Gamma(k/2,1) for the leading column yields exact integral 1−prod_j F_s(r_j t); at even k=2m, the integer-gamma CDF and inclusion-exclusion give the stated finite rational sum over nonempty competitor subsets and degrees 0..m−1. A competitor j has beta tail I_{alpha_j/(alpha_1+alpha_j)}(k/2,k/2), whose endpoint Laplace expansion gives [4t(1-t)]^{k/2}/[(1−2t)sqrt(2πk)]. When r runners-up have squared norm beta and R=alpha_1/beta>1, simultaneous runner-up exceedances obey Chernoff exponent J_2(R)>J(R), certified by (R−1)²(5R+4)>0; strictly shorter columns have greater J. Therefore P_k ~ r(R+1)/[(R−1)sqrt(2πk)] [4R/(R+1)^2]^(k/2) and the inverse small-risk row bound has the asserted loglog correction. Independently compared three exact k=2 inclusion-exclusion expressions with conditional gamma integration. The infinite-k asymptotic rests on the analytic beta tail and strict exponent comparisons, not simulations.

## originality

PASS

Best-of-knowledge comparison of exact statements and mathematical implications across relevant primary literature and Resultary; key source-access/alias risks are explicitly retained. The assessed new claim is not the background object, source algorithm, or textbook intermediate identities.

## value

PASS

Sketched pivot selection is a central randomized matrix-factorization decision. The exact first-pivot failure probability on the canonical orthogonal-column test family offers a precise numerical benchmark; its large-k leading constant detects how many columns tie for second rank and proves why shared leading-column fluctuations do not spoil rare-event additivity. This is a natural complete first-decision classification and useful sketch-height calibration, not a claim about later QR pivots or full factorization accuracy.

The dated certificate retains the supplied scientific assessment, sources and limitations.
