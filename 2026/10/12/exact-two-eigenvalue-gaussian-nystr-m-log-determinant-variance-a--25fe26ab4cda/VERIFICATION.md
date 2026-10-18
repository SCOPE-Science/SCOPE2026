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

PASS. The rank-one Nyström residual is PSD of rank one, so the preconditioned M has eigenvalues 1 and exp Z. Conditional independent Gaussian trace probing gives error Z(χ1²−1) and exact MSE=2 E Z². The determinant lemma expresses Z as log ratio of two diagonal angular quadratic forms; uniform Fourier expansions with radii u,v followed by orthogonality give E Z=m and Var Z=2[Li2(u²)+Li2(v²)−2Li2(uv)]. Ahat<=A and tr Ahat<=a force Z>=log(1+b), strictly if a>b almost surely; equality if a=b. For fixed b and contrast a→∞, Cauchy ratio s=√(b/a) ω2/ω1 and domination by logarithmic integrable envelope yield exact excess coefficient 8[log(1+b)+2 log 2] in units sqrt(b/a). Fresh independent high-precision angular quadrature/dilog comparisons at positive spectral pairs agree; proof covers continuum and limiting regime.

## originality

PASS

PASS, best of knowledge. Cortinovis–Toni 2026 establish conditional Gaussian-probe variance and broad estimates for the same algorithm, but the inspected main rank-oversampling bound assumes ℓ>=4 rather than exactly one sketch direction in 2×2, and does not compute the unconditional joint law over sketch and probe. Saibaba et al. and Persson–Kressner address different logdet estimators or matrix-function approximation targets. The dilogarithmic exact two-eigenvalue risk and sharp square-root contrast penalty appear not to be directly implied by inspected results. Possible equivalent 2D angular-integration literature remains a risk.

## value

PASS

PASS. A natural smallest nontrivial rank-deficient Nyström sketch provides a meaningful exact benchmark for the currently studied logdet method. The discovered sqrt(b/a) excess, rather than 1/a, quantifies rare sketch orientations and separates random/ideal preconditioners; a narrow exact invariant is motivated by the stochastic estimator, not arbitrary parameter slicing.

The dated certificate retains the supplied scientific assessment, sources and limitations.
