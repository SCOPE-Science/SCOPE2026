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

# Verification and reproducibility

The included `verify.py` checks the Taylor expansion of the scalar sine difference through sixth order, the analytic midpoint and parameter series, and both second-return multiplier series using symbolic algebra. It also directly solves the two-cycle equations at seven positive offsets from the double-flip threshold with high precision and verifies each orbit against the full three-edge map. All seven numerical cases satisfy \(0<\mu_{\parallel}<1<\mu_{\perp}\).

Reproduction: install the package named in `requirements.txt` and run `python verify.py`. The run used Python 3 with SymPy and mpmath and printed the reported PASS messages; the package is self-contained apart from those explicitly declared standard mathematical dependencies.

These computations do not prove an infinite-parameter statement. Analytic existence and uniqueness rely on the implicit-function theorem; the strict eigenvalue inequalities follow from explicit nonzero leading Taylor coefficients. The source-paper and priority comparisons are bibliographic assessments and are not tested by the verifier.
