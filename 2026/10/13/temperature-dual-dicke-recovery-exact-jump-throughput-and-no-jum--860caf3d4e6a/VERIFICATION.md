---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

For n≥5 and 1≤a≤floor((n-3)/2), weight sets {a,b},{a-1,b-1},{a+1,b+1} are pairwise disjoint. R0,R-,R+ consequently have orthogonal inputs and contraction singular values for sufficiently small γ. Projection of each local σ± between Dicke states has amplitude sqrt[w(n-w+1)]/n or sqrt[(n-w)(w+1)]/n; the diagonal ξ filter equalizes both logical amplitudes at sqrt[a(b+1)]/n, proving J=γa(b+1)/n and branch factors p,1-p, while R0 balances no-jump amplitudes at smax. Counting zero-jump A0/B0 patterns gives hypergeometric f_wl and exact cosine D=Mab/sqrt(MaaMbb), with strict D<1 when 0<p<1 by ℓ=0,n ratio separation. Binomial covariance yields 1-D=(b-a)²p(1-p)γ²/(2n)+O(γ³). Independent numerical hypergeometric calculations checked n=5,7,8 at several p and γ, and endpoint equality; this corroborates but does not replace all-n proof.

## originality

PASS

Best-of-knowledge original explicit all-n restricted-family jump throughput and no-jump coherence/invariant, after crediting the published five-qubit Dicke PAQEC construction and general probabilistic error correction. Full closest-paper text was not accessible; uncertainty is recorded instead of asserting unseen sections lack the formulas.

## value

PASS

A natural, physically motivated code family has an exact analytic temperature-independent jump acceptance rate and separately temperature-dependent residual no-jump decoherence, giving a useful restricted-family Pareto choice of excitation gap. The exact jump/fidelity-throughput tradeoff is a meaningful mathematical invariant beyond demonstrating that one five-qubit code has O(γ²) fidelity; no global QEC optimum is implied.

The dated certificate retains the supplied scientific assessment, sources and limitations.
