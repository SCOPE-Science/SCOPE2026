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

The complete all-parameter proof, including global optimality over asymmetric edge choices, is in `RESULT.md`. The following finite independent checks support its algebra and numerical consequences; they are not an independent mathematical audit, an exhaustive test of all dimensions, or a guarantee of novelty.

Install `numpy>=1.24` and `scipy>=1.10` as listed in `requirements.txt`. From this directory, run:

```
python verify_alternating_cycle.py
python optimize_global.py
```

The first program independently constructs a stochastic matrix from undirected stationary flows, checks detailed balance and row sums, symmetrizes it, then computes eigenvalues for all integer \(m\) from \(2\) through \(24\) and nine stationarity ratios. It tests the analytic formula against spectral eigendecomposition, checks a fine scalar optimization grid and the Metropolis threshold on the same cases, compares the analytic optimum against 3,960 randomized feasible asymmetric kernels for sizes \(2\) through \(12\), and checks exact rational thresholds for \(m\) equal to \(2,3,4,6\). The test reports **4,585 passed checks**.

The second program uses SciPy constrained numerical optimization of all \(2m\) edge flows directly rather than fixing them to be equal. It tests 25 parameter combinations for sizes \(2\) through \(6\) with five stationary ratios, two distinct initial points each; it asserts that the best successful solver value matches the independently derived analytic global optimum within \(3\cdot10^{-6}\). This is a finite numerical cross-check, not a certificate of optimality for unrestricted parameters.

The analytical proof is distinct from the numerical experiments: convexity and averaging justify reduction to a common stationary flow over **all** admissible reversible kernels; the Fourier block diagonalization evaluates **all** eigenvalues in every dimension; and the final constrained minimax proves the exact threshold and value for every real \(0<r\le1\). The strongest unproved extensions concern nonreversible walks, arbitrary stationary patterns, and uniqueness of asymmetrically weighted optimizing kernels. Independent audit: not performed.
