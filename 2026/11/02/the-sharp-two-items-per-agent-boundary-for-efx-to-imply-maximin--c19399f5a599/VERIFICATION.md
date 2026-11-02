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

# Reproducibility and limits

Run `python3 verify.py` under Python 3.9 or later. No third-party modules or network operations are required.

The verifier independently computes MMS-exceedance through an integer dynamic program: for each chosen high-good count, compute the minimum number of low goods required for all \(n\) parts to reach the integer threshold \(s+1\). It separately evaluates all positive-good deletion EFX inequalities in each foreign bundle. It enumerates all distributions of high/low good counts across the bundles for \(2\le n\le5\), \(0\le m<2n\), \(L\in\{1,2,3\}\), and \(H\in\{L+1,L+2,L+3\}\). Since same-valued goods are indistinguishable for a fixed agent, count vectors suffice for these finite tests.

Recorded output from running the exact program:

```
witness n= 2 m= 4 EFX=True own=4 MMS>=5
witness n= 3 m= 6 EFX=True own=4 MMS>=5
witness n= 4 m= 8 EFX=True own=4 MMS>=5
witness n= 5 m= 10 EFX=True own=4 MMS>=5
VERIFY_OK count_profiles= 893790 count_EFX= 305148 count_sufficient= 305148 cache= CacheInfo(hits=296767, misses=8385, maxsize=None, currsize=8385)
```

The computation is finite corroboration, not an independent formal verification of the proof. The general theorem follows from the two-case mathematical argument in RESULT.md. The example at \(m=2n\) has an exact partition with the focal bundle value \(5\) or more. No independent external audit is asserted or supplied.
