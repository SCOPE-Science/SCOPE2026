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

The standalone `verify.py` script uses Python 3 and standard-library functions only. Run `python verify.py`; successful execution prints `CHECK_OK` and a description of tested identities. It compares active/silent direct composition with scalar symmetry reduction, verifies uniform difference contraction in 630 independent randomly parameterized cases, and checks the exact rational comparison between uniform and clustered two-pulse schedules. It also checks the rational group-size cutoff and selected long-time trajectories near the onset.

The all-group-size theorem, uniqueness at threshold, extinction from asymmetric states, and right-neighborhood strictness are established by analytic inequalities and continuity in `RESULT.md`, not by finite numerical samples. The calculation concerns the deterministic individual-probability closure; it is not a calculation of an exact stochastic finite-population survival probability. No external independent scientific audit has been performed.
