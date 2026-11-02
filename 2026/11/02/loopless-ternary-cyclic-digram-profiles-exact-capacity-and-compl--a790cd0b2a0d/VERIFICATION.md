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

Run `python3 verify.py` using standard Python 3 from the directory containing this file. The program constructs every cyclic proper-coloring word through length 16, computes its directed six-coordinate profile literally (including the wraparound read), canonicalizes only under rotation, and counts profiles and singleton necklaces. Independently it enumerates flow parameters through length 100 and compares the predicted counts with direct finite sums. It checks all individual observed profile singleton classifications, not just aggregate counts.

Observed output of the packaged script:

```text
VERIFY_OK cyclic_words_checked=131070 profile_classes_checked=506 singleton_classes_checked=127 lengths=2..16 flow_lengths=1..100
EXAMPLES [(2, 3, 3), (3, 2, 2), (4, 6, 6), (5, 6, 6), (6, 12, 11), (7, 12, 6), (8, 21, 15), (9, 22, 8), (10, 33, 9), (11, 36, 12), (12, 50, 11), (13, 54, 6), (14, 72, 15), (15, 78, 8), (16, 99, 9)]
```

The infinite claim follows from the connected balanced-flow parametrization, the two-switch witness operation, exact cyclic-excursion descriptions and disjoint rational generating functions in `RESULT.md`. A finite program cannot replace those arguments. Checks involve deterministic integer arithmetic; no random inputs or external dependencies. Claims about scientific novelty still carry residual literature risk. Independent audit is not yet performed.
