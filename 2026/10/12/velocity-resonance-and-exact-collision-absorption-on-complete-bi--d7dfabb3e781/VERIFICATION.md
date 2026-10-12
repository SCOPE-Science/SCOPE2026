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

Run `python verify_bipartite.py` using NumPy and SciPy as declared in `requirements.txt`. It constructs the adjacency matrix, independent two-particle Kronecker-sum Hamiltonians and coincidence-detector isometry without calling the proof's closed-form projector formulas. Spectral eigenspaces and singular-value decomposition yield the detected projector. All diagonal entries, spectral ranks, commutators, and projector identities are compared against the closed forms. Small unequal-rate absorbing Hamiltonians provide separate checks of the predicted count of undamped eigenvalues.

Replayed output:

`VERIFY_OK spectral_cases=35 localized_probabilities=2290 loss_spectra=6 max_error=6.44e-15`

The calculation uses finite floating-point diagonalizations and cannot prove the formulas for arbitrary sizes. The proof in `RESULT.md` uses positive-definite Gram matrices and all-size spectral decompositions. The loss spectra tests confirm only finitely many instances; finite-time convergence rates and nonuniform behavior near velocity equality are not certified.
