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

# Reproduction checks

Run `python verify.py` with Python 3 and the standard library. This enumerates all labeled binary assignments on each \(C_n\) for \(5\le n\le17\), independently tests domination and locating-neighborhood uniqueness, checks every forbidden cyclic factor, and computes the coefficients of the proved rational generating function with integer polynomial arithmetic. It additionally checks the exact symbolic two-state determinant by sparse polynomial multiplication. Successful output is recorded in `verify_output.txt`.

These checks cannot establish correctness for unbounded \(n\); the complete mathematical proof in `RESULT.md` does so. The paper-comparison and originality judgments are self-review assessments, not independent certifications.
