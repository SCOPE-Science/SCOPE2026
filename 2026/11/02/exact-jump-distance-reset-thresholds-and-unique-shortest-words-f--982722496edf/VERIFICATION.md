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

Run `python3 verify.py` with Python 3.9 or newer. The script requires no third-party modules and constructs the subset transition graph directly from the letter definitions. For each pair with \(2\le n\le11\) and \(1\le d<n\), it computes the exact shortest reset length and the number of words attaining it by breadth-first search, testing both coprime and noncoprime cases. It also checks the constructed word for all coprime \(12\le n\le100\).

Expected completed output:

```
VERIFY_OK exhaustive_n=2..11 cases=55 sync=41 nonsync=14 witness_n=2..100 shortest_word_multiplicity=1
```

This finite test detects implementation errors or low-parameter counterexamples; the all-integer assertion is established by the proof in `RESULT.md`, not by exhaustive code. No external or independent scientific audit has been conducted.
