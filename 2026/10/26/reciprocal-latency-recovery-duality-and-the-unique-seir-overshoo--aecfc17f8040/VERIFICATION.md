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

# Reproducible checks

Run `python3 verify.py` with SymPy and SciPy. The program checks the four-equation reciprocal conjugacy by exact symbolic cancellation and independently checks the invariant/reduced equation symbolically. It integrates the original system for three reproduction ratios and five rate ratios and confirms reciprocal infected-peak susceptible coordinates and a strict local minimum at equal progression/recovery rates; further two extreme rates check the numerical overshoot examples.

The analytic proof is in `RESULT.md`. Floating-point integrations do not certify a theorem for all positive rates or mathematically exclude every additional peak; those steps are proved analytically. Exact stage-rate reciprocity compares transformed initial stage compositions, not identical arbitrary finite initial compositions. The source date belongs to the 2023-03-03 first public arXiv version, not the later journal publication.
