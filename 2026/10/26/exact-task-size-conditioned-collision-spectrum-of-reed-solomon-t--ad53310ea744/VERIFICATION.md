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

The standalone checker `verification/verify.py` uses only Python's standard library and integer/fraction arithmetic. Its independent direct enumeration over prime fields 2, 3 and 5 checks 113 complete small parameter grids, comparing the histogram, mean, variance, sharp maximum, and unsaturated maximizer population with the stated formulas. It reports `VERIFY_OK` when successful. The included `verification/output.txt` records one execution. This finite check is not a substitute for the polynomial interpolation, combinatorial inversion, or asymptotic arguments in `RESULT.md`.

The analysis assumes a uniformly selected set of *distinct* positive messages, conditioned on a fixed negative query, with a uniformly selected evaluation point and a noiseless channel. The comparison with deterministic task-specific errors and prior support-enumerator literature is limited as described in the result. Independent assessment is not claimed.
