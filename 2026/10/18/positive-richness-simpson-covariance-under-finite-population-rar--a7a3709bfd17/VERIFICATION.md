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

The exact all-population proof appears in `RESULT.md`. The accompanying standalone program `verify_rarefaction_covariance.py` requires Python 3.10 or later and only standard-library dependencies. Execute `python verify_rarefaction_covariance.py`; its deterministic JSON output is `verification_certificate.json`.

The program checks all 270 positive-integer abundance partitions of census sizes 2 through 12 and all 2,375 feasible sample depths. It compares three independent exact-rational calculations (labeled subset enumeration, hypergeometric composition enumeration, and the claimed closed formula), verifies the explicit nonnegative lower bound, and tests the exact strictness/zero conditions. All checks pass, including 1,891 positive and 484 zero covariance instances.

The enumeration through twelve individuals cannot prove an all-population statement; that claim rests on the conditional-pair calculation, algebraic symmetrization, and monotonicity of absence weights. No independently performed audit or mathematical certification is asserted.
