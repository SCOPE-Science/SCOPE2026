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

Execute `python verify_biclique.py` in a standard Python 3 environment (standard library only). The recorded execution printed:

```
PASS matching_subsets= 58546 positive_profiles= 11100 negative_obstructions= 116
```

The matching loop exhaustively checks every remaining-vertex subset of size at most the smaller bipartition size for \(1\le a\le6\), \(a\le b\le10\). The construction tests 60 independent profiles at every high-band agent count in that range, with nonnegative integer singleton values and extra positive pair-complementarity values (a subclass of nonadditive monotone functions). The negative tests confirm the strict capacity inequality in the middle interval.

The mathematical proof is complete for **all** positive integer part sizes and all admissible agent numbers; no finite sample is used as a proof of infinitely many instances. The publication-priority literature check has a residual risk from a related paper whose full text was unavailable. No externally certified verification is claimed.
