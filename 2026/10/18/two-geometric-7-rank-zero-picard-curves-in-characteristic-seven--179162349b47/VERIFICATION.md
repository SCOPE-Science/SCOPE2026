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

## Reproducible checks
Execute `python3 verify.py` from this directory. The script uses only Python's standard library. It checks the defining quartic expansions exactly over \(\mathbf F_7\), the Cartier coefficients, the finite-field realization \(\mathbf F_{7^3}\) with an irreducible cubic, and the exact semilinear-square census on \(343\) normalized parameter values.

Expected terminal output:
```
SYMBOLIC_COEFFICIENTS_OK
GF343_CENSUS_OK: smooth rank-zero models b=1: 4 ; singular rank-zero models: 3
TWO_COARSE_CLASSES_AND_A_NUMBER_TWO_OK
```
The geometric all-parameter theorem and abstract isomorphism comparison are proved in `RESULT.md`, not inferred from enumeration. The program does not compute Newton polygons or arithmetic twist counts. Independent audit has not been performed.
