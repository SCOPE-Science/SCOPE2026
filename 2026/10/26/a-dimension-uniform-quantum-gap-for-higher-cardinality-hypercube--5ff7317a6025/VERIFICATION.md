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

The accompanying `verify.py` (with the dependency declared in `requirements.txt`) checks seven Hamming-parameter cases and forty independently generated symmetrized deterministic strategies and six independently generated entangled-qubit strategies. It verifies the exact counting identity, adjacency eigenvalue formulas, spectral gap, two-layer sphere geometry, score-deficit identity, and the claimed positive numerical bound. It reports 861 passing finite assertions when run with Python 3 and NumPy.

The checks are finite diagnostic corroboration, not an exhaustive search over quantum strategies or a proof for arbitrary dimensions. The analytic proof is given in RESULT.md. In particular, the nonstandard steps requiring conceptual verification are the vector deficit identity, Kneser spectral Poincaré inequality, translation-invariant definition of the deviation parameter, and two-sphere inner-product contradiction.

The estimate is not asserted to be sharp; no independent external audit has occurred.
