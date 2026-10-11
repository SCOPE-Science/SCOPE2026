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

# Verification and reproducibility

This package contains a frozen Graph Atlas graph6 list, a complete exact integral-homology torsion checker, an independently written finite-field checker, and an explicit integral cycle and chain certificate. All inputs are ordinary UTF-8 or graph6 text. The results concern all simple graphs with at most seven underlying vertices.

Install Python with the packages listed in `requirements.txt`. In one directory containing all the supplied files, execute:

```bash
python verify_exact.py
python verify_modular.py
```

The exact checker parses each graph6 entry without NetworkX, builds every matching of sizes one through three, constructs the signed second simplicial boundary and computes integral Smith normal form using SymPy. It checks the canonical 1,253-graph order distribution, all forty torsion indices and the complete edge histogram. For `G1105` it also reconstructs the signed certificate `torsion_certificate.json` and checks \(\partial_1 z=0\), \(\partial_2 c=3z\), rank of the second boundary, and nondivisibility of a chain coefficient by three.

The second checker independently constructs the disjointness graph as the complement of the line graph, enumerates triangles of that graph, forms its boundary matrix, and performs separate modular elimination in characteristics three and five for every atlas graph. It compares graph6 inputs with the canonical NetworkX graph atlas. For the sparse witness it additionally checks characteristics two, seven and 101.

Both commands completed successfully on the packaged source files and produced `EXACT_OK` and `MODULAR_OK`. The integral Smith computation, not the modular rank comparison alone, establishes the exact torsion classification. Reproduction presumes completeness of the published Graph Atlas and correctness of installed mathematical software; it is not independent external scientific auditing.
