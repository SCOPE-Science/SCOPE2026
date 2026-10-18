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

# Reproducibility and scope

Run `python3 verify.py`. This requires only Python 3 standard libraries (`fractions`, `itertools`). It checks 1120 exact fan-affine tests and 784 exact parity/genus parameter instances. Expected terminal line: `VERIFY_OK exact_fan_samples=1120 generating=203 obstruction_curves=784`.

The classifier is proved using the projective-bundle formula, the positive and negative section restrictions, all vertical toric surfaces, all invariant curves, and the toric orbit-closure test. The verifier is a finite algebraic cross-check, not an exhaustive search over integers or a substitute for the proof. Historical mathematical priority and independent external verification remain open.
