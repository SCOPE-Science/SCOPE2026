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

# Verification and proof limits

Execute `python3 verify.py` with Python 3. The script independently enumerates every nonempty contiguous factor, constructs candidate minimal absent words by overlapping one-letter deletions, and compares the resulting sets to the explicit mathematical classification. It tests all \(4096\) positive quadruples \((a,b,c,d)\) with \(1\le a,b,c,d\le8\). It additionally compares predicted maxima for every length \(4\le n\le21\) with direct parameter enumeration and compares full bivariate coefficients for \(4\le n\le17\) with a separate pairwise enumeration.

The observed output from the extracted standalone program was:

```
VERIFY_OK: exact minimal-absent sets on 4096 parameter quadruples; sharp maxima at 18 lengths; full bivariate counts through length 17
```

The mathematical infinite-parameter proof is in `RESULT.md`, Steps 1–7. The finite program cannot establish universality for unbounded run lengths or publication priority. No independent audit has yet occurred.
