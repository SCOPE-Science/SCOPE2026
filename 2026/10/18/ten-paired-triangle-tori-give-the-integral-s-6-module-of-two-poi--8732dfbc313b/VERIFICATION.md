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

Run `python3 verify.py` with Python 3.10 or newer, without third-party dependencies. The script generates all 15 graph edges, all 45 unordered disjoint-edge two-cubes, all 60 edge-and-disjoint-vertex one-cubes, and the ten three–three triangle-pair tori. It calculates integer boundary coefficients and signs without imported data tables.

The script checks the exact 10-column cycle matrix against the full boundary, the normalized diagonal sum coefficientwise, a determinant-one 9-by-9 torus minor, a nonzero determinant-two 36-by-36 boundary minor, and all 720 vertex permutations on all 10 normalized torus cycles. Its fraction-free Bareiss integer determinant procedure is included as source.

The two determinants have zero-based row/column index data explicitly specified in `RESULT.md` and in the verifier. The determinant-two minor proves only the boundary rank lower bound. The nine independent primitive cycles provide the matching rank upper bound and integral saturation, so the proof does not assume a numerical rank computation or confuse a finite test with a universal statement.

Actual verifier output:

```text
VERIFY_OK_K6_UNORDERED_TWO_POINT_TORUS_LATTICE
CELLS_C0_15_C1_60_C2_45
EXACT_BOUNDARY_TEN_CYCLES_ZERO; NORMALIZED_SUM_ZERO
NINE_TORUS_UNIMODULAR_MINOR 1 R9 (0, 1, 3, 6, 7, 9, 12, 13, 18)
THIRTYSIX_BOUNDARY_NONZERO_MINOR 2 R36 (0, 1, 2, 4, 5, 6, 8, 9, 10, 12, 13, 14, 16, 17, 18, 20, 21, 22, 24, 25, 26, 28, 29, 30, 33, 34, 36, 37, 38, 40, 41, 42, 46, 48, 49, 50) C36 (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 33, 34, 36, 37)
TEN_CARRIERS_UNIQUE_RELATION_SIGNS [1, -1, 1, -1, 1, -1, 1, 1, -1, 1]
ALL_720_S6_PERMUTATIONS_SIGN_TWIST_ACTION_VERIFIED
CONCLUSION_H2_Z9_ANY_NINE_INTEGRAL_BASIS
```

Limits: These calculations establish the precisely specified finite complex. Its equivalence to the continuous collision-free configuration space relies on the stated subdivision criterion from the cited literature. No independent external mathematical audit has been completed.
