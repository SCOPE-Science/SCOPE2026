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

# Reproducible checks and proof limits

Run `python3 verify.py` in the directory containing the standalone files. The program uses only Python's standard library; it tests exact geometric probability-generating-function iterations, exact lower-tail inequalities for scaled geometric variables, and finite triangular exceedance intensity trends. Its authentic output is recorded in `verify_output.txt`.

These tests do not verify convergence of a Poisson point process, independence of the two limit coordinates, or limiting laws for all sample sizes. Those conclusions follow from the proof in `RESULT.md`: independent rare-event Laplace transforms and extreme-point truncations, marking/mapping of the limiting Poisson process, uniform geometric-family log-size bounds, and the deterministic runner-up versus aggregate minority-mass inequality. The Poisson top-gap transformation is an analytic calculation, not asserted to be established by finite arithmetic checks.

Source comparison: arXiv:2610.29759v1 supplies the original geometric branching model and qualitative one-genotype dominance, but the specific joint rate law is assessed separately in `REVIEW.md` and `AUDIT.json`. External, independent mathematical and historical-priority audits have not been performed.
