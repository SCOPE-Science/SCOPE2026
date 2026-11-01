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

# Reproducibility of the integral calculation

From a directory containing `verify.py`, run `python verify.py` using Python 3.10+ and SymPy. No source downloads or datasets are required. The procedure builds lexicographically ordered arcs of a bidirected octahedral graph and enumerates every valid directed partial injection with no directed cycles. It independently enumerates all qualifying subsets of the 24 arcs up to size five, confirms equality, and checks maximal facets.

It constructs 835 disjoint matching pairs and explicitly verifies acyclicity of the 1816-vertex directed Hasse diagram by topological sorting all 6408 nonempty cover relations. Signed gradient-path reductions construct the integral critical boundary matrices; SymPy computes the exact Smith normal form of the 12-by-101 matrix. A separate direct computation of the original simplicial boundary ranks over the binary field checks the Betti ranks.

Observed complete successful output:

```
VERIFY_OK arcs=24 faces_nonempty=1816 f_vector=(24, 192, 616, 744, 240)
VERIFY_OK facets_4simplices=240 facets_3simplices=24 matched_pairs=835 directed_Hasse_incidences=6408 dag_vertices=1816
VERIFY_OK critical_counts=(1,0,12,101,32) morse_D3_12x101_nonzero=257 smith=1^9 morse_D4_101x32_zero
VERIFY_OK original_GF2_ranks=(23,169,444,208) integral_reduced_Betti=(0,0,3,92,32) no_torsion
```

The program checks finite chain groups and boundary computations, not infinite families, higher homotopy attaching classes, or independent validation. The integer Smith computation (rather than finite-field experiments) is what excludes torsion. The absence of critical one-cells provides simple connectivity; the second homotopy group follows from the classical Hurewicz theorem.
