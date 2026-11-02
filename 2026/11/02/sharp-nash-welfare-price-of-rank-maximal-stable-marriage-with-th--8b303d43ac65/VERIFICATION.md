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

Run both standalone Python 3 programs:

```text
python3 verify_rank_price.py
python3 verify_rank_price_alt.py
```

Both rely solely on the Python standard library. Each must report the same full finite census. The first additionally proves the explicit two-stable-matching maximum-price witness by exhaustive testing of its six possible matchings; the second uses an independently structured base-six traversal and pairwise-edge score factors. All counts are integer and every ratio is an exact reduced fraction, not a floating-point estimate.

The two-pair theorem follows directly from the utility product identity, separately from the finite verifier. For three pairs, the explicitly complete verification procedure is the finite proof. No assertion is made for larger market sizes or altered preferences. No independent scientific audit has been performed.
