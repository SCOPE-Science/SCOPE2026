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

The defining equations, assumptions, group action and complete enumeration are specified in `RESULT.md` and `classify.py`. Run `python classify.py` followed by `python crosscheck.py` in the extracted directory. The second check needs SymPy. Primary enumeration reconstructs the complete set of 1,296 squarefree sextics, 69 arithmetic classes, 19 partition/rank strata, 46 partition/rank/point strata, and the Burnside sum 1,656.

The independent arithmetic check computes the zeta coefficients from exact point counts over the explicit field of order nine and confirms the `3`-rank of **each of the 1,296 forms** without using the primary Cartier matrix. It independently tests squarefreeness with SymPy gcd and verifies all 69 branch partitions with SymPy's factorization. Both scripts ran successfully against the embedded data; the included output files show the observed results. This is finite exhaustive verification only for the stated base field, not a theorem about other finite fields.

No independent external validation is claimed; the independent-audit field remains not performed.
