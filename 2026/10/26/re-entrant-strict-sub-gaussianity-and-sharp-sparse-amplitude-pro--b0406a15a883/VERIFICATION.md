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
The finding is proved analytically for every real \(a\ge4\). The strictness witness is \(t=a\), the endpoint regimes use fourth-order Taylor control, compact continuity, and the uniform large-parameter MGF bound, while the sparse proxy is bounded above and below by expressions agreeing at first order. There is no appeal to a numerical optimizer for global strictness or to finite sampling for an infinite theorem.

The optional `verify.py` script computes exact moments, checks the analytic witness numerically at several amplitudes, and compares the analytic proxy evaluation against \(a^2/(2\log(2a^4))\). Run `python verify.py`; Python's standard library suffices. It does not independently certify the infinite statements.

Independent audit and validation have not been performed.
