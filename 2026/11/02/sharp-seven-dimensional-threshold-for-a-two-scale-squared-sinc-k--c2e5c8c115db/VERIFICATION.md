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

# Reproducibility and proof checks

Run `python check.py` with Python 3 and SymPy installed. The program reconstructs the four-uniform cubic B-spline, obtains the prescribed seven-dimensional signed Schoenberg density on both scale-ratio chambers, verifies its total mass and second moment, and checks the sharp quadratic cutoff and the upward-jump algebra. It also checks representative rational parameters on both sides of the cutoff.

The analytic proof identifies all parameter intervals, proves density nonnegativity on the complete closed range, proves a strictly negative interval outside it, and excludes dimension eight by double Abel inversion. The code does not substitute for that proof, does not assert an infinite-dimensional numerical enumeration, and does not establish novelty. External independent mathematical validation has not been performed.
