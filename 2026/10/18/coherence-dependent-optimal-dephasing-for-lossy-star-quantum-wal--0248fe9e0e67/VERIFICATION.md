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

# Reproduction

Install NumPy and SciPy, then run `python verification.py` in a directory containing this file and the companion script. The script independently forms the full matrix superoperator, tests pure and mixed leaf preparations, and compares its resolvent trace with the proposed closed formula. Its reproducible output is `PASS: 326 independent checks; max_abs=2.096e-13; max_rel=7.130e-15` with the indicated numerical environment; floating-point roundoff may vary modestly across libraries.

The mathematical proof is the finite-dimensional dissipation argument, four-equation closure, integrated identities, completion of the square, and separate zero-dephasing bright/dark decomposition in `RESULT.md`. The random numerical samples are nonexhaustive and certify neither novelty nor mathematical correctness for every parameter. No independent validation has been performed.
