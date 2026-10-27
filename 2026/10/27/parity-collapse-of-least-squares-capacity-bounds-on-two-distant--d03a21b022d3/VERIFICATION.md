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

# Verification and limits

The plain Python 3 program `verify.py` is standalone. Run `python3 verify.py`; it returns `CHECK_OK` only after exact rational disk moments, Schur-complement norms, degree-zero/one/two formulas, and sample strict inequalities pass. It also checks finite-degree normalization at large separation; these finite checks do not establish a universal asymptotic theorem.

The analytical proof verifies the uniform finite Gram inverse for each *fixed* degree, the cancellation of linear perturbations in diagonal moments, and the capacity enclosure. The statement does not assert uniformity as the degree grows. Independent external assessment has not been performed.
