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

# Reproducibility

Use Python 3 with no nonstandard packages. Place `verify_clebsch.py` and `verify_homology.py` in the same directory as this document and execute both directly:

```
python3 verify_clebsch.py
python3 verify_homology.py
```

The first program enumerates the entire independence complex of the degree-five Clebsch graph, checks strongly regular parameters, all 392 nonempty simplices, the face vector \((16,80,160,120,16)\), maximal-simplex dimensions, 191 disjoint Morse pairs, and a complete DAG topological sort of 1,200 directed cover incidences. The critical dimensions are exactly one zero-cell and nine three-cells.

The second program uses recursive extension to enumerate independent sets and bitwise elimination to compute every simplicial boundary rank modulo two, yielding \((15,65,95,16)\) and reduced Betti vector \((0,0,0,9,0)\). The two enumerations share only the finite graph's mathematical definition, not face-list data or stored results.

The homotopy conclusion, including integral homology, follows from the verified discrete-Morse critical-cell profile; a mod-two check alone would not suffice. No claim about larger folded cubes, literature completeness, or independent external verification is made.
