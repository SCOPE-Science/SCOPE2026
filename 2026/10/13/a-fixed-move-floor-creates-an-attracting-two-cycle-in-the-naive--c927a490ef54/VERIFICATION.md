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

The exact verifier `verify_counterexample.py` uses rational arithmetic. It checks:

- the initial unique linear-minimization vertex and initial clipping inequality;
- the endpoint inequalities proving that the negative and positive rectangles map into each other;
- strict lower bounds for both unclipped coefficients relative to \(9/10\);
- strict negativity of the selected stopping quantity on both invariant rectangles;
- the exact two-cycle \((28/19,-50/19)\leftrightarrow(29/19,50/19)\);
- the exact two-step factor \(81/100\).

The verifier returned `VERIFY_OK` from the packaged path. The infinite nontermination statement does not rely on iterating a finite number of steps: it follows from the analytic invariant-region proof. No independent audit has been performed.
