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

# Reproducibility and scope

Run `python artifacts/frustrated_sampling_verification.py` with SymPy, NumPy and SciPy. The script verifies transition and stationary identities, three exact-rational characteristic spectra, and 450 independently optimized numerical samples over 90 admissible parameter pairs. Exact rational identities are algebraic checks; randomized numerical trials cannot prove global optimality. The unrestricted optimization follows from concavity and the analytic mode analysis in `RESULT.md`. The test output is embedded as `artifacts/verification.txt`.

The computation does not examine every possible prior theorem and does not constitute independent mathematical certification. No independent audit has been performed.
