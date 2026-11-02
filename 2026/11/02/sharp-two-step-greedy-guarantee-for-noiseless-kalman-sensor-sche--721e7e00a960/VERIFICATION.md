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

# Verification

Execute `python verify.py` with Python 3; no nonstandard packages are needed. The script uses exact rational arithmetic for all four schedule costs and for 20,000 reproducible parameter draws. It checks the analytic optimum, the greedy failure condition, and the claimed fixed-dynamics upper bound, then evaluates a sharpness family for squared growth factors \(1/4\), \(1\), \(9\), and \(100\). A separate floating-point test verifies strict-regret persistence at small positive measurement noise. The analytical argument in `RESULT.md`, not finite computation, establishes the universal quantifiers, exact supremum, and boundary statements. Independent audit has not been performed.
