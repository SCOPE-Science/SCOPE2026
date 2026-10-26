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

# Reproduction and limits

Run `python3 verify.py` from the extracted package. It requires only Python 3 standard facilities. The program exhaustively enumerates all recurrence orbits for each modulus \(2^k\) with \(1\le k\le9\), independently checks whether the orbit ever contains a zero coordinate, computes the common dyadic depth, checks the precise quadratic congruence and expected lengths and numbers of safe/bad cycles, and asserts the total counts. The actual run returned:

```
k=1 modulus=2 zero_avoiding=0 zero_avoiding_cycles=0
k=2 modulus=4 zero_avoiding=0 zero_avoiding_cycles=0
k=3 modulus=8 zero_avoiding=24 zero_avoiding_cycles=2
k=4 modulus=16 zero_avoiding=120 zero_avoiding_cycles=6
k=5 modulus=32 zero_avoiding=504 zero_avoiding_cycles=14
k=6 modulus=64 zero_avoiding=2040 zero_avoiding_cycles=30
k=7 modulus=128 zero_avoiding=8184 zero_avoiding_cycles=62
k=8 modulus=256 zero_avoiding=32760 zero_avoiding_cycles=126
k=9 modulus=512 zero_avoiding=131064 zero_avoiding_cycles=254
VERIFY_OK: complete modular orbit enumeration through 512, dyadic norm test, periods, and exact counts
```

The exhaustive finite checks are not proofs at unbounded \(k\). The infinite theorem is proved by the integer matrix identities, exact Fibonacci zero spacing, projective counting and mod-eight lifting in `RESULT.md`. The residual scientific risk is an undiscovered mathematically equivalent precedent, particularly the uninspected full text of a 2020 paper on generalized modular Fibonacci recurrences. Independent audit is not performed.
