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

Run `python3 verify.py` with Python 3's standard library. The script computes the pentagonal constants to 85 decimal digits from radicals, tests the positive support-weight cancellation, four active facet identities, fifth-facet slack factorization and area equality on 1,001 orientations, and independently performs 50,000 seeded random rectangle containment checks. In the executed package preparation the output was:

```text
DECIMAL_SUPPORT_CHECKS 12012 MAX_AREA 1.624598481164532
VERIFY_OK sampled_rectangles=50000 feasible= 27961
```

For universal validity, the proof is the exact four-facet support inequality, the positive weighted AM–GM argument, the explicitly nonnegative fifth-facet slack and the analytic sine comparison. The sample and high-precision decimal checks support the algebra but are not infinite proofs or an independent audit. The geometry is proved for every circumradius greater than zero and all rectangle orientations. There is no assertion of historical priority over unidentified sources.
