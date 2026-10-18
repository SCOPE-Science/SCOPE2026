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

Run `python3 verify_period_doubling.py` with Python 3 (standard library only). A completed direct run returned:

```
VERIFY_OK independent_generation=262144 dyadic_scales=10 other_even_lengths=63
```

The script independently constructs the first 262,144 bits both from the substitution and the parity of the exponent of two dividing the index plus one. It counts every length-three factor with independent sliding counters for even lengths \(4,6,\ldots,128\) and at dyadic lengths \(8,16,\ldots,4096\). For all checked even lengths, complete frequency signatures correspond bijectively to the triple of ones count and two-symbol endpoints. For each checked dyadic length at least 16, it also checks that all exactly twelve predicted signatures and no others occur, as well as the explicit formula for the 101 count.

Reconstruction identities, the base witnesses, and the substitution induction in RESULT.md—not these finite checks—establish the theorem for all claimed lengths. The finite sample does not prove the factor language is exhausted beyond the checked prefixes. No independent scientific audit was performed.
