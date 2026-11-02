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

# Verification and reproducibility

Run `python3 verify.py` with standard Python 3 from the directory containing this file and `verify.py`.

Recorded output:

`VERIFY_OK fixed_sets=4 exact_sum_cases=867 even_offsets_for_3_5_19=82`

The program constructs the prime list with a sieve, computes minimum products for each exact target sum using a descending distinct-prime dynamic program, independently enumerates finite even offsets from sets with smaller products, and checks the equivalence for four fixed minimum-product sets and 867 prime extensions. It separately asserts explicit small offset sets. All calculations use exact integers.

The code checks only finite examples (many below the stated sufficient threshold). The general equivalence is proved mathematically in `RESULT.md`. The quantitative density statement additionally invokes the classical Selberg-sieve upper bound for prime pairs separated by any fixed nonzero even integer. No general independence or third-party mathematical audit has been performed.
