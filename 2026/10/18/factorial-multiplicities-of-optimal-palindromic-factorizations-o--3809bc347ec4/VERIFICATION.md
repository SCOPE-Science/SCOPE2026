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

# Verification scope

The attached `verify.py` uses only the Python 3 standard library. Run it with:

```sh
python3 verify.py
```

Expected successful terminal prefix:

```text
VERIFY_OK ruler_Zimin_optimal_palindrome_factorizations
```

The verifier generates the actual ruler/Zimin symbols from two-adic valuation rather than from the claimed predecessor formula. It enumerates **all** palindromic intervals of its first \(65{,}535\) symbols by expanding around each possible center, including even centers. Using these intervals, a dynamic program computes for every prefix its minimum palindromic length and the count of optimal cut chains, with arbitrary-precision integer arithmetic. It separately checks the exact histogram of binary run counts for all indices below \(2^{16}\) and checks large-integer run changes for random binary integers up to 256 bits. The independently computed checks have succeeded with the following counts:

```text
VERIFY_OK ruler_Zimin_optimal_palindrome_factorizations exhaustive_prefixes=65535 palindrome_occurrences=524288 dyadic_histogram_levels=16 large_integer_bit_transition_checks=254553
```

The center-expansion and DP tests are finite evidence, not an exhaustive check of all prefix lengths. The mathematical proof in `RESULT.md` establishes the all-length theorem. The reported review is internal self-review; no independent scientific audit has been carried out.
