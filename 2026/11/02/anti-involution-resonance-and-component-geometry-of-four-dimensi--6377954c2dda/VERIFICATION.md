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

The standalone `check_quantum_anti.py` is reproducible using Python 3's standard library:

```
python3 check_quantum_anti.py
```

The checker enumerates all invertible degree-one matrices and all socle corrections for each tested finite field. It constructs multiplication directly from the original presentation, checks each reversed relation and the square of each proposed anti-map on all four basis elements, and independently computes fixed-space dimensions using Gaussian elimination. Counts are independently compared to the closed formulas; assertion failures cause nonzero exit. Nine complete parameter/field tests, including a polynomial-basis implementation of \(\mathbb F_4\), passed. `check_quantum_anti.out` gives their exact output and the final marker `QUANTUM_EXTERIOR_ANTI_INVOLUTIONS_ORIGINAL_PRODUCTS_OK`.

The computation does not determine global geometric components; those follow from the structural proof. It does not enumerate semilinear anti-involutions, higher truncations, or any nonreduced scheme structure. Independent audit is not performed.
