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

# Reproducibility checks

Run `python3 verify_pascal_second_min.py` using Python 3's standard library; no external packages are required. The verifier separately counts nonzero binomial coefficients using digitwise borrow-state transitions and exact integer binomial arithmetic. It checks 84 complete row intervals containing 138920 row indices and 3680 direct binomial evaluations, including exact second-minimum and complete equality sets for every tested parameter tuple.

Expected final line:

`CHECK_OK full_intervals=84 counted_rows=138920 direct_binomial_checks=3680`

Finite experiments do not establish the infinite universal theorem; the all-parameter proof is in RESULT.md. No independent mathematical audit has been performed.
