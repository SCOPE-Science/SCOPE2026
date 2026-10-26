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

Run `python3 verification.py` with standard Python 3 (no third-party packages). The program uses fixed random seed `451019` and prints PASS only if all assertions succeed. The actual packaged program passed on the supplied runtime.

Checks include 900 finite-difference derivatives; positive-root spectral identities; pure-channel speed equivalences; 90 sampled parameter sets with nonenhancing boundary comparisons; 90 sampled enhancing cases with exact optimizer expressions and nearby alternatives; root tests for the universal minimum; and the \(R=1.5,s=0.95\) example. All resulting values are numerical approximations with floating-point tolerances, not formal interval certificates.

The proof in `RESULT.md` supplies all universal claims. In particular, positivity of tilt curvature, uniqueness of the minimizing tilt, the sign of the pure-channel comparison, uniqueness of the interior stationary allocation, and strict concavity of the universal-threshold auxiliary function do not follow from the finite tests. No independent audit, mechanized proof, or external experimental validation was conducted. Inaccessible historical literature remains a priority uncertainty.
