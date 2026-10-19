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
# Verification details

The analytic verification follows four independent logical ingredients: (i) a full determinant criterion for the positive-definite symmetric part of the sketched form, (ii) the beta distribution of two independent Gaussian column directions, (iii) a fixed-direction correlated-Gaussian sign tail combined with the attained two-point Kantorovich angle, and (iv) a chi-square/normal scaling argument with Markov control in the strongly oversampled regime.

`CHECKER.py` is reproducible with NumPy and SciPy. It compares direct finite Gram-matrix determinant signs with the predicted threshold, checks the exact beta parameter shift for multiple dimensions and contrasts, tests the fixed-direction angular minimizer, and runs seeded finite Gaussian Monte Carlo simulations. The original execution passed all asserted checks. Its simulation counts are finite and cannot independently certify an infinite-parameter assertion.

Only real two-dimensional symmetric positive-definite operators and real Gaussian sketches are covered. One-dimensional sketched Rayleigh/harmonic scalar sign loss is not a claim about negative eigenvalues of an entire two-dimensional projected operator. The 2026 motivation source was not available in full, and possible uninspected coverage is a remaining literature risk. No independent validation has been performed.
