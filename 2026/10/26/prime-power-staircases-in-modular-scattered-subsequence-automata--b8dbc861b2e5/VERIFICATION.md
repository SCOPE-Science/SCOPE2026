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

# Reproducibility

From the directory containing `verify.py`, run `python verify.py` with Python 3. The program uses only the standard library. It computes prime-power periods directly, builds the full finite transition graph, minimizes it by repeated partition refinement for every target residue, and checks the formula for 44 prime/exponent pairs. It separately enumerates 85,995 binary words and checks the state invariant against direct scattered-subsequence counts. Finally, it evaluates Lucas-support translation rigidity for extra prime/exponent ranges. The observed terminal line was:

```
VERIFY_OK minimal_automata 44 direct_words 85995
```

No finite enumeration proves the all-parameter claim. The source-level argument for arbitrary primes and lengths is in `RESULT.md`; the verifier tests bounded cases and the package's computation paths only. All reported checks are local and do not constitute independent or formal certification.
