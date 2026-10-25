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

# Verification of the random affine regular-simplex section laws

The analytic proof is given in `RESULT.md`. The executable, standard-library-only companion `verify.py` checks the finite edge-crossing rule in 2,310 synthetic sections, compares four Monte Carlo Crofton-weighted means with the Gaussian-integral exact expectation, checks the Gaussian integral normalization and evaluates three threshold-quantile identities. It was run from the file staged with this finding and reported PASS.

Re-run from the same directory with `python verify.py`. This script uses a fixed pseudorandom seed, a finite sample size and numerical integration tolerances. Its outputs corroborate finite claims and normalization; they do not constitute a proof of asymptotic convergence or a check of all dimensions. The exact expression and the two asymptotic probability theorems are justified analytically, not by simulation.

The sampling law must be `dσ(normal) dt`, normalized over all hyperplanes intersecting the regular simplex. Replacing it with uniformly sampled normals followed by conditionally uniform offsets changes the finite law; the proof explicitly uses width weighting. No independent review or audit has been performed.
