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

The analytic proof, not finite enumeration, establishes the global time-map count and the exact half-wave threshold. In the two-frequency numerical check, the parameter values are \(b=1\), \(h(t)=\cos t+\tfrac18\cos(3t)\), and \(L=\pi\). These satisfy the strictly decreasing half-wave condition because \(1-3/8>0\).

The script `verification.py` uses fourth-order Runge–Kutta over one forcing period, checks the zero return displacement at the threshold and strict opposite signs on neighboring biases, and compares the observed square-root splitting with the analytic coefficient. It also checks the mirrored second orbit and local curvature. Execute using `python3 verification.py`; no third-party libraries are required.

The finite-grid integration gives numerical consistency only; it cannot certify universal quantifiers over the smooth waveform class or exclude equivalent published results. Full older-source priority comparison remains limited by access, and independent validation has not been performed.
