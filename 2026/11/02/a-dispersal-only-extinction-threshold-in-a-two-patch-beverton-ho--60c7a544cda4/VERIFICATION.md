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

# Reproducibility and scope

Run `python3 verify.py` from the directory containing this document and `verify.py`. Only Python's standard library is needed. The executable uses exact rational arithmetic for polynomial multiplication and sign tests and independently evaluates conservative Jacobian derivative bounds on the isolated-root intervals. Successful execution prints a single `PASS` line.

The analytic argument, not the program, supplies the all-parameter positive-equilibrium existence theorem and the intermediate-value and Descartes root-exhaustion steps. The program checks every displayed rational identity and inequality needed by the specialized exact example. It does not attempt to certify uniqueness of literature priority, global basins, or arbitrary-parameter stability types.

Independent audit: not performed.
