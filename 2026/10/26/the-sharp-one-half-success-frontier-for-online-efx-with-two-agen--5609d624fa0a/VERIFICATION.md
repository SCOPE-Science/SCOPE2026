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

# Reproducibility and independent-evidence status

Run `python3 verify_efx.py` using Python 3 and the standard library only. The checker independently evaluates the strong removal-of-any-good EFX predicate at each complete allocation rather than assuming the proof's singleton characterization. It enumerates 4096 pairs of weak nonnegative additive value triples over \(\{0,1,2,3\}\), all 36 strict ordinal profiles, 729 pairs of nonadditive normalized monotone set functions of maximum-singleton type, and the two strictly positive rational upper-bound instances.

Observed output:

```text
729 pairs of nonadditive maximum-value set functions also checked.
4096 exact weak-value profile pairs checked; minimum success >= 1/2.
Success probability distribution: [(Fraction(1, 2), 2144), (Fraction(3, 4), 856), (Fraction(1, 1), 1096)]
Strict-ranking profile distribution: [(Fraction(1, 2), 32), (Fraction(1, 1), 4)]
Both upper-bound witness instances force opposite first recipients.
ALL EXACT CHECKS PASSED
```

The exact mathematical guarantee for uncountably many real valuations is proven analytically in `RESULT.md`; finite enumeration alone could not establish it. The online policy chooses the final good only after all three singleton reports have arrived. There are no unresolved numerical approximations or external binary dependencies. Independent scientific review and validation have not been performed.
