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

Let T=G1^2/G2^2 with density [pi sqrt(T)(1+T)]^-1 and tau=(kappa^(2q)G1^2+G2^2)/(kappa^(2q-1)G1^2+G2^2). The Nyström residual A-N is PSD by its orthogonal-projector factorization; for 0<theta<=1, operator monotonicity yields A^theta-N^theta PSD, so nuclear error is kappa^theta+1-tau^theta. Rescaling z=kappa^(2q-1)T gives exact normalized half-Cauchy integral. Its pointwise limit has integrable majorant z^-1/2[1-(z/(1+z))^theta] (bounded at origin as z^-1/2, infinity O(z^-3/2)); dominated convergence gives Ctheta=(2theta Gamma(theta+1/2))/(sqrt(pi) Gamma(theta+1)), yielding kappa^(theta-q+1/2) equivalent. At theta=1 the Cauchy integral gives EΔ=(kappa-1)/(1+kappa^(q-1/2)). Coupled fixed T>0 makes Δ~theta kappa^(theta-2q+1)/T; q=1 theta=1 is the separate 1/T limit. Independently integrated transformed exact Gaussian expression at kappa=5000 for theta=0.5,0.75,1 and q=1,2: normalized constants within 1.5 percent of predicted, theta=1 exact formula within 0.1 percent; bounded quadrature supports but does not replace uniform proof. Valid strictly for real 2x2 two-eigenvalue one Gaussian column, fixed q and theta.

## originality

PASS

Persson-Kressner gives funNyström and a nuclear-norm EXPECTATION upper bound under sketch size and oversampling conditions, notably >=2 columns (Theorem 3.9); the exact one-column untruncated 2x2 Gaussian trace excess, its sharp exponent/pass phase transition and mean/typical gap are not covered by the inspected theorem. Gittens-Mahoney Theorem 4 gives a deterministic alignment-sensitive Nyström error bound, not this integrated matrix-power expectation. The elementary half-Cauchy ratio and projector formula are credited premises. Searches revealed no direct published same-model asymptotic; originality qualified by broader unindexed literature risk.

## value

PASS

One-column no-oversampling Nyström is exactly the regime omitted by common expectation guarantees. A sharp stochastic mean-risk law, critical square-root functional exponent, transition from one to two passes, and a mathematically explicit uniform-integrability failure are motivated diagnostics for low-rank matrix-function approximation. The two-eigenvalue restriction is a transparent model rather than an arbitrary unmotivated slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
