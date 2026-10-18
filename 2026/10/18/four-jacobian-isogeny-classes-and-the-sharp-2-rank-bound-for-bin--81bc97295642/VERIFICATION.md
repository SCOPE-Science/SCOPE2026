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

Run `python3 verify.py` with Python 3 and SymPy. It uses only exact integer arithmetic, characteristic-two coefficient arithmetic, four affine-chart Gröbner bases over a finite field, a complete 36-element ambient group action, and explicit small finite field multiplication tables. No external file, network resource, or hidden input is required.

The program checks the rank-nine rational evaluation matrix, exhausts all 2047 possible equations, confirms 364 rationally nonsingular and 66 geometrically smooth, constructs four orbits of sizes 6, 18, 36, 6, counts points for each representative over F2 to F64, derives the four Weil polynomials, and verifies initial and sixfold Cartier ranks. It compares all computed arrays against independent literal expected arrays and emits `PASS` only after every assertion succeeds.

The exact unit-ideal Gröbner criterion is used for geometric smoothness, not extension-field sampling. The point counting itself is finite, but a degree-twelve Weil numerator is determined by counts through the sixth extension only after genus six and the functional equation have been established. These checks are self-reviewed; no independent external audit has occurred.
