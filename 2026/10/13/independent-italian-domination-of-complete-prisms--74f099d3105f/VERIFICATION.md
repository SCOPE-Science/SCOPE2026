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

The verifier constructs the complete prism directly from two \(n\)-cliques joined by a perfect matching.

For each ternary labeling it independently checks:
1. no two positive-labeled vertices are adjacent;
2. every zero-labeled vertex has neighborhood-label sum at least \(2\).

It exhausts all labelings for
\[
2\le n\le6,
\]
and compares the entire feasible set with the theorem for every \(n\ge3\) in that range.

Recorded output:

```text
VERIFY_OK
n=2: feasible=8, i_I=2, minima=2
n=3: feasible=6, i_I=4, minima=6
n=4: feasible=12, i_I=4, minima=12
n=5: feasible=20, i_I=4, minima=20
n=6: feasible=30, i_I=4, minima=30
ternary_labelings_checked = 597861
construction_checked_n = 3..50
for every exhaustive n>=3, all feasible functions matched the ordered anti-matching 2-2 classification
```

The construction check then generates all \(n(n-1)\) predicted labelings and tests the original definition for every
\[
3\le n\le50.
\]

The finite checks do not prove the theorem for arbitrary \(n\). The all-orders result follows from the symbolic argument that positive-support independence permits one positive vertex per clique layer, cross-layer independence forbids a matching pair, and a third index forces both surviving positive labels to equal \(2\).
