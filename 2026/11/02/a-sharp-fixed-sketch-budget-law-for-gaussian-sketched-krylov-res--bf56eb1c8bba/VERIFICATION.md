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

Run `python verify.py` with NumPy and SciPy installed. The script independently checks the worst-case Chebyshev interpolation normal equations and residual, simulates 18,000 fresh Gaussian sketch-and-solve trials, checks the published exact Student mean/median, and enumerates 15 finite-budget minimizations (including the precise integral-tie condition). Expected terminal line:

`VERIFY_OK chebyshev_cases=16 gaussian_sketch_draws=18000 finite_budget_cases=15 tie_case=1`

The script is a numerical crosscheck, not a formal certificate of the infinite-dimensional supremum or the eventual-\(s\) statement. Those are proved analytically in `RESULT.md`. No independent mathematical audit has been conducted.
