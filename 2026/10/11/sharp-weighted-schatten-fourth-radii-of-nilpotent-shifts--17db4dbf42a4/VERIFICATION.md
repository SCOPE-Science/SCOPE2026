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

## Analytic checks
The proof derives the fourth trace moment from the full nonzero diagonal and distance-two entries of \(B^*B\). This identifies the coefficient \(4t^2(1-t)^2\) in front of adjacent squared weights. The path eigenvalue computation uses exact Dirichlet boundary conditions, not a sampled spectrum. The sharp stability multiplier is the first spectral gap, and a positive perturbation of the Perron sine vector by the second sine eigenvector attains its value. In infinite dimension, the \(\ell_2\) discrete gradient identity excludes any nonzero maximizing vector at interior \(t\).

## Executable checks
File: `verify_shift_s4.py`. Requires Python 3 standard library only. Execute `python verify_shift_s4.py` and expect `SCHATTEN_FOURTH_SHIFT_EXACT_MATRIX_AND_PATH_CHECK_OK`. The verifier checks 135 cases of the exact matrix trace identity using `fractions.Fraction`, plus path-eigenvalue and sharp-gap saturation tests for dimensions 3 through 33. An independent singular-value test in complex phase-weighted finite matrices likewise agreed within numerical tolerance.

## Scientific limits
Finite tests cannot certify arbitrary dimension or infinite Hilbert spaces; the argument for those cases is the exact analytic proof in `RESULT.md`. Neither the verifier nor this note asserts independent peer review, formal-machine proof, publication novelty, or comprehensive prior-art clearance.
