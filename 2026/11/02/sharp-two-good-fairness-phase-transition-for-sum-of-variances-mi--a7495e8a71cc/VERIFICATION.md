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

# Verification notes

The analytical proof gives a complete extreme-point description and independently compares every candidate. Strict concavity of the transition polynomial-rational function proves a unique phase boundary for every admissible first-agent parameter. The bundled `verify.py` uses exact rational Gaussian elimination to enumerate polytope vertices from all 20 active sets, then checks moment formulas and the explicit rational witness.

Executed command: `python3 verify.py`

Observed output: `VERIFY_OK exact_parameter_pairs=330 active_sets_per_pair=20 witness_t=5/6 fair_variance=17/100 risky_variance=13/80`

The finite grid tests do not establish the theorem for all real parameter pairs; the displayed algebraic proof supplies the universal argument. Neither an external audit nor independent formal validation has been performed.
