---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification and reproducibility

The analytic proof is self-contained in `RESULT.md`. The following checks were performed on the displayed assumptions:

1. The positive coefficients obey exactly `c[n+1]/c[n]=(n+alpha)/(n+1)`; Stirling's formula yields the critical summability criterion.
2. For fixed block start and fixed `m`, the diagonal discrepancy telescopes to a finite sum; no hidden limit interchange is used.
3. Abel summation controls each off-diagonal geometric frequency by `2*q[N]/abs(1-rho)`. Dominated convergence is valid because the weights are summable and the normalized errors have a uniform bound.
4. The residual estimate is uniform at every partial cutoff in a block, and the stagewise square norms have a summable upper envelope; therefore the constructed functions genuinely lie in the ordinary-series domain.
5. On polynomials the output matrix is triangular with diagonal `sum(weights)>0`; thus every polynomial output is realized exactly, and dense zero-output approximants force full product graph closure.
6. Poisson atomic recovery with growth `O((1-r)**(-alpha))` establishes that the Herglotz representing measure has no point mass when `alpha<1`.

Numerical sanity checks: with four distinct unit-circle phases, positive weights `(0.4,0.3,0.2,0.1)`, and phases `(0,0.03,1.3,2.6)` radians, the first normalized block-response error `abs(response/B-w[0])` for block start 9 decreased from approximately `0.095575` at length 1000 to `0.0473644` at length 150000 for `alpha=1/2`; for `alpha=3/4` it decreased from `0.0327231` to `0.0026691`. These are finite illustrations and do not prove the infinitely-many-phases theorem. The proof covers the infinite setting by dominated convergence.

The domain is **not** that of the closed adjoint of multiplication by the Smirnov symbol. Independent evaluation of originality and correctness remains unperformed.
