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
# Verification of the dodecahedral resolving polynomial

Run `python3 verify.py` with Python 3.9 or newer; no external packages or network are required. The verifier constructs \(P(10,2)\) independently from the edge definitions, recomputes all-pairs graph distances by BFS, and compares them with the three ten-entry distance rows in `RESULT.md`. It checks that the ten pairs \(\{u_i,u_{i+5}\}\), \(\{v_i,v_{i+5}\}\) are antipodal and that \(d(x,\bar y)=5-d(x,y)\) for all 400 ordered vertex pairs.

It exhaustively evaluates all \(190\) unordered distinct vertex pairs' equidistance loci and verifies ten empty loci and \(180\) four-vertex loci. Each nonempty locus is exactly two of the ten antipodal pairs, and every one of the \(45\) unordered antipodal-class pairs appears (the numbers of witnesses per pair are \(2\) for thirty classes and \(8\) for fifteen classes).

A *direct* distance-vector resolving predicate is compared with the antipodal criterion on all \(6196\) vertex subsets of sizes zero through four. The verifier then enumerates all \(1,048,576\) subsets, computes the exact cardinality distribution, and compares each coefficient with \(\sum_{j=3}^{10}\binom{10}{j}\binom{j}{k-j}2^{2j-k}\). Its expected final lines include:

```
VERIFY_OK graph_vertices=20 graph_edges=30 antipodal_pairs=10 distance_diameter=5
VERIFY_OK equidistance_sets=190 empty=10 four_vertices=180 all_45_fiber_pairs_realized=YES
VERIFY_OK direct_distance_signatures_all_subsets_sizes_0_through_4=6196
VERIFY_OK all_masks=1048576 resolving=1048140 nonresolving=436
VERIFY_OK metric_dimension=3 metric_bases=960 full_resolving_polynomial=exact
```

The mathematical proof consists of the actual distance rows, a finite equalizer table exhausted by specified symmetries, and a constructive combinatorial enumeration. The code corroborates these critical finite lemmas and the resulting coefficients; it is not a certificate of independent audit, generalization beyond this graph, or publication priority.
