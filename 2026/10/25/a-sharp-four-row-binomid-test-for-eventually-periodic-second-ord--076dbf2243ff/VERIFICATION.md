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
# Reproducibility and verification

The symbolic proof of the finite-recognition criterion and its six families is in `RESULT.md`. The checker `check.py` uses only the Python 3 standard library. Run `python3 check.py` in the same directory.

Observed checks: `PASS: all six positive/negative signed families through n=30`; `PASS: 984 second-order periodic/transient parameter cases through n=24`; and `PASS: sharpness witness: rows <= 3 integral but [4,2] = -3/2`.

The recurrence classification comes from the squarefree cyclotomic factors of the exact eventual-periodicity annihilator. The computer program verifies small instances and witness arithmetic only; it cannot establish the unrestricted infinite statement. The at-every-level implication uses published results for GCD and divisor-chain sequences; the necessary implications and sharpness are proved in `RESULT.md`. No independent mathematical audit has been performed.
