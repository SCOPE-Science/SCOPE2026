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

Run `python3 verify.py` with a standard Python 3 interpreter. The script independently builds every labelled parent tree for 50 small horizon/parameter combinations, compares the exact height and leaf count against additive recurrences, and matches six rational moments to a separate finite-state dynamic program. It also compares the three renewal-reward asymptotic covariance entries with high-precision finite geometric sums, tests convergence of scaled finite moments and the covariance sign crossing.

The limiting two-dimensional Gaussian theorem is established by the proof in `RESULT.md`, not by finite testing. The only nontrivial probabilistic input is the classical iid renewal-reward CLT; its hypotheses hold because the block-length law is geometric and therefore has moments of all orders. Geometric mixing of a finite-state reward chain supplies the stated linear covariance asymptotics with bounded errors. Independent expert validation has not been performed.
