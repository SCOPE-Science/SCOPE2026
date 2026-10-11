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

The proof is analytic and finite-dimensional after Parseval. The critical checks are:

- the collision-free identity \(\|F\|_4^4=2S^2-\sum x_j^2\);
- exhaustiveness of the two-, three-, and four-index collision patterns by cancellation of characters;
- the exact case-2 identity
  \[
  -\frac{u^2}2-v^2+2uv=\frac{(u+v)^2}7-\frac{(3u-4v)^2}{14};
  \]
- the two arithmetic-mean inequalities in case 3 and their equality conditions.

The standalone `verify.py` constructs one explicit finite-group model for each collision type, checks that each model has exactly one nonsingleton product fiber, compares direct Haar averages with the derived fourth-moment formula on random coefficients, and tests sharp equality witnesses. Running `python3 verify.py` gives:

`VERIFY_OK collision_types=3 exact_B_identities=1000 direct_checks=900 equality_witnesses=3`

Random testing is not an infinite proof and is used only as a regression check. Historical novelty remains subject to the literature-access limitations stated in `REVIEW.md` and `AUDIT.json`.
