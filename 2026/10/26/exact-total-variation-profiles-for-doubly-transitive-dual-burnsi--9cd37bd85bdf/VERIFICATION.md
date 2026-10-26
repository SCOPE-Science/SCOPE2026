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

# Verification record

Running `python verify_dual_burnside.py` with a standard Python 3 interpreter checks the stationary distribution, orbit structure, rational transition probabilities, two-step semigroup identity, first-step exact total variation, and conjugacy projection for three symmetric and three affine permutation actions. It additionally checks symbolic rational formulas for 17 symmetric-group degrees and 47 affine parameters, reporting 8,370 exact assertions. Exact outputs are preserved as `verify_dual_burnside_output.txt`. Finite calculations cannot establish the quantified theorem for all groups; the finite-group algebra proof in `RESULT.md` is the evidence for that assertion. No external independent audit has been performed.
