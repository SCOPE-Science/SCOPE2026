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

# Verification and reproducibility
The proof is entirely analytical. Two freely assigned complex sample values produce the exact Lagrange-coefficient sum at each target point; the supremum over the compact arc is an elementary two-region trigonometric maximization. The final minimax optimization reduces to a unique crossing of two strictly monotone positive functions. Uniqueness uses strict monotonicity in the absolute midpoint. These steps establish the universal statement without computational extrapolation.

The standalone `check_sampling.py` uses only the Python standard library. Running `python check_sampling.py` must print `CIRCULAR_ARC_SAMPLING_CHECK_OK 2400`. It checks the sharp-node equality at eight apertures, then verifies the lower bound on 2,400 deterministically generated admissible node pairs. The finite checker is an error-detection aid, not an infinite proof or an independent scientific audit.

The literature evidence covers the cited primary source's introductory theorem and nonisometry arguments, the full publicly available closest circular-arc Hilbertian-result text, and relevant interval and disk interpolation statements. An independently conducted historical-priority search has not been performed.
