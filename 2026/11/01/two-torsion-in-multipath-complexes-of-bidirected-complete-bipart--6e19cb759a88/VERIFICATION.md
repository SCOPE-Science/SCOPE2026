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

# Reproducing the integral homology computation

Use Python 3.10+ and install the package version in `requirements.txt` (SymPy 1.14.0). From the directory containing `verify.py`, execute `python verify.py`. This program requires no data downloads. It enumerates every eligible arc subset, validates all faces, constructs each full integral signed simplicial boundary, checks that consecutive boundaries compose to zero, computes the Smith normal form over \(\mathbb Z\), and independently reduces each boundary modulo \(2\) using bit-packed elimination.

The actual executed checks produced:

```text
MODULE_OK n=4 all_arcs_forced=16 all_vertices_unstable=true
CHAIN_OK n=4 face_vector=(16, 80, 144, 72) boundaries=[(16, 80), (80, 144), (144, 72)] ranks=[15, 65, 72]
SMITH_OK n=4 factors=[{1: 15}, {1: 65}, {1: 71, 2: 1}] mod2_ranks=[15, 65, 71] mod2_betti=(0, 8, 1)
HOMOLOGY_OK n=4 H1=0 H2=Z^7+Z/2 H3=Z^0
MODULE_OK n=5 all_arcs_forced=20 all_vertices_unstable=true
CHAIN_OK n=5 face_vector=(20, 130, 320, 240) boundaries=[(20, 130), (130, 320), (320, 240)] ranks=[19, 111, 209]
SMITH_OK n=5 factors=[{1: 19}, {1: 111}, {1: 208, 2: 1}] mod2_ranks=[19, 111, 208] mod2_betti=(0, 1, 32)
HOMOLOGY_OK n=5 H1=0 H2=Z^0+Z/2 H3=Z^31
ALL_VERIFY_OK exact_integer_smith_F2_independent_differentials_module_closure
```

The degree-one and degree-two differential Smith forms also show that both complexes have no first homology. Each \(\partial_3\) has just one nonunit invariant factor, precisely \(2\). Because \(\operatorname{im}\partial_2\) is torsion-free, these factors give genuine two-torsion in \(H_2\). The explicit directed-module closure assertion is also verified for every starting arc.

**Limits:** Tests are complete for the two input graphs only. The argument for arbitrary-width module indecomposability is mathematical, not inferred from the two enumerations. No independent audit or external mathematical validation has been performed.
