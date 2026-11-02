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
The standalone `verify_bst_rank_depth.py` uses only the Python 3 standard library, `fractions.Fraction`, exhaustive permutations and exact integer coefficients. Run it with `python3 verify_bst_rank_depth.py`. The successful executed output is:

```
PASS: 6,500 exact assertions; exhaustive insertion trees through n=8; recurrence and all adjacent tails through n=24; beta-binomial/record mixture through n=12
```

The independent recurrence chooses the first key uniformly and recurses into the relevant subtree; the second implementation integrates the binomial/record representation over a uniform priority; the third constructs each tree directly from every insertion order. Checks include all ranks, reflection symmetry, upper-tail signs and strictness, endpoint equalities, exact means and Wasserstein distance. Runtime arithmetic is exact; complete enumeration covers only the explicitly stated finite sizes. The all-size claim is justified separately by the proof's pairing inequality and strict positive-support witnesses. The reproducibility code makes no calls to proprietary services or unpublished resources.
