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

# Verification

Run \(\texttt{python3 verify.py}\) next to this file using Python 3 and its standard library. The program computes the six-dimensional Lie structure constants, constructs the ordinary tensor CYBE directly, and compares it with the proposed quadratic condition.

Actual observed output:

```text
EXHAUSTIVE_B 2 512 ZERO 256
EXHAUSTIVE_B 3 19683 ZERO 6561
EXHAUSTIVE_ALL 2 32768 CYBE 2048
COBRACKET_RANKS {2: 8, 3: 9, 5: 9}
FREE_CLASS_TWO_CYBE_QUADRIC_OK
```

The binary experiment verifies all \(2^{15}\) alternating tensors over \(\mathbb F_2\) and is an out-of-scope stress test of the direct tensor identity. The ternary experiment tests all \(3^9\) middle-block matrices, and the odd-prime cobracket-rank checks independently test injectivity. These are exhaustive only for the explicitly enumerated finite configurations. The general proof in \(\texttt{RESULT.md}\) is symbolic and applies over every field of characteristic different from \(2\); these tests are not a substitute for the infinite-field argument. No external or independent audit has been performed.
