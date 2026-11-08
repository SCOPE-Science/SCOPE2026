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

Run `python verify_grassmann.py` from this directory with SymPy. The script calculates the conditional moments of the second Haar frame vector, then integrates the first via exact spherical quadratic-form moments, for symbolic integer dimension parameter \(n\). It tests the full rational fourth-moment and variance formulas as zero symbolic identities, independently recomputes six-dimensional samples of the Dirichlet integral in multiple spectral configurations, and checks the phase-transition sign and endpoint order for \(5\le n\le200\).

Observed successful output concludes with `SYMBOLIC_ALL_DIMENSIONS_FOURTH_MOMENT_IDENTITY_OK`, `SYMBOLIC_SECOND_MOMENT_NORMALIZATION_OK`, `SYMBOLIC_NORMALIZED_KURTOSIS_IDENTITY_OK`, the independent Dirichlet checks for \(n=5,6,7,8,9,10\), `DIMENSION_TRANSITION_AND_EXACT_EXTREMAL_ORDER_OK n=5..200`, and `EXACT_CHECKS_PASSED`.

The symbolic moments verify the rational algebra; they do not independently establish the classification of global stationary spectra or the Banach–Mazur optimality argument. Those are proved analytically in `RESULT.md`. The many-integer order check is not a proof for all dimensions; the factor \(n^2-6n-8\) and the spectral extremum lemma supply the dimension-uniform reasoning. No external human verification has been performed.
