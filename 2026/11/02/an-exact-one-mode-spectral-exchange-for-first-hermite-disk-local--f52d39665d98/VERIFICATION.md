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

# Verification notes

The exact eigenvalue integration and sign calculation are fully stated in `RESULT.md`. A self-contained Python 3 program (`check_selection.py`) uses only the standard library, performs exact rational checks on 6,219 instances plus 15 supplementary Stirling estimates, and prints `PASS 6234 finite exact rational and supplementary asymptotic assertions` on successful execution. Reproduce with `python check_selection.py`.

These are finite consistency checks. Infinite-dimensional completeness is built into the specified first-excited Landau basis; all radii are handled by the exact sign identity and a strict two-step comparison; the asymptotic statement follows analytically from uniform Stirling estimates. At integer-area cutoffs, a spectral projector is not uniquely selected, and the noninteger trace-norm identity must not be applied. The known underlying diagonalization and eigenvalue integral are credited to Abreu–Gröchenig–Romero. No independent audit has been performed.
