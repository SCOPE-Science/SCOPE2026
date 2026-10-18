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

The provided `verify.py` program uses only the Python 3 standard library. It directly enumerates every binary vertex subset for each tested loose hypercycle; it computes its empty/mixed/full status word from the actual hyperedges, then compares every possible status word to the closed-form transfer-product prediction. This is a separate finite implementation of the theorem's definitions, not a certificate for infinitely many parameters.

Parameters tested: \(k=3\) and \(3\le r\le7\); \(k=4\) and \(3\le r\le5\); \(k=5\) and \(3\le r\le4\); \((k,r)=(6,3)\). Total vertex subsets explicitly processed: \(161600\). The checker asserts that the all-mixed observation is uniquely largest, that precisely \(2r\) single-definite observations attain the second maximum, that every other realized fiber is smaller, that all statuses (including unrealized words) have the predicted fiber counts, and that the observation total follows the cyclic smooth-word formula. The final output ends:

```text
VERIFY_OK subsets 161600 all_status_fibers=PASS unique_maximum=PASS exact_runnerup=PASS observation_count=PASS
```

To reproduce, place `verify.py` in the current directory and run `python3 verify.py`. The exact file and its SHA-256 hash are supplied in the enclosing transport package. External proof checking has not occurred; the all-parameter result is justified by the proof in `RESULT.md`.
