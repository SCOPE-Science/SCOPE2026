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
# Verification of the all-degree sampling formulas

The proof identifies the exact evaluation reproducing kernel under probability-normalized surface measure, reduces antipodal samples to 12 root lines, and diagonalizes the even signed/unsigned line algebra. The all-degree positivity inequalities are proved symbolically rather than inferred from samples.

To reproduce the finite checks, run `python3 CHECK.py` alongside `RESULT.md` using Python 3.10 or later; no additional packages are required. The checker constructs the root-line coordinates exactly, verifies the four-by-twelve incidence and two matrix spectral polynomial relations, forms exact projector matrices, checks the complete predicted 12-point Gram and ranks for degrees zero through 120, and directly checks the 24-vertex antipodal Gram ranks for degrees zero through 15.

Observed stdout: `PASS: 399 degree/spectral/rank assertions plus exact geometry/projector identities`.

All tests use rational arithmetic; they are corroboration, not exhaustive verification of the infinite degree range. The analytic estimates in Proof step 4 establish the unbounded range. No independent audit has been performed.
