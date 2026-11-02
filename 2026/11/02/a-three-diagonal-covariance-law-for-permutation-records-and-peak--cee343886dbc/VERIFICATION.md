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

Execute `python3 verify.py` beside this file to enumerate every uniformly random permutation for \(3\le n\le8\) and check the exact mixed record–peak covariance matrix, the total covariance, and the two marginal variances. The script uses only Python's standard library and exact rational arithmetic.

The script performed 150 exact assertions across 46,230 permutations. The general result for every \(n\ge3\) is proved analytically in RESULT.md using conditioning and independence of initial ranks; enumeration does not verify an infinite domain by itself. The usual peak variance formula used for correlation is stated only for \(n\ge4\), with the three-element case treated separately.

Independent audit: not performed.
