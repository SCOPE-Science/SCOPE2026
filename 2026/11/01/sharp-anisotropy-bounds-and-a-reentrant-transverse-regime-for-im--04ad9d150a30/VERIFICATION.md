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

# Reproducibility and verification
Run `python verify_diffusion.py` using Python 3 standard library only. The checked script prints `PASS 412 independent numerical/algebraic tests`. It independently checks Fourier generator cancellation at modes one and two for random atomic resets, all sharp extremal measures, admissible mixtures, exact phase-window signs, and agreement of the delta-reset specialization with the formulas of Baouche et al., arXiv:2405.06769v1. Numerical checks do not establish claims for arbitrary Borel reset measures: that is proved by the Fourier-generator identity, exponential covariance integration and the elementary sharp moment inequality in RESULT.md.

Limitations: no independent scientific audit has been conducted; the priority comparison may not cover every general theorem. The source date is the arXiv first-submission date, not a journal publication date.
