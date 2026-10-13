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

The checker constructs \(\operatorname{Cr}_n\), computes all-pairs distances, and directly applies the ordered-pair solid-resolving criterion. For every \(3\le n\le9\), it enumerates every vertex subset, compares it with the complement classification, checks every coefficient of \(2z^n(1+z)^n-z^{2n}+nz^{2n-2}\), and verifies that the two bipartition classes are the only bases.

Recorded output:

```text
VERIFY_OK
parameters_n_checked = [3, 4, 5, 6, 7, 8, 9]
subset_trials = 349504
minimum_bases_checked = 14
all solid-resolving sets matched the complement classification
all coefficient distributions matched 2 z^n(1+z)^n-z^(2n)+n z^(2n-2)
all solid-metric dimensions matched n
all minimum bases were exactly the two bipartition classes
```

The finite enumeration is corroborative only; the all-parameter theorem follows from the proof.
