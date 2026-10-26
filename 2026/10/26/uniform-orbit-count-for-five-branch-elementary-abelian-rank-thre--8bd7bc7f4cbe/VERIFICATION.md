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

## Reproducibility
Run `python check_rank3_five.py` with Python 3 and SymPy installed. It enumerates affine orbits of five-element multisets and checks the Burnside expression for primes 3, 5, 7, 11, and 13. The expected final output is `RANK3_ORBIT_OK`.

## Mathematical checks and limits
The proof is a symbolic all-prime argument using the row-space/dual identification, exactly two excluded orbit types, and the cycle decomposition of affine transformations. This checker validates small cases, not the all-prime theorem or historical originality. Independent mathematical audit has not been performed.
