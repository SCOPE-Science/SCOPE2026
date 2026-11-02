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

Run `python3 verify.py` with Python 3.9 or later and no third-party packages. The verifier directly calculates every length-three scattered-subsequence vector by a dynamic program, enumerates all length-\(z+3\) words with exactly three \(1\)'s for every integer \(0\le z\le15\), and compares the resulting classes to the asserted parameterized involution and generating-function coefficients. Actual checked output:

```
VERIFY_OK zeros=0..15 words=3876 classes=3590 doubletons=286 signature_class_partner_and_gf=TRUE
```

All 3,876 words and 3,590 corresponding classes are examined, with every class size tested to be at most two. The coefficient check uses a direct sum over the nonnegative integer parameters and compares it to actual class counts. The infinite proof is mathematical, not inferred from these finite checks. Published claims of higher-weight equivalence classification or independent external validation are **not** made.
