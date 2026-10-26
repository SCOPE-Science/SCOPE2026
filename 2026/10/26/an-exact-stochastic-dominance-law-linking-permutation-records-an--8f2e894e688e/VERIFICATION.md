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

# Verification evidence
The included `verify.py` can be executed directly with a recent standard Python 3 interpreter: `python verify.py`. No third-party packages are needed. It determines ordinary permutation cycle counts from one-row permutations, independently tests every upper-record indicator and tabulates the joint statistics using exact integers and `fractions.Fraction`.

The exact full enumerations cover each permutation of size 1 through 8, and compare the unconditional and every conditional cycle-count coefficient, every integer threshold of their signed tail difference, and the covariance formula at every position. The checker additionally verifies the independent conditional generating-function recurrence through size 35. Its successful run prints:

```
EXHAUSTIVE_PASS n=1 permutations=1 marked_positions=1
EXHAUSTIVE_PASS n=2 permutations=2 marked_positions=2
EXHAUSTIVE_PASS n=3 permutations=6 marked_positions=3
EXHAUSTIVE_PASS n=4 permutations=24 marked_positions=4
EXHAUSTIVE_PASS n=5 permutations=120 marked_positions=5
EXHAUSTIVE_PASS n=6 permutations=720 marked_positions=6
EXHAUSTIVE_PASS n=7 permutations=5040 marked_positions=7
EXHAUSTIVE_PASS n=8 permutations=40320 marked_positions=8
EXACT_PGF_RECURRENCE_PASS n<= 35
VERIFY_OK
```

**Limits.** The finite calculation does not prove validity for arbitrary size. The cycle-insertion recurrence, solution and telescoping argument in `RESULT.md` provide the unrestricted proof. This verification is neither an independent audit nor an external mathematical certification.
