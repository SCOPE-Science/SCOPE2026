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

The attached `verify.py` uses Python 3 standard-library mathematics, integrates \(du/d\theta=2(\lambda-Fu)/g\) with a fourth-order Runge–Kutta method, reconstructs \(T=\int_0^{2\pi}1/(ug)\,d\theta\), and compares against the exact period obtained analytically. It evaluates angular residence near the four slow rays and the fraction inside the unit-width Cauchy window at two positive drifts. Replaying the actual embedded file produced `CHECK_OK`. The finite checks support consistency but cannot certify limits as \(\varepsilon\downarrow0\); the analytical proof uses exact cancellation, radial comparison and tail tightness. Independent audit has not been performed.
