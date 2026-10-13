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

The checker constructs \(\operatorname{Cr}_n\) directly as \(K_{n,n}\) with the deleted perfect matching, computes all-pairs shortest-path distances, and evaluates mixed representations for every vertex and edge. Domination is checked independently from adjacency.

For every \(3\le n\le9\), every vertex subset below the claimed dominant mixed metric dimension is tested and rejected, and every minimum set is enumerated. For \(n\ge7\), the exact family is compared with the balanced one-omitted-pair transversal classification and the closed counting formula. For \(4\le n\le6\), all size-\(n-1\) mixed bases are separately verified to be one-sided and non-dominating.

Recorded output:

```text
VERIFY_OK
crown_parameters_checked = 7
vertex_subsets_checked_for_dominant_mixed_optima = 142924
minimum_dominant_mixed_sets_checked = 3066
parameters n = 3..9
all smaller dominant mixed sets failed directly
n=3..6 values matched 3,n,n,n
n=7..9 values matched n-1
all stable minimum sets matched the one-omitted-pair balanced-transversal classification
all stable counts matched n*(2^(n-1)-n^2+n-2)
size-(n-1) mixed bases checked as one-sided/non-dominating for n=4..6 = 30
```

The finite computation is corroborative only. The all-\(n\) theorem follows from the distance-signature proof.
