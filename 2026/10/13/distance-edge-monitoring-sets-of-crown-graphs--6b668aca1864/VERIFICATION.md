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

The verifier constructs the crown graph
\[
\operatorname{Cr}_n=K_{n,n}-M
\]
directly from its deleted-matching definition.

For every edge \(e\) and every probe vertex \(x\), it computes all distances from \(x\) before and after deleting \(e\). Thus the monitored edges are recovered directly from the defining distance-change condition, with no use of the theorem being checked.

For every
\[
4\le n\le7,
\]
the verifier checks that each edge is monitored exactly by its two endpoints. It then exhaustively enumerates every vertex subset, compares the direct DEM predicate with the vertex-cover predicate, and compares every cardinality coefficient with
\[
2z^n(1+z)^n-z^{2n}+nz^{2n-2}.
\]
It separately checks the boundary graph \(\operatorname{Cr}_3\), where the incident-edge-only property fails and the minimum is \(2\).

Recorded output:

```text
VERIFY_OK
n=4: edges=12, DEM_sets=35, minimum=4, bases=2
n=5: edges=20, DEM_sets=68, minimum=5, bases=2
n=6: edges=30, DEM_sets=133, minimum=6, bases=2
n=7: edges=42, DEM_sets=262, minimum=7, bases=2
boundary_n=3: minimum=2, incident-edge-only property fails
n_checked = 4..7 plus boundary n=3
vertex_subsets_checked = 21824
probe_edge_checks = 1280
minimum_bases_checked = 8
all n>=4 DEM sets matched vertex covers
all DEM polynomial coefficients matched
```

The finite computation is corroborative only. The arbitrary-parameter theorem is established by the explicit surviving-geodesic proof in the result.
