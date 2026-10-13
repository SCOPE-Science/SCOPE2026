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

The verifier constructs the crown edge set
\[
E(\operatorname{Cr}_n)=\{a_i b_j:i\ne j\}
\]
and all forbidden three-edge geodesics directly from the deleted-matching structure.

For
\[
n=3,4,5,
\]
it exhaustively enumerates every edge subset and rejects a subset exactly when it contains all three edges of one forbidden geodesic. The independently computed maxima are
\[
4,\qquad 8,\qquad 12,
\]
which equal
\[
\left\lfloor\frac{n^2}{2}\right\rfloor.
\]

The checker also constructs the balanced bidirected-cut witness for every
\[
3\le n\le20
\]
and verifies directly that no transitive directed triangle occurs.

Recorded output:

```text
VERIFY_OK
n=3: edges=6, forbidden_geodesic_triples=6, maximum=4, maximum_sets=3
n=4: edges=12, forbidden_geodesic_triples=24, maximum=8, maximum_sets=3
n=5: edges=20, forbidden_geodesic_triples=60, maximum=12, maximum_sets=10
vertex_index_cut_constructions_checked = 3..20
exhaustive_edge_subsets_checked = 1052736
all exhaustive maxima equal floor(n^2/2)
```

The finite enumeration is corroborative only. The theorem for all \(n\ge3\) follows from the exact geodesic-to-transitive-triangle correspondence, the endpoint degree-sum inequalities, and Cauchy--Schwarz.
