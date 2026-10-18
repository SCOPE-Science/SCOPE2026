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

# Reproducible verification

Execute `python forest_polarization_check.py`. It requires Python 3 and no third-party packages. The expected deterministic terminal output is `PASS: 1230 exact rational assertions`.

The code enumerates all 16 full directed rooted forests for the stated three-vertex graph with nonnegative rational arc weights, normalizes the weights, calculates each sampled root-opinion vector, and verifies its expectation against an independent rational Gaussian elimination solve of the equilibrium system. It checks the closed-form true polarization, the finite-sample expected bias, the exact expectation ratio and unbiased independent-cross-forest kernel for multiple positive rational group weights, contribution distributions and intrinsic opinions.

Proof-level checks are separately explained in RESULT.md, including the rank-one inverse, forest-weight partition, iid quadratic expectation and bounded-difference concentration. These analytic steps provide the universal quantifiers; finitely many tests do not verify all real weights or all sample sizes. The independent scientific audit has not been performed.
