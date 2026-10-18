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

The stationary law of the source is used as an explicit premise. The run multiplicities, frozen-state exclusion, rational current identity, strictly positive deficit polynomial, summable-domination argument and Bessel derivative identity are proved in RESULT.md.

Reproducibility: run `python3 verify.py`. This tests the weighted stationary Markov-generator balance for all combinations of \(4\le N\le11\), \(2\le K\le N-2\), \(q\in\{1/3,3,7/2\}\); independently enumerates stationary current and run distributions for \(q\in\{1/3,1,5,17/2\}\); and compares exact decimal finite-ring scaled deficits against a Bessel-series prediction for five parameter pairs. Exhaustive checks cover only the stated finite rings. The analytical proof, not finite enumeration, establishes the all-size claim and asymptotic law.

Primary scientific limitation: results hold only for the active recurrent class at fixed positive particle and vacancy densities. Independent audit has not been performed.
