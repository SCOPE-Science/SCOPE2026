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

The derivation in `RESULT.md` verifies every critical quantifier and boundary analytically: scalar curvatures are strictly positive, all center choices are allowed, the local step lies strictly inside the individual contraction interval, and the epoch count is a positive integer. Unique tuning is a necessary-and-sufficient property of the dimensionless polynomial level sets. Exact expressions establish the rational example and all asymptotic statements are proved rather than extrapolated.

The companion file `verify.py` runs without third-party dependencies. It performs 1,148 successful checks, including exact rational agreement between iterated local-gradient updates and the affine communication-round map for several curvature and center families, fixed-point verification, exact biased/unbiased examples, numerical bracketing of odd-epoch steps, and large-odd-epoch asymptotic consistency using 80-digit decimal arithmetic. The integer check count is reported by the program upon replay. These finite computations are corroboration, not an exhaustive search of all real parameters or a substitute for the derivative and compactness arguments in the proof.

Only synchronized communication-round outputs are asserted to converge to the global minimizer at exceptional tuning. Intermediate local states remain generally different. The uniqueness classification holds uniformly in client centers; it does not prevent accidental exactness for a special fixed center vector. Robustness under nonuniform mixing, perturbed steps, stochasticity and finite precision remains unproved. Independent external audit has not been performed.
