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

The closed-form counting recurrence, exact weighted automaton and Perron–Frobenius argument are in `RESULT.md`. Run `python3 verify.py` with Python 3.8 or newer; the expected final marker is `VERIFY_OK`. The current finite tests check 507 exhaustive histograms against dynamic-programming and recurrence counts, plus finite primitivity witnesses. They do not prove the central limit theorem.

The critical infinite assertions checked analytically are the integer–word bijection, positivity of a power of the period transfer matrix, analytic simplicity of the Perron eigenvalue, and strict positivity of the additive-reward variance by a pair of incompatible closed walks. There is no claim of independent audit or external certification.
