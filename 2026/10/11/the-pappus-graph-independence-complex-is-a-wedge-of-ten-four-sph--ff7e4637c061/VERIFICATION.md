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
# Computational verification

Run, using Python 3.10 or later with standard-library modules only:

```
python3 verify_morse.py
python3 verify_independent.py
```

Both programs were executed successfully with their present contents. The first program verifies the full graph edge bijection between LCF and incidence presentations, enumerates 2,598 faces including the empty face, checks all 1,293 ordinary matching pairs and eleven critical cells, and checks acyclicity on the directed Hasse diagram of 2,597 nonempty faces containing 11,430 incidences. Its complete topological sort visits all faces. The second program builds the independent incidence graph, enumerates the identical face vector and computes complete simplicial boundary ranks \((17,109,329,472,274,74,16,2)\) over each of the prime fields of orders two and three.

The nonaugmented matching is obtained by omitting the one pair incident to the empty face. Its exact critical-cell vector has one zero-cell and ten four-cells. The resulting wedge decomposition follows from classical discrete Morse theory; finite-field ranks and the alternating face sum are independent checks, not substitutes for this integral homotopy argument.

Limitations: exhaustive finite calculation only for the specified eighteen-vertex graph; the modular checks alone would not certify integral torsion-freeness, and independent external scientific validation has not been performed.
