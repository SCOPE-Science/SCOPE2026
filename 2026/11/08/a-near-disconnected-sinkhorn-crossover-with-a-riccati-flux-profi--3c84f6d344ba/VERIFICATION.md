---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

For K_delta=[[1,delta],[delta,1]], row targets a,1-a and column targets b,1-b, direct row-then-column normalization yields x^+=B[(1-a+a delta^2)x+delta]/[delta x+a+(1-a)delta^2]. The positive matrix M=[[BA,B delta],[delta,C]] has determinant B*a*(1-a)*(1-delta^2)^2>0 and positive eigenvalues; the two fixed points have opposite signs, and exact Möbius cross-ratio conjugacy has eigenvalue multiplier (S-D)/(S+D). Independent rational-arithmetic spot tests matched the exact update and cross-ratio conjugacy. For b=a+kappa*delta, independent symbolic expansion of (F_delta(x)-x)/delta equals [a+kappa*x-(1-a)*x^2]/[a(1-a)]. The positive attracting fixed point stays in a uniform compact interval along fixed x0, giving the needed uniform discrete-Euler/Gronwall convergence over bounded t=n*delta; the explicit row-normalized fluxes follow by substitution and preserve correct normalization. The discriminant and log expansion give the joint mismatch/delta rate with no illegal division at kappa=0. Tests are finite corroboration, not infinite proof.

## originality

PASS

Best-of-knowledge original combined critical two-parameter singular-kernel/marginal-mismatch Riccati trajectory and normalized flux profiles. Exact two-by-two Möbius fixed-kernel local rates are known and not assigned novelty credit.

## value

PASS

The mismatch-dependent critical slowdown at a nearly disconnected transport kernel is a natural singular perturbation phenomenon; the uniform entire-trajectory Riccati equation together with observable cross-flux/column residual profiles and sharp sweep scale answers a motivated quantitative algorithmic question. It is not only a reparametrized fixed-kernel contraction constant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
