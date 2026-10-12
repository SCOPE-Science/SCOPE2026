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

The checker constructs every complete split graph
\[
S_{m,n}=K_m\vee\overline{K_n}
\]
with
\[
1\le m,n\le6.
\]

For each graph it computes all-pairs shortest-path distances by breadth-first search. It then enumerates every vertex subset and, for every adjacent pair of edges, compares the two edge-distance vectors directly from
\[
d(s,uv)=\min\{d(s,u),d(s,v)\}.
\]

The direct local-edge test is compared with the structural theorem. Minimum dimensions and minimum-basis counts are checked independently.

Recorded output:

```text
VERIFY_OK
parameter_pairs_checked = 36
m,n ranges = 1..6
vertex_subsets_checked = 15876
minimum_bases_checked = 247
all direct adjacent-edge tests matched the classification
all minimum dimensions and basis counts matched
```

The finite enumeration is corroborative only. The all-parameter theorem follows from the exact description of the local edge resolving neighborhood of an adjacent edge pair.
