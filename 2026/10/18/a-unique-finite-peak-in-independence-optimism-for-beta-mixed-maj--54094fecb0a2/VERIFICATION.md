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

# Mathematical verification

`verify_jury_beta.py` requires only the Python standard library. Executing `python verify_jury_beta.py` calculates binomial and beta-binomial majority probabilities as exact rational numbers, independently verifies the displayed gain-ratio formula against the quotient of direct majority-probability increments, tests the recurrence and validates the \((10,1)\) five-voter peak. The execution reported `PASS: 336 rational step and recurrence checks; 10:1 example peaks at 5`.

These finite rational checks do not establish the all-real-positive-parameter theorem. Its proof is the two-voter increment identity, Beta moment evaluation, the quadratic's unique positive root, the asymptotic ratio strictly greater than one, and the positive signed-gap limit. Shape-equality and small-jury boundaries are treated explicitly. Full independent mathematical validation remains outstanding.
