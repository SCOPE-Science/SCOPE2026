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

Executed the included standard-library Python checker by extracting the included file content and running \(\texttt{python check.py}\). It enumerated every matching for \(n=2,3,4,5,6\), including 10,395 matchings at \(n=6\). It compared direct crossing-count distributions weighted by falling factorials of the number of cyclic simple chords with the exact smaller-diagram law for every admissible factorial order. It also checked the exact crossing mean and variance, simple-chord mean and variance, and their covariance. **266 exact rational assertions passed.**

Proof-dependent limits: the joint independence theorem is not inferred from finite enumeration. Its inputs are the already established Gaussian crossing limit, exact conditional deletion for all finite sizes, mixed-factorial convergence, tightness, and probability-generating-function uniqueness. No numerical experiment certifies uniformity in an unbounded factorial order or gives a convergence rate. Independent mathematical auditing remains not performed.
