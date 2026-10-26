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
# Verification of the rank census

Execute `python3 partial_idempotent_product_rank_checker.py` using only Python 3's standard library. The code enumerates all partial self-maps for sizes zero through five using `-1` for undefined; it selects genuine idempotents, computes all ordered compositions directly, and checks every joint rank coefficient against two independent expressions. It also checks the total number of idempotents at each size and the coefficient expressions for all allowed parameters through size fourteen.

The recorded output in `partial_idempotent_product_rank_checker_output.txt` reports 1, 4, 36, 529, 10816, 288369 ordered idempotent pairs at sizes zero to five respectively, totaling 299755. It reports 5440 independent coefficient comparisons at sizes up to fourteen. Re-running the packaged checker should reproduce the recorded output exactly.

These finite tests are not a proof of the all-size enumeration, limiting law, or literature novelty. The mathematical proof separately establishes the root-image decomposition, finite inclusion–exclusion, and the hypergeometric/occupancy concentration argument. A further independent mathematical audit has not been performed.
