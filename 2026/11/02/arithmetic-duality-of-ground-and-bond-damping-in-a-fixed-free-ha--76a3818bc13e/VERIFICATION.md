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

The reproducibility program `verify_damping.py` uses NumPy and SciPy. Run `python verify_damping.py` in a directory containing the file. It directly assembles fixed–free stiffness and site/bond viscous-damping matrices, compares analytic node sets with trigonometric values, compares undamped imaginary-axis eigenpairs with the arithmetic prediction, tests the totient placement counts, and checks the local-kick projector identity.

An observed passing run reported: `{'mode_index_cases': 6478, 'single_damper_spectral_cases': 238, 'mixed_spectral_cases': 390, 'placement_counts': 79, 'local_kick_projectors': 31950}`.

The computations use floating-point tolerances specified in the checker and only the finite sizes specified there; they cannot establish the full theorem. The proof in `RESULT.md` supplies the arbitrary-finite-size quantifiers, including positivity and nonzero damping assumptions. No independent audit has been performed.
