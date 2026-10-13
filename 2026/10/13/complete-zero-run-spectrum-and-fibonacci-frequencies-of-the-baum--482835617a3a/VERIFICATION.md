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

# Reproduction and limits

Run `python3 verify.py` in the directory containing `verify.py`, using Python 3 without third-party packages. Expected output:

```
VERIFY_OK direct_terms=262144 dyadic_cutoffs=18 symbolic_central_boundaries=12 exact_counts=all
```

The program compares the direct binary-zero-block predicate and the recurrence for all positions less than 262144. For each dyadic prefix through the eighteenth it computes the complete histogram of spacings between consecutive ones, compares every count with the closed Fibonacci formula, and checks the total. For suffix lengths two through thirteen, it enumerates admissible strings and independently confirms each central inter-group gap.

Finite enumeration supplies reproducibility and catches boundary and indexing errors but is not a proof of the infinite claim. The infinite spectrum and frequencies follow from the explicit token-language decomposition, exact recursion-tree gap count, and Fibonacci asymptotics in RESULT.md. No independent external audit has been performed.
