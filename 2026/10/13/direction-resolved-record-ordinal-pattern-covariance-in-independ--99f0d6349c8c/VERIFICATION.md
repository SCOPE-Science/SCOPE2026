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

# Verification details

Run `python verify.py` with Python 3 standard library only. The checker reads no external data. It generates every permutation of size \(3\) through \(8\), directly counts upper records and every length-three ordinal type, and compares the exact covariances using rational arithmetic. It separately enumerates the joint probabilities of local pattern indicators and neighboring record events for centers \(2\) through \(7\). Expected last line:

```
VERIFY_OK exact_covariance_checks= 36 exact_joint_local_checks= 108
```

The six sums of local covariance numerators over \(i=2,\ldots,n-1\) were also checked by exact symbolic telescoping, with difference zero in all six cases. No external file or opaque certificate is required for this standalone direct finite check.

The general result is justified by the accompanying proof: nonlocal record events are independent of triple ranks, the three overlapping probabilities follow from conditional beta-uniform distributions, and six rational sums telescope. Finite checks do not establish the identities at arbitrarily large \(n\). Historical originality and physical applicability beyond iid atomless observations are outside this verification.
