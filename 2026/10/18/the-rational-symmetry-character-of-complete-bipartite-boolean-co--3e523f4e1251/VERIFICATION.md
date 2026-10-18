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
# Verification

The exact source code `verify_boolean_character.py` uses only the Python standard library. Run `python3 verify_boolean_character.py` in the directory holding this document and the code. It enumerates distinct orientation matrices arising from all vertex orders, then performs a direct signed fixed-cell Lefschetz sum for all pairs of conjugacy classes at the seven sizes \\((1,1),(1,2),(2,2),(2,3),(3,3),(2,4),(3,4)\\). Its 47 equalities are independent of the cycle-collapse reduction used in the theoretical proof. It additionally averages the predicted character over every permutation to test the dimension of invariant top homology for each of 25 pairs with part sizes from one to five. It checks identity traces against the known Boolean-number formula.

All 47 character equalities and all 25 invariant-dimension equalities passed in a direct execution before packaging. These checks concern only the enumerated finite parameters and do not independently validate the infinite proof, which proceeds through the nested-neighborhood and augmented Lefschetz arguments in `RESULT.md`. Integral equivariance, transposition of bipartition classes, and external independent mathematical validation are not covered.
