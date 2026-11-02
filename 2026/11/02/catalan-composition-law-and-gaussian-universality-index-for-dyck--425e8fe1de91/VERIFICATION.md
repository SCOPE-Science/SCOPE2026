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

The included `verify.py` uses only the Python standard library. Run `python3 verify.py` from the directory containing the extracted files. Its output is `VERIFY_OK assertions= 390 direct_Dyck_words= 290512 transfer_cells= 171 mean_slope= 2/3 variance_slope= 4/27`.

The program independently compares direct greedy subsequence-universality counts on every Dyck word through semilength 12 with coefficients of the algebraic formula. A second arch-height dynamic program checks all cells with at most 18 arches and ascent defect at most 8. It checks the two explicit top-defect coefficient formulas up to semilength 64 and computes the singularity-derivative constants using exact fractions. The infinite generating-function identity follows from the arch-height recurrence and its formal unique solution, not from these checks. The Gaussian limit uses a standard analytic quasi-powers theorem and uniform singularity transfer, not a numerical fit. No independent assessment has been performed.
