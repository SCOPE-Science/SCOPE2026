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

Execute `python3 verify.py` with the standard Python library. The program reconstructs the grounded weighted incidence matrix and its orthogonal projection from exact rational Gaussian elimination, with conductance square roots selected rationally. It checks every spoke and rim absolute row sum, the Green-row normalization, symmetry, and for a subset, idempotence. It also evaluates the logarithmic asymptotic scaling at four finite rim sizes.

Completed local output: `PASS: 16896 exact rational and asymptotic checks`. The matrix inversions and row-norm comparisons are exact; the four asymptotic scaling comparisons are floating-point. These tests are finite and therefore do not establish any all-size or asymptotic theorem by themselves. The proof in `RESULT.md` supplies the universal recurrence and optimization arguments. Independent scientific validation has not been performed.
