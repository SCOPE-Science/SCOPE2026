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

The standalone `verify.py` artifact was read from its actual packaged path before replay.

For each \(2\le n\le7\), it constructs every nonempty proper support, verifies
\[
\deg(S)=2^{n-|S|}-1,
\]
checks that the maximum-degree vertices are exactly the singleton supports, and reconstructs every support from its nonadjacency pattern to those singletons. For \(n\le5\), it also checks every coordinate permutation preserves adjacency.

It then exhaustively enumerates every candidate family of size \(k=\lceil\log_2 n\rceil\), tests the pairwise-distinct coordinate-signature criterion, and compares the count with
\[
\frac{(2^k)!}{(2^k-n)!k!}.
\]
It also exhaustively confirms that no family of size \(k-1\) determines the graph. Larger sample values through \(n=33\) verify the explicit binary-code construction and closed count.

Exact replay output:

```text
n k minimum_set_count
2 1 2
3 2 12
4 2 12
5 3 1120
6 3 3360
7 3 6720
published_n5_two_set_obstruction 4
VERIFY_OK
```

The finite enumeration is corroborative. The arbitrary-\(n\) theorem follows from the graph-theoretic reconstruction of the coordinate action and the separating-signature argument.
