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

Run `python3 verify.py` in the same directory as the six research files; no nonstandard Python packages or network access are required. The script reports `VERIFY_OK 6099`.

The script compares the actual \(s\)-stage undamped RKC recurrence with a separately coded Chebyshev recurrence across rational step parameters, stages, and both sampled curvatures. It checks exact rational binomial enumeration of all sample patterns at finite horizons against the closed-form second-moment factor; checks the strict-outlier stability boundary algebraically; and confirms an exact family of odd-stage roots and the rational \(s=3\), \(\kappa=3\) witness. Floating-point comparisons are used only for selected asymptotic numerical diagnostics.

The complete infinite-time and all-real-parameter result relies on the mathematical proof in RESULT.md, including the Chebyshev identity, iid product law, strong law, Jensen inequality, and asymptotic expansion. Finite computations are not treated as exhaustive proof. The result assumes exact arithmetic, undamped coefficients, fixed macrostep and common-within-macrostep random curvature; no independent validation has been performed.
