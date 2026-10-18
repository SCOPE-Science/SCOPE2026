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

The full finite-dimensional proof is given in RESULT.md. To replay the exact computations, run `python3 verify.py` in the unpacked package directory, with SymPy installed. The checker verifies the exact algebraic fourth-norm reduction, stationary resultant and linear subresultant, rational sign interval for the unique positive algebraic root, and the uniform rational positivity gap for the explicit every-radius witness. It then evaluates the root at high precision to print the reported numerical norm. The output is `VERIFY_OK ...`. It does not attempt to certify an infinite parameter range by enumeration; that follows from the displayed convexity and polynomial arguments. This is not an independent audit.
