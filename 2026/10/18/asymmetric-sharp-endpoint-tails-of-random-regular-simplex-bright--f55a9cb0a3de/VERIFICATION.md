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

The exact claim follows from the proof in `RESULT.md`, not the output of numerical sampling. `check_brightness.py` independently forms random directions by centering standard Gaussian vectors, checks brightness bounds and the exact spherical-cap probability for dimensions \(m=3,4,5,6,8\), and checks the upper leading coefficients by quadrature. The deterministic proof resolves the behavior for every fixed integer \(m\ge3\); finite tests do not establish that quantifier. Source comparisons and scientific limitations are reported in `REVIEW.md` and `AUDIT.json`. No external/independent audit has been performed.
