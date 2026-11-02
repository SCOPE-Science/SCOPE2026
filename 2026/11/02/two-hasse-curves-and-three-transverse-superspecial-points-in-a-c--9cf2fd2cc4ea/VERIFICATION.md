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

# Reproducibility and limits

Run `python verify_symbolic.py` and `python verify_fields.py` in the directory of these files. The first requires SymPy and checks the exact coefficients, factorization, gradients and discriminant; expected marker `GENUS2_CHAR7_EXACT_CARTIER_HASSE_SNC_INTERSECTION_OK`. The second uses only Python's standard library, builds a finite-field extension by hand and independently computes the Cartier coefficients by convolution; expected markers `GF7_EXACT_INDEPENDENT_CARTIER_CENSUS_OK` and `GF49_EXACT_INDEPENDENT_CARTIER_CENSUS_OK`.

The finite computations test \(\mathbb F_7\) and \(\mathbb F_{49}\) only; the all-extension statement follows from the exact repeated-root and Hasse-component arguments in `RESULT.md`. No independent external mathematical audit has been performed.
