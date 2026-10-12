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
The theorem is proved symbolically in `RESULT.md`. The critical identities are checked there prime by prime: valuation of a least common multiple is a maximum, and the vector \((\max(v_\ell(e_i),v_\ell(\alpha)))_i\) records exactly the excess of \(v_\ell(\alpha)\) above \(v_\ell(h)\).

`verify.py` supplies finite regression checks only. It compares output exponent vectors with the normalized parameter invariant throughout the stated finite box and independently checks the closed fiber parametrization. The replay result is:

`VERIFY_OK parameter_checks=2714400 fiber_cases=7900 supports=1..4 exponent_max=12 alpha_max=120`

The finite checks do not certify the unbounded theorem and are not used to infer it. No external or independent validation has been performed.
