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

The checker builds the half graph from its adjacency rule and computes all-pairs shortest-path distances. It independently enumerates every oriented length-three path whose endpoints are at distance three, converts each to an unordered triple of edge identifiers, and compares that set with the symbolic family
\[
\{a_\ell b_j,a_\ell b_k,a_i b_k\},
\qquad
\ell\le j<i\le k.
\]

For \(2\le n\le6\), it then exhausts every edge subset of size
\[
\left\lfloor\frac{(n+1)^2}{4}\right\rfloor
\]
and one larger. Every oversized set fails. The feasible sets at the proposed optimum are compared exactly, as sets of bitmasks, with the balanced complete-bipartite constructions whose binary strings have at most three runs.

Recorded output:

```text
VERIFY_OK
n=2: gp_e=2, maximum_sets=3, geodesic_triples=1
n=3: gp_e=4, maximum_sets=2, geodesic_triples=5
n=4: gp_e=6, maximum_sets=5, geodesic_triples=15
n=5: gp_e=9, maximum_sets=3, geodesic_triples=35
n=6: gp_e=12, maximum_sets=7, geodesic_triples=70
definition_level_triple_comparisons = 1926
near_extremal_subsets_checked = 505783
classification_exhaustive_through_n = 6
predicted_maximum_constructions_checked_through_n = 20
```

The checker also builds every predicted maximum construction through \(n=20\) and tests it directly against the reconstructed geodesic triples. These computations corroborate the theorem; the arbitrary-order proof is the Mantel reduction and equality/run analysis in RESULT.md.
