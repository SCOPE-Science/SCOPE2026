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

## Finite verification
Both source files run with Python 3 and the standard library only, from the directory in which all package files were extracted:

```
python3 verify.py
python3 verify_independent.py
```

The first enumerates the \(45\) weight-two words at blocklength ten, constructs compatibility edges directly from the cyclic pair-distance, exhausts all compatible subsets, and gets \(22\) optima of size \(5\). It also computes exact maxima \(1,1,1,1,1,2,2,3,5\) for lengths \(2\) through \(10\), respectively, and partitions the length-ten optima into three dihedral orbits of sizes \(2,10,10\). The second uses a state recursion over unused edges of \(K_5\) and a separate explicit Euler-tour generator. It returns \(528\) closed trails starting at graph vertex zero and \(22\) distinct support-code sets after forgetting graph labels; each member is checked directly for cyclic pair-distance at least seven.

Observed successful output includes:

```
VERIFY_OK direct_45_words_10_length10=22 orbit_sizes=[2, 10, 10]
INDEPENDENT_VERIFY_OK K5_tours_start0=528 K5_color_sequences=2640 optimal_unlabeled_sets=22
```

## Beyond the finite domain
The \(n\ge10\) existence and optimality statement is justified by a graph construction and a support-disjointness upper bound. The even-length equality converse is proved from the partition of occupied coordinates; no experimental extrapolation is used. The numerical orbit enumeration is restricted to \(n=10\), not extended to arbitrary lengths.

## Evidence and limits
The historical Chee et al. Eulerian construction and the Elishco et al. even-distance constant-pair-weight theorem were compared at the level of their mathematical statements. Zhao–Chang's later distance-seven study was available as an abstract and first-page preview, not as readable full text; it remains an originality risk and is not treated as definitively excluding overlap. Independent audit has not been performed.
