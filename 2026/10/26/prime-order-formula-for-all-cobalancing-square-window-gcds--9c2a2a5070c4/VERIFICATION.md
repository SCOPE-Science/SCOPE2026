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

# Reproducibility

Run the accompanying standalone `verify.py` with Python 3. The program uses no external modules, reports the actual exact-arithmetic consistency checks, and raises an assertion if a check fails. It evaluates first-window sums directly for window lengths through 350; for 351 through 2500 it checks the proposed result against the GCD of twelve shifted sums together with the modulus 40 times the length. It also tests the exact dyadic-block congruence, the quadratic-unit powers, and the exceptional prime orders.

The computer program is finite verification, not a proof of the infinite prime-by-prime formula; that proof is in RESULT.md. No independent audit has been conducted.
