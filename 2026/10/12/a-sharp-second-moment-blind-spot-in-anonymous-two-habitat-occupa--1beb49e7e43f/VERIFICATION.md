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

The identities for stationary mean, lag covariance, and third centered mixed moment are proved from two-state transition kernels and independence in RESULT.md. The positivity of every component covariance weight guarantees uniqueness of its exponential support and excludes cancellation. Two possible Bernoulli roots per distinct relaxation rate are exhausted using a four-sign-sum argument; coincident relaxation rates are treated separately by a quadratic reconstruction. The complementary-probability witness has unequal turnover rates and is genuinely inequivalent under whole-patch relabeling. The third moment is nonzero at every strictly positive lag in the exceptional class, with the opposite sign for the rival assignment.

To reproduce finite independent arithmetic checks, run `python3 CHECK.py` in the directory containing that file (Python standard library only). Expected output: `VERIFY_OK exact_two_time_joint_cases=90 complementary_ambiguity=1 equal_rate_reconstruction=16 third_order_resolution=4`.

The checker evaluates rational two-time transition kernels at 90 chosen parameter tuples, the exact counterexample and equal-turnover reconstruction, but these tests are not an exhaustive proof. The theorem concerns exact population moments; finite estimation error, observation noise, interactions between patches, and more than two habitats are not addressed. Some broad aggregated-Markov identifiability literature could include equivalent specializations.
