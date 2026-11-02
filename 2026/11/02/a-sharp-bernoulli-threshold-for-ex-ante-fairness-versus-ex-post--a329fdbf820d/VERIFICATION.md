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

# Reproducible verification

In a directory containing `verify.py`, run `python3 verify.py` with Python 3 and no third-party packages.

The verifier separately enumerates the two agents' independent fair-binary valuations to compute the exact fraction of outcomes that are ex-post envy-free. This direct calculation is compared to the stated closed form for all \(1\le r\le10\) and all permissible ordinary-good counts \(0\le t\le r\): **65 exact combinations**. Next it independently evaluates all allocation probabilities for \(1\le r\le200\), compares the maximizing counts with the single-crossing binomial-tail rule, and tests the sharp \(r\ge3\) phase distinction: **200 complete finite parameter checks**. All comparisons use exact integer or rational arithmetic.

Observed output:

```
VERIFY_OK direct_exact_cases=65 crossing_threshold_cases=200 r3_p0=81/256 r3_p1=21/64
```

The all-parameter theorem is proved symbolically in RESULT.md; the finite checks do not certify an infinite domain or novelty. The verification does not assess external independent validation.
