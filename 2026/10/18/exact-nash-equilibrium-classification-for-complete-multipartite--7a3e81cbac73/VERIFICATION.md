---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Completing the strictly concave conditional opinion square gives y_i^(s)=(β(1−γ)M_i+βγu+λs)/(β+λ) in [0,1]. The optimized payoff difference is −α(1−r/n)+κ((1−γ)M_i+γu−1/2). At any given x the opinion map contracts with factor t=β(1−γ)/(β+λ)<1. On the degree-weighted mean-zero space the eigenvalues of W are nonpositive: A=11ᵀ−Σ1_a1_aᵀ has nonpositive form ON the plane orthogonal to 1, and diagonal congruence transfers inertia. The frozen proof's word 'outside' in this sentence should read 'on'; the identity and downstream inequality are correct. The payoff sign constraints make the degree-weighted covariance between centered x and Wy nonnegative, while the resolvent has nonpositive eigenvalues μ/(1−tμ) transversely. Equality forces every player to tie and Wx=p1. Summing (k−k_a)=p(n−n_a) over parts yields k=pn and k_a=pn_a. Conversely equal fractions give y=m(p)1+(λ/(β+λ))(x−p1) and the common discriminant F(p). The positive slope of F gives at most one interior j/g, with both unanimous profiles Nash whenever an interior one is; the boundary inequalities are weak because ties are allowed. A cooperator would revise to defection in any universally indifferent mixed equilibrium, so the tie-to-defect fixed-point claim follows. Independent exact part-mean elimination and payoff comparisons checked 1,842 part-count/parameter combinations, including 14 mixed tie combinations, without a graph eigenvalue calculation. Replay: python -B /workspace/branches/frozen_recheck.py 3.

## originality

PASS

The same game's joint best responses and zero-prejudice consensus results are prior. The supported increment is the multipartite no-strict-mixing obstruction and complete weak-tie census, including common positive prejudice, exact balanced fractions and their labeled multiplicities. None of the strongest inspected comparators supplies this classification.

## value

PASS

The result answers the model's mixed-equilibrium question for a natural class of networks rather than merely recalculating a consensus threshold. It separates weak Nash equilibria from deterministic stationary outcomes, showing both why mixed Nash profiles are exceptional and exactly how many occur at resonance. The gcd obstruction sharply distinguishes unequal part-size patterns.

The dated certificate retains the supplied scientific assessment, sources and limitations.
