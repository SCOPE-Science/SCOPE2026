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

# Reproducibility and verification

The analytical proof is in `RESULT.md`. It establishes the almost-everywhere Bernoulli representation, the exact bounded difference of the quantile sum and a reversal-odd block sum, a complete four-bit graph coboundary potential, and the finite-dependence central limit theorem with an explicit positive variance. The exceptional four thresholds are obtained from a displayed indicator formula; the proof does not infer an infinite-time result from numerical experiments.

Run `python verify.py` with Python 3 and its standard library. The code exhaustively checks all binary blocks of lengths one to four using integers and exact rational fractions. It establishes:

- Every short reversal-odd basis function is a de Bruijn graph gradient.
- The complete bilinear Green–Kubo matrix on the six reversal-pair basis functions is exactly \(vv^{\mathsf T}/32\), for \(v=(0,1,-1,1,0,1)\).
- The displayed four covariance values of the one noncoboundary representative are exact.
- Five independent generators of the zero-obstruction subspace are actual gradients on all sixteen four-bit edges.
- Exactly the four threshold indices \(k\in\{3,5,11,13\}\) have nonzero obstruction, each of magnitude one; all other fourth-level indices are gradients.

Observed execution produced four PASS messages. No floating-point calculations, external packages or stochastic sampling are required.

Limits: exact rational finite enumeration checks the finite symbol calculus, not the target-density transport theorem or a self-contained proof of the standard finite-dependent Gaussian theorem. Those follow analytically from the hypotheses and classical probability. It does not validate publication priority, nonstationary behavior, or levels beyond four bits. An independent mathematical audit has not been performed.
