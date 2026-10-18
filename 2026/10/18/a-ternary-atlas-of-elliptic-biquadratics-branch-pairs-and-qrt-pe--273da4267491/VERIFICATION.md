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
# Exact finite-field verification

The package contains all normalized-orbit representatives, their orbit sizes and all invariants in `data/orbits.json`.

From the package directory run:

```
python verify/census.py > /tmp/ternary_biquadratic_census.json
python verify/symbolic_crosscheck.py
```

The first script (Python standard library only) exhaustively builds 9,841 projective equations, partitions their ambient action into 41 orbits, verifies discriminant squarefreeness and computes the arithmetic/QRT data. It internally asserts that the generated JSON is identical to `data/orbits.json`, and reports the JSON to standard output. The second (requiring SymPy) independently constructs all 24 projective matrices in each factor, verifies all 41 orbits, checks the Jacobian unit ideal on four affine charts for every representative, and independently computes ramification and deck-product orders. Its success output is:

```
PASS: 24 projective matrices; 1152 ambient maps; 41 disjoint exhaustive orbits
PASS: exact Groebner smoothness in four charts for all 41 representatives
PASS: independently recomputed rational points, branch counts, deck orders
```

These checks have been executed on the delivered source and table. All derived results follow from exhaustive finite algebra and standard double-cover/elliptic geometry. SymPy is required only for the independent symbolic crosscheck. No external peer review or independent audit has been performed.
