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

# Verification of the finite counterpossible witness budget

The theorem has a symbolic proof in `RESULT.md`. Run `python3 check.py` using Python 3 standard library only. The checker independently enumerates all \(r\)-by-\(s\) Boolean tables for \(1\le r\le 4\) and \(1\le s\le 3\) (5,050 tables), computes their Boolean rank both with and without the nonempty row-selection constraint, and checks the exact extra-world identity and sharp maximum. It also tests 196 algebraic sharpness constructions and 682 explicit factorizations reproduced as selected anti-world truth tables.

Expected terminal markers: `EXHAUSTIVE_MATRIX_CHECK_OK 5050`, `SHARPNESS_CONSTRUCTION_OK 196`, `FINITE_SEMANTIC_REALIZATION_OK 682`.

Only Boolean matrices of the specified finite ranges are exhaustively tested. The global well-founded extension of the semantic selection function over arbitrary formulas, and the bound for all positive integers \(r,s\), are mathematically proved in `RESULT.md` and not claimed to follow from experiments. Independent audit has not been performed.
