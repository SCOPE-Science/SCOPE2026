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

# Verification and limitations

Run `python VERIFY.py` with Python 3; the script depends only on the Python standard library. The successful run prints `ALL VERIFICATIONS PASSED` after checking exact rank probabilities, pairwise collisions and distinct exposed support vectors for all plane full binary tree shapes with two through six leaves and all score permutations. It also tests exact collision-gap inequalities for all tree shapes with up to eight leaves, computes the six-leaf extremizers and compares dyadically expanded shape families at six scales. All equality tests use exact fractions.

The universal formula and equality characterization are established mathematically in `RESULT.md`; finite tests do not imply them on their own. The major assumptions are strict positivity of internal simplex coefficients, Euclidean geometry in the coordinate-sum hyperplane, and independent isotropic Gaussian exposure. An independent mathematical audit has not been performed.
