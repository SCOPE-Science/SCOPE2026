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

The symbolic proof is given in RESULT.md. The included `verify.py` uses two independent exact enumeration methods: all preference sequences at small sizes and admissible multiplicity vectors using multinomial weights at larger sizes. It compares the complete bivariate coefficient table with the proposed formula, rational covariance values, and finite stochastic-regression inequalities. Invocation: `python3 verify.py`. Recorded result: `VERIFY_OK 5026`.

The tests are finite corroboration only. The formula for every admissible size follows from the weight-preserving bijection and the preexisting single-value parking-function enumerator; the covariance and limiting distribution follow analytically. Historical novelty is subject to independent scrutiny. No independent audit has been performed.
