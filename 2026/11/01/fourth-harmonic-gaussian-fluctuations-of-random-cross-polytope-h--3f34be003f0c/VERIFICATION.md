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

# Verification of the random hyperplane-brightness formulas

Execute `python verification/check_crosspolytope_brightness.py` using Python 3.10+ and the `mpmath` library. The packaged file (not a file from any other investigation) was run successfully, reporting 117 passing checks. These include the exact gamma and finite-binomial moments in ten dimensions, nonnegative fourth-harmonic residual variance, five asymptotic variance comparisons, eighty independent direct three-dimensional convex-hull area computations and two exact closed-moment identities at dimension four.

The script computes finite mathematical identities and numerical examples. The all-dimensional formula, the sharp remainder bound and the normal limit require the analytic proof in RESULT.md and are not independently established by the checks. The pairwise folded-normal identity and the Gaussian delta method are standard mathematical ingredients; there is no machine-checked infinite certificate and no independently performed audit. Full-text access to one plausible related manuscript remains unresolved.
