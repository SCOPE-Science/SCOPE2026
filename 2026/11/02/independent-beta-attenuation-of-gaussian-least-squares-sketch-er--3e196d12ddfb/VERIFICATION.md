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

Rank-one SVD A=σu vᵀ reduces the pseudoinverse error to v/σ times e=(uᵀ ΩΩᵀR)/(uᵀΩΩᵀu), with Δ=||e||². For Gaussian Ω, conditioning on its first row gives e_G=(ZᵀR)/sqrt(X), X~χ²_ell, Z standard in u⊥ independent. Haar projection P gives T=uᵀPu~Beta(ell/2,(n−ell)/2), orthogonal projection length sqrt(T(1−T)), independent uniform sphere direction S; hence e_H=sqrt(Y/X)SᵀR with Y~χ²_{n−ell}. Beta–gamma factorization B||Z||²~χ²_{n−ell} and rotation invariance identify the entire joint row-vector law, not merely coordinate marginals. B strictly (0,1) implies all-threshold error stochastic dominance when R≠0. Chi-square small-ball and dominated convergence give exact t^(−ell/2) constants and moment cutoff; rank-deficient d and multiple outputs are handled. Independent beta moment check at n=10,ell=4 gives E B=2/3 and E B²=16/33, matching tail constant 2/11 vs 3/8. No numerical experiment substitutes for distributional proof.

## originality

PASS

Epperly–Webber 2026 establish optimal orthonormal sketch mean residual error via matrix-beta moments, and Gaussian-sketch distribution identities are classical. The all-output finite-sample independent beta scaling, strict every-threshold dominance and explicit catastrophic-tail coefficient go beyond the accessible abstract/summaries, but the very relevant original full paper was inaccessible, so a specialized distributional formula may already occur in it or older matrix-variate theory.

## value

PASS

Exact every-threshold reliability and heavy-tail coefficient answer a practical mathematical question not settled by average-error minimax analysis; the independence coupling gives a natural complete rank-one law and improves understanding even when mean errors diverge (ell=2).

The dated certificate retains the supplied scientific assessment, sources and limitations.
