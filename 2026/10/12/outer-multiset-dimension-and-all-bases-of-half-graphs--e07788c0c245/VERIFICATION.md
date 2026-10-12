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

The checker constructs \(H_n\) for
\[
2\le n\le10.
\]
It computes all-pairs shortest-path distances. For every candidate set of size \(n-2\) and \(n-1\), it forms the sorted distance multiset from each outside vertex and tests pairwise distinctness.

The direct result is compared with the shifted-pair classification
\[
W_T=\{a_{k+1}:k\in T\}\cup\{b_k:k\notin T\}
\]
and the odd-order balanced exclusion.

Recorded output:

```text
VERIFY_OK
n=2: outer_multiset_dimension=1, bases=2
n=3: outer_multiset_dimension=2, bases=2
n=4: outer_multiset_dimension=3, bases=8
n=5: outer_multiset_dimension=4, bases=10
n=6: outer_multiset_dimension=5, bases=32
n=7: outer_multiset_dimension=6, bases=44
n=8: outer_multiset_dimension=7, bases=128
n=9: outer_multiset_dimension=8, bases=186
n=10: outer_multiset_dimension=9, bases=512
candidate_subsets_checked = 395691
all bases matched the shifted-complement classification
```

The checker examines \(395{,}691\) candidate subsets. The finite computation is corroborative only; the arbitrary-order result follows from the cumulative-count proof.
