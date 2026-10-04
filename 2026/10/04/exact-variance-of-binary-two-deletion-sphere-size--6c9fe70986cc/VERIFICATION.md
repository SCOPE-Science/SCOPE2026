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
The theorem is proved symbolically in `RESULT.md`. The executable check is corroborative and uses no external packages.

`verify.py` performs three checks. First, for every binary word with \(2\le n\le12\), it constructs the set of distinct length-\(n-2\) descendants by literal deletion of every index pair. Second, it independently evaluates the run statistic \(\binom{R+1}{2}-2I-E\) and requires exact equality word by word. Third, for each \(n\) in the exhaustive range it computes the empirical mean and variance as rational numbers and compares them with \((n^2+n+2)/8\) and \((n-1)(n-2)(2n-3)/32\). It then checks the Walsh-sum simplification algebraically through \(n=200\).

The finite enumeration is not an exhaustive proof for unbounded \(n\); the infinite proof is the boundary-indicator/Walsh argument. No claim is made beyond uniform binary centers and two deletions.
