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

# Reproducibility and verification

Run `python verify.py` using Python 3 standard library. It directly enumerates fixed-content words and unordered source multisets, constructs the actual multiset of literal longest prefix/suffix reads and counts the number and cardinality of inverse fibers, checks these values against the generating-function coefficients, and counts even rotation orbits directly without using the Möbius formulas. The tested range includes two, three and four labeled symbols, length at most eight, six and five respectively, and pool sizes at most three, three and two respectively. Empty pool size is included.

The expected summary from the actual checks is:

```
VERIFY_OK composition_pool_cases=687 source_multisets=602425 alphabets=2,3,4
```

Further printed examples include content `(1, 1, 2)` with even cycles `{4: 3}` and profile/singleton pairs `(75, 72)` at pool size two, and content `(2, 2, 2)` with even cycles `{6: 14}` and pairs `(125566, 125552)` at pool size three.

This enumeration is finite corroboration only. All-length correctness relies on the independent read-incidence decomposition, alternating-kernel argument, orbit enumeration and first-ambiguity proof supplied in `RESULT.md`. No formal proof assistant, independent scientific review or noisy-channel experiment is claimed.
