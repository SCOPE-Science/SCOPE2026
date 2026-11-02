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

# Computational verification and proof boundaries

Run `python3 artifacts/verify.py`. The program evaluates \(\binom{x}{4}\) for every residue modulo the selected prime powers, independently constructs the image predicted by the regular balls and exceptional quadratic-square balls, and compares the complete sets and their cardinalities.

Test primes: \(7,11,13,17,19,23,29,31,37,41\). For each, all exponents from one to four with modulus at most \(120000\) are evaluated. The result recorded for the included checker is:

```text
VERIFY_OK cases=34 fully_enumerated_inputs=337286 complete_set_matches
```

For instance, the predicted and directly enumerated image sizes modulo \(7^4\) and \(11^4\) are \(708\) and \(4105\), respectively.

Finite checking does not establish the statements for all primes/exponents. The unrestricted argument requires the exact nested-square identity, the finite-field character sum, and the two Hensel/local-square descriptions supplied in the proof. The code makes no independent validation claim and does not cover the bad primes \(2,3,5\).
