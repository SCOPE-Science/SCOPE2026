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

`verify.py` is a Python 3 standard-library-only executable. Execute `python3 verify.py` in the extracted package directory. It reconstructs the valuation matrix and boundary witness and verifies all pairwise EFX inequalities for the listed integer parameter values with exact rational arithmetic, including exact equality for agent \(3\) versus agent \(1\). It checks absence of a Pareto dominator by full enumeration of \(4^9\) assignments at the listed finite test parameters, and verifies the one-unit utilitarian gap. These tests are not an infinite-range proof. The proof in `RESULT.md` supplies the all-parameter conclusion, with the cited paper's Theorem 2 providing the strict upper bound.

No independent review has been performed.
