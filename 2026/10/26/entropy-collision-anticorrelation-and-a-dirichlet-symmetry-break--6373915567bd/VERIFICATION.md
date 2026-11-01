---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

Differentiating the Dirichlet gamma moment identity at mixed exponents gives the exact H-Q covariance. The rational term is strictly negative since A²-sum(alpha_i²)=2 sum_{i<j}alpha_i alpha_j>0; a weighted covariance of alpha with strictly increasing digamma is nonnegative. Along fixed-sum tangent vectors the second variation of V=-Cov is [2a(Ka+1)trigamma(a+1)-1]sum(v_i²)/[Ka(Ka+1)²(Ka+2)]. The integral a*trigamma(a+1)=integral_0^infty e^-u [(u/a)/(e^(u/a)-1)] du increases strictly from 0 to 1, hence exactly one positive threshold; strict local maximum before, minimum after, with no assertion at zero curvature. Independent numerical differentiation of raw gamma moments and closed formula agreed for five nonsymmetric/symmetric shape vectors to 6.1e-16; the symbolic argument, not finite checks, covers every positive real shape and integer K>=2.

## originality

PASS

Qualified PASS for combined universal asymmetric sign and unique fixed-A Hessian reversal; raw Dirichlet mixed moments and both marginal diversity indices are established background, not a novelty claim. Botha–Ferreira–Bekker (2021) provide power-sum Dirichlet moments, and Bissiri–Corradin–Ongaro (2026) provide marginal Gini–Simpson posterior dispersion, but the material compared does not supply this exact sign plus unique constrained-curvature statement.

## value

PASS

Shannon entropy and collision concentration are complementary but non-equivalent ecological/Bayesian diversity summaries. Identifying their universal Dirichlet covariance sign and a concentration-dependent change in sensitivity to symmetry breaking is a natural nontrivial structural phenomenon; the critical surface is exact, not a numerical threshold sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
