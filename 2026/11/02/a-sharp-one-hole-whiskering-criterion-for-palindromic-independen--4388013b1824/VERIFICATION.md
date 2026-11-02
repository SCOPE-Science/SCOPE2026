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

# Verification record

The accompanying `verify.py` is a standalone Python 3 standard-library script. Run `python verify.py` in the folder containing this document and the verifier. The observed run output was:

```
ALL_LABELED_CHECK 5044 CLIQUE 2570 NONCLIQUE 2474
LITERAL_BRUTE_FORCE_CHECK 244
LARGER_RANDOM_CHECK 5167
VERIFY_OK
```

The deletion-recurrence polynomial computation uses the actual constructed graph and is separate from the combinatorial proof. For labelled bases with two through five vertices, it tests every graph and every distinguished vertex with at least one neighbor. A second brute-force path counts literal independent vertex subsets in smaller graphs. Larger checks use a fixed pseudorandom seed and base sizes six, seven and eight. Tests verify the top coefficient and degree, exact next-to-top deficit, palindrome criterion and full gamma formula where applicable. No finite search is treated as proof for all orders. The correctness proof is in `RESULT.md`. Independent mathematical assessment has not been performed.
