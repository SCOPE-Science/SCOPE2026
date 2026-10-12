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

The verifier constructs the crown graph \(\operatorname{Cr}_n\), computes all-pairs graph distances by breadth-first search, truncates them according to
\[
d_k(x,y)=\min\{d(x,y),k+1\},
\]
and tests both distance-\(k\) resolution and distance-\(k\) domination directly.

For every \(5\le n\le8\) and \(k\in\{1,2,3\}\), it checks every candidate of size at most \(n-1\). Every smaller set fails, and every size-\(n-1\) set is compared with the structural theorem.

Recorded output:

```text
VERIFY_OK
crown_parameters_checked = 4
parameters n = 5..8
distance_ranges_checked = 1,2,3
subset_trials = 104343
minimum_bases_checked = 4884
all smaller sets failed
all minimum sets matched the structural classifications
k=1 counts matched n(2^(n-1)-2n)
k>=2 counts matched n*2^(n-1)
```

The finite enumeration is corroborative only. The theorem for all \(n\ge5\) and all \(k\ge1\) follows from the proof.
