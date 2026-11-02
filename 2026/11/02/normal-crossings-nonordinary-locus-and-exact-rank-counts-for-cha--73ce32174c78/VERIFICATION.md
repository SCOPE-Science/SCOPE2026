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

# Reproducible checks

The associated files `verify_symbolic.py` and `verify_fields.py` are standalone source files in the package. The symbolic script requires SymPy and checks the characteristic-three quartic-square Hasse coefficients, the discriminant graph identity, boundary evaluations, normal direction rank at the sole triple point, and finite-count polynomial equalities.

Command: `python3 verify_symbolic.py`

Observed final line: `CHAR3_CIANI_EXACT_CARTIER_SNC_AND_COUNT_IDENTITIES_OK`.

The independent finite-field script uses a pure-Python polynomial-basis implementation of \(\mathbb F_3\), \(\mathbb F_9\), and \(\mathbb F_{27}\). It enumerates every coefficient triple over each field, tests the smoothness discriminant and three Hasse factors, and checks all rank-stratum counts against the theorem. It does not call or depend on the symbolic verifier.

Command: `python3 verify_fields.py`

Observed final line: `CHAR3_CIANI_INDEPENDENT_GF3_GF9_GF27_CENSUS_OK`.

This finite enumeration is confirmatory only. The infinite-field smoothness, crossing structure, and all finite-extension formulas are established by exact algebra and the character sum in the proof. Independent external mathematical audit has not been performed.
