---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For the equiangular unit-row frame U, U^T U=3I/2 and the fixed least-squares residual is delta*(1,1,1); centering gives A_i=I-eta u_i u_i^T and affine eta*delta*u_i. The one-step IID mean-square map q||e||^2+eta^2 delta^2, q=1-eta+eta^2/2, iterates to c_I=q^3 and d_I=eta^2 delta^2(1+q+q^2). Independent explicit symbolic multiplication of all six RR affine permutation maps confirmed E[M^T M]=c_R I and E[M^T v]=0, with c_R=1-3eta+3eta^2-eta^3+eta^6/32 and d_R=eta^4 delta^2(eta^2+6eta+12)/16. Symbolic factorization confirms c_R-c_I=-3eta^2(2-eta)^4/32. Positive-coordinate polynomial transforms and Descartes rule give unique quartic eta1=1.1803110213; monotone cubic eta_inf=1.2126391135 gives stationary sign threshold. The real-epoch geometric ratio decreases, establishing exactly one transient reversal window eta1<eta<eta_inf from e0=0; at eta=6/5 first RR worse then eventually better. General starts only enjoy universal RR dominance at eta<=eta1. The finite path examples are not relied on for all eta or k.

## originality

PASS

Primary RRK analysis under consistency and generalized noisy Kaczmarz convergence-to-neighborhood estimates do not state the fixed-residual six-permutation affine moment comparison, two distinct thresholds, or finite-epoch unique crossover. The independent-correlation vs per-visit-noise assumption matters: existing upper bounds do not give the new exact comparative signs. Published Resultary semantic search did not identify equivalent statements, but the negative search is not a novelty proof.

## value

PASS

This is a motivated exact sampling-law comparison on a minimal perfectly conditioned but inconsistent tight-frame example. It distinguishes the immediate noise-injection threshold from the stationary error threshold and proves a genuine short-to-long horizon policy reversal; a source with condition number one removes ill-conditioning as an alternative explanation. The result is useful within these precise fixed-residual, constant-step, epoch-terminal bounds without implying a general RR advantage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
