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
# Computational reproducibility

From this artifact directory, run `python code/q7_survey.py`, `python code/q7_independent.py`, and `python code/weil_pair_check.py`. Python 3 and SymPy are required for the first two scripts. Inputs are in `data/q7_models.txt` and do not require access to any external network. Full deterministic expected standard output is in the three `data/*_output.txt` files. The first two programs check all 32 classes and all 57 rational projective lines; the second proves geometric smoothness over the algebraic closure using Gröbner bases on three charts. The last program independently constructs explicit finite fields and confirms that the two selected D4-labeled curves both have 0, 60 and 384 points over the first three extensions.

The published catalog is used for class completeness, nonisomorphism and rational automorphism labels; those external classification theorems are not reconstructed here. The computations provide exact finite arithmetic, not a claim of independent external validation. Self-review passed; independent audit was not performed.
