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

# Verification details

The exact moment formula and Mittag–Leffler kernel are derived from polar integration of the normalized measure. The local-limit computation uses the sectorial kernel expansion and the quadratic identity giving coefficient \(\alpha p^2\) in the exponent. A global intrinsic-metric bound from Borichev–Fantolini–Youssfi, arXiv:2610.33937v1, controls the tails needed for strong \(L^2\) convergence; that input is attributed rather than independently reproduced.

A compact smooth planar wave packet has Fourier-multiplier error at most \(\sqrt\pi\|\nabla\chi\|_2/(2Lp\sqrt\alpha)\). The diagonal choice of its dilation center is made separately for each packet, and the compactness argument requires weak convergence to zero. The endpoint multiplier zero follows by sending the envelope frequency to infinity.

`CHECK.py` uses the exact kernel series, numerical gamma moments, Fourier integrals, and an independent scalar maximization. It reports `CHECK_OK 67`. These are finite numerical checks only, not infinite-dimensional certification. The result is subject to independent mathematical audit, which has not been performed.
