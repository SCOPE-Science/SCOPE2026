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

The standalone `verification.py` uses exact integer calculations and no third-party libraries. Run `python3 verification.py`; it checks the transfer-matrix scalar-power identity, 234 instances of the sign formula, direct enumeration of invariant faces in small cases, and mod-two augmented simplicial homology in 34 further path instances. Successful execution prints `PATH_HIGHER_INDEPENDENCE_REFLECTION_VERIFIED 234 34`.

The full proof uses the published homotopy theorem and symbolic recurrence; finite calculations do not constitute exhaustive verification of the infinite family. Independent mathematical audit has not been performed.
