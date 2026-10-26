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

# Reproducibility and limits

The included `verify.py` uses only the Python standard library. Run `python verify.py` from the directory containing this file and the checker. It enumerates every independent-parent recursive tree through order nine, verifies that conditional deletion produces exactly one outcome per shorter-tree/attachment-parent pair, and checks the full marked covariance formula and summed covariance using `fractions.Fraction`. It then checks the unique minimizing birth label and exact harmonic threshold for orders three through three hundred.

Recorded output:

```
EXHAUSTIVE_MARKED_LEAF_BIJECTION_PASS 2 trees= 1
EXHAUSTIVE_MARKED_LEAF_BIJECTION_PASS 3 trees= 2
EXHAUSTIVE_MARKED_LEAF_BIJECTION_PASS 4 trees= 6
EXHAUSTIVE_MARKED_LEAF_BIJECTION_PASS 5 trees= 24
EXHAUSTIVE_MARKED_LEAF_BIJECTION_PASS 6 trees= 120
EXHAUSTIVE_MARKED_LEAF_BIJECTION_PASS 7 trees= 720
EXHAUSTIVE_MARKED_LEAF_BIJECTION_PASS 8 trees= 5040
EXHAUSTIVE_MARKED_LEAF_BIJECTION_PASS 9 trees= 40320
EXACT_UNIQUE_AGE_OPTIMUM_PASS n=3..300
VERIFY_OK
```

Enumeration is finite evidence only. The uniform conditional deletion coupling and the parity proof of uniqueness in `RESULT.md` are the unrestricted proof. Prior work determines the unmarked leaf-count/path-length joint generating function, but the stated theorem is birth-indexed. No independent audit has been undertaken.
