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

Run `python3 verify_hyperelliptic.py` and `g++ -O2 -std=c++17 verify_quadrics.cpp -o verify_quadrics && ./verify_quadrics`.

The first script checks all 63 nonzero binary degree-at-most-five polynomials, all nine degree-six base orbits and 11 trace matrix columns, proves that all-nine-inert is not in any matrix image, and verifies the Artin–Schreier degree-five witness. The second script enumerates every one of 65,535 reduced cubic sections for each of three canonical quadrics, counts degree-six Frobenius orbits by exact 64-element-field arithmetic, and verifies singularity at explicit rational points for all five exceptional nonsplit cubic forms.

Previously observed terminal markers were `HYPERELLIPTIC_VERIFY_OK` and `QUADRIC_VERIFY_OK`. These calculations are exhaustive only on the finite parameter sets stated. The asserted existence of degree-n points for all n≥7 uses the separately cited Weil/theorem bounds. Independent external validation has not been performed.
