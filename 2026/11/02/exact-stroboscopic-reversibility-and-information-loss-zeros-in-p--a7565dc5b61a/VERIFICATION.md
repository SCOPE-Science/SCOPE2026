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

# Verification

## Analytical checks

The proof starts from the positive-definite Lyapunov solution and compares the two full Gaussian covariance matrices under observation swapping. With \(G=\left(\begin{smallmatrix}u&k\\-k&v\end{smallmatrix}\right)\), direct inversion gives the KL identity exactly, while the determinant of the conditional innovation covariance is strictly positive. Cayley–Hamilton supplies the characteristic polynomial square and three discriminant regimes without relying on an eigenvector basis. At the stroboscopic zeros the transition is a scalar multiple of identity, hence the entire sampled Gaussian Markov chain satisfies detailed balance. A separate stationary-current calculation gives positive continuous-time entropy production in the nonzero-rotation example.

## Reproduction

Install dependencies listed in `requirements.txt`, then execute `python verify.py` in the extracted package directory. The executed run returned `PASS: 2120 independent floating-point comparisons and sign checks`. The checks compare the invariant formula against direct \(4\times4\) Gaussian KL divergence, cover randomized positive-definite noise, verify scalar transitions and exactly zero reversed-pair divergence at half-turn lags, and test the local quadratic coefficient plus real-spectral strictly positive regimes.

## Limits

Finite floating-point checks are not a proof of an infinite zero-set classification. The proof is given in `RESULT.md`. These tests do not claim experimental validation, independent review, complete literature novelty certification or a proof of arbitrary game-equilibrium uniqueness.
