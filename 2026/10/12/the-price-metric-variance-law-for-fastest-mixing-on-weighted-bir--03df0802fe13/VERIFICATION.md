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

# Reproducibility and boundaries

The sole numerical artifact is `verify.py`, a standalone Python 3 program requiring only the standard library. Run it with `python3 verify.py`. It constructs deterministic positive rational stationary masses and positive perfect-square edge prices, then verifies exact budget equality, centered path-coordinate variance, positive cumulative fluxes, the generalized eigenvector equation, and the sum-of-squares equality for eight separate edge signals per instance. The successful output from the packaged program is:

`VERIFY_OK 801 exact positive-mass/price instances; 6408 exact ground-state quadratic-identity checks; budgets/eigenrelations`

The exact program also tests the fully heterogeneous four-state example from `RESULT.md`. An additional, unpublished verification calculation sampled 420 positive real nonsquare-price cases (path sizes \(2\) through \(15\)) and numerically compared the algebraic second eigenvalue with \(1/D\), finding maximum relative error below \(2.36\times10^{-14}\). These checks are **finite**: neither exact samples nor numerical eigenvalue comparisons prove a universally quantified eigenvalue-optimization theorem. The proof of the all-real-parameter statement is the covariance identity and all-direction nonnegative quadratic factorization in `RESULT.md`, with equality conditions proving uniqueness and simplicity.

The exact theorem assumes \(\pi_i>0\), \(c_i>0\), \(\sum\pi_i=1\), and a unit *linear* edge-price budget. It does not determine discrete-time SLEM-optimal chains, total-variation mixing times, nonreversible generators, graphs with additional edges, or designs with hard exit-rate caps. No external/independent mathematical audit has been carried out.
