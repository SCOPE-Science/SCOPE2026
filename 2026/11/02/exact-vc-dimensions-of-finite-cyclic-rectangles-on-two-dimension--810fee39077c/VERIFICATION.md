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

The standalone Python program `torus_grid_certificate.py` uses only the standard library and exact integer/bit-set operations. It implements the precise trace criterion and exhaustively checks the finite base cases required by the cyclic compression and tie-splitting lemmas.

Execution command:

```text
python3 torus_grid_certificate.py
```

Executed output:

```text
INDEPENDENT_RECTANGLE_TRACES_PASS 1119
EXPLICIT_LOWER_WITNESSES_PASS 9
ABSENCE_PASS 1 4 4 1
ABSENCE_PASS 2 2 3 3
ABSENCE_PASS 2 3 4 10
ABSENCE_PASS 2 5 5 126
ABSENCE_PASS 3 5 5 1001
ABSENCE_PASS 4 6 6 33649
ABSENCE_PASS 5 5 6 42504
SEVEN_POINT_ORDER_TYPES_PASS 5040
TOTAL_ORIGIN_FIXED_ABSENCE_CASES 77294
ALL_FINITE_TORUS_VC_CHECKS_PASS
```

`INDEPENDENT_RECTANGLE_TRACES_PASS` compares two distinct implementations on every support of up to four points in four specified small grids. `EXPLICIT_LOWER_WITNESSES_PASS` verifies all traces using both algorithms. Every `ABSENCE_PASS` uses exhaustive combinations, with no randomized or truncated search. The seven-point check exhausts all seven-coordinate permutations after the proved coordinate-tie refinement.

The finite computations establish only the finite statements they enumerate; the separate mathematical lemmas in `RESULT.md` transfer these statements to unrestricted finite side lengths. No claims are made about adaptive learning dimensions, an all-coefficient shattering polynomial, fixed-width rectangles, or independent external certification.
