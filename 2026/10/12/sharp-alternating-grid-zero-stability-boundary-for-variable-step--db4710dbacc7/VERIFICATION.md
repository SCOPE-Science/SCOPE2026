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
# Reproducibility

`bdf_alternating_check.py` requires SymPy and can be run with `python bdf_alternating_check.py`. The mathematical proof and definitions of all matrices and coefficients appear in `RESULT.md`. The checker reconstructs derivative weights from interpolation nodes, tests the Schur conditions symbolically and all claimed polynomial factorizations, confirms the reciprocity and coprimality boundary identities, and executes twenty exact-rational cross-checks. A `VERIFY_OK` line indicates those symbolic and finite checks succeeded.

The proof for every real positive ratio uses polynomial identities together with exact sign arguments; only printing and numerical roots use approximations. This is a self-reviewed calculation; independent audit is not performed.
