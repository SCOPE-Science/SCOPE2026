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

Run the standalone standard-library program by placing `verify.py` next to this document and executing `python verify.py` with Python 3. No external packages, stochastic seeds, datasets, or network access are required. Expected output: `PASS 18107 exact rational checks`.

The checker uses `fractions.Fraction` and exhaustive Rademacher noise arrays to compare the directly enumerated random one-step quadratic risk with the exact Hessian/covariance formula for real rational two- and three-coordinate test problems, multiple differencing intervals and learning rates, and multiple valid baseline assignments. It tests the resulting cut identity, explicit signed two-dimensional witness, and all simple graphs with two through five vertices for the graph-cut reduction. These are finite algebraic consistency tests. The proof for every dimension is the independent-noise covariance calculation, exact quadratic expectation identity, and rational MAX-CUT reduction in `RESULT.md`.

One randomly observed baseline value is reused whenever a group has multiple coordinates; an unused additional baseline does not enter the estimator. All noise distributions have zero mean, independent calls and the same finite positive variance. Higher moments are unnecessary. For independent oracle noises of unequal variance, correlated perturbed-point samples, or nonquadratic objectives, the displayed formulas are not claimed. At a fixed number of baseline groups, the method compares expected noiseless quadratic objective after a single finite-difference step, not total computational cost or a multi-step convergence rate.

Self-review passed on correctness, originality, and scientific value, with the literature priority limitations recorded in `REVIEW.md`. Independent audit has not been performed.
