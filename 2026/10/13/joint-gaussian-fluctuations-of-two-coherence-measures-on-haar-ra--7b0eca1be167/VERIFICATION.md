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

The exact formulas can be checked by differentiating the Dirichlet moment identity and matching the five index-multiplicity patterns in the fourth power of the sum of square roots. A self-contained executable `verify_joint_coherence.py` checks those identities numerically for 118 integer dimensions, then uses independently sampled exponentials for moment and covariance sanity checks at four dimensions. It prints a `VERIFY_OK` line if all assertions hold.

Run `python3 verify_joint_coherence.py` using only Python 3.9+ standard-library modules. Random numbers use a fixed seed for reproducibility, not as an assumption in the proof.

The bivariate Gaussian convergence is mathematical: apply the ordinary multivariate central limit theorem to the empirical means of three functions of independent exponentials, then the delta method with the gradients listed in `RESULT.md`. Simulation cannot prove convergence and no tail rate is asserted. Positive definiteness follows analytically from distinct functional growth, not finite eigenvalue tests.

A self-review assessed correctness, originality relative to inspected primary sources, and mathematical value; an independent audit has not been performed.
