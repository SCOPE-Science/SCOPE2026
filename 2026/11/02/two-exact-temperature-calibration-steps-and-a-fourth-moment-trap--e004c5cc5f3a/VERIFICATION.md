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

# Verification record

Run `python verify.py` after installing the dependency in `requirements.txt`. The checker symbolically derives the exact rRKN position update from the two force evaluations, evaluates the beta-distributed stage moments, verifies both calibration roots and the fourth-moment classification, checks rational values of the stationary covariance recurrence, and compares a seeded stationary simulation at the smaller calibration root. The final source executed with `PASS: 245 checks; numerical variance 1.003265; harmonic stability root 7.0367846180`.

The tests are finite and cannot substitute for the exact stationary contraction proof, characteristic-function non-Gaussianity, or fourth-moment impossibility argument. All independent external audit channels remain unperformed.
