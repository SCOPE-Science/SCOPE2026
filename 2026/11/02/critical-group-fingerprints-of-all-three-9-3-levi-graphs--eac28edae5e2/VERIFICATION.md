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

Exact checks executed on the packaged source files:

- `c++ -O2 -std=c++17 verify_census93.cpp -o census93 && ./census93`:
  `point_triangles=27 labelled_designs=3360`,
  `point_triangles=29 labelled_designs=30240`,
  `point_triangles=30 labelled_designs=40320`,
  point automorphism orders `108`, `12`, `9`, and `NINE_THREE_CLASSIFICATION_PASS labels=73920 nodes=1690154 isomorphism_classes=3`.
- `python verify_smith93.py` (dependency: `sympy`): exact nonunit Smith invariant factors `[2,6,6,18,18,54]`, `[2,6,48,2160]`, `[214,5778]`; determinants `1259712`, `1244160`, `1236492`; each factor product agrees with a separate exact Bareiss cofactor determinant, and `THREE_CONFIGURATIONS_EXACT_SANDPILE_PASS`.

The C++ enumeration is exhaustive under the explicitly stated combinatorial configuration definition; the Python arithmetic uses exact integers and does not extrapolate from samples. The published Pappus group is an independently known comparison, not a new claim. The computations are not externally audited, and no external certification is asserted.
