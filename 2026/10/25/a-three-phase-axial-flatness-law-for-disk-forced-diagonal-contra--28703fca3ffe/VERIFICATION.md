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

# Reproducibility and verification

The companion standard-library-only `check_axis_contact.py` can be executed using `python3 check_axis_contact.py`. The checker evaluates finite truncations of the exact support-point formula and avoids catastrophic cancellation in the contact deficit. It tests positive rational diagonal parameters in all three regimes, the power exponent at an explicit rational example, the convergence of the logarithmic correction, and the positive-curvature coefficient. It terminates with a PASS count of 22 finite assertions on the tested environment.

The **proof**, not the test script, establishes the asymptotics as limits. In particular, the geometric head/tail estimates at the critical line and the weighted Cauchy–Schwarz inequality in the power-flat regime require infinite-series reasoning not certified by numerical truncation. Every model assumption, quantifier and asymptotic domain appears in RESULT.md. No independent audit has been conducted.
