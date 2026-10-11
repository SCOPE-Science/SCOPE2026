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
# Reproduction and limits

Run the accompanying standard-library `verify_ratio.py` with Python 3. Its exact rational calculations establish the reported rational example and independently check the evaluation formulas at rational parameter values, including a tied maximum and the degenerate \(q=1,\rho=2\) case. The script terminates with `RANK_ONE_Q_RHO_SHARP_COMPARISON_EXACT_CHECKS_OK` when all assertions hold.

The universal assertions have a separate analytical argument in `RESULT.md`: two published rank-one formulas, strict monotonicity of the derivative sign function, evaluation of its unique zero, endpoint comparison, and a separate endpoint-parameter proof. Exact rational examples are consistency checks, not a proof for continuously many parameters or all Hilbert-space dimensions. The argument relies on the correctness of the two cited input theorems. Independent audit has not been performed.
