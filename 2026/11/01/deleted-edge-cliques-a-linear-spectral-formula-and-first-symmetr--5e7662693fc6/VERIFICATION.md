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

# Reproduction and scope of checks

Run `python verify.py` using Python 3 standard library. The verifier uses scaled integer averaging matrices, exact fraction-free determinant elimination and Sylvester positive-definiteness tests. It checks all 18, 36 and 72 ball-selection matrices for the three-, four- and five-vertex cases. The strict/exceptional breakdown is respectively 17/1, 35/1 and 69/3. For the five-vertex case, the strict threshold is exactly \(7/5\). It checks the full characteristic polynomial by exact determinant interpolation and isolates the unique relevant root in \( (1.416,1.417) \) using rational arithmetic.

The root interval also provides rational strict inequalities for the averaging-row choices and positivity of the proposed extremizer. The polynomial identity for the eigenvector is written explicitly in `RESULT.md`. Finite checks do not prove the all-size assertion; Steps 1–4 in `RESULT.md` supply the infinite-parameter argument. Verification is an ordinary self-review, not independent certification.
