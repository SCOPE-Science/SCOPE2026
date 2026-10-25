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

The all-order results are proved by the successor permutation and transposition arguments in `RESULT.md`. The packaged `verify.py` implements two separate exhaustive finite computations: feedback-mask cycle testing and direct canonical de Bruijn-word generation, each for orders two through five. Running `python3 verify.py` produced complete agreement and the indicated passing message. The first enumerator visits all \(65536\) order-five masks; the second visits every canonical order-five cycle using the unique all-zero length-five factor. The order-five table, twelve unit weights, four double weights, exact mean and variance, and total number of cycles are checked by exact integer/rational arithmetic. An exhaustive finite calculation proves only its exact finite domain. Independent audit was not performed.
