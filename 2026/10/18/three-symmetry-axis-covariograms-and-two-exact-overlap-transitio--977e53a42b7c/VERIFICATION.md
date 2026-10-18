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

# Verification

The analytical proof in `RESULT.md` is the argument for all real parameters. Numerical reproduction with Python 3, NumPy and SciPy: `python3 verify.py`. The script builds the intersection from all twelve pair-sum halfspaces and the shifted twelve halfspaces, finds its vertices via `scipy.spatial.HalfspaceIntersection`, and computes the hull volume. It tests 21 independent interior examples over all three axes, the two thresholds, and representative strict orderings; it cannot prove the infinite real assertions or historical novelty. The reader can independently check the fiber integrals and the sign arguments without installing scientific packages.

The principal constraints are the *fixed orientation*, the *three symmetry-axis orbits only* restriction for the phase result, and positivity of the measured intersection before support endpoints. Prior-work priority remains open to further scholarly review.
